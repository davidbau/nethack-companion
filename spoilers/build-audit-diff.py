#!/usr/bin/env python3
"""Render the spoilers/companion.md audit diffs as a single HTML page."""

import html
import subprocess
import sys
from pathlib import Path

REPO = Path("/Users/davidbau/git/mazesofmenace/teleport/maud")
BOUNDARY = "63364e694^"  # commit just before the audit framework
OUT = REPO / "spoilers" / "audit-diff.html"


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args], text=True)


def commits():
    """List audit commits newest-first that touched companion.md."""
    raw = git("log", "--pretty=%H%x09%s", f"{BOUNDARY}..HEAD", "--",
              "spoilers/companion.md").strip().splitlines()
    return [line.split("\t", 1) for line in raw]


def diff_for(commit):
    """Diff for one commit, filtered to drop audit HTML-comment badges."""
    raw = git("show", "--no-color", "--format=", commit, "--",
              "spoilers/companion.md")
    out = []
    for line in raw.splitlines():
        if line.startswith(("+<!-- audit", "-<!-- audit")):
            continue
        out.append(line)
    return "\n".join(out)


def line_class(line):
    if line.startswith("@@"):
        return "hunk"
    if line.startswith("+++") or line.startswith("---"):
        return "filehdr"
    if line.startswith("diff --git"):
        return "filehdr"
    if line.startswith("+"):
        return "add"
    if line.startswith("-"):
        return "del"
    return "ctx"


def render_diff(text):
    rows = []
    for line in text.splitlines():
        cls = line_class(line)
        rows.append(f'<div class="line {cls}">{html.escape(line) or "&nbsp;"}</div>')
    return "\n".join(rows)


def main():
    cs = commits()
    print(f"Found {len(cs)} commits", file=sys.stderr)

    parts = []
    parts.append("""<!doctype html>
<html lang=en>
<meta charset=utf-8>
<title>Companion-audit diffs</title>
<style>
  :root {
    --add-bg: #e6ffed; --add-fg: #22863a;
    --del-bg: #ffeef0; --del-fg: #b31d28;
    --hunk-bg: #f1f8ff; --hunk-fg: #005cc5;
    --hdr-bg: #f6f8fa; --hdr-fg: #586069;
    --ctx-fg: #24292e;
    --commit-bg: #fffbea; --commit-border: #d4a72c;
  }
  html { color-scheme: light; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    margin: 0; padding: 20px; background: #fff; color: #24292e;
    max-width: 1100px; margin-inline: auto;
  }
  h1 { font-size: 22px; margin-top: 0; }
  h2 {
    font-size: 15px; font-family: ui-monospace, Menlo, monospace;
    background: var(--commit-bg); border-left: 4px solid var(--commit-border);
    padding: 10px 14px; margin: 28px 0 0;
    border-top-right-radius: 6px;
  }
  details { margin-bottom: 16px; }
  details > summary { cursor: pointer; padding: 4px 0; }
  .toc {
    background: var(--hdr-bg); padding: 12px 16px; border-radius: 6px;
    font-size: 13px; line-height: 1.7;
  }
  .toc a { color: var(--hunk-fg); text-decoration: none; font-family: ui-monospace, Menlo, monospace; }
  .toc a:hover { text-decoration: underline; }
  .diff {
    font-family: ui-monospace, Menlo, monospace; font-size: 12.5px; line-height: 1.45;
    background: #fafbfc; border: 1px solid #e1e4e8; border-radius: 6px;
    overflow-x: auto;
  }
  .line { padding: 0 12px; white-space: pre; }
  .line.add    { background: var(--add-bg); color: var(--add-fg); }
  .line.del    { background: var(--del-bg); color: var(--del-fg); }
  .line.hunk   { background: var(--hunk-bg); color: var(--hunk-fg); padding: 4px 12px; font-weight: 600; }
  .line.filehdr { background: var(--hdr-bg); color: var(--hdr-fg); font-weight: 600; padding: 4px 12px; }
  .line.ctx    { color: var(--ctx-fg); }
  .nochange { color: #6a737d; font-style: italic; padding: 8px 12px; }
  .meta { color: #6a737d; font-size: 13px; margin-bottom: 16px; }
</style>
<body>
<h1>A Traveler's Companion: chapter-by-chapter audit diffs</h1>
<p class=meta>Each section below is one git commit on <code>spoilers/companion.md</code>
since the audit framework was set up. Audit-badge HTML comments are
filtered out to keep the focus on the prose changes. Newest commits
first.</p>

<details open><summary><strong>Contents</strong></summary>
<div class=toc>
""")

    for sha, subj in cs:
        short = sha[:9]
        anchor = f"c-{short}"
        parts.append(f'<a href="#{anchor}">{short}</a> &nbsp; {html.escape(subj)}<br>')

    parts.append("</div></details>\n")

    for sha, subj in cs:
        short = sha[:9]
        anchor = f"c-{short}"
        d = diff_for(sha).strip()
        parts.append(f'<h2 id="{anchor}">{short} — {html.escape(subj)}</h2>')
        if d:
            parts.append(f'<div class=diff>{render_diff(d)}</div>')
        else:
            parts.append('<div class=nochange>(no prose changes after filtering)</div>')

    parts.append("</body></html>")

    OUT.write_text("\n".join(parts))
    print(f"Wrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
