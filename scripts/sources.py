"""Network sources: arXiv API, HuggingFace papers, arXiv HTML full text, git repo probing.

Only the standard library is used so the pipeline runs anywhere Python + git exist.
"""
from __future__ import annotations

import html
import json
import os
import logging
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

log = logging.getLogger("sources")

USER_AGENT = "awesome-physical-ai/0.2 (+https://github.com/junyuan-fang/awesome-physical-ai)"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
GITHUB_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
HF_REPO_RE = re.compile(r"https?://huggingface\.co/(datasets/)?([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
GITHUB_NOISE_OWNERS = {"features", "about", "orgs", "topics", "sponsors", "login", "marketplace", "arxiv", "brucemiller"}
HF_NOISE_OWNERS = {"docs", "spaces", "blog", "papers", "models", "learn", "join", "settings", "datasets"}


def is_hf_repo(url: str) -> bool:
    m = HF_REPO_RE.match(url or "")
    return bool(m) and m.group(2).lower() not in HF_NOISE_OWNERS


def http_get(url: str, timeout: int = 30, retries: int = 3, accept: str | None = None) -> str | None:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            log.warning("GET %s failed (%s), try %d/%d", url, e.code, attempt, retries)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            log.warning("GET %s failed (%s), try %d/%d", url, e, attempt, retries)
        time.sleep(3 * attempt)
    return None


# ----------------------------------------------------------------------- arXiv
def _parse_entry(entry: ET.Element) -> dict[str, Any]:
    def text(tag: str) -> str:
        el = entry.find(tag, ATOM)
        return " ".join((el.text or "").split()) if el is not None else ""

    m = ARXIV_ID_RE.search(text("atom:id"))
    links = [l.get("href", "") for l in entry.findall("atom:link", ATOM)]
    return {
        "arxiv_id": m.group(1) if m else text("atom:id"),
        "version": m.group(2) if m and m.group(2) else "v1",
        "title": text("atom:title"),
        "abstract": text("atom:summary"),
        "authors": [" ".join((a.findtext("atom:name", "", ATOM) or "").split()) for a in entry.findall("atom:author", ATOM)],
        "published": text("atom:published")[:10],  # v1 submission date
        "updated": text("atom:updated")[:10],
        "categories": [c.get("term", "") for c in entry.findall("atom:category", ATOM)],
        "comment": text("arxiv:comment"),
        "journal_ref": text("arxiv:journal_ref"),
        "links": links,
    }


def arxiv_search(query: str, max_results: int = 2000, page: int = 200) -> list[dict[str, Any]]:
    """Run an arXiv API search, paging politely (3 s between calls, per arXiv ToU)."""
    out: list[dict[str, Any]] = []
    for start in range(0, max_results, page):
        params = urllib.parse.urlencode(
            {
                "search_query": query,
                "start": start,
                "max_results": page,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
        )
        body = http_get(f"{ARXIV_API}?{params}", timeout=60)
        if body is None:
            break
        entries = ET.fromstring(body).findall("atom:entry", ATOM)
        out += [_parse_entry(e) for e in entries]
        log.info("arXiv %s: +%d (total %d)", query[:60], len(entries), len(out))
        if len(entries) < page:
            break
        time.sleep(3)
    return out


def arxiv_by_ids(ids: list[str]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        params = urllib.parse.urlencode({"id_list": ",".join(chunk), "max_results": len(chunk)})
        body = http_get(f"{ARXIV_API}?{params}", timeout=60)
        if body:
            for e in ET.fromstring(body).findall("atom:entry", ATOM):
                rec = _parse_entry(e)
                if rec["title"] and rec["title"] != "Error":
                    out[rec["arxiv_id"]] = rec
        time.sleep(3)
    return out


# ----------------------------------------------------------------- HuggingFace
def hf_daily(day: str) -> list[dict[str, Any]]:
    body = http_get(f"https://huggingface.co/api/daily_papers?date={day}&limit=100")
    if not body:
        return []
    out = []
    for item in json.loads(body):
        paper = item.get("paper", {})
        out.append(
            {
                "arxiv_id": paper.get("id", ""),
                "upvotes": paper.get("upvotes", 0),
                "github": paper.get("githubRepo") or "",
                "project": paper.get("projectPage") or "",
                "title": paper.get("title", ""),
            }
        )
    return out


def hf_paper(arxiv_id: str) -> dict[str, Any]:
    body = http_get(f"https://huggingface.co/api/papers/{arxiv_id}", retries=2)
    if not body:
        return {}
    data = json.loads(body)
    return {
        "upvotes": data.get("upvotes", 0),
        "github": data.get("githubRepo") or "",
        "project": data.get("projectPage") or "",
    }


# ---------------------------------------------------------------- full text
class _ArxivHTML(HTMLParser):
    """Collect section headings + text, affiliations, table/figure captions and links."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sections: list[list[str]] = [["(front)", ""]]
        self.affiliations: list[str] = []
        self.captions: list[str] = []
        self.links: set[str] = set()
        self._stack: list[tuple[str, str]] = []
        self._heading: str | None = None
        self._buf: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag in ("script", "style", "math", "nav", "footer"):
            self._skip += 1
        if tag == "a" and a.get("href", "").startswith("http"):
            self.links.add(a["href"])
        mode = ""
        if tag in ("h2", "h3") and "ltx_title" in cls:
            mode = "heading"
        elif "ltx_role_affiliation" in cls or "ltx_affiliation" in cls or "ltx_author_notes" in cls:
            mode = "affil"
        elif tag in ("figcaption",) or "ltx_caption" in cls:
            mode = "caption"
        self._stack.append((tag, mode))
        if mode:
            self._flush()

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style", "math", "nav", "footer") and self._skip:
            self._skip -= 1
        while self._stack:
            t, mode = self._stack.pop()
            if mode:
                txt = " ".join("".join(self._buf).split())
                self._buf = []
                if mode == "heading" and txt:
                    self.sections.append([txt, ""])
                elif mode == "affil" and txt:
                    self.affiliations.append(txt)
                elif mode == "caption" and txt:
                    self.captions.append(txt)
            if t == tag:
                break
        if tag in ("p", "div", "li", "tr"):
            self._buf.append(" ")

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._buf.append(data)

    def _flush(self) -> None:
        txt = " ".join("".join(self._buf).split())
        self._buf = []
        if txt:
            self.sections[-1][1] += " " + txt

    def close(self) -> None:
        super().close()
        self._flush()


SECTION_BUDGET = [
    (re.compile(r"abstract", re.I), 2500),
    (re.compile(r"introduction", re.I), 3000),
    (re.compile(r"limitation|conclusion|discussion|future", re.I), 2500),
    (re.compile(r"experiment|evaluation|result|benchmark|ablation|real.world|deployment", re.I), 3500),
    (re.compile(r"method|approach|model|architecture|framework|dataset|data|system|training|design", re.I), 2000),
]
TOTAL_BUDGET = 22000


def fetch_paper_text(arxiv_id: str) -> dict[str, Any] | None:
    """Fetch arXiv HTML and condense it into reviewable sections."""
    body = http_get(f"https://arxiv.org/html/{arxiv_id}", timeout=60, retries=2)
    if not body or "ltx_document" not in body:
        return None
    parser = _ArxivHTML()
    parser.feed(body)
    parser.close()
    kept: list[tuple[str, str]] = []
    used = 0
    for heading, txt in parser.sections:
        txt = txt.strip()
        if not txt:
            continue
        budget = 900  # unmatched sections get a short preview
        for pat, b in SECTION_BUDGET:
            if pat.search(heading):
                budget = b
                break
        if heading == "(front)":
            budget = 2500
        chunk = txt[:budget] + (" …[truncated]" if len(txt) > budget else "")
        if used + len(chunk) > TOTAL_BUDGET:
            chunk = chunk[: max(0, TOTAL_BUDGET - used)]
        if chunk:
            kept.append((heading, chunk))
            used += len(chunk)
        if used >= TOTAL_BUDGET:
            break
    affils = list(dict.fromkeys(a for a in parser.affiliations if len(a) < 300))[:20]
    return {
        "affiliations": affils,
        "sections": kept,
        "captions": [c[:300] for c in parser.captions[:25]],
        "github": sorted({normalize_github(u) for u in parser.links if normalize_github(u)}),
        "huggingface": sorted({u for u in parser.links if is_hf_repo(u)})[:10],
    }


# ------------------------------------------------------------------ repo probe
def normalize_github(url: str) -> str:
    m = GITHUB_RE.match(url or "")
    if not m or m.group(1).lower() in GITHUB_NOISE_OWNERS:
        return ""
    repo = re.sub(r"\.git$", "", m.group(2))
    if repo.lower() in ("", "issues", "pulls"):
        return ""
    return f"https://github.com/{m.group(1)}/{repo}"


def find_github_on_page(url: str) -> str:
    """Return the first plausible code repo linked from a project page."""
    if not url or "github.com" in url and normalize_github(url):
        return normalize_github(url)
    body = http_get(url, timeout=20, retries=1)
    if not body:
        return ""
    for m in GITHUB_RE.finditer(body):
        repo = normalize_github(m.group(0))
        # Skip the github.io site's own source repo and generic template credits.
        if repo and not repo.lower().endswith(".github.io") and "nerfies" not in repo.lower():
            return repo
    return ""


CODE_EXT = {
    ".py", ".pyx", ".ipynb", ".c", ".cc", ".cpp", ".cxx", ".h", ".hpp", ".cu", ".cuh",
    ".rs", ".go", ".jl", ".java", ".scala", ".m", ".lua", ".cs", ".swift", ".kt",
}
CONFIG_EXT = {".yaml", ".yml", ".toml", ".cfg", ".json", ".gin", ".xml", ".urdf", ".mjcf"}
PLACEHOLDER_RE = re.compile(r"coming soon|code will be (released|available)|stay tuned|to be released|\bTBD\b|under construction", re.I)
LICENSE_HINTS = [
    ("Apache-2.0", re.compile(r"Apache License", re.I)),
    ("MIT", re.compile(r"\bMIT License\b|Permission is hereby granted, free of charge", re.I)),
    ("BSD", re.compile(r"\bBSD\b|Redistribution and use in source and binary forms", re.I)),
    ("GPL", re.compile(r"GNU (Affero )?General Public License", re.I)),
    ("CC-BY-NC", re.compile(r"NonCommercial", re.I)),
    ("CC-BY", re.compile(r"Creative Commons Attribution", re.I)),
]


def _git(args: list[str], cwd: Path | None = None, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )


def probe_repo(repo: str) -> dict[str, Any]:
    """Classify a GitHub repo's code release without the rate-limited REST API."""
    result: dict[str, Any] = {"repo": repo}
    if not repo:
        result["code"] = "no-repo"
        return result
    tmp = Path(tempfile.mkdtemp(prefix="probe-"))
    try:
        try:
            cp = _git(["clone", "--depth", "1", "--filter=blob:none", "--no-checkout", "--quiet", repo + ".git", str(tmp / "r")])
        except subprocess.TimeoutExpired:
            result.update(code="unknown", note="clone timed out")
            return result
        if cp.returncode != 0:
            result.update(code="no-repo", note="repo link unreachable (deleted/private?)")
            return result
        r = tmp / "r"
        files = [f for f in _git(["ls-tree", "-r", "--name-only", "HEAD"], cwd=r).stdout.splitlines() if f]
        code_files = [f for f in files if Path(f).suffix.lower() in CODE_EXT]
        cfg_files = [f for f in files if Path(f).suffix.lower() in CONFIG_EXT]
        last_commit = _git(["log", "-1", "--format=%cs"], cwd=r).stdout.strip()
        readme_name = next((f for f in files if "/" not in f and f.lower().startswith("readme")), "")
        readme = _git(["show", f"HEAD:{readme_name}"], cwd=r, timeout=60).stdout if readme_name else ""
        lic_name = next((f for f in files if "/" not in f and re.match(r"(?i)(licen[cs]e|copying)", f)), "")
        lic_text = _git(["show", f"HEAD:{lic_name}"], cwd=r, timeout=60).stdout[:3000] if lic_name else ""
        license_ = "none-found"
        if lic_text:
            license_ = next((name for name, pat in LICENSE_HINTS if pat.search(lic_text)), "custom")
        hf_links = sorted({m.group(0) for m in HF_REPO_RE.finditer(readme) if is_hf_repo(m.group(0))})
        placeholder_text = bool(PLACEHOLDER_RE.search(readme))
        n = len(code_files)
        if n == 0:
            code = "placeholder"
        elif n < 8 or (placeholder_text and n < 20):
            code = "partial"
        else:
            code = "substantive"
        result.update(
            code=code,
            license=license_,
            stats={
                "files": len(files),
                "code_files": n,
                "config_files": len(cfg_files),
                "last_commit": last_commit,
                "readme_says_coming_soon": placeholder_text,
            },
            hf_weights=[u for u in hf_links if "/datasets/" not in u][:5],
            hf_datasets=[u for u in hf_links if "/datasets/" in u][:5],
        )
        return result
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
