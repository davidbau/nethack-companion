#!/usr/bin/env python3
"""Build a coil-bound exterior cover PDF (cover2.pdf).

Single-page exterior cover for spiral / coil binding. No spine — the
back cover panel sits directly against the front cover panel at the
page center line.

Dimensions: A5 (148 × 210 mm = 419.528 × 595.276 pt) trim per panel,
0.125" bleed all around, no spine — back panel meets front panel
at the page centre line.

  Each panel trim:      A5 = 419.528 x 595.276 pt
  Bleed:                9 pt = 0.125" all sides
  Page (with bleed):    2*A5w + 2*bleed  x  A5h + 2*bleed
                        = 857.056 x 613.276 pt
  Centre line:          back ends / front begins
  Safety margin:        36 pt (0.5" from trim edge)

Re-uses the intermediate PDFs left in cover/build/ by build-cover.py
when those exist; otherwise renders them on the fly via rsvg-convert
or headless Chrome the same way build-cover.py does.
"""

from pathlib import Path
import re
import subprocess
import sys

import fitz  # PyMuPDF

HERE = Path(__file__).parent
TMP = HERE / "build"
TMP.mkdir(exist_ok=True)

# ---- A5 coil-no-spine template dimensions ----
A5_W = 419.528  # 148 mm
A5_H = 595.276  # 210 mm
BLEED = 9.0
PAGE_W = 2 * A5_W + 2 * BLEED    # 857.056 pt
PAGE_H = A5_H + 2 * BLEED        # 613.276 pt
CENTER_X = PAGE_W / 2.0          # back/front boundary, no spine
BACK_LEFT = BLEED
BACK_RIGHT = CENTER_X
FRONT_LEFT = CENTER_X
FRONT_RIGHT = PAGE_W - BLEED
TRIM_TOP = BLEED
TRIM_BOTTOM = PAGE_H - BLEED
SAFETY_INSET = 36.0              # 0.5" from trim edge

TITLE_LINE1 = "A Traveller's Companion"
TITLE_LINE2_PARTS = ('to the Mazes of', 'Menace')
GARAMOND = "EB Garamond,Garamond,Georgia,serif"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Status-line and message-line crop thresholds (SVG pixels), matching
# build-cover.py's TOP_CLIP / BOTTOM_CLIP.
TOP_CLIP = 56
BOTTOM_CLIP = 47


def svg_to_pdf_rsvg(svg_path: Path, pdf_path: Path):
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
        check=True, capture_output=True)


def svg_to_pdf_chrome(svg_path: Path, pdf_path: Path):
    text = svg_path.read_text()
    m = re.search(r'viewBox\s*=\s*"\s*[\d.eE+-]+\s+[\d.eE+-]+\s+([\d.eE+-]+)\s+([\d.eE+-]+)\s*"', text)
    vb_w, vb_h = (float(m.group(1)), float(m.group(2))) if m else (749, 456)
    page_w_in = vb_w / 96.0
    page_h_in = vb_h / 96.0
    html_path = pdf_path.with_suffix(".html")
    html_path.write_text(
        f'<!doctype html>'
        f'<html><head><meta charset="utf-8"><style>'
        f'@page {{ size: {page_w_in:.6f}in {page_h_in:.6f}in; margin: 0; }} '
        f'html, body {{ margin: 0; padding: 0; background: transparent; }} '
        f'svg {{ display: block; }}'
        f'</style></head><body>{text}</body></html>',
        encoding='utf-8')
    args = [
        CHROME, "--headless", "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path.resolve()}",
    ]
    subprocess.run(args, check=True, capture_output=True)


def get_svg_size(svg_path: Path):
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


def prepare(name: str, svg: Path, renderer="rsvg"):
    pdf = TMP / f"{name}.pdf"
    if not pdf.exists() or pdf.stat().st_mtime < svg.stat().st_mtime:
        if renderer == "chrome":
            svg_to_pdf_chrome(svg, pdf)
        else:
            svg_to_pdf_rsvg(svg, pdf)
    w, h = get_svg_size(svg)
    return pdf, w, h


