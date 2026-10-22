"""Render vla_survey-style reports: per-run daily digest, weekly / monthly picks.

    python scripts/digest.py --week 2026-10-19     # ISO week containing that date (≤ weekly_cap)
    python scripts/digest.py --month 2026-09       # calendar month (≤ monthly_cap)

Daily digests are written by apply_reviews.py. Period digests select from
data/papers.yaml by first-public date, core route first, then priority/score.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from curation import DIGESTS, ROOT, load_config, load_papers, parse_date, sort_key, today  # noqa: E402

PRIORITY_ZH = {"must-read": "🔥 重点阅读", "notable": "👀 值得关注", "watching": "观察中", "unrated": "暂不评级"}
CODE_ZH = {
    "substantive": "已公开实质相关代码",
    "partial": "部分开放",
    "placeholder": "找到仓库但未发现实质相关代码",
    "no-repo": "未找到官方仓库链接",
    "unknown": "未核查",
}
ROUTE_ZH = {"core": "核心", "adjacent": "相邻路线"}
ROLE_ZH = {"proposes": "提出", "pretrain": "预训练", "finetune": "微调/后训练", "eval": "评测"}


def _rel(target: str, out_path: Path) -> str:
    import os

    return os.path.relpath(ROOT / target, out_path.parent).replace("\\", "/")


def render_entry(n: int, p: dict[str, Any], out_path: Path) -> str:
    r = p.get("review", {})
    o = p.get("open", {})
    aid = p.get("arxiv_id")
    link = (p.get("links") or {}).get("arxiv") or (f"https://arxiv.org/abs/{aid}" if aid else "")
    lines = [f"### {n}. {p['title']} — {PRIORITY_ZH[r.get('priority', 'unrated')]}", ""]
    when = f"{p['date']}（[arXiv]({link})）" if link else str(p["date"])
    if p.get("updated") and p["updated"] != p["date"]:
        when += f"；最近版本 {p['updated']}"
    if p.get("late_found"):
        when += "；**迟发现**"
    lines.append(f"- **时间：** {when}")
    if r.get("scores"):
        s, why = r["scores"], r.get("rationale") or {}
        parts = [f"{k}{s[k]}（{why.get(k, '')}）" if why.get(k) else f"{k}{s[k]}" for k in ("C", "E", "O", "T")]
        lines.append(f"- **评分：** {' / '.join(parts)} = **{r['total']}/100**；**优先级：** {PRIORITY_ZH[r['priority']]}")
    else:
        lines.append(f"- **评分：** 暂不评级{('（' + '；'.join(r.get('pending_checks') or []) + '）') if r.get('pending_checks') else ''}")
    who = "；".join(p.get("affiliations") or []) or (p.get("authors") or "未知/待核实")
    lines.append(f"- **作者/团队单位：** {who}")
    lines.append(
        f"- **分类：** `{p['category']}` · {ROUTE_ZH.get(p.get('route', ''), '未标注')} · {p.get('contribution', '—')}"
    )
    lines.append(f"- **核心内容：** {p.get('summary') or p.get('abstract_short') or '（待补）'}")
    checked = r.get("reviewed") or o.get("last_check") or "—"
    venue = p.get("venue") or "arXiv 预印本；未检索到正式录用记录"
    lines.append(f"- **发表状态（核验：{checked}）：** {venue}")
    code = CODE_ZH.get(o.get("code", "unknown"), o.get("code"))
    repo = f"[仓库]({o['repo']})" if o.get("repo") else "无仓库链接"
    extra = f"；权重 {o.get('weights', 'unknown')}，数据 {o.get('data', 'unknown')}，许可 {o.get('license', 'unknown')}"
    note = f"。{o['note']}" if o.get("note") else ""
    lines.append(
        f"- **开源状态（首次核查：{o.get('first_check', '—')}；last_check：{o.get('last_check', '—')}）：** {code}，{repo}{extra}{note}"
    )
    if p.get("uses"):
        uses = "、".join(f"{u['resource']}（{ROLE_ZH.get(u['role'], u['role'])}）" for u in p["uses"])
        lines.append(f"- **数据/基准关系：** {uses}")
    if r.get("pending_checks") and r.get("scores"):
        lines.append(f"- **待核验事项：** {'；'.join(r['pending_checks'])}")
    lines.append("")
    return "\n".join(lines)


def render_sections(papers: list[dict[str, Any]], out_path: Path) -> list[str]:
    lines: list[str] = []
    n = 0
    for route, title in (("core", "## 核心工作"), ("adjacent", "## 相邻路线（数据 / 基准 / 基础设施 / 分析）")):
        group = sorted([p for p in papers if p.get("route", "core") == route], key=sort_key)
        if not group:
            continue
        lines += [title, ""]
        for p in group:
            n += 1
            lines.append(render_entry(n, p, out_path))
    return lines


def render_daily(run: dict[str, Any], included: list[dict[str, Any]], skipped: list[dict[str, Any]], out_path: Path) -> str:
    st = run.get("stats", {})
    excl = [s for s in skipped if s["decision"] == "exclude"]
    defer = [s for s in skipped if s["decision"] == "defer"]
    lines = [
        f"# 扫描报告：{run['scan_date']}",
        "",
        "## 本期说明",
        "",
        f"- **覆盖时间：** {run['window_start']} 至 {run['window_end']}（按 arXiv 首次提交日期；含向上次截止日 {run.get('last_covered_end') or '—'} 前 2 天的重叠回看）。",
        f"- **扫描日期：** {run['scan_date']}；类型：{run.get('kind', 'daily')}。",
        f"- **上限计算：** d = {run['d']}，cap = min(5×{run['d']}, 20) = **{run['cap']}**；本期收录 **{len(included)}** 项（上限不是目标）。",
        f"- **来源：** {'；'.join(run.get('sources', []))}。来源不声称穷尽；重要事实以论文正文、项目页和仓库内容为准。",
        f"- **候选统计：** 抓取 {st.get('fetched', '—')} 篇；已收录/已分诊去重 {st.get('already_tracked_or_triaged', '—')}；"
        f"超出范围 {st.get('out_of_scope', '—')}；相关性预筛未进池 {st.get('below_pool_cut', '—')}；"
        f"进入分诊池 {st.get('pool', '—')}；第一层排除 {len(excl)}、暂缓 {len(defer)}。",
        "- **评分口径：** 贡献 C 30% / 证据 E 25% / 开放 O 30% / 团队 T 15%，总分 = 6C+5E+6O+3T；详见 [METHODOLOGY](" + _rel("docs/METHODOLOGY.md", out_path) + ")。",
        "",
    ]
    if excl or defer:
        reasons: dict[str, int] = {}
        for s in excl:
            key = (s.get("reason") or "未注明").split("：")[0].split(":")[0][:40]
            reasons[key] = reasons.get(key, 0) + 1
        top = "；".join(f"{k}（{v}）" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1])[:6])
        lines += [f"- **主要排除原因：** {top or '—'}", ""]
    lines += render_sections(included, out_path)
    if defer:
        lines += ["## 暂缓核验", ""]
        lines += [f"- [{s['title']}](https://arxiv.org/abs/{s['arxiv_id']}) — {s.get('reason') or ''}" for s in defer]
        lines.append("")
    return "\n".join(lines)


def render_migration(run: dict[str, Any], included: list[dict[str, Any]], skipped: list[dict[str, Any]], out_path: Path) -> str:
    dist: dict[str, int] = {}
    for p in included:
        pr = p.get("review", {}).get("priority", "unrated")
        dist[pr] = dist.get(pr, 0) + 1
    moved = [p for p in included if any("category" in h.get("change", "") for h in p.get("history") or [])]
    lines = [
        f"# 存量整理报告：{run.get('scan_date')}",
        "",
        "## 本期说明",
        "",
        "- **范围：** v2 流程上线前已收录的全部论文，按 [METHODOLOGY](" + _rel("docs/METHODOLOGY.md", out_path) + ") 重新做两层筛选与四维评分。",
        f"- **结果：** 保留 {len(included)} 篇（" + "、".join(f"{PRIORITY_ZH[k]} {dist.get(k, 0)}" for k in PRIORITY_ZH) + f"）；移出 {len(skipped)} 篇；调整类别 {len(moved)} 篇。",
        "- **变化说明：** 旧版按日期把 2026-04 之后的论文一律标 🔥，现改为由评分推导；🔥/👀 只代表跟进优先级。开放状态由仓库实际内容探测并人工/agent 复核。",
        "",
    ]
    top = [p for p in included if p.get("review", {}).get("priority") in ("must-read", "notable")]
    lines += render_sections(top, out_path)
    rest = sorted([p for p in included if p not in top], key=sort_key)
    if rest:
        lines += ["## 观察中 / 暂不评级", "", "| 论文 | 日期 | 类别 | 总分 | 代码 | 备注 |", "|---|---|---|---|---|---|"]
        for p in rest:
            r = p.get("review", {})
            note = "；".join(r.get("pending_checks") or [])[:80]
            lines.append(
                f"| [{p['title']}](https://arxiv.org/abs/{p.get('arxiv_id')}) | {p['date']} | `{p['category']}` | "
                f"{r.get('total', '—')} | {CODE_ZH.get(p.get('open', {}).get('code', 'unknown'))} | {note} |"
            )
        lines.append("")
    if skipped:
        lines += ["## 移出列表", ""]
        lines += [f"- [{s['title']}](https://arxiv.org/abs/{s['arxiv_id']}) — {s.get('reason')}" for s in skipped]
        lines.append("")
    if moved:
        lines += ["## 类别调整", ""]
        for p in moved:
            ch = [h["change"] for h in p["history"] if "category" in h["change"]][-1]
            lines.append(f"- {p['title']}：{ch}")
        lines.append("")
    return "\n".join(lines)


def render_period(kind: str, start: date, end: date, label: str, out_path: Path) -> str:
    cfg = load_config()
    cap = int(cfg["weekly_cap"] if kind == "week" else cfg["monthly_cap"])
    pool = [
        p
        for p in load_papers()
        if len(str(p.get("date", ""))) == 10
        and start <= parse_date(p["date"]) <= end
        and p.get("review", {}).get("priority") in ("must-read", "notable", "watching")
    ]
    core = sorted([p for p in pool if p.get("route", "core") == "core"], key=sort_key)
    adj = sorted([p for p in pool if p.get("route") == "adjacent"], key=sort_key)
    picked = (core + adj)[:cap] if len(core) >= cap else core + adj[: cap - len(core)]
    title = "周精选" if kind == "week" else "月报"
    lines = [
        f"# {title}：{label}",
        "",
        "## 本期说明",
        "",
        f"- **覆盖时间：** {start} 至 {end}（按首次可核查公开日期归属）。",
        f"- **整理日期：** {today()}；上限 {cap} 项，本期 {len(picked)} 项（候选 {len(pool)} 项已评分工作，核心优先、按优先级与总分排序）。",
        "- **说明：** 自动从 `data/papers.yaml` 选取，评分与开放状态以 `docs/index.md` 当前值为准；历史 digest 为时间快照。",
        "",
    ]
    lines += render_sections(picked, out_path)
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--week", help="any date inside the ISO week")
    g.add_argument("--month", help="YYYY-MM")
    args = ap.parse_args()
    if args.week:
        d = parse_date(args.week)
        start = d - timedelta(days=d.weekday())
        end = start + timedelta(days=6)
        iso = start.isocalendar()
        label = f"{iso[0]}-W{iso[1]:02d}"
        out = DIGESTS / "weekly" / f"{label}.md"
        text = render_period("week", start, end, label, out)
    else:
        start = parse_date(args.month + "-01")
        end = (start.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        out = DIGESTS / "monthly" / f"{args.month}.md"
        text = render_period("month", start, end, args.month, out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"✅ wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
