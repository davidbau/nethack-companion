#!/usr/bin/env python3
"""Build the soft-cover PDFs for "A Traveler's Companion
to the Mazes of Menace."

Pipeline: render each input SVG to its own PDF (rsvg-convert handles the
font correctly when the source font is installed on the system), then
compose each cover page by stamping those PDFs onto positioned rectangles
of a black/white background, using PyMuPDF's show_pdf_page().

Outputs two files:
  cover.pdf         single-page KDP-style wraparound exterior, primary
                    print PDF for the print-on-demand service
  cover-inside.pdf  single-page A5 wraparound inside-leaf artwork, used
                    by build-book2.py to bind the inside-cover panels
                    into the coil-bound book block

Primary KDP exterior (cover.pdf):
  Trim:            6.08" x 8.77" = 437.76 x 631.44 pt per panel
  Wrap (bleed):    0.625" = 45 pt on all sides
  Spine width:     0.938" = 67.54 pt for 288 pages
  Safety inset:    0.625" = 45 pt inside the trim line
  Total document:  14.348" x 10.02" = 1033.06 x 721.44 pt
                   (= 2*trim_w + spine + 2*wrap by trim_h + 2*wrap)

Inside leaf (cover-inside.pdf), sized for build-book2.py's A5 extraction:
  Per-panel trim:  A5 = 419.528 x 595.276 pt
  Bleed:           9 pt (0.125") all sides
  Spine width:     51.746 pt (placeholder; matches old Lulu Novella)
  Page (with bleed): 2*A5w + spine + 2*bleed  x  A5h + 2*bleed
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

# ---- KDP-style wraparound dimensions (cover.pdf exterior) ----
TRIM_W = 437.76         # 6.08" — book trim width
TRIM_H = 631.44         # 8.77" — book trim height
BLEED = 45.0            # 0.625" — wrap area on all sides
SPINE_W = 67.54         # 0.938" — for 288 pages
PAGE_W = 2 * TRIM_W + SPINE_W + 2 * BLEED   # 1033.06 pt
PAGE_H = TRIM_H + 2 * BLEED                 # 721.44 pt
BACK_LEFT = BLEED
BACK_RIGHT = BACK_LEFT + TRIM_W             # 482.76 pt
SPINE_LEFT = BACK_RIGHT
SPINE_RIGHT = SPINE_LEFT + SPINE_W          # 550.30 pt
FRONT_LEFT = SPINE_RIGHT
FRONT_RIGHT = FRONT_LEFT + TRIM_W           # 988.06 pt
TRIM_TOP = BLEED
TRIM_BOTTOM = PAGE_H - BLEED                # 676.44 pt
SAFETY_INSET = 45.0                         # 0.625" inside trim line

# ---- A5 wraparound dimensions (cover-inside.pdf inside leaf for book2) ----
I_TRIM_W = 419.528       # A5 width: 148 mm
I_TRIM_H = 595.276       # A5 height: 210 mm
I_BLEED = 9.0            # 0.125" all sides
I_SPINE_W = 51.746       # placeholder; build-book2.py reads it back
I_PAGE_W = 2 * I_TRIM_W + I_SPINE_W + 2 * I_BLEED
I_PAGE_H = I_TRIM_H + 2 * I_BLEED
I_BACK_LEFT = I_BLEED
I_BACK_RIGHT = I_BACK_LEFT + I_TRIM_W
I_SPINE_LEFT = I_BACK_RIGHT
I_SPINE_RIGHT = I_SPINE_LEFT + I_SPINE_W
I_FRONT_LEFT = I_SPINE_RIGHT
I_FRONT_RIGHT = I_FRONT_LEFT + I_TRIM_W
I_TRIM_TOP = I_BLEED
I_TRIM_BOTTOM = I_PAGE_H - I_BLEED
I_SAFETY_INSET = 13.536  # ~0.188" inside trim line

TITLE_MAIN = "NetHack Spoilers"
TITLE_LINE1 = "A Traveler's Companion"
TITLE_LINE2_PARTS = ('to the Mazes of', 'Menace')  # split before M to add a kern nudge
GARAMOND = "EB Garamond,Garamond,Georgia,serif"


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def svg_to_pdf_rsvg(svg_path: Path, pdf_path: Path):
    """Render an SVG to PDF using rsvg-convert. Good for SVGs that rely on
    system fonts (e.g. EB Garamond title, generated cover frame)."""
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
        check=True, capture_output=True)


def svg_to_pdf_chrome(svg_path: Path, pdf_path: Path):
    """Render an SVG to PDF using headless Chrome. Chrome HONORS @font-face
    declarations with embedded woff2 — which is what the NetHack ASCII-art
    SVGs need for character-by-character x-alignment.

    We wrap the SVG in a minimal HTML page with @page { margin: 0 } and
    a body sized to match the SVG's viewBox, so the rendered PDF has
    NO surrounding white-space margin (Chrome's default 0.5" margin would
    otherwise shift the content and break our downstream cropping)."""
    # Extract viewBox to size the page
    text = svg_path.read_text()
    m = re.search(r'viewBox\s*=\s*"\s*[\d.eE+-]+\s+[\d.eE+-]+\s+([\d.eE+-]+)\s+([\d.eE+-]+)\s*"', text)
    vb_w, vb_h = (float(m.group(1)), float(m.group(2))) if m else (749, 456)
    # Chrome default print is 96 DPI: 1 SVG px = 0.75 pt = 1/96 inch.
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


def crop_pdf_to_viewbox(pdf_path: Path, vb_w: float, vb_h: float, out_path: Path,
                        top_px=0, bottom_px=0):
    """Chrome lays the SVG at the top-left of a US-letter page. Crop to the
    viewBox (1 SVG px = 0.75 pt at default 96 DPI), optionally trimming
    `top_px` SVG-pixels off the top and `bottom_px` SVG-pixels off the
    bottom. This is used to clip the NetHack-screenshot SVGs to just the
    map area (no top "You hear..." message line, no bottom status line)."""
    src = fitz.open(pdf_path)
    page = src[0]
    px_to_pt = 0.75
    top_pt = top_px * px_to_pt
    bottom_pt = (vb_h - bottom_px) * px_to_pt
    crop_w = vb_w * px_to_pt
    # Clamp to MediaBox — chrome's PDF size is the viewBox rounded
    # to PDF points and can be a hair narrower than crop_w by
    # rounding (e.g. 553.92 pt vs 554.40 pt for a 739.2 px viewBox).
    mb = page.mediabox
    crop_w = min(crop_w, mb.width)
    bottom_pt = min(bottom_pt, mb.height)
    page.set_cropbox(fitz.Rect(0, top_pt, crop_w, bottom_pt))
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
    # Three level-detail maps generated by render-level-svg.py. These
    # also embed woff2, so chrome rendering is required for character-
    # precise tracking.
    dlvl5_raw,   dlvl5_w,   dlvl5_h   = prepare("level-dlvl5",    HERE / "level-dlvl5.svg",    renderer="chrome")
    gehmaze_raw, gehmaze_w, gehmaze_h = prepare("level-gehennom", HERE / "level-gehennom.svg", renderer="chrome")
    medusa_raw,  medusa_w,  medusa_h  = prepare("level-medusa",   HERE / "level-medusa.svg",   renderer="chrome")
    # The other diagrams are vector primitives (no monospace tracking required);
    # rsvg-convert handles them fine.
    flow_pdf, flow_w, flow_h = prepare("flowchart", HERE / "flowchart.svg")
    # Inside leaf uses the monochrome variants (no inverse video, all
    # black text on white) since coil-bound printers handle pure BW
    # better than gold-on-dark-gray and white-on-color. Generate with
    #   python3 dungeon_map.py --bw-pdfs cover
    d0_pdf, d0_w, d0_h = prepare("dmap0", HERE / "dmap-dod-bw.svg")
    d1_pdf, d1_w, d1_h = prepare("dmap1", HERE / "dmap-geh-bw.svg")
    d2_pdf, d2_w, d2_h = prepare("dmap2", HERE / "dmap-planes-bw.svg")

    # Chrome embeds the SVG on a US-letter page with margins. Crop to viewBox
    # AND trim the top message line ("You hear...") and bottom status line
    # ("Rodney the Peregrinator / Dlvl:25 ..."). In the SVGs the top message
    # is at SVG-y≈14 and the status line is at y≈432/451 — so skip the top
    # 56 px and bottom 36 px (each line ≈ 19 px tall with leading).
    castle_pdf  = TMP / "front-castle-crop.pdf"
    sanctum_pdf = TMP / "back-sanctum-crop.pdf"
    dlvl5_pdf   = TMP / "level-dlvl5-crop.pdf"
    gehmaze_pdf = TMP / "level-gehennom-crop.pdf"
    medusa_pdf  = TMP / "level-medusa-crop.pdf"
    TOP_CLIP = 56
    # The two status lines have baselines at y≈432 and y≈451; the last map
    # row has baseline y≈413. Crop at SVG y=409 (BOTTOM_CLIP=47) so we keep
    # the full last row's descenders but stay above the status ascenders.
    BOTTOM_CLIP = 47
    for raw, w, h, dst in (
        (castle_raw,  castle_w,  castle_h,  castle_pdf),
        (sanctum_raw, sanctum_w, sanctum_h, sanctum_pdf),
        (dlvl5_raw,   dlvl5_w,   dlvl5_h,   dlvl5_pdf),
        (gehmaze_raw, gehmaze_w, gehmaze_h, gehmaze_pdf),
        (medusa_raw,  medusa_w,  medusa_h,  medusa_pdf),
    ):
        crop_pdf_to_viewbox(raw, w, h, dst, top_px=TOP_CLIP, bottom_px=BOTTOM_CLIP)
    # show_pdf_page uses the cropbox dimensions; recompute logical w/h in pt:
    castle_w  *= 0.75
    sanctum_w *= 0.75
    dlvl5_w   *= 0.75
    gehmaze_w *= 0.75
    medusa_w  *= 0.75
    castle_h  = (castle_h  - TOP_CLIP - BOTTOM_CLIP) * 0.75
    sanctum_h = (sanctum_h - TOP_CLIP - BOTTOM_CLIP) * 0.75
    dlvl5_h   = (dlvl5_h   - TOP_CLIP - BOTTOM_CLIP) * 0.75
    gehmaze_h = (gehmaze_h - TOP_CLIP - BOTTOM_CLIP) * 0.75
    medusa_h  = (medusa_h  - TOP_CLIP - BOTTOM_CLIP) * 0.75

    outer = fitz.open()
    inner = fitz.open()

    # ===== cover.pdf: OUTSIDE COVER (BLACK) at KDP wraparound dimensions =====
    page1 = outer.new_page(width=PAGE_W, height=PAGE_H)
    page1.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=(0, 0, 0), fill=(0, 0, 0))

    # ---- Back cover (left panel): three maps stacked top-to-bottom
    #      (Medusa, Gehennom maze, Moloch's Sanctum). Same crop applied
    #      to all three as the original sanctum/castle treatment.
    bx = BACK_LEFT + SAFETY_INSET
    by = TRIM_TOP + SAFETY_INSET + 30
    bw = (BACK_RIGHT - SAFETY_INSET) - bx
    bh = (TRIM_BOTTOM - SAFETY_INSET - 30) - by
    back_maps = [
        (medusa_pdf,  medusa_w,  medusa_h),
        (gehmaze_pdf, gehmaze_w, gehmaze_h),
        (sanctum_pdf, sanctum_w, sanctum_h),
    ]
    # ~2 lines of text-height gap between adjacent maps (each cell row
    # in the source SVG is ~19 pt; cropped maps get scaled down by
    # `scale` below, so the gap is specified in output PDF points).
    MAP_GAP_PT = 26
    n_gaps = len(back_maps) - 1
    total_native_h = sum(h for _, _, h in back_maps)
    max_native_w = max(w for _, w, _ in back_maps)
    scale_h = (bh - n_gaps * MAP_GAP_PT) / total_native_h
    scale_w = bw / max_native_w
    scale = min(scale_h, scale_w)
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
            page1.show_pdf_page(fitz.Rect(x, y, x + w_scaled, y + h_scaled), src, 0)
        y += h_scaled
        if i < n_gaps:
            y += MAP_GAP_PT

    # ---- Title and spine: render via an SVG → PDF intermediate so we can
    # use Garamond (which rsvg-convert can find via the system font cache).
    # PyMuPDF's builtin fonts don't include Garamond.
    spine_cx = (SPINE_LEFT + SPINE_RIGHT) / 2
    spine_text = TITLE_MAIN
    spine_size = 40           # short title -> larger; cap height fits the spine width
    spine_y_start = TRIM_TOP + 175   # roughly centered along the spine length
    title_x = FRONT_LEFT + SAFETY_INSET + 8
    main_size = 44            # large front-cover title (the title is short now)
    main_y = TRIM_TOP + SAFETY_INSET + 36 + 12   # baseline of the large title
    sub_size = 21
    sub_leading = 26
    sub_y1 = main_y + 42
    sub_y2 = sub_y1 + sub_leading

    title_svg = TMP / "title.svg"
    title_svg.write_text(
        f'<?xml version="1.0"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{PAGE_W}pt" height="{PAGE_H}pt" '
        f'viewBox="0 0 {PAGE_W} {PAGE_H}">'
        # Front-cover large main title
        f'<text x="{title_x}" y="{main_y}" fill="white" font-weight="600" '
        f'font-family="{GARAMOND}" font-size="{main_size}" font-kerning="normal" text-rendering="optimizeLegibility">'
        f'{TITLE_MAIN}</text>'
        # Front-cover subtitle (two lines, italic, smaller). Split before
        # "Menace" and nudge it so the f and M don't touch.
        f'<text x="{title_x}" y="{sub_y1}" fill="white" font-style="italic" '
        f'font-family="{GARAMOND}" font-size="{sub_size}" font-kerning="normal" text-rendering="optimizeLegibility">'
        f'{TITLE_LINE1}</text>'
        f'<text x="{title_x}" y="{sub_y2}" fill="white" font-style="italic" '
        f'font-family="{GARAMOND}" font-size="{sub_size}" font-kerning="normal" text-rendering="optimizeLegibility">'
        f'{TITLE_LINE2_PARTS[0]} '
        f'<tspan dx="0.07em">{TITLE_LINE2_PARTS[1]}</tspan>'
        f'</text>'
        # Spine title (rotated +90°, reads top→bottom). After rotation
        # the glyphs extend rightward of the baseline by ~cap_height
        # (≈0.6*em); offset the baseline LEFT by spine_size/3 so the
        # visual center of the caps lands on the spine centerline.
        f'<g transform="translate({spine_cx - spine_size/3}, {spine_y_start}) rotate(90)">'
        f'<text x="0" y="0" fill="white" font-weight="600" '
        f'font-family="{GARAMOND}" font-size="{spine_size}">'
        f'{spine_text}</text></g>'
        f'</svg>')
    title_pdf = TMP / "title.pdf"
    svg_to_pdf_rsvg(title_svg, title_pdf)
    with fitz.open(title_pdf) as src:
        page1.show_pdf_page(fitz.Rect(0, 0, PAGE_W, PAGE_H), src, 0)

    # Front-cover artwork: Dlvl 5 above Castle, stacked vertically.
    fx = FRONT_LEFT + SAFETY_INSET
    fy = sub_y2 + 30
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
            page1.show_pdf_page(fitz.Rect(x, y, x + w_scaled, y + h_scaled), src, 0)
        y += h_scaled
        if i < n_gaps:
            y += MAP_GAP_PT

    # ===== cover-inside.pdf: INSIDE COVER (WHITE) at A5 wraparound dimensions =====
    # Composed at A5 dims (not the new KDP dims) so build-book2.py's panel-
    # extraction math (BLEED=9, COVER_PANEL_W=A5_W) keeps working.
    page2 = inner.new_page(width=I_PAGE_W, height=I_PAGE_H)
    page2.draw_rect(fitz.Rect(0, 0, I_PAGE_W, I_PAGE_H), color=(1, 1, 1), fill=(1, 1, 1))

    # ---- Inside FRONT cover (left panel): dungeon maps stacked ----
    ifc_l = I_BACK_LEFT + I_SAFETY_INSET
    ifc_t = I_TRIM_TOP + I_SAFETY_INSET
    ifc_w = (I_BACK_RIGHT - I_SAFETY_INSET) - ifc_l
    ifc_h = (I_TRIM_BOTTOM - I_SAFETY_INSET) - ifc_t

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

    # ---- Inside BACK cover (right panel): flowchart up top, then a
    # ---- "key to the cover" block with thumbnail + caption rows.
    ibc_l = I_FRONT_LEFT + I_SAFETY_INSET
    ibc_t = I_TRIM_TOP + I_SAFETY_INSET
    ibc_w = (I_FRONT_RIGHT - I_SAFETY_INSET) - ibc_l
    ibc_h = (I_TRIM_BOTTOM - I_SAFETY_INSET) - ibc_t

    # Reserve the bottom portion for the key block; flowchart fills
    # the rest at the top.
    KEY_BLOCK_H = 200  # pt; tighter rows
    KEY_TOP_GAP = 16   # gap between flowchart and key block

    flow_box_h = ibc_h - KEY_BLOCK_H - KEY_TOP_GAP
    ox, oy, fw, fh = fit_into(ibc_w, flow_box_h, flow_w, flow_h)
    with fitz.open(flow_pdf) as src:
        page2.show_pdf_page(fitz.Rect(ibc_l + ox, ibc_t + oy,
                                      ibc_l + ox + fw, ibc_t + oy + fh), src, 0)

    # Key block — two columns, 2 rows on the left (front-cover maps)
    # and 3 rows on the right (back-cover maps).
    key_t = ibc_t + flow_box_h + KEY_TOP_GAP
    key_l = ibc_l
    key_w = ibc_w
    col_gap = 16
    col_w = (key_w - col_gap) / 2

    # Symmetric 2x3 grid. Upper-left cell is a heading; the other
    # five cells each hold a thumbnail + caption for one cover map.
    KEY_HEADER = ('Maps on the cover', 'thumbnails of the five level views')
    KEY_CAPTIONS = {
        'front': [
            ('thumb-dlvl5.svg',  'Dungeons of Doom',
             'early level with shop & vault'),
            ('thumb-castle.svg', 'The Castle',
             'wand of wishing inside'),
        ],
        'back': [
            ('thumb-medusa.svg',  "Medusa's island", 'one of four layouts'),
            ('thumb-gehennom.svg','Gehennom', 'a typical maze level'),
            ('thumb-sanctum.svg', "Moloch's Sanctum",
             'the Amulet awaits below'),
        ],
    }

    # Pre-render the thumbnails (chrome to honor embedded woff2),
    # then crop the top/bottom message and status rows so the
    # thumbnail is pure map.
    thumb_pdfs = {}
    for col_name in ('front', 'back'):
        for svg_name, _, _ in KEY_CAPTIONS[col_name]:
            stem = Path(svg_name).stem
            raw, vw, vh = prepare(stem, HERE / svg_name, renderer='chrome')
            cropped = TMP / f"{stem}-crop.pdf"
            crop_pdf_to_viewbox(raw, vw, vh, cropped,
                                top_px=TOP_CLIP, bottom_px=BOTTOM_CLIP)
            cropped_w = vw * 0.75
            cropped_h = (vh - TOP_CLIP - BOTTOM_CLIP) * 0.75
            thumb_pdfs[svg_name] = (cropped, cropped_w, cropped_h)

    # The grid: 3 rows tall, 2 cols wide. Front col = [header, dlvl5,
    # castle]; back col = [medusa, gehennom, sanctum].
    def thumb(entry):
        return ('thumb',) + entry
    grid_rows = [
        [('header',) + KEY_HEADER,             thumb(KEY_CAPTIONS['back'][0])],
        [thumb(KEY_CAPTIONS['front'][0]),      thumb(KEY_CAPTIONS['back'][1])],
        [thumb(KEY_CAPTIONS['front'][1]),      thumb(KEY_CAPTIONS['back'][2])],
    ]
    row_h = KEY_BLOCK_H / 3
    col_xs = [key_l, key_l + col_w + col_gap]

    # Register EB Garamond bold + italic as embedded TTFs.
    # PyMuPDF's insert_text() with the PDF base-14 ("Times-Bold",
    # "Times-Italic") leaves the fonts unembedded, which Lulu's
    # preflight rejects. Embed Garamond — it also matches the
    # title font on the front cover.
    GARAMOND_BOLD_TTF = HERE.parent / "fonts" / "EBGaramond-Bold.ttf"
    GARAMOND_ITALIC_TTF = HERE.parent / "fonts" / "EBGaramond-Italic.ttf"
    page2.insert_font(fontname="garamond-bold",   fontfile=str(GARAMOND_BOLD_TTF))
    page2.insert_font(fontname="garamond-italic", fontfile=str(GARAMOND_ITALIC_TTF))

    def draw_thumb_cell(cell_x, cell_y, cell_w, cell_h, svg_name, line1, line2):
        raw, vw, vh = thumb_pdfs[svg_name]
        pad = 3
        inner_y = cell_y + pad
        inner_h = cell_h - 2 * pad
        thumb_w_max = cell_w * 0.40
        scale = min(thumb_w_max / vw, inner_h / vh)
        thumb_w = vw * scale
        thumb_h = vh * scale
        thumb_x = cell_x
        thumb_y = inner_y + (inner_h - thumb_h) / 2
        with fitz.open(raw) as src:
            page2.show_pdf_page(
                fitz.Rect(thumb_x, thumb_y, thumb_x + thumb_w, thumb_y + thumb_h),
                src, 0)
        cap_x = thumb_x + thumb_w + 6
        cap_top = inner_y + (inner_h - 22) / 2
        # insert_text places the line at a baseline (no min-height
        # check), so it always renders even if the cell is tight.
        page2.insert_text(
            fitz.Point(cap_x, cap_top + 9),
            line1, fontname='garamond-bold', fontsize=9.5, color=(0, 0, 0))
        page2.insert_text(
            fitz.Point(cap_x, cap_top + 21),
            line2, fontname='garamond-italic', fontsize=8.5,
            color=(0.25, 0.25, 0.25))

    def draw_header_cell(cell_x, cell_y, cell_w, cell_h, title, subtitle):
        # Align the bold title baseline with the vertical center of
        # the adjacent (Medusa) thumbnail.
        title_baseline = cell_y + cell_h / 2 + 1
        page2.insert_text(
            fitz.Point(cell_x, title_baseline),
            title, fontname='garamond-bold', fontsize=13, color=(0, 0, 0))
        page2.insert_text(
            fitz.Point(cell_x, title_baseline + 13),
            subtitle, fontname='garamond-italic', fontsize=9,
            color=(0.25, 0.25, 0.25))

    for r_i, row in enumerate(grid_rows):
        cell_y = key_t + r_i * row_h
        for c_i, cell in enumerate(row):
            cell_x = col_xs[c_i]
            kind = cell[0]
            if kind == 'header':
                draw_header_cell(cell_x, cell_y, col_w, row_h, cell[1], cell[2])
            else:
                draw_thumb_cell(cell_x, cell_y, col_w, row_h,
                                cell[1], cell[2], cell[3])

    # Subset the embedded Garamond TTFs down to just the glyphs used
    # (insert_font embeds the full file by default).
    outer_path = HERE.parent / "cover.pdf"
    inner_path = HERE.parent / "cover-inside.pdf"
    outer.subset_fonts()
    outer.save(str(outer_path), garbage=4, deflate=True, clean=True)
    outer.close()
    inner.subset_fonts()
    inner.save(str(inner_path), garbage=4, deflate=True, clean=True)
    inner.close()
    print(f"Wrote {outer_path} ({outer_path.stat().st_size} bytes)")
    print(f"Wrote {inner_path} ({inner_path.stat().st_size} bytes)")


if __name__ == '__main__':
    main()
