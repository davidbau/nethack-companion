#!/usr/bin/env bash
# One-shot setup for the build pipeline.
#
# Fetches the NetHack 5.0 C source as a git submodule into
# nethack-c/upstream/. The appendix builders
# (build_armor_appendix.py, build_bestiary_appendix.py,
# build_weapons_appendix.py) read from there to regenerate
# the data tables in companion.md.
#
# build.sh and build-latex.sh themselves do not need the submodule;
# they only need Pandoc and (for LaTeX) xelatex. Run those after
# this setup if you intend to re-derive the appendices.

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Initializing nethack-c/upstream submodule ==="
git submodule update --init --recursive nethack-c/upstream

echo
echo "Pinned to:"
( cd nethack-c/upstream && git describe --tags --always )

echo
echo "Setup complete. The build pipeline lives in spoilers/:"
echo "  python3 spoilers/build_armor_appendix.py"
echo "  python3 spoilers/build_weapons_appendix.py"
echo "  python3 spoilers/build_bestiary_appendix.py"
echo
echo "Or to rebuild the rendered book:"
echo "  spoilers/build.sh              # HTML"
echo "  spoilers/build-latex.sh        # PDF (needs xelatex)"
