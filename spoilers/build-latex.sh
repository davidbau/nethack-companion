#!/usr/bin/env bash
# Build script for "A Traveler's Companion to the Mazes of Menace"
# LaTeX pipeline: companion.md → pandoc + lua filter → xelatex → book.pdf
#
# Usage:
#   ./build-latex.sh        # color dungeon overview map → book.pdf
#   ./build-latex.sh --bw   # monochrome map for print    → book-bw.pdf
#
# The BW variant is what build-book2.py picks up so the coil-bound
# inside-leaf maps and the in-book "Lay of the Land" map are both
# rendered in the same all-black-on-white treatment.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

BW=0
if [ "${1:-}" = "--bw" ]; then
  BW=1
fi

if [ "$BW" = "1" ]; then
  OUTPUT_PDF=book-bw.pdf
  DMAP_SUFFIX=-bw
else
  OUTPUT_PDF=book.pdf
  DMAP_SUFFIX=
fi

# Check dependencies
if ! command -v pandoc &>/dev/null; then
  echo "Error: pandoc not found. Install with: brew install pandoc" >&2
  exit 1
fi

if ! command -v xelatex &>/dev/null; then
  echo "Error: xelatex not found. Install with: brew install --cask mactex" >&2
  exit 1
fi

echo "=== Building $OUTPUT_PDF via LaTeX ==="

# Make sure the dungeon-map PDFs are present and current.
if [ "$BW" = "1" ]; then
  if [ ! -f images/dmap-dod-bw.pdf ] || [ companion.md -nt images/dmap-dod-bw.pdf ]; then
    python3 dungeon_map.py --bw-pdfs images
  fi
else
  if [ ! -f images/dmap-dod.pdf ] || [ companion.md -nt images/dmap-dod.pdf ]; then
    python3 dungeon_map.py --pdfs
  fi
fi

# Make sure the identification-flowchart PDF is present and current.
# The SVG source lives in cover/ alongside the cover-art SVGs; the
# print build includes the rendered PDF directly. (build-cover.py
# also produces this file, but the main book build needs it
# whether or not the cover has been built.)
if [ ! -f cover/build/flowchart.pdf ] || [ cover/flowchart.svg -nt cover/build/flowchart.pdf ]; then
  if ! command -v rsvg-convert &>/dev/null; then
    echo "Error: rsvg-convert not found. Install with: brew install librsvg" >&2
    exit 1
  fi
  mkdir -p cover/build
  rsvg-convert -f pdf -o cover/build/flowchart.pdf cover/flowchart.svg
fi

# Print version drops web-only asides ("or more likely scrolling
# through" — true in a browser, false on paper). Anything that's
# accurate-on-screen-only-and-wrong-in-print belongs in this sed.
sed -e 's/ (or more likely scrolling through)//' companion.md > .companion-print.md

# Replace the inline-SVG dungeon map block with markdown image
# references to the PDFs that dungeon_map.py wrote. Pandoc turns
# these into \begin{figure}\includegraphics... blocks that LaTeX
# pages correctly. DMAP_SUFFIX controls color vs BW.
DMAP_SUFFIX="$DMAP_SUFFIX" python3 - <<'PY'
import os
import re
from pathlib import Path
suffix = os.environ.get('DMAP_SUFFIX', '')
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
    # A5 text area is 7.018 in tall. At width 4.12 in (3% up from
    # the original 4.0 in), the DoD+Geh stack is about 7.00 in
    # tall, sitting just inside the text area with a thin slack
    # margin. (We use \centerline rather than the center env so
    # there's no env padding eating that budget.) The Planes
    # figure on the facing page uses the same width and so scales
    # in matching proportion.
DMAP_WIDTH = "4.12in"
replacement = (
    '\n\n```{=latex}\n'
    '\\begingroup\\setlength{\\parskip}{0pt}\n'
    '\\centerline{\\vbox{\\offinterlineskip%\n'
    f'  \\hbox{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-dod{suffix}.pdf}}}}%\n'
    f'  \\hbox{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-geh{suffix}.pdf}}}}%\n'
    '}}\n'
    '\\endgroup\n'
    '\\clearpage\n'
    f'\\centerline{{\\includegraphics[width={DMAP_WIDTH}]{{images/dmap-planes{suffix}.pdf}}}}\n'
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
  --output=$OUTPUT_PDF
)

# Two-pass build: first pass writes the .aux file (labels and pages);
# second pass uses it to resolve cross-references like the index's
# \pageref calls. Without this, page numbers in the index will be
# stale (showing values from a previous build, or ?? on a fresh build).
pandoc "${PANDOC_ARGS[@]}" 2>&1
pandoc "${PANDOC_ARGS[@]}" 2>&1
rm -f .companion-print.md

echo "    → $OUTPUT_PDF"
echo "=== Done ==="
