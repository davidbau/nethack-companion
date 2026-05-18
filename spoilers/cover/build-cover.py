#!/usr/bin/env python3
"""Build the Lulu Novella duplex soft-cover PDF for "A Traveller's Companion
to the Mazes of Menace."

The output is a 2-page PDF at 789.746 × 594 pt (10.969" × 8.25" with 0.125"
bleed all around).

Layout (page 1, outside, BLACK):
  x= 0..  9  : bleed (back)
  x= 9..369  : back cover trim panel (360pt = 5") — back-sanctum.svg
  x=369..420.746 : spine — title text in white, rotated to read top→bottom
  x=420.746..780.746 : front cover trim panel (360pt = 5") — title top, castle below
  x=780.746..789.746 : bleed (front)

Layout (page 2, inside, WHITE):
  x= 9..369  : INSIDE FRONT COVER — identification flowchart
  x=369..420.746 : spine glue area — left white
  x=420.746..780.746 : INSIDE BACK COVER — dungeon topology (3 maps stacked)
"""

from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).parent

# ---- template-derived dimensions (extracted from Novella-Duplex-Soft-Cover.pdf) ----
PAGE_W = 789.746
PAGE_H = 594.0

BLEED = 9.0           # 0.125 inch
SPINE_LEFT = 369.0
SPINE_RIGHT = 420.746
SPINE_W = SPINE_RIGHT - SPINE_LEFT

BACK_LEFT = BLEED
BACK_RIGHT = SPINE_LEFT
FRONT_LEFT = SPINE_RIGHT
FRONT_RIGHT = PAGE_W - BLEED

TRIM_TOP = BLEED
TRIM_BOTTOM = PAGE_H - BLEED
TRIM_H = TRIM_BOTTOM - TRIM_TOP    # 576 pt = 8"

SAFETY_INSET = 13.536              # from template; ≈ 0.188"

# ---- read raw inline SVG content (the inner contents, ready for nesting) ----
def read_svg(path, force_font=None):
    """Return (viewbox, inner_xml, root_font) of an SVG file.

    If force_font is provided, replace any font-family declarations in the
    root <svg> tag and inside <style> blocks with that font stack. (rsvg-convert
    and cairosvg often can't load woff2 fonts embedded via @font-face data
    URIs, so we override the font-family to a system-installed font.)
    """
    text = path.read_text()
    # Strip XML decl if any
    text = re.sub(r'<\?xml[^>]*\?>\s*', '', text)
    # Find the root <svg ...> opening tag
    m = re.match(r'\s*<svg\b([^>]*)>', text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: no <svg> root")
    attrs = m.group(1)
    # Capture viewBox
    vb_m = re.search(r'viewBox\s*=\s*"([^"]+)"', attrs)
    if not vb_m:
        w_m = re.search(r'\bwidth\s*=\s*"([^"]+)"', attrs)
        h_m = re.search(r'\bheight\s*=\s*"([^"]+)"', attrs)
        if w_m and h_m:
            viewbox = f"0 0 {w_m.group(1)} {h_m.group(1)}"
        else:
            raise ValueError(f"{path}: no viewBox and no width/height")
    else:
        viewbox = vb_m.group(1)
    # Strip root <svg> and closing </svg> to get inner content
    body_start = m.end()
    body_end = text.rfind('</svg>')
    inner = text[body_start:body_end]
    # Capture the root's font-family for possible reuse on the outer wrapper
    root_font_m = re.search(r'font-family\s*=\s*"([^"]+)"', attrs)
    root_font = root_font_m.group(1) if root_font_m else None
    if force_font is not None:
        # Override font-family in inline style blocks. Note: the root's
        # font-family doesn't apply to nested SVGs (per spec), so we apply
        # force_font to the nested SVG element itself instead.
        inner = re.sub(
            r'font-family\s*:\s*[^;\'"]+',
            f'font-family:{force_font}',
            inner)
        # Also kill any @font-face blocks that pre-load DejaVu via woff2
        # (cairosvg/rsvg can't render woff2 from data URIs reliably).
        inner = re.sub(
            r'@font-face\s*\{[^}]*\}',
            '',
            inner,
            flags=re.DOTALL)
    return viewbox, inner, root_font


def nested_svg(viewbox, inner, x, y, w, h, preserve='xMidYMid meet', font=None):
    """Return a nested <svg> element placed at (x,y) with size (w,h).

    `font`, if given, is set as the font-family on the nested <svg> element
    so all text descendants inherit it. (Useful when the source SVG was
    designed for a font that cairosvg/rsvg can't render — we override here
    rather than touching the source file.)
    """
    extra = f' font-family="{font}"' if font else ''
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" '
            f'viewBox="{viewbox}" preserveAspectRatio="{preserve}" '
            f'overflow="visible"{extra}>{inner}</svg>')


