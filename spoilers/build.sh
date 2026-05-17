#!/usr/bin/env bash
# Build script for "A Traveler's Companion to the Mazes of Menace"
# Converts companion.md → index.html → companion.pdf
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR="$SCRIPT_DIR/.venv"
WEASYPRINT="$VENV_DIR/bin/weasyprint"

# Check dependencies
if ! command -v pandoc &>/dev/null; then
  echo "Error: pandoc not found. Install with: brew install pandoc" >&2
  exit 1
fi

echo "=== Building HTML ==="
pandoc companion.md \
  --from=markdown \
  --to=html5 \
  --template=template.html \
  --section-divs \
  --syntax-highlighting=none \
  --output=index.html

echo "    → index.html"

if [ -x "$WEASYPRINT" ]; then
  echo "=== Building PDF ==="
  # Print version drops web-only asides ("or more likely scrolling
  # through" — true in a browser, false on paper). Anything that's
  # accurate-on-screen-only-and-wrong-in-print belongs in this sed.
  sed -e 's/ (or more likely scrolling through)//' companion.md > .companion-print.md
  pandoc .companion-print.md \
    --from=markdown \
    --to=html5 \
    --template=template.html \
    --section-divs \
    --syntax-highlighting=none \
    --output=.companion-print.html
  "$WEASYPRINT" .companion-print.html companion.pdf 2>&1 | grep -v "^$" || true
  rm -f .companion-print.md .companion-print.html
  echo "    → companion.pdf"
else
  echo "(PDF skipped: weasyprint not found in .venv. To enable:"
  echo "   python3 -m venv .venv && .venv/bin/pip install weasyprint)"
fi

echo "=== Done ==="
