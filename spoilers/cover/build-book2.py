#!/usr/bin/env python3
"""Build book2.pdf — book.pdf extended with the inside-cover artwork
from cover.pdf as new first and last pages.

The coil-bound exterior cover (cover2.pdf) has no interior. If you
print book2.pdf as the bound block alongside cover2.pdf, the bound
block's first and last pages carry the inside-cover artwork that
the coil cover can't.

Both new pages go at the END to keep book.pdf's odd/even (recto/verso)
parity intact. If book.pdf has an odd page count, a blank is inserted
before the inside-cover panels so they always land together on a fresh
leaf (recto + verso), never split across two physical leaves.

Page assembly:
  book2 pages 1..N:     book.pdf pages 1..N
  book2 page N+1:       blank (only when N is odd)
  book2 page (N+1|N+2): inside-FRONT-cover artwork  (left  panel of cover.pdf p2)
  book2 page (N+2|N+3): inside-BACK-cover artwork   (right panel of cover.pdf p2)
"""

from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).parent
SPOILERS = HERE.parent
BOOK = SPOILERS / "book.pdf"
COVER = SPOILERS / "cover.pdf"
OUT = SPOILERS / "book2.pdf"

# Book trim is A5: 148 × 210 mm = 419.528 × 595.276 pt (1 mm = 2.83465 pt).
BOOK_W = 419.528
BOOK_H = 595.276

# cover.pdf p2 layout (top-left origin, PDF points). Computed live from
# the source PDF so that the panel rects stay in sync if build-cover.py
# changes its dimensions (e.g. when the spine width is re-templated).
#   Layout: bleed | back panel (A5) | spine | front panel (A5) | bleed
BLEED = 9.0
COVER_PANEL_W = BOOK_W
COVER_PANEL_H = BOOK_H


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

    # Derive panel rectangles from cover.pdf p2 dimensions, so the
    # extraction tracks any spine-width change. Layout:
    #   bleed | back panel | spine | front panel | bleed
    cover_w = cover[1].rect.width
    cover_h = cover[1].rect.height
    spine_w = cover_w - 2 * BLEED - 2 * COVER_PANEL_W
    spine_left = BLEED + COVER_PANEL_W
    spine_right = spine_left + spine_w
    left_panel = fitz.Rect(BLEED, BLEED, spine_left, cover_h - BLEED)
    right_panel = fitz.Rect(spine_right, BLEED, cover_w - BLEED, cover_h - BLEED)

    inside_front = extract_panel(cover, 1, left_panel)
    inside_back  = extract_panel(cover, 1, right_panel)

    out = fitz.open()
    out.insert_pdf(book)
    if book.page_count % 2 == 1:
        out.new_page(width=BOOK_W, height=BOOK_H)
    out.insert_pdf(inside_front)
    out.insert_pdf(inside_back)
    # PyMuPDF's insert_font embeds the full TTF; the cover panels'
    # embedded Garamond doubles the file size when both panels are
    # included verbatim. Subset to just the glyphs actually used.
    out.subset_fonts()
    out.save(str(OUT), garbage=4, deflate=True, clean=True)

    n = out.page_count
    out.close()
    cover.close()
    book.close()
    inside_front.close()
    inside_back.close()

    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {n} pages)")


if __name__ == '__main__':
    main()