def crop_pdf_to_viewbox(pdf_path: Path, vb_w: float, vb_h: float,
                        out_path: Path, top_px=0, bottom_px=0):
    src = fitz.open(pdf_path)
    page = src[0]
    px_to_pt = 0.75
    top_pt = top_px * px_to_pt
    bottom_pt = (vb_h - bottom_px) * px_to_pt
    crop_w = vb_w * px_to_pt
    mb = page.mediabox
    crop_w = min(crop_w, mb.width)
    bottom_pt = min(bottom_pt, mb.height)
    page.set_cropbox(fitz.Rect(0, top_pt, crop_w, bottom_pt))
    src.save(str(out_path))
    src.close()


def main():
    castle_raw,  castle_w,  castle_h  = prepare("front-castle",   HERE / "front-castle.svg",   renderer="chrome")
    sanctum_raw, sanctum_w, sanctum_h = prepare("back-sanctum",   HERE / "back-sanctum.svg",   renderer="chrome")
    dlvl5_raw,   dlvl5_w,   dlvl5_h   = prepare("level-dlvl5",    HERE / "level-dlvl5.svg",    renderer="chrome")
    gehmaze_raw, gehmaze_w, gehmaze_h = prepare("level-gehennom", HERE / "level-gehennom.svg", renderer="chrome")
    medusa_raw,  medusa_w,  medusa_h  = prepare("level-medusa",   HERE / "level-medusa.svg",   renderer="chrome")

    castle_pdf  = TMP / "front-castle-crop.pdf"
    sanctum_pdf = TMP / "back-sanctum-crop.pdf"
    dlvl5_pdf   = TMP / "level-dlvl5-crop.pdf"
    gehmaze_pdf = TMP / "level-gehennom-crop.pdf"
    medusa_pdf  = TMP / "level-medusa-crop.pdf"
    for raw, w, h, dst in (
        (castle_raw,  castle_w,  castle_h,  castle_pdf),
        (sanctum_raw, sanctum_w, sanctum_h, sanctum_pdf),
        (dlvl5_raw,   dlvl5_w,   dlvl5_h,   dlvl5_pdf),
        (gehmaze_raw, gehmaze_w, gehmaze_h, gehmaze_pdf),
        (medusa_raw,  medusa_w,  medusa_h,  medusa_pdf),
    ):
        if not dst.exists() or dst.stat().st_mtime < raw.stat().st_mtime:
            crop_pdf_to_viewbox(raw, w, h, dst, top_px=TOP_CLIP, bottom_px=BOTTOM_CLIP)
    # Convert SVG-pixel dimensions to PDF points (1 SVG px = 0.75 pt at 96 DPI),
    # accounting for the top/bottom crop.
    castle_w,  castle_h  = castle_w  * 0.75, (castle_h  - TOP_CLIP - BOTTOM_CLIP) * 0.75
    sanctum_w, sanctum_h = sanctum_w * 0.75, (sanctum_h - TOP_CLIP - BOTTOM_CLIP) * 0.75
    dlvl5_w,   dlvl5_h   = dlvl5_w   * 0.75, (dlvl5_h   - TOP_CLIP - BOTTOM_CLIP) * 0.75
    gehmaze_w, gehmaze_h = gehmaze_w * 0.75, (gehmaze_h - TOP_CLIP - BOTTOM_CLIP) * 0.75
    medusa_w,  medusa_h  = medusa_w  * 0.75, (medusa_h  - TOP_CLIP - BOTTOM_CLIP) * 0.75

    out = fitz.open()
    page = out.new_page(width=PAGE_W, height=PAGE_H)
    page.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=(0, 0, 0), fill=(0, 0, 0))

    # ---- Back cover (left panel): three maps stacked ----
    bx = BACK_LEFT + SAFETY_INSET
    by = TRIM_TOP + SAFETY_INSET + 30
    bw = (BACK_RIGHT - SAFETY_INSET) - bx
    bh = (TRIM_BOTTOM - SAFETY_INSET - 30) - by
    back_maps = [
        (medusa_pdf,  medusa_w,  medusa_h),
        (gehmaze_pdf, gehmaze_w, gehmaze_h),
        (sanctum_pdf, sanctum_w, sanctum_h),
    ]
    MAP_GAP_PT = 26
    n_gaps = len(back_maps) - 1
    total_native_h = sum(h for _, _, h in back_maps)
    max_native_w = max(w for _, w, _ in back_maps)
    scale = min((bh - n_gaps * MAP_GAP_PT) / total_native_h, bw / max_native_w)
    stack_w = max_native_w * scale
    stack_h_total = total_native_h * scale + n_gaps * MAP_GAP_PT
    stack_x = bx + (bw - stack_w) / 2
    stack_y = by + (bh - stack_h_total) / 2
    y = stack_y
    for i, (pdf, mw, mh) in enumerate(back_maps):
        h_scaled = mh * scale
        w_scaled = mw * scale
        x = stack_x + (stack_w - w_scaled) / 2
        with fitz.open(pdf) as src:
            page.show_pdf_page(fitz.Rect(x, y, x + w_scaled, y + h_scaled), src, 0)
        y += h_scaled
        if i < n_gaps:
            y += MAP_GAP_PT

    # ---- Front cover (right panel): title plus two maps ----
    title_x = FRONT_LEFT + SAFETY_INSET + 8
    title_y = TRIM_TOP + SAFETY_INSET + 36 + 20
    title_size = 26
    title_leading = 30

    title_svg = TMP / "title-cover2.svg"
    title_svg.write_text(
        f'<?xml version="1.0"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{PAGE_W}pt" height="{PAGE_H}pt" '
        f'viewBox="0 0 {PAGE_W} {PAGE_H}">'
        f'<text x="{title_x}" y="{title_y}" fill="white" '
        f'font-family="{GARAMOND}" font-size="{title_size}" font-kerning="normal" text-rendering="optimizeLegibility">'
        f'{TITLE_LINE1}</text>'
        f'<text x="{title_x}" y="{title_y + title_leading}" fill="white" '
        f'font-family="{GARAMOND}" font-size="{title_size}" font-kerning="normal" text-rendering="optimizeLegibility">'
        f'{TITLE_LINE2_PARTS[0]} '
        f'<tspan dx="0.07em">{TITLE_LINE2_PARTS[1]}</tspan>'
        f'</text>'
        f'</svg>')
    title_pdf = TMP / "title-cover2.pdf"
    svg_to_pdf_rsvg(title_svg, title_pdf)
    with fitz.open(title_pdf) as src:
        page.show_pdf_page(fitz.Rect(0, 0, PAGE_W, PAGE_H), src, 0)

    fx = FRONT_LEFT + SAFETY_INSET
    fy = title_y + 2 * title_leading + 30
    fw_box = (FRONT_RIGHT - SAFETY_INSET) - fx
    fh_box = (TRIM_BOTTOM - SAFETY_INSET) - fy
    front_maps = [
        (dlvl5_pdf,  dlvl5_w,  dlvl5_h),
        (castle_pdf, castle_w, castle_h),
    ]
    n_gaps = len(front_maps) - 1
    total_native_h = sum(h for _, _, h in front_maps)
    max_native_w = max(w for _, w, _ in front_maps)
    scale = min((fh_box - n_gaps * MAP_GAP_PT) / total_native_h,
                fw_box / max_native_w)
    stack_w = max_native_w * scale
    stack_h_total = total_native_h * scale + n_gaps * MAP_GAP_PT
    stack_x = fx + (fw_box - stack_w) / 2
    stack_y = fy + (fh_box - stack_h_total) / 2
    y = stack_y
    for i, (pdf, mw, mh) in enumerate(front_maps):
        h_scaled = mh * scale
        w_scaled = mw * scale
        x = stack_x + (stack_w - w_scaled) / 2
        with fitz.open(pdf) as src:
            page.show_pdf_page(fitz.Rect(x, y, x + w_scaled, y + h_scaled), src, 0)
        y += h_scaled
        if i < n_gaps:
            y += MAP_GAP_PT

    final = HERE.parent / "cover2.pdf"
    out.save(str(final))
    out.close()
    print(f"Wrote {final} ({final.stat().st_size} bytes)")


if __name__ == '__main__':
    main()
