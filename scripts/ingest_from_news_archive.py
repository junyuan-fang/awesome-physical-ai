"""Ingest 2026 papers from ~/code/claude_bot/news_archive/embodied-*.md → data/papers.yaml.

Workflow (designed to run from cc-connect cron --exec):
  1. Scan all embodied-*.md files in news_archive.
  2. Extract arXiv IDs via regex (YYMM.NNNNN, with YY >= 25).
  3. Skip IDs already present in data/papers.yaml.
  4. Hit arXiv API (batch) to pull real title / authors / abstract / submission_date.
  5. Map to category via keyword heuristics.
  6. Append to data/papers.yaml.
  7. Run scripts/generate_readme.py to refresh README.md.
  8. git add + commit + push (only if there is actually something to push).

Usage:
    python3 scripts/ingest_from_news_archive.py

Designed to be idempotent — running twice without new papers is a no-op.
"""
from __future__ import annotations

import html
import json
import logging
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAPERS_YAML = ROOT / "data" / "papers.yaml"
NEWS_ARCHIVE = Path.home() / "code" / "claude_bot" / "news_archive"

ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_ABS = "https://arxiv.org/abs/{arxiv_id}"
S2_API = "https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=title,abstract,authors,publicationDate,year"
META_TAG_RE = re.compile(
    r'<meta\s+name="citation_(?P<key>[a-z_]+)"\s+content="(?P<value>[^"]*)"\s*/?>',
    re.IGNORECASE,
)
BULLET_RE = re.compile(r"^\s*[-*]\s+(?P<text>.+)$", re.MULTILINE)
NOISE_BULLET_PREFIXES = ("来源", "源：", "Source", "见 ", "参见", "信源", "扩展阅读", "延伸阅读")
USER_AGENT = "awesome-physical-ai/0.1 (https://github.com/junyuan-fang/awesome-physical-ai; mailto:fangjunyuan1@gmail.com)"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_NS = {"arxiv": "http://arxiv.org/schemas/atom"}

# arXiv id YYMM.NNNNN, where YY >= 25 (≈ 2025+) — keep "physical AI era" only
ARXIV_RE = re.compile(r"\b(2[5-9]\d{2}|3\d{3})\.(\d{4,5})\b")

# Category mapping: order matters, first hit wins. Keys are case-insensitive needles
# matched against title + abstract + summary text.
CATEGORY_HEURISTICS: list[tuple[str, str]] = [
    ("teleop", "teleoperation"),
    ("teleoperation", "teleoperation"),
    ("locomotion", "locomotion"),
    ("walking", "locomotion"),
    ("running", "locomotion"),
    ("sprint", "locomotion"),
    ("sim-to-real", "sim2real"),
    ("sim2real", "sim2real"),
    ("domain randomization", "sim2real"),
    ("gaussian splat", "scene"),
    ("nerf", "scene"),
    ("scene understanding", "scene"),
    ("3d generation", "scene"),
    ("3d segmentation", "scene"),
    ("world model", "foundation-models"),
    ("foundation model", "foundation-models"),
    ("survey", "foundation-models"),
    ("vla", "vla"),
    ("vision-language-action", "vla"),
    ("vision language action", "vla"),
    ("manipulation", "manipulation"),
    ("grasp", "manipulation"),
    ("dexterous", "manipulation"),
    ("bimanual", "manipulation"),
    ("navigation", "navigation"),
    ("embodied qa", "navigation"),
    ("diffusion policy", "rl-il"),
    ("imitation learning", "rl-il"),
    ("reinforcement learning", "rl-il"),
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ingest")


def fetch_arxiv_html(arxiv_id: str) -> dict[str, Any] | None:
    """Scrape arXiv abstract page HTML for citation_* meta tags. Primary path."""
    url = ARXIV_ABS.format(arxiv_id=arxiv_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, 3):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                content = resp.read().decode("utf-8", errors="replace")
            break
        except (urllib.error.URLError, TimeoutError) as e:
            log.warning("arXiv HTML fetch failed for %s (try %d/2): %s", arxiv_id, attempt, e)
            time.sleep(3)
    else:
        return None

    fields: dict[str, list[str]] = {}
    for m in META_TAG_RE.finditer(content):
        fields.setdefault(m.group("key"), []).append(html.unescape(m.group("value")))
    title = (fields.get("title") or [""])[0].strip()
    if not title:
        return None
    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "abstract": (fields.get("abstract") or [""])[0].strip(),
        "published": (fields.get("date") or [""])[0].replace("/", "-")[:10],
        "authors": [a.strip() for a in fields.get("author", [])],
    }


