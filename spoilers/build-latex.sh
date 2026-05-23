#!/usr/bin/env bash
# Build script for "A Traveler's Companion to the Mazes of Menace"
# LaTeX pipeline: companion.md → pandoc + lua filter → xelatex → book.pdf
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Check dependencies
if ! command -v pandoc &>/dev/null; then
  echo "Error: pandoc not found. Install with: brew install pandoc" >&2
  exit 1
fi

if ! command -v xelatex &>/dev/null; then
  echo "Error: xelatex not found. Install with: brew install --cask mactex" >&2
  exit 1
fi

echo "=== Building PDF via LaTeX ==="

# Make sure the dungeon-map PDFs are present and current.
if [ ! -f images/dmap-dod.pdf ] || [ companion.md -nt images/dmap-dod.pdf ]; then
  python3 dungeon_map.py --pdfs
fi

# Print version drops web-only asides ("or more likely scrolling
# through" — true in a browser, false on paper). Anything that's
# accurate-on-screen-only-and-wrong-in-print belongs in this sed.
sed -e 's/ (or more likely scrolling through)//' companion.md > .companion-print.md

# Replace the inline-SVG dungeon map block with markdown image
# references to the PDFs that dungeon_map.py wrote. Pandoc turns
# these into \begin{figure}\includegraphics... blocks that LaTeX
# pages correctly.
python3 - <<'PY'
import re
from pathlib import Path
md = Path('.companion-print.md').read_text()
caption = (
    'Dungeons of Doom, Gehennom, and the Elemental Planes. '
    'Branches extend left and right of the main trunk. Pearls '
    '(small colored dots) indicate the approximate number of '
    'intervening dungeon levels. ★ marks the three Invocation '
    'items (Bell of Opening, Candelabrum, Book of the Dead) '
    "needed to enter Moloch's Sanctum and claim the Amulet."
)
    # Map image dimensions (PDF points, native):
    #   dmap-dod.pdf:    570 x 458.25
    #   dmap-geh.pdf:    570 x 510.75  (combined aspect h/w = 1.700)
    #   dmap-planes.pdf: 570 x 224.25
    # A5 text area is 7.018 in tall. At width 4.0 in, the DoD+Geh
    # stack is 6.8 in tall, with 0.2 in slack inside the text area
    # (we use \centerline rather than the center env so there's no
    # env padding eating that budget). Planes uses the same width.
DMAP_WIDTH = "4.0in"
replacement = (
    '\n\n```{=latex}\n'
    '\\begingroup\\setlength{\\parskip}{0pt}\n'
    '\\centerline{\\vbox{\\offinterlineskip%\n'
    f'  \\hbox{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-dod.pdf}}}}%\n'
    f'  \\hbox{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-geh.pdf}}}}%\n'
    '}}\n'
    '\\endgroup\n'
    '\\clearpage\n'
    f'\\centerline{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-planes.pdf}}}}\n'
    '\\vspace{0.6em}\n'
    f'{{\\footnotesize\\itshape\\noindent {caption}\\par}}\n'
    '```\n\n'
)
md = re.sub(
    r'<!-- DMAP-BEGIN -->.*?<!-- DMAP-END -->',
    lambda _m: replacement, md, flags=re.DOTALL,
)
Path('.companion-print.md').write_text(md)
PY

PANDOC_ARGS=(
  .companion-print.md
  --from=markdown
  --pdf-engine=xelatex
  --template=template.tex
  --lua-filter=latex-filter.lua
  --top-level-division=part
  --toc
  --output=book.pdf
)

# Two-pass build: first pass writes the .aux file (labels and pages);
# second pass uses it to resolve cross-references like the index's
# \pageref calls. Without this, page numbers in the index will be
# stale (showing values from a previous build, or ?? on a fresh build).
pandoc "${PANDOC_ARGS[@]}" 2>&1
pandoc "${PANDOC_ARGS[@]}" 2>&1
rm -f .companion-print.md

echo "    → book.pdf"
echo "=== Done ==="