# ---- TITLE ----
TITLE_LINE1 = "A Traveller's Companion"
TITLE_LINE2 = "to the Mazes of Menace"
# Garamond font stack (cairo will pick the first one it finds)
FONT_STACK = "EB Garamond, Garamond, Georgia, serif"


MONO_FONT = "Source Code Pro,Menlo,Monaco,monospace"

def build_outside():
    """Page 1 — outside cover (BLACK background)."""
    # Front-cover SVG (NetHack screenshot ASCII art — needs a monospace font)
    front_vb, front_inner, _ = read_svg(HERE / "front-castle.svg",
                                        force_font=MONO_FONT)
    # Back-cover SVG (NetHack screenshot ASCII art)
    back_vb, back_inner, _ = read_svg(HERE / "back-sanctum.svg",
                                      force_font=MONO_FONT)

    # Title placement on front cover
    title_x = FRONT_LEFT + SAFETY_INSET + 8        # left padding inside safety area
    title_y = TRIM_TOP + SAFETY_INSET + 36         # top padding inside safety
    title_size = 26                                # pt — Garamond
    title_leading = 30                             # line spacing

    # Castle artwork — below the title, fills remaining height
    # Title block ~85 pt tall (two lines + space)
    art_top = title_y + 2 * title_leading + 30
    art_left = FRONT_LEFT + SAFETY_INSET
    art_right = FRONT_RIGHT - SAFETY_INSET
    art_bottom = TRIM_BOTTOM - SAFETY_INSET
    art_w = art_right - art_left
    art_h = art_bottom - art_top

    # Back cover artwork — fills the back panel within safety
    back_art_left = BACK_LEFT + SAFETY_INSET
    back_art_right = BACK_RIGHT - SAFETY_INSET
    back_art_top = TRIM_TOP + SAFETY_INSET + 30
    back_art_bottom = TRIM_BOTTOM - SAFETY_INSET - 30
    back_art_w = back_art_right - back_art_left
    back_art_h = back_art_bottom - back_art_top

    # Spine title — rotated 90° clockwise, reads top→bottom (US convention)
    # Spine center
    spine_cx = (SPINE_LEFT + SPINE_RIGHT) / 2
    # Title text — use both lines joined with em-space
    spine_text = f"{TITLE_LINE1} {TITLE_LINE2}"
    spine_size = 14

    parts = []
    parts.append(f'<?xml version="1.0" encoding="UTF-8"?>')
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{PAGE_W}pt" height="{PAGE_H}pt" '
        f'viewBox="0 0 {PAGE_W} {PAGE_H}">')

    # Solid black background (covers bleed too)
    parts.append(f'<rect x="0" y="0" width="{PAGE_W}" height="{PAGE_H}" fill="black"/>')

    # Back cover artwork (centered in back panel)
    parts.append(nested_svg(back_vb, back_inner,
                            back_art_left, back_art_top,
                            back_art_w, back_art_h,
                            font=MONO_FONT))

    # Front cover: title in white Garamond at top
    parts.append(
        f'<text x="{title_x}" y="{title_y}" '
        f'fill="white" font-family="{FONT_STACK}" '
        f'font-size="{title_size}" text-anchor="start">'
        f'<tspan x="{title_x}" dy="0">{TITLE_LINE1}</tspan>'
        f'<tspan x="{title_x}" dy="{title_leading}">{TITLE_LINE2}</tspan>'
        f'</text>')

    # Front cover artwork (castle)
    parts.append(nested_svg(front_vb, front_inner,
                            art_left, art_top, art_w, art_h,
                            font=MONO_FONT))

    # Spine title — rotated. Rotate the text 90° clockwise around (spine_cx, spine_cy),
    # then it reads top→bottom along the spine. For "top→bottom" convention,
    # rotate the text by +90° (clockwise) and lay it from the top edge downward.
    spine_y_start = TRIM_TOP + 60
    parts.append(
        f'<g transform="translate({spine_cx}, {spine_y_start}) rotate(90)">'
        f'<text x="0" y="{spine_size/3}" '
        f'fill="white" font-family="{FONT_STACK}" '
        f'font-size="{spine_size}" text-anchor="start">'
        f'{spine_text}</text>'
        f'</g>')

    parts.append('</svg>')
    return '\n'.join(parts)