def extract_chinese_summary(arxiv_id: str) -> str | None:
    """Find arXiv ID in news_archive markdown, pull surrounding Chinese 业内意义."""
    if not NEWS_ARCHIVE.exists():
        return None
    pattern = re.compile(rf"https?://arxiv\.org/abs/{re.escape(arxiv_id)}")
    for md_file in sorted(NEWS_ARCHIVE.glob("embodied-*.md"), reverse=True):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        m = pattern.search(text)
        if not m:
            continue
        before = text[: m.start()]
        h_idx = before.rfind("### 业内意义")
        if h_idx == -1:
            h_idx = max(before.rfind("\n## "), before.rfind("\n### "))
        if h_idx == -1:
            continue
        section = text[h_idx : m.start()]
        bullets = [b.group("text").strip() for b in BULLET_RE.finditer(section)]
        bullets = [b for b in bullets if not b.startswith(NOISE_BULLET_PREFIXES) and len(b) > 6]
        if not bullets:
            continue
        summary = "；".join(bullets[:2])
        summary = re.sub(r"\*\*([^*]+)\*\*", r"\1", summary)
        summary = re.sub(r"\*([^*]+)\*", r"\1", summary)
        if len(summary) > 240:
            summary = summary[:240].rsplit("，", 1)[0] + "…"
        return summary
    return None


def update_existing_chinese_summaries(papers: list[dict[str, Any]]) -> int:
    """Walk all existing papers; overwrite abstract_short with Chinese where found."""
    updated = 0
    for p in papers:
        aid = p.get("arxiv_id")
        if not aid:
            continue
        chinese = extract_chinese_summary(aid)
        if chinese and chinese != p.get("abstract_short"):
            p["abstract_short"] = chinese
            updated += 1
    return updated


def extract_arxiv_ids() -> set[str]:
    """Scan embodied-*.md files for arXiv IDs."""
    if not NEWS_ARCHIVE.exists():
        log.warning("news_archive not found: %s", NEWS_ARCHIVE)
        return set()
    ids: set[str] = set()
    for f in sorted(NEWS_ARCHIVE.glob("embodied-*.md")):
        for m in ARXIV_RE.finditer(f.read_text(encoding="utf-8", errors="ignore")):
            ids.add(f"{m.group(1)}.{m.group(2)}")
    return ids


def existing_ids() -> set[str]:
    if not PAPERS_YAML.exists():
        return set()
    doc = yaml.safe_load(PAPERS_YAML.read_text()) or {}
    return {str(p.get("arxiv_id")) for p in doc.get("papers", []) if p.get("arxiv_id")}


