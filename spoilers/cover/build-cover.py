#!/usr/bin/env python3
"""Build the Lulu Novella duplex soft-cover PDF for "A Traveller's Companion
to the Mazes of Menace."

Pipeline: render each input SVG to its own PDF (rsvg-convert handles the
font correctly when the source font is installed on the system), then
compose the final 2-page cover by stamping those PDFs onto positioned
rectangles of a black/white background, using PyMuPDF's show_pdf_page().

Page dimensions are taken from the Lulu template
(Novella-Duplex-Soft-Cover.pdf):

  Page: 789.746 x 594 pt  (10.969" x 8.25", 0.125" bleed all around)
  Trim: (9, 9) to (780.746, 585)
  Spine fold: x = 369 to 420.746  (width 51.746)
  Back trim: 9..369    (5")
  Front trim: 420.746..780.746  (5")
  Safety inset from trim: 13.536 pt
"""

from pathlib import Path
import re
import shutil
import subprocess
import sys

import fitz  # PyMuPDF

HERE = Path(__file__).parent
TMP = HERE / "build"        # working dir for per-SVG PDFs
TMP.mkdir(exist_ok=True)

# ---- template-derived dimensions ----
PAGE_W = 789.746
PAGE_H = 594.0
BLEED = 9.0
SPINE_LEFT = 369.0
SPINE_RIGHT = 420.746
SPINE_W = SPINE_RIGHT - SPINE_LEFT
BACK_LEFT = BLEED
BACK_RIGHT = SPINE_LEFT
FRONT_LEFT = SPINE_RIGHT
FRONT_RIGHT = PAGE_W - BLEED
TRIM_TOP = BLEED
TRIM_BOTTOM = PAGE_H - BLEED
SAFETY_INSET = 13.536

TITLE_LINE1 = "A Traveller's Companion"
TITLE_LINE2 = "to the Mazes of Menace"
GARAMOND = "EB Garamond,Garamond,Georgia,serif"


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def svg_to_pdf_rsvg(svg_path: Path, pdf_path: Path):
    """Render an SVG to PDF using rsvg-convert. Good for SVGs that rely on
    system fonts (e.g. EB Garamond title, generated cover frame)."""
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
        check=True, capture_output=True)


def svg_to_pdf_chrome(svg_path: Path, pdf_path: Path, width_pt=None, height_pt=None):
    """Render an SVG to PDF using headless Chrome. Crucially, Chrome HONORS
    @font-face declarations with embedded woff2 — which is what the NetHack
    ASCII-art SVGs need for character-by-character x-alignment."""
    args = [
        CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
    ]
    args.append(f"file://{svg_path.resolve()}")
    subprocess.run(args, check=True, capture_output=True)


def get_svg_size(svg_path: Path):
    """Return (width_px, height_px) of an SVG."""
    text = svg_path.read_text(errors='replace')
    m = re.match(r'\s*(?:<\?xml[^>]*\?>\s*)?<svg\b([^>]*)>', text, re.DOTALL)
    attrs = m.group(1) if m else ''
    vb_m = re.search(r'viewBox\s*=\s*"\s*[\d.eE+-]+\s+[\d.eE+-]+\s+([\d.eE+-]+)\s+([\d.eE+-]+)\s*"', attrs)
    if vb_m:
        return float(vb_m.group(1)), float(vb_m.group(2))
    w = re.search(r'\bwidth\s*=\s*"([\d.eE+-]+)', attrs)
    h = re.search(r'\bheight\s*=\s*"([\d.eE+-]+)', attrs)
    return (float(w.group(1)) if w else 100.0,
            float(h.group(1)) if h else 100.0)


def prepare(name: str, svg: Path, renderer="rsvg") -> tuple[Path, float, float]:
    """Render SVG to PDF using the given renderer ("rsvg" or "chrome"),
    return (pdf, viewbox_w, viewbox_h)."""
    pdf = TMP / f"{name}.pdf"
    if renderer == "chrome":
        svg_to_pdf_chrome(svg, pdf)
    else:
        svg_to_pdf_rsvg(svg, pdf)
    w, h = get_svg_size(svg)
    return pdf, w, h