def build_inside():
    """Page 2 — inside cover (WHITE background).

    Note on layout: when the duplex page is flipped horizontally, the LEFT
    panel of the inside (page 2) sits behind the FRONT cover (right panel of
    page 1), so the LEFT panel of page 2 IS the "inside front cover". We put
    the dungeon overview maps there and the identification flowchart on the
    "inside back cover" (right panel of page 2).
    """
    fc_vb, fc_inner, _ = read_svg(HERE / "flowchart.svg")
    d0_vb, d0_inner, _ = read_svg(HERE / "dmap-0-dungeons-of-doom-map.svg")
    d1_vb, d1_inner, _ = read_svg(HERE / "dmap-1-gehennom-map.svg")
    d2_vb, d2_inner, _ = read_svg(HERE / "dmap-2-elemental-planes-and-ascension.svg")

    # Inside FRONT cover (left panel) — dungeon overview maps (3 stacked)
    ifc_left = BACK_LEFT + SAFETY_INSET
    ifc_right = BACK_RIGHT - SAFETY_INSET
    ifc_top = TRIM_TOP + SAFETY_INSET
    ifc_bottom = TRIM_BOTTOM - SAFETY_INSET
    ifc_w = ifc_right - ifc_left
    ifc_h = ifc_bottom - ifc_top

    # Inside BACK cover (right panel) — identification flowchart
    ibc_left = FRONT_LEFT + SAFETY_INSET
    ibc_right = FRONT_RIGHT - SAFETY_INSET
    ibc_top = TRIM_TOP + SAFETY_INSET
    ibc_bottom = TRIM_BOTTOM - SAFETY_INSET
    ibc_w = ibc_right - ibc_left
    ibc_h = ibc_bottom - ibc_top

    # Parse heights from viewBoxes to compute stack proportions for the
    # three dungeon-overview SVGs (all share viewBox width 760).
    def vb_dims(vb):
        nums = [float(x) for x in vb.split()]
        return nums[2], nums[3]

    d0_w, d0_h = vb_dims(d0_vb)
    d1_w, d1_h = vb_dims(d1_vb)
    d2_w, d2_h = vb_dims(d2_vb)

    # The stack lives on the inside-front-cover (left) panel.
    scale_w = ifc_w / 760.0
    total_h = (d0_h + d1_h + d2_h) * scale_w
    if total_h > ifc_h:
        scale = ifc_h / (d0_h + d1_h + d2_h)
    else:
        scale = scale_w
    stack_w = 760 * scale
    stack_x = ifc_left + (ifc_w - stack_w) / 2
    stack_y = ifc_top
    y0 = stack_y
    y1 = y0 + d0_h * scale
    y2 = y1 + d1_h * scale
    h0 = d0_h * scale
    h1 = d1_h * scale
    h2 = d2_h * scale

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{PAGE_W}pt" height="{PAGE_H}pt" '
        f'viewBox="0 0 {PAGE_W} {PAGE_H}">')

    # White background
    parts.append(f'<rect x="0" y="0" width="{PAGE_W}" height="{PAGE_H}" fill="white"/>')

    # Inside FRONT cover (left panel): three dungeon maps stacked
    parts.append(nested_svg(d0_vb, d0_inner, stack_x, y0, stack_w, h0,
                            preserve='xMidYMin meet'))
    parts.append(nested_svg(d1_vb, d1_inner, stack_x, y1, stack_w, h1,
                            preserve='xMidYMin meet'))
    parts.append(nested_svg(d2_vb, d2_inner, stack_x, y2, stack_w, h2,
                            preserve='xMidYMin meet'))

    # Inside BACK cover (right panel): identification flowchart fitted
    parts.append(nested_svg(fc_vb, fc_inner, ibc_left, ibc_top, ibc_w, ibc_h))

    parts.append('</svg>')
    return '\n'.join(parts)


def svg_to_pdf(svg_path, pdf_path):
    """Use rsvg-convert (preferred) or cairosvg as fallback."""
    try:
        subprocess.run(
            ['rsvg-convert', '-f', 'pdf', '-o', str(pdf_path), str(svg_path)],
            check=True, capture_output=True)
        return
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"  rsvg-convert failed ({e}); trying cairosvg")
    import cairosvg
    cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path))


def concat_pdfs(pdf_paths, out_path):
    """Concatenate the per-page PDFs into one duplex PDF using PyMuPDF."""
    import fitz
    out = fitz.open()
    for p in pdf_paths:
        with fitz.open(p) as src:
            out.insert_pdf(src)
    out.save(str(out_path))
    out.close()


def main():
    outside_svg = HERE / 'cover-outside.svg'
    inside_svg = HERE / 'cover-inside.svg'
    outside_pdf = HERE / 'cover-outside.pdf'
    inside_pdf = HERE / 'cover-inside.pdf'
    final_pdf = HERE / 'cover.pdf'

    print("Building outside SVG ...")
    outside_svg.write_text(build_outside())
    print(f"  -> {outside_svg} ({outside_svg.stat().st_size} bytes)")

    print("Building inside SVG ...")
    inside_svg.write_text(build_inside())
    print(f"  -> {inside_svg} ({inside_svg.stat().st_size} bytes)")

    print("Converting outside SVG -> PDF ...")
    svg_to_pdf(outside_svg, outside_pdf)
    print("Converting inside SVG -> PDF ...")
    svg_to_pdf(inside_svg, inside_pdf)

    print("Concatenating ...")
    concat_pdfs([outside_pdf, inside_pdf], final_pdf)
    print(f"  -> {final_pdf} ({final_pdf.stat().st_size} bytes)")


if __name__ == '__main__':
    main()