def fetch_semantic_scholar(arxiv_id: str) -> dict[str, Any] | None:
    """Fetch a single paper via Semantic Scholar (more reliable rate limits than arXiv)."""
    url = S2_API.format(arxiv_id=arxiv_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            if not data.get("title"):
                return None
            authors = [a.get("name", "") for a in (data.get("authors") or [])]
            pub_date = data.get("publicationDate") or f"{data.get('year', '')}-01-01"
            return {
                "arxiv_id": arxiv_id,
                "title": data["title"].strip(),
                "abstract": (data.get("abstract") or "").strip(),
                "published": pub_date[:10],
                "authors": authors,
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # paper doesn't exist on S2
            if e.code == 429:
                wait = 10 * attempt
                log.warning("S2 rate-limited on %s (try %d/3), sleeping %ds", arxiv_id, attempt, wait)
                time.sleep(wait)
                continue
            log.warning("S2 HTTP %s on %s", e.code, arxiv_id)
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning("S2 fetch error on %s: %s", arxiv_id, e)
            time.sleep(3)
    return None


def fetch_arxiv_metadata(ids: list[str]) -> dict[str, dict[str, Any]]:
    """Batch-fetch arXiv API for a list of IDs (max 25 per call to be friendly)."""
    out: dict[str, dict[str, Any]] = {}
    BATCH = 25
    MAX_RETRIES = 3
    for i in range(0, len(ids), BATCH):
        batch = ids[i : i + BATCH]
        url = f"{ARXIV_API}?id_list={','.join(batch)}&max_results={len(batch)}"
        log.info("Fetching arXiv batch %d-%d (%d IDs)", i, i + len(batch), len(batch))

        content = None
        for attempt in range(1, MAX_RETRIES + 1):
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    content = resp.read()
                if b"Rate exceeded" in content[:200]:
                    raise urllib.error.URLError("Rate exceeded")
                break
            except (urllib.error.URLError, TimeoutError) as e:
                wait = 10 * attempt  # 10s, 20s, 30s backoff
                log.warning(
                    "arXiv batch %s failed (attempt %d/%d): %s — sleeping %ds",
                    batch[0], attempt, MAX_RETRIES, e, wait,
                )
                time.sleep(wait)
                content = None
        if content is None:
            log.error("Giving up on batch starting %s after %d attempts", batch[0], MAX_RETRIES)
            continue

        root = ET.fromstring(content)
        for entry in root.findall("atom:entry", ATOM_NS):
            id_url = entry.find("atom:id", ATOM_NS).text  # http://arxiv.org/abs/2606.02486v1
            arxiv_id = id_url.rsplit("/", 1)[-1].split("v")[0]
            title_el = entry.find("atom:title", ATOM_NS)
            summary_el = entry.find("atom:summary", ATOM_NS)
            published_el = entry.find("atom:published", ATOM_NS)
            authors = [
                a.find("atom:name", ATOM_NS).text
                for a in entry.findall("atom:author", ATOM_NS)
            ]
            out[arxiv_id] = {
                "arxiv_id": arxiv_id,
                "title": (title_el.text or "").strip().replace("\n", " ").replace("  ", " "),
                "abstract": (summary_el.text or "").strip().replace("\n", " "),
                "published": (published_el.text or "")[:10],  # YYYY-MM-DD
                "authors": authors,
            }
        # arXiv rate limit recommends ≥3s between requests; we go slower to be friendly
        time.sleep(5)
    return out


def short_authors(authors: list[str]) -> str:
    if not authors:
        return "Unknown"
    if len(authors) == 1:
        return authors[0]
    return f"{authors[0]} et al."


def categorize(meta: dict[str, Any]) -> str:
    haystack = (meta.get("title", "") + " " + meta.get("abstract", "")).lower()
    for needle, cat in CATEGORY_HEURISTICS:
        if needle in haystack:
            return cat
    return "vla"  # safe default for embodied AI papers


def to_paper_entry(meta: dict[str, Any]) -> dict[str, Any]:
    chinese = extract_chinese_summary(meta["arxiv_id"])
    if chinese:
        abstract_short = chinese
    else:
        abstract_short = meta.get("abstract", "")[:240].strip()
        if abstract_short and not abstract_short.endswith("."):
            abstract_short = abstract_short.rsplit(" ", 1)[0] + "..."
    return {
        "arxiv_id": meta["arxiv_id"],
        "title": meta["title"],
        "authors": short_authors(meta["authors"]),
        "date": meta["published"][:7],  # YYYY-MM
        "category": categorize(meta),
        "tags": ["news-archive"],
        "abstract_short": abstract_short,
        "links": {
            "arxiv": f"https://arxiv.org/abs/{meta['arxiv_id']}",
        },
        "highlight": "🔥" if (meta.get("published", "") >= "2026-04") else "👀",
        "added": date.today().isoformat(),
        "source": "news_archive",
    }


def git_run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    update_existing = "--update-existing" in sys.argv

    all_ids = extract_arxiv_ids()
    log.info("Found %d unique arXiv IDs in news_archive", len(all_ids))

    have = existing_ids()
    new_ids = sorted(all_ids - have)
    log.info("New IDs to ingest: %d (have %d already)", len(new_ids), len(have))

    existing_doc = yaml.safe_load(PAPERS_YAML.read_text()) or {}
    existing_papers: list[dict[str, Any]] = existing_doc.get("papers", [])

    # Optional backfill: refresh abstract_short for existing entries.
    backfilled = 0
    if update_existing:
        backfilled = update_existing_chinese_summaries(existing_papers)
        log.info("--update-existing: refreshed %d entries", backfilled)

    # Fetch new papers, if any.
    added = 0
    if new_ids:
        meta_by_id: dict[str, dict[str, Any]] = {}
        # Primary: arXiv HTML scrape (no rate limit, no SSL issues)
        for aid in new_ids:
            m = fetch_arxiv_html(aid)
            if m:
                meta_by_id[aid] = m
            time.sleep(2)
        log.info("arXiv HTML scrape: %d / %d", len(meta_by_id), len(new_ids))

        # Fallback 1: Semantic Scholar
        missing = [aid for aid in new_ids if aid not in meta_by_id]
        if missing:
            log.info("Falling back to Semantic Scholar for %d IDs", len(missing))
            for aid in missing:
                m = fetch_semantic_scholar(aid)
                if m:
                    meta_by_id[aid] = m
                time.sleep(1.1)

        # Fallback 2: arXiv API batch
        missing = [aid for aid in new_ids if aid not in meta_by_id]
        if missing:
            log.info("Falling back to arXiv API for %d IDs", len(missing))
            meta_by_id.update(fetch_arxiv_metadata(missing))

        log.info("Final coverage: %d / %d", len(meta_by_id), len(new_ids))

        for aid in new_ids:
            meta = meta_by_id.get(aid)
            if not meta or not meta.get("title"):
                log.warning("Skipping %s — no metadata", aid)
                continue
            existing_papers.append(to_paper_entry(meta))
            added += 1

    if added == 0 and backfilled == 0:
        log.info("Nothing to write — exiting cleanly.")
        return 0

    PAPERS_YAML.write_text(
        yaml.safe_dump(
            {"papers": existing_papers},
            sort_keys=False,
            allow_unicode=True,
            width=120,
        ),
        encoding="utf-8",
    )
    log.info("Wrote papers.yaml: +%d new, %d refreshed", added, backfilled)

    rc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_readme.py")], check=False,
    ).returncode
    if rc != 0:
        log.error("generate_readme.py failed (rc=%d)", rc)
        return rc

    status = git_run("status", "--porcelain")
    if not status.stdout.strip():
        log.info("No git changes after regenerate — exiting.")
        return 0

    git_run("add", "data/papers.yaml", "README.md")
    parts = []
    if added: parts.append(f"+{added} papers")
    if backfilled: parts.append(f"refreshed {backfilled} summaries")
    msg = f"chore: {' & '.join(parts)} ({date.today().isoformat()})"
    commit = git_run(
        "-c", "user.email=fangjunyuan1@gmail.com",
        "-c", "user.name=junyuan-fang",
        "commit", "-m", msg,
    )
    if commit.returncode != 0:
        log.error("git commit failed: %s", commit.stderr)
        return commit.returncode

    push = git_run("push")
    if push.returncode != 0:
        log.error("git push failed: %s", push.stderr)
        return push.returncode

    log.info("✅ Pushed %d new papers to GitHub.", added)
    return 0


if __name__ == "__main__":
    sys.exit(main())
