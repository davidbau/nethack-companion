#!/usr/bin/env python3
"""Build book2.pdf — book.pdf extended with the inside-cover artwork
from cover.pdf as new first and last pages.

The coil-bound exterior cover (cover2.pdf) has no interior. If you
print book2.pdf as the bound block alongside cover2.pdf, the bound
block's first and last pages carry the inside-cover artwork that
the coil cover can't.

Page assembly:
  book2 page 1:         inside-FRONT-cover artwork  (left  panel of cover.pdf p2)
  book2 pages 2..N+1:   book.pdf pages 1..N
  book2 page N+2:       inside-BACK-cover artwork   (right panel of cover.pdf p2)
"""

from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).parent
SPOILERS = HERE.parent
BOOK = SPOILERS / "book.pdf"
COVER = SPOILERS / "cover.pdf"
OUT = SPOILERS / "book2.pdf"

# cover.pdf p2 layout (top-left origin, PDF points):
#   Page:        789.746 x 594  (10.969" x 8.25", 0.125" bleed all sides)
#   Bleed:       9 pt
#   Spine:       x = 369 .. 420.746
#   Left panel  (inside FRONT cover): x = 9..369,         y = 9..585
#   Right panel (inside BACK cover):  x = 420.746..780.746, y = 9..585
# Each panel's trim is 360 x 576 pt = 5" x 8", which matches book.pdf.
PAGE_W_COVER = 789.746
PAGE_H_COVER = 594.0
BLEED = 9.0
SPINE_LEFT = 369.0
SPINE_RIGHT = 420.746
LEFT_PANEL  = fitz.Rect(BLEED,       BLEED, SPINE_LEFT,             PAGE_H_COVER - BLEED)
RIGHT_PANEL = fitz.Rect(SPINE_RIGHT, BLEED, PAGE_W_COVER - BLEED,   PAGE_H_COVER - BLEED)

BOOK_W = 360.0
BOOK_H = 576.0


def extract_panel(cover_doc, page_num: int, clip_rect: fitz.Rect):
    """Render a clipped region of cover_doc[page_num] onto a fresh
    BOOK_W x BOOK_H page, scaled to fill the new page."""
    out = fitz.open()
    page = out.new_page(width=BOOK_W, height=BOOK_H)
    page.show_pdf_page(
        fitz.Rect(0, 0, BOOK_W, BOOK_H),
        cover_doc, page_num,
        clip=clip_rect,
    )
    return out


def main():
    if not BOOK.exists():
        raise SystemExit(f"missing: {BOOK}; run build-latex.sh first")
    if not COVER.exists():
        raise SystemExit(f"missing: {COVER}; run cover/build-cover.py first")

    cover = fitz.open(COVER)
    book = fitz.open(BOOK)

    inside_front = extract_panel(cover, 1, LEFT_PANEL)
    inside_back  = extract_panel(cover, 1, RIGHT_PANEL)

    out = fitz.open()
    out.insert_pdf(inside_front)
    out.insert_pdf(book)
    out.insert_pdf(inside_back)
    out.save(str(OUT))

    n = out.page_count
    out.close()
    cover.close()
    book.close()
    inside_front.close()
    inside_back.close()

    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {n} pages)")


if __name__ == '__main__':
    main()