def crop_pdf_to_viewbox(pdf_path: Path, vb_w: float, vb_h: float, out_path: Path):
    """Chrome adds page margins and lays the SVG at the top-left of a
    full US-letter page (612x792 by default). Crop to the SVG content
    (assumed at origin)."""
    src = fitz.open(pdf_path)
    page = src[0]
    # Chrome at default settings renders SVG at its viewBox size in pt (1px = 0.75pt),
    # so we need to know what scale Chrome used. Default Chrome print is 96 DPI:
    # 1 SVG px = 0.75 pt. Our viewBox is in SVG px, so cropped rect = vb_w*0.75 x vb_h*0.75.
    crop_w = vb_w * 0.75
    crop_h = vb_h * 0.75
    page.set_cropbox(fitz.Rect(0, 0, crop_w, crop_h))
    src.save(str(out_path))
    src.close()


def fit_into(box_w, box_h, content_w, content_h):
    """Compute (x_offset, y_offset, fit_w, fit_h) when content is scaled
    proportionally to fit a (box_w, box_h) area centered."""
    scale = min(box_w / content_w, box_h / content_h)
    fit_w = content_w * scale
    fit_h = content_h * scale
    return ((box_w - fit_w) / 2, (box_h - fit_h) / 2, fit_w, fit_h)


