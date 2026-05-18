#!/bin/bash
# Pull the latest spoilers content from the public authority
# (davidbau/nethack-companion) into this working copy.
#
# The teleport repo's spoilers/ directory is a downstream copy of
# https://github.com/davidbau/nethack-companion — that repo is the
# public source of truth for the book. Local edits here should be
# pushed there first, then synced back via this script.
#
# Usage:
#   bash spoilers/sync-from-companion.sh
#
# What it does:
#   1. Fetches the latest main of nethack-companion into a temp dir.
#   2. Rsyncs everything (minus .git, build artifacts) into spoilers/.
#   3. Prints a diff summary so you can decide whether to commit.
#
# It does NOT touch maud-specific files (e.g. anything outside
# spoilers/) and does NOT commit.

set -e

REPO_URL="git@github.com:davidbau/nethack-companion.git"
DEST="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Fetching latest from $REPO_URL ..."
git clone --depth=1 --quiet "$REPO_URL" "$TMP/nh"

echo "Syncing into $DEST ..."
rsync -a --delete \
  --exclude='.git/' \
  --exclude='sync-from-companion.sh' \
  --exclude='cover/build/' \
  --exclude='cover/template.pdf' \
  --exclude='cover/template-qdf.pdf' \
  "$TMP/nh/" "$DEST/"

echo
echo "Done. Changes in spoilers/:"
( cd "$(git -C "$DEST" rev-parse --show-toplevel)" && git status --short spoilers/ )
echo
echo "Review with: git diff spoilers/"
echo "Commit with: git add spoilers/ && git commit"
