#!/usr/bin/env bash
# Bootstrap fonts/ directory for the LaTeX PDF build.
# Run once per clone:  bash spoilers/bootstrap-fonts.sh
#
# Fetches Source Code Pro (Adobe upstream, static TTFs) and slices
# EB Garamond static instances out of the Google Fonts variable
# font using fontTools. The result is the 8 .ttf files that
# template.tex expects under spoilers/fonts/.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p fonts

# --- Source Code Pro: download the four static instances we need ---
# Adobe ships them as -It (not -Italic); rename for fontspec.
declare -a SCP=(
  "Medium:SourceCodePro-Medium.ttf"
  "MediumIt:SourceCodePro-MediumItalic.ttf"
  "Bold:SourceCodePro-Bold.ttf"
  "BoldIt:SourceCodePro-BoldItalic.ttf"
)
for entry in "${SCP[@]}"; do
  src="${entry%%:*}"
  dst="${entry##*:}"
  if [ ! -f "fonts/$dst" ]; then
    echo "Fetching $dst..."
    curl -sL --fail \
      -o "fonts/$dst" \
      "https://github.com/adobe-fonts/source-code-pro/raw/release/TTF/SourceCodePro-${src}.ttf"
  fi
done

# --- EB Garamond: Google Fonts ships only variable fonts now, so
# slice the four weights we need with fontTools varLib.instancer. ---
VENV_DIR="$SCRIPT_DIR/.venv"
if [ ! -x "$VENV_DIR/bin/fonttools" ]; then
  echo "Creating venv and installing fonttools..."
  python3 -m venv "$VENV_DIR"
  "$VENV_DIR/bin/pip" install --quiet fonttools
fi

declare -a EBG_NEEDS=(
  "EBGaramond.ttf"
  "EBGaramond-Italic.ttf"
  "EBGaramond-Bold.ttf"
  "EBGaramond-BoldItalic.ttf"
)
missing_ebg=0
for f in "${EBG_NEEDS[@]}"; do
  [ -f "fonts/$f" ] || missing_ebg=1
done

if [ $missing_ebg -eq 1 ]; then
  for vf in "EBGaramond%5Bwght%5D.ttf:EBGaramond-VF.ttf" \
            "EBGaramond-Italic%5Bwght%5D.ttf:EBGaramond-Italic-VF.ttf"; do
    src="${vf%%:*}"
    dst="${vf##*:}"
    if [ ! -f "fonts/$dst" ]; then
      echo "Fetching variable $dst..."
      curl -sL --fail \
        -o "fonts/$dst" \
        "https://raw.githubusercontent.com/google/fonts/main/ofl/ebgaramond/$src"
    fi
  done

  echo "Slicing EB Garamond static instances..."
  "$VENV_DIR/bin/fonttools" varLib.instancer \
    -q -o fonts/EBGaramond.ttf fonts/EBGaramond-VF.ttf wght=400
  "$VENV_DIR/bin/fonttools" varLib.instancer \
    -q -o fonts/EBGaramond-Bold.ttf fonts/EBGaramond-VF.ttf wght=700
  "$VENV_DIR/bin/fonttools" varLib.instancer \
    -q -o fonts/EBGaramond-Italic.ttf fonts/EBGaramond-Italic-VF.ttf wght=400
  "$VENV_DIR/bin/fonttools" varLib.instancer \
    -q -o fonts/EBGaramond-BoldItalic.ttf fonts/EBGaramond-Italic-VF.ttf wght=700
fi

echo "Done. fonts/:"
ls -1 fonts/*.ttf | grep -v VF | sed 's,^,  ,'