def main():
    # 1. Render each input SVG to its own PDF.
    # The two NetHack ASCII screenshots NEED Chrome rendering to honor the
    # embedded woff2 DejaVu Sans Mono font (character-precise x-alignment
    # depends on it). rsvg-convert produces drift because it uses the system
    # DejaVu whose metrics don't match the embedded version.
    castle_raw, castle_w, castle_h = prepare("front-castle", HERE / "front-castle.svg", renderer="chrome")
    sanctum_raw, sanctum_w, sanctum_h = prepare("back-sanctum", HERE / "back-sanctum.svg", renderer="chrome")
    # The other diagrams are vector primitives (no monospace tracking required);
    # rsvg-convert handles them fine.
    flow_pdf, flow_w, flow_h = prepare("flowchart", HERE / "flowchart.svg")
    d0_pdf, d0_w, d0_h = prepare("dmap0", HERE / "dmap-0-dungeons-of-doom-map.svg")
    d1_pdf, d1_w, d1_h = prepare("dmap1", HERE / "dmap-1-gehennom-map.svg")
    d2_pdf, d2_w, d2_h = prepare("dmap2", HERE / "dmap-2-elemental-planes-and-ascension.svg")

    # Chrome embeds the SVG on a US-letter page with margins. Crop to viewBox.
    castle_pdf = TMP / "front-castle-crop.pdf"
    sanctum_pdf = TMP / "back-sanctum-crop.pdf"
    crop_pdf_to_viewbox(castle_raw, castle_w, castle_h, castle_pdf)
    crop_pdf_to_viewbox(sanctum_raw, sanctum_w, sanctum_h, sanctum_pdf)
    # show_pdf_page uses the cropbox dimensions; recompute logical w/h in pt:
    castle_w *= 0.75; castle_h *= 0.75
    sanctum_w *= 0.75; sanctum_h *= 0.75

    out = fitz.open()

    # ===== PAGE 1: OUTSIDE COVER (BLACK) =====
    page1 = out.new_page(width=PAGE_W, height=PAGE_H)
    page1.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=(0, 0, 0), fill=(0, 0, 0))

    # ---- Back cover (left panel): sanctum SVG centered ----
    bx = BACK_LEFT + SAFETY_INSET
    by = TRIM_TOP + SAFETY_INSET + 30
    bw = (BACK_RIGHT - SAFETY_INSET) - bx
    bh = (TRIM_BOTTOM - SAFETY_INSET - 30) - by
    ox, oy, fw, fh = fit_into(bw, bh, sanctum_w, sanctum_h)
    with fitz.open(sanctum_pdf) as src:
        page1.show_pdf_page(fitz.Rect(bx + ox, by + oy, bx + ox + fw, by + oy + fh), src, 0)

    # ---- Title and spine: render via an SVG → PDF intermediate so we can
    # use Garamond (which rsvg-convert can find via the system font cache).
    # PyMuPDF's builtin fonts don't include Garamond.
    spine_cx = (SPINE_LEFT + SPINE_RIGHT) / 2
    spine_text = f"{TITLE_LINE1} {TITLE_LINE2}"
    spine_y_start = TRIM_TOP + 60
    title_x = FRONT_LEFT + SAFETY_INSET + 8
    title_y = TRIM_TOP + SAFETY_INSET + 36 + 20    # baseline for first line
    title_size = 26
    title_leading = 30
    spine_size = 14

    title_svg = TMP / "title.svg"
    title_svg.write_text(
        f'<?xml version="1.0"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{PAGE_W}pt" height="{PAGE_H}pt" '
        f'viewBox="0 0 {PAGE_W} {PAGE_H}">'
        # Front-cover title (left-justified, broken before "to")
        f'<text x="{title_x}" y="{title_y}" fill="white" '
        f'font-family="{GARAMOND}" font-size="{title_size}">'
        f'{TITLE_LINE1}</text>'
        f'<text x="{title_x}" y="{title_y + title_leading}" fill="white" '
        f'font-family="{GARAMOND}" font-size="{title_size}">'
        f'{TITLE_LINE2}</text>'
        # Spine title (rotated +90°, reads top→bottom)
        f'<g transform="translate({spine_cx + spine_size/3}, {spine_y_start}) rotate(90)">'
        f'<text x="0" y="0" fill="white" '
        f'font-family="{GARAMOND}" font-size="{spine_size}">'
        f'{spine_text}</text></g>'
        f'</svg>')
    title_pdf = TMP / "title.pdf"
    svg_to_pdf_rsvg(title_svg, title_pdf)
    with fitz.open(title_pdf) as src:
        page1.show_pdf_page(fitz.Rect(0, 0, PAGE_W, PAGE_H), src, 0)

    # Castle artwork
    fx = FRONT_LEFT + SAFETY_INSET
    fy = title_y + 2 * title_leading + 30
    fw_box = (FRONT_RIGHT - SAFETY_INSET) - fx
    fh_box = (TRIM_BOTTOM - SAFETY_INSET) - fy
    ox, oy, fw, fh = fit_into(fw_box, fh_box, castle_w, castle_h)
    with fitz.open(castle_pdf) as src:
        page1.show_pdf_page(fitz.Rect(fx + ox, fy + oy, fx + ox + fw, fy + oy + fh), src, 0)

    # ===== PAGE 2: INSIDE COVER (WHITE) =====
    page2 = out.new_page(width=PAGE_W, height=PAGE_H)
    page2.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=(1, 1, 1), fill=(1, 1, 1))

    # ---- Inside FRONT cover (left panel): dungeon maps stacked ----
    ifc_l = BACK_LEFT + SAFETY_INSET
    ifc_t = TRIM_TOP + SAFETY_INSET
    ifc_w = (BACK_RIGHT - SAFETY_INSET) - ifc_l
    ifc_h = (TRIM_BOTTOM - SAFETY_INSET) - ifc_t

    # Stack the three dungeon maps (all viewbox width 760) proportionally
    scale_w = ifc_w / 760.0
    total_h = (d0_h + d1_h + d2_h) * scale_w
    if total_h > ifc_h:
        scale = ifc_h / (d0_h + d1_h + d2_h)
    else:
        scale = scale_w
    stack_w = 760 * scale
    stack_x = ifc_l + (ifc_w - stack_w) / 2
    stack_y = ifc_t
    y = stack_y
    for pdf, hh in ((d0_pdf, d0_h), (d1_pdf, d1_h), (d2_pdf, d2_h)):
        h_scaled = hh * scale
        with fitz.open(pdf) as src:
            page2.show_pdf_page(fitz.Rect(stack_x, y, stack_x + stack_w, y + h_scaled), src, 0)
        y += h_scaled

    # ---- Inside BACK cover (right panel): identification flowchart ----
    ibc_l = FRONT_LEFT + SAFETY_INSET
    ibc_t = TRIM_TOP + SAFETY_INSET
    ibc_w = (FRONT_RIGHT - SAFETY_INSET) - ibc_l
    ibc_h = (TRIM_BOTTOM - SAFETY_INSET) - ibc_t
    ox, oy, fw, fh = fit_into(ibc_w, ibc_h, flow_w, flow_h)
    with fitz.open(flow_pdf) as src:
        page2.show_pdf_page(fitz.Rect(ibc_l + ox, ibc_t + oy, ibc_l + ox + fw, ibc_t + oy + fh), src, 0)

    final = HERE / "cover.pdf"
    out.save(str(final))
    out.close()
    print(f"Wrote {final} ({final.stat().st_size} bytes)")


if __name__ == '__main__':
    main()
