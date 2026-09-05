#!/usr/bin/env python3
"""Catch shifted box-drawing walls in fenced ASCII maps.

The checker deliberately looks only at rooms with matching box corners.
Sokoban maps and irregular dungeon sketches may have different row widths,
but a room's left and right walls must stay in the columns established by
its top and bottom borders.  A missing wall is allowed for a doorway; a wall
that has slid one column is not.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


FENCE = re.compile(r"^```[^\n]*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
CORNER_PAIRS = (("┌", "┐", "└", "┘"), ("┏", "┓", "┗", "┛"))
VERTICAL = {"│", "┃"}


def check_block(text: str, first_line: int, block_number: int) -> list[str]:
    lines = text.splitlines()
    errors: list[str] = []
    for top_left, top_right, bottom_left, bottom_right in CORNER_PAIRS:
        for top_index, line in enumerate(lines):
            left = line.find(top_left)
            right = line.find(top_right, left + 1)
            if left < 0 or right < 0:
                continue
            for bottom_index in range(top_index + 1, len(lines)):
                bottom = lines[bottom_index]
                if (bottom.find(bottom_left) != left
                        or bottom.find(bottom_right, left + 1) != right):
                    continue
                for row_index in range(top_index + 1, bottom_index):
                    row = lines[row_index]
                    for column, side in ((left, "left"), (right, "right")):
                        actual = row[column] if column < len(row) else "<end>"
                        if actual in VERTICAL:
                            continue
                        # A doorway may interrupt a wall. A vertical glyph
                        # immediately beside the expected column is instead
                        # the characteristic one-column drift this catches.
                        next_char = row[column + 1] if column + 1 < len(row) else ""
                        if next_char in VERTICAL:
                            errors.append(
                                f"block {block_number}, source line "
                                f"{first_line + row_index}: {side} wall "
                                f"shifted from column {column + 1} to "
                                f"{column + 2}"
                            )
                break
    return errors


def main(path: str) -> int:
    source = Path(path).read_text()
    errors: list[str] = []
    for number, match in enumerate(FENCE.finditer(source), 1):
        first_line = source.count("\n", 0, match.start()) + 2
        if any(c in match.group(1) for c in "┌┐└┘┏┓┗┛"):
            errors.extend(check_block(match.group(1), first_line, number))
    if errors:
        print("ASCII map check failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("ASCII map check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "companion.md"))
