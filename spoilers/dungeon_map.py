#!/usr/bin/env python3
"""Generate the dungeon overview map SVG for spoilers/companion.md.

Usage:
    python3 dungeon_map.py              # print SVG to stdout
    python3 dungeon_map.py --inplace    # rewrite the block in companion.md
                                          between <!-- DMAP-BEGIN --> and
                                          <!-- DMAP-END --> markers
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Literal
import shutil
import subprocess
import sys
import re
from pathlib import Path


# ============================================================================
# Layout constants
# ============================================================================

WIDTH = 760
TRUNK_X = 380
TRUNK_DOD = '#B5651D'
TRUNK_GEH = '#A14A3F'
TRUNK_PLANES = '#5D3C8E'
TRUNK_W = 2.5

BUBBLE_W = 180
BUBBLE_H = 32
BUBBLE_H_2 = 40
BIG_BUBBLE_W = 300
BIG_BUBBLE_H = 58
SANCTUM_H = 58

LEFT_X = 60                           # left-side branch column
LEFT_EDGE = LEFT_X + BUBBLE_W         # 240
RIGHT_X = 540                         # right-side branch column
RIGHT_EDGE = RIGHT_X + BUBBLE_W       # 720

PEARL_R = 4
PEARL_SPACING = 10                    # vertical advance per pearl
PEARL_PADDING = 4                     # pad before first/after last pearl in a gap

GAP_NO_PEARL = 6                      # gap between bubbles when no pearls between

SECT_BAR_H = 39                       # 50% taller than before
SECT_BAR_FONT = 22                    # 50% bigger than before
SECT_BAR_MARGIN = 40
TRUNK_PADDING = 14                    # padding at section bar transitions

# Bubble colors (fill, stroke)
COLORS = {
    'dod':       ('#FAF3E0', '#B5651D'),
    'mines':     ('#E8F4DC', '#5B8E3A'),
    'soko':      ('#FFF4CC', '#B58A1A'),
    'quest':     ('#DDE9F5', '#3B6FA0'),
    'geh':       ('#FAD7C0', '#A14A3F'),
    'vlad':      ('#E3D8F0', '#6B4E96'),
    'ludios':    ('#FFD966', '#B5891A'),
    'medusa':    ('#B8D4F0', '#2E5C8E'),
    'castle':    ('#FFFFFF', '#B5891A'),
    'sanctum':   ('#2D2D2D', '#FFC857'),
    'ascension': ('#FFE680', '#B5891A'),
    'earth':     ('#E8DDC8', '#8B6F47'),
    'air':       ('#E0F4FA', '#3B9FA8'),
    'fire':      ('#FAD7C0', '#A14A3F'),
    'water':     ('#DDE9F5', '#3B6FA0'),
    'astral':    ('#D8C6F0', '#5D3C8E'),
}

PEARL_COLOR = {
    'dod':    '#B5651D',
    'geh':    '#A14A3F',
    'mines':  '#5B8E3A',
    'soko':   '#B58A1A',
    'quest':  '#3B6FA0',
    'vlad':   '#6B4E96',
    'ludios': '#B5891A',
}


# ============================================================================
# Data model
# ============================================================================

@dataclass
class Bubble:
    title: str
    detail: str = ''
    color: str = 'dod'
    star: bool = False
    is_big: bool = False
    is_sanctum: bool = False

    @property
    def h(self) -> int:
        if self.is_sanctum or self.is_big:
            return BIG_BUBBLE_H
        return BUBBLE_H_2 if self.detail else BUBBLE_H

    @property
    def w(self) -> int:
        return BIG_BUBBLE_W if (self.is_big or self.is_sanctum) else BUBBLE_W


@dataclass
class Branch:
    side: Literal['left', 'right']
    color: str                                # pearl/connector color key
    bubbles: list[Bubble]
    pearls: list[int]                         # between-bubble pearl counts
    attach: Literal['top', 'bottom'] = 'top'  # which bubble joins the trunk
    label: str = ''                           # tiny label above the trunk-to-branch arrow
    label_pos: float = 0.75                   # 0.0=at trunk, 1.0=at bubble; default biases toward the branch


@dataclass
class TrunkRow:
    bubble: Optional[Bubble] = None           # None = pure branch point (circle marker)
    branch: Optional[Branch] = None
    pearls_below: int = 0                     # pearls between this row and the next


# ============================================================================
# Dungeon structure
# ============================================================================

DOD: list[TrunkRow] = [
    TrunkRow(bubble=Bubble('The Dungeon Entrance', 'up-stair to exit'), pearls_below=2),
    TrunkRow(  # Mines branch LEFT (down-stairs)
        branch=Branch(
            side='left', color='mines',
            bubbles=[
                Bubble('Gnomish Mines', color='mines'),
                Bubble('Minetown', 'shops, temple', color='mines'),
                Bubble("Mine's End", 'luckstone', color='mines'),
            ],
            pearls=[2, 3],
            attach='top',
            label='down',
        ),
        pearls_below=3,
    ),
    TrunkRow(bubble=Bubble('The Oracle', 'paid hints'), pearls_below=0),
    TrunkRow(  # Sokoban branch RIGHT (up-stair from main dungeon), 1 DLvl below Oracle
        branch=Branch(
            side='right', color='soko',
            bubbles=[
                Bubble('Sokoban prize', 'bag of holding/amulet of reflection', color='soko'),
                Bubble('Sokoban entry', color='soko'),
            ],
            pearls=[2],
            attach='bottom',
            label='up',
        ),
        pearls_below=5,
    ),
    TrunkRow(  # Quest portal + Quest RIGHT (portal)
        bubble=Bubble('Quest portal'),
        branch=Branch(
            side='right', color='quest',
            bubbles=[
                Bubble('Quest entry', "your role's dungeon", color='quest'),
                Bubble('Quest goal', '★ Bell of Opening, role artifact', color='quest'),
            ],
            pearls=[3],
            attach='top',
            label='portal',
            label_pos=0.5,  # short arrow; midpoint reads better than the default 75%
        ),
        pearls_below=2,
    ),
    TrunkRow(bubble=Bubble('Big Room (40%)'), pearls_below=2),
    TrunkRow(bubble=Bubble('Rogue Level'), pearls_below=1),
    TrunkRow(  # Fort Ludios branch LEFT (portal)
        branch=Branch(
            side='left', color='ludios',
            bubbles=[Bubble('Fort Ludios', 'vault of gold', color='ludios')],
            pearls=[],
            attach='top',
            label='portal',
        ),
        pearls_below=3,
    ),
    TrunkRow(bubble=Bubble("Medusa's Island", color='medusa'), pearls_below=2),
    TrunkRow(bubble=Bubble('THE CASTLE', 'wand of wishing', color='castle', is_big=True)),
]

GEH: list[TrunkRow] = [
    TrunkRow(bubble=Bubble('Valley of the Dead', "Gehennom's entrance", color='geh'), pearls_below=4),
    TrunkRow(bubble=Bubble("Asmodeus's Lair", color='geh'), pearls_below=1),
    TrunkRow(bubble=Bubble("Juiblex's Swamp", color='geh'), pearls_below=2),
    TrunkRow(bubble=Bubble("Baalzebub's Lair", color='geh'), pearls_below=3),
    TrunkRow(  # Vlad's Tower branch LEFT (attaches at bottom; tower goes UP)
        branch=Branch(
            side='left', color='vlad',
            bubbles=[
                Bubble('Vlad the Impaler', '★ Candelabrum', color='vlad'),
                Bubble("Vlad's Tower", color='vlad'),
            ],
            pearls=[1],
            attach='bottom',
            label='up',
        ),
        pearls_below=2,
    ),
    TrunkRow(bubble=Bubble('Orcus Town', 'Wand of Orcus · magic lamp/marker', color='geh'), pearls_below=2),
    # Wizard's Tower is 3 inline Gehennom levels (wizard1 entry -> wizard2 ->
    # wizard3 where the Wizard and Book live). Render as two trunk bubbles
    # with one pearl between so the depth shows on the map.
    TrunkRow(bubble=Bubble("Wizard's Tower", color='geh'), pearls_below=1),
    TrunkRow(bubble=Bubble('Wizard of Yendor', '★ Book of the Dead', color='geh'), pearls_below=5),
    TrunkRow(bubble=Bubble("Moloch's Sanctum", 'the Amulet of Yendor', color='sanctum', is_sanctum=True)),
]


# ============================================================================
# Layout
# ============================================================================

@dataclass
class Placed:
    """Everything we've placed during layout, ready to be rendered."""
    bubbles: list[tuple[Bubble, int, int]] = field(default_factory=list)        # (bubble, x, y)
    pearls: list[tuple[int, int, str]] = field(default_factory=list)            # (x, y, color)
    trunk_circles: list[tuple[int, int, str]] = field(default_factory=list)     # (x, y, color)
    branch_arrows: list[tuple[int, int, int, int]] = field(default_factory=list)  # (x1, y1, x2, y2)
    branch_connectors: list[tuple[int, int, int, str]] = field(default_factory=list)  # (x, y1, y2, color)
    trunk_segments: list[tuple[int, int, int, str]] = field(default_factory=list)    # (x, y1, y2, color)
    arrow_labels: list[tuple[int, int, str]] = field(default_factory=list)            # (x, y, text)


def gap_for_pearls(n: int) -> int:
    """Vertical gap needed to fit n pearls (counts buffer on either side)."""
    if n == 0:
        return GAP_NO_PEARL
    return 2 * PEARL_PADDING + n * PEARL_SPACING


def place_pearls(x: int, y_start: int, n: int, color: str) -> list[tuple[int, int, str]]:
    """Place n pearls in a vertical gap starting at y_start. Returns list of pearl tuples."""
    return [
        (x, y_start + PEARL_PADDING + (i + 0.5) * PEARL_SPACING, color)
        for i in range(n)
    ]


def branch_total_height(branch: Branch) -> int:
    total = 0
    for i, b in enumerate(branch.bubbles):
        total += b.h
        if i < len(branch.bubbles) - 1:
            total += gap_for_pearls(branch.pearls[i])
    return total


def layout_branch(branch: Branch, attach_y: int, placed: Placed) -> None:
    """Place a branch into `placed`. attach_y is the trunk Y where the branch joins."""
    x = LEFT_X if branch.side == 'left' else RIGHT_X
    cx = x + BUBBLE_W // 2

    if branch.attach == 'top':
        # First bubble's center == attach_y
        top_y = attach_y - branch.bubbles[0].h // 2
    else:
        # Last bubble's center == attach_y
        top_y = attach_y - branch_total_height(branch) + branch.bubbles[-1].h // 2

    # Place bubbles
    cur_y = top_y
    bubble_ys = []  # (top_y, bottom_y) for each bubble
    for i, b in enumerate(branch.bubbles):
        placed.bubbles.append((b, x, cur_y))
        bubble_ys.append((cur_y, cur_y + b.h))
        cur_y += b.h
        if i < len(branch.bubbles) - 1:
            gap = gap_for_pearls(branch.pearls[i])
            # Pearls in this gap
            for p in place_pearls(cx, cur_y, branch.pearls[i], PEARL_COLOR[branch.color]):
                placed.pearls.append(p)
            cur_y += gap

    # Solid connector line between bubbles
    if len(branch.bubbles) > 1:
        placed.branch_connectors.append((
            cx, bubble_ys[0][1], bubble_ys[-1][0], COLORS[branch.color][1]
        ))


def layout_arrow_to_branch(branch: Branch, attach_y: int, trunk_has_bubble: bool,
                           placed: Placed) -> None:
    """Add the trunk→branch arrow for `branch` at trunk Y `attach_y`."""
    if branch.side == 'left':
        x1 = TRUNK_X - BUBBLE_W // 2 if trunk_has_bubble else TRUNK_X
        x2 = LEFT_X + BUBBLE_W
        placed.branch_arrows.append((x1, attach_y, x2, attach_y))
    else:
        x1 = TRUNK_X + BUBBLE_W // 2 if trunk_has_bubble else TRUNK_X
        x2 = RIGHT_X
        placed.branch_arrows.append((x1, attach_y, x2, attach_y))
    if branch.label:
        # Default bias is 75% along the trunk→bubble arrow, which keeps
        # the label clear of neighbouring trunk bubbles (the Sokoban "up"
        # label would otherwise overlap The Oracle). Branches with a
        # short arrow or a roomy neighbourhood can override via
        # `label_pos` to sit nearer the midpoint.
        cx = x1 + int(round((x2 - x1) * branch.label_pos))
        placed.arrow_labels.append((cx, attach_y - 4, branch.label))


def layout_trunk(rows: list[TrunkRow], y_start: int, trunk_color_key: str,
                 placed: Placed) -> int:
    """Lay out a trunk section. Returns the final y position (end of trunk)."""
    cur_y = y_start
    trunk_start = cur_y
    for row in rows:
        if row.bubble:
            b = row.bubble
            x = TRUNK_X - b.w // 2
            placed.bubbles.append((b, x, cur_y))
            attach_y = cur_y + b.h // 2
            row_h = b.h
        else:
            # Pure branch point — trunk circle marker. The trunk pearl is
            # placed at the same rhythm as the surrounding pearls (one
            # PEARL_SPACING away from neighbours), not padded out by
            # PEARL_PADDING the way a full pearl batch is. The branch
            # bubble is off to the side and is free to extend above or
            # below this row's tight vertical strip.
            row_h = PEARL_SPACING - 2 * PEARL_PADDING  # = 2
            attach_y = cur_y + row_h // 2
            placed.trunk_circles.append((TRUNK_X, attach_y, COLORS[trunk_color_key][1]))

        if row.branch:
            layout_branch(row.branch, attach_y, placed)
            layout_arrow_to_branch(row.branch, attach_y, row.bubble is not None, placed)

        cur_y += row_h
        if row.pearls_below > 0:
            for p in place_pearls(TRUNK_X, cur_y, row.pearls_below, PEARL_COLOR[trunk_color_key]):
                placed.pearls.append(p)
            cur_y += gap_for_pearls(row.pearls_below)
        else:
            cur_y += GAP_NO_PEARL

    trunk_end = cur_y - GAP_NO_PEARL  # last gap shouldn't extend trunk
    # Trunk segment (drawn behind bubbles)
    placed.trunk_segments.append((TRUNK_X, trunk_start, trunk_end, COLORS[trunk_color_key][1]))
    return trunk_end


# ============================================================================
# Rendering
# ============================================================================

def text_el(x, y, content, **kwargs):
    parts = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in kwargs.items())
    # rsvg-convert misrenders EB Garamond's Qu ligature: the u is positioned
    # above the Q instead of nestled in its curve. Wrapping Q in a tspan
    # breaks the OpenType ligature substitution while preserving plain
    # rendering. (No effect on Chrome or fontspec/xelatex.)
    content = re.sub(r'Q(?=u)', '<tspan>Q</tspan>', content)
    return f'<text x="{x}" y="{y}" {parts}>{content}</text>'


def render_bubble(b: Bubble, x: int, y: int) -> list[str]:
    fill, stroke = COLORS[b.color]
    sw = 2.5 if (b.is_big or b.is_sanctum or b.color == 'castle') else 1.5
    rx = 8 if (b.is_big or b.is_sanctum) else 6
    cx = x + b.w // 2

    parts = [f'<rect x="{x}" y="{y}" width="{b.w}" height="{b.h}" rx="{rx}" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>']

    title = ('★ ' if b.star else '') + b.title

    # Color of text differs for sanctum (gold on dark)
    if b.is_sanctum:
        title_color = '#FFC857'
        detail_color = '#FFE680'
    elif b.color == 'castle':
        title_color = '#1f2933'
        detail_color = '#7A5A0A'
    elif b.color == 'ascension':
        title_color = '#7A5A0A'
        detail_color = '#7A5A0A'
    else:
        title_color = '#1f2933'
        detail_color = '#555'

    title_size = 17 if (b.is_big or b.is_sanctum) else 15
    detail_size = 14 if (b.is_big or b.is_sanctum) else 12
    title_weight = 600 if (b.is_big or b.is_sanctum or b.detail) else 600

    if b.detail:
        # Two-line layout
        title_y = y + b.h // 2 - 3
        detail_y = y + b.h // 2 + 14
        parts.append(text_el(cx, title_y, title,
                             font_size=title_size, font_weight=title_weight,
                             fill=title_color, text_anchor='middle'))
        parts.append(text_el(cx, detail_y, b.detail,
                             font_size=detail_size, font_style='italic',
                             fill=detail_color, text_anchor='middle'))
    else:
        # Single-line, centered
        title_y = y + b.h // 2 + 5
        parts.append(text_el(cx, title_y, title,
                             font_size=title_size, font_weight=title_weight,
                             fill=title_color, text_anchor='middle'))
    return parts


def render_pearls(pearls: list[tuple[int, int, str]]) -> list[str]:
    return [
        f'<circle cx="{x}" cy="{y}" r="{PEARL_R}" fill="{color}"/>'
        for x, y, color in pearls
    ]


def render_trunk_circles(circles: list[tuple[int, int, str]]) -> list[str]:
    return [
        f'<circle cx="{x}" cy="{y}" r="{PEARL_R}" fill="{color}"/>'
        for x, y, color in circles
    ]


def render_branch_arrows(arrows: list[tuple[int, int, int, int]]) -> list[str]:
    return [
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/>'
        for x1, y1, x2, y2 in arrows
    ]


def render_branch_connectors(connectors: list[tuple[int, int, int, str]]) -> list[str]:
    return [
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="2" fill="none"/>'
        for x, y1, y2, color in connectors
    ]


def render_trunk_segments(segments: list[tuple[int, int, int, str]]) -> list[str]:
    return [
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{TRUNK_W}" fill="none"/>'
        for x, y1, y2, color in segments
    ]


# ============================================================================
# Planes section (special: horizontal row + curved arrows)
# ============================================================================

def render_planes_section(y_start: int) -> tuple[list[str], int]:
    """Render the Planes section starting at y_start. Returns (svg parts, final y)."""
    parts = []
    bar_y = y_start
    bar_bottom = bar_y + SECT_BAR_H
    parts.extend(render_section_bar(bar_y, 'THE ELEMENTAL PLANES', TRUNK_PLANES))

    # Planes row: Earth, Air, Fire, Water (4 boxes, centered)
    plane_w = 120
    plane_h = 40
    gap_x = 48                                   # 20% wider than the original 40
    n = 4
    row_total = n * plane_w + (n - 1) * gap_x   # 4*120 + 3*48 = 624
    row_x_start = (WIDTH - row_total) // 2       # 68
    row_y = bar_bottom + 50                      # leave space for curved arrow

    earth_cx = row_x_start + plane_w // 2

    # Plane boxes (drawn before curved arrows so arrowheads are on top of box edges)
    plane_data = [
        ('Earth', 'earth'),
        ('Air',   'air'),
        ('Fire',  'fire'),
        ('Water', 'water'),
    ]
    plane_cx = []
    for i, (name, color_key) in enumerate(plane_data):
        x = row_x_start + i * (plane_w + gap_x)
        fill, stroke = COLORS[color_key]
        parts.append(f'<rect x="{x}" y="{row_y}" width="{plane_w}" height="{plane_h}" rx="6" '
                     f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        parts.append(text_el(x + plane_w // 2, row_y + plane_h // 2 + 6, name,
                             font_size=15, font_weight=600, fill='#1f2933', text_anchor='middle'))
        plane_cx.append(x + plane_w // 2)

    water_bottom = row_y + plane_h
    water_cx = plane_cx[-1]

    # Astral
    astral_y = water_bottom + 50
    astral_h = 42
    astral_w = 240
    astral_x = (WIDTH - astral_w) // 2
    astral_cx = WIDTH // 2

    fill, stroke = COLORS['astral']
    parts.append(f'<rect x="{astral_x}" y="{astral_y}" width="{astral_w}" height="{astral_h}" rx="6" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    parts.append(text_el(astral_cx, astral_y + 18, 'Astral Plane',
                         font_size=15, font_weight=600, fill='#1f2933', text_anchor='middle'))
    parts.append(text_el(astral_cx, astral_y + 34, 'three altars · pick yours',
                         font_size=12, font_style='italic', fill='#555', text_anchor='middle'))

    astral_bottom = astral_y + astral_h
    asc_y = astral_bottom + 18

    # Ascension (width matches Castle and Sanctum)
    asc_w = BIG_BUBBLE_W
    asc_h = 50
    asc_x = (WIDTH - asc_w) // 2
    fill, stroke = COLORS['ascension']
    parts.append(f'<rect x="{asc_x}" y="{asc_y}" width="{asc_w}" height="{asc_h}" rx="10" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
    parts.append(text_el(astral_cx, asc_y + 23, 'ASCENSION',
                         font_size=18, font_weight=700, fill='#7A5A0A',
                         text_anchor='middle', letter_spacing='0.1em'))
    parts.append(text_el(astral_cx, asc_y + 42, 'offer the Amulet at your altar',
                         font_size=11, font_style='italic', fill='#7A5A0A', text_anchor='middle'))

    # === Arrows drawn AFTER boxes so arrowheads sit on top of box edges ===

    # Curved arrow from bar bottom-center to Earth top-center.
    # The cubic forms a symmetric S (both control points at the midpoint
    # y of the cubic segment) so its end tangent is long-vertical and
    # smoothly continues into a vlen-px straight segment ending at the
    # Earth bubble's top — no kink at the join.
    vlen = 22
    cubic_end_y = row_y - vlen
    mid_y = (bar_bottom + cubic_end_y) // 2
    parts.append(
        f'<path d="M {WIDTH//2} {bar_bottom} '
        f'C {WIDTH//2} {mid_y} {earth_cx} {mid_y} {earth_cx} {cubic_end_y} '
        f'L {earth_cx} {row_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

    # Horizontal arrows between adjacent planes. The first arrow is
    # labeled "portals" since the planes are connected by randomly-
    # placed magic portals on each level (not stairs); the label
    # applies to all of them.
    for i in range(len(plane_data) - 1):
        x = row_x_start + i * (plane_w + gap_x)
        x1 = x + plane_w
        x2 = row_x_start + (i + 1) * (plane_w + gap_x)
        arr_y = row_y + plane_h // 2
        parts.append(
            f'<line x1="{x1}" y1="{arr_y}" x2="{x2}" y2="{arr_y}" '
            f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
        )
        if i == 0:
            parts.append(text_el((x1 + x2) // 2, arr_y - 4, 'portals',
                                 font_size=11, font_style='italic',
                                 fill='#5a5a5a', text_anchor='middle'))

    # Curved arrow Water bottom-center → Astral top-center, same S-into-line shape.
    cubic_end_y2 = astral_y - vlen
    mid_y2 = (water_bottom + cubic_end_y2) // 2
    parts.append(
        f'<path d="M {water_cx} {water_bottom} '
        f'C {water_cx} {mid_y2} {astral_cx} {mid_y2} {astral_cx} {cubic_end_y2} '
        f'L {astral_cx} {astral_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

    # Astral → Ascension
    parts.append(
        f'<line x1="{astral_cx}" y1="{astral_bottom}" x2="{astral_cx}" y2="{asc_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

    return parts, asc_y + asc_h


# ============================================================================
# Main SVG assembly
# ============================================================================

def render_section_bar(y: int, label: str, color: str) -> list[str]:
    text_y = y + SECT_BAR_H // 2 + SECT_BAR_FONT // 3   # baseline ~ visual center
    parts = [
        f'<rect x="{SECT_BAR_MARGIN}" y="{y}" width="{WIDTH - 2 * SECT_BAR_MARGIN}" '
        f'height="{SECT_BAR_H}" rx="4" fill="{color}"/>',
        text_el(WIDTH // 2, text_y, label,
                font_size=SECT_BAR_FONT, font_weight=600, fill='#fff',
                text_anchor='middle', letter_spacing='0.08em'),
    ]
    return parts


def _wrap_svg(parts: list[str], height: int, aria_label: str) -> str:
    """Wrap a list of SVG parts in an <svg> element that stacks block-flush
    against its siblings (display:block, no vertical margin)."""
    svg_open = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'role="img" aria-label="{aria_label}" '
        f'style="display:block;margin:0 auto;max-width:{WIDTH}px;width:100%;'
        f"height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;"
        f"font-feature-settings:'liga' 0, 'dlig' 0;\">"
    )
    defs = (
        '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs>'
    )
    return svg_open + defs + ''.join(parts) + '</svg>'


def _section_parts(placed: Placed, y_min: int, y_max: int, y_offset: int,
                   bar_label: str, bar_color: str,
                   extra_after: Optional[list[str]] = None) -> list[str]:
    """Build the SVG body for one section: trunk + bar + boxes + pearls,
    with all coordinates translated to local (subtract y_offset)."""
    parts: list[str] = []

    # Layer 1: trunk segments (clipped to [y_min, y_max])
    for x, sy1, sy2, color in placed.trunk_segments:
        cy1 = max(sy1, y_min)
        cy2 = min(sy2, y_max)
        if cy1 < cy2:
            parts.append(
                f'<line x1="{x}" y1="{cy1 - y_offset}" x2="{x}" y2="{cy2 - y_offset}" '
                f'stroke="{color}" stroke-width="{TRUNK_W}" fill="none"/>'
            )

    # Layer 2: section bar at local y=0
    parts.extend(render_section_bar(0, bar_label, bar_color))

    # Layer 3: branch connectors (BEHIND bubbles)
    for x, sy1, sy2, color in placed.branch_connectors:
        cy1 = max(sy1, y_min)
        cy2 = min(sy2, y_max)
        if cy1 < cy2:
            parts.append(
                f'<line x1="{x}" y1="{cy1 - y_offset}" x2="{x}" y2="{cy2 - y_offset}" '
                f'stroke="{color}" stroke-width="2" fill="none"/>'
            )

    # Layer 4: bubbles (filter by center y)
    for b, x, y in placed.bubbles:
        if y_min <= y + b.h // 2 < y_max:
            parts.extend(render_bubble(b, x, y - y_offset))

    # Layer 5: branch arrows (ON TOP of bubbles, BEHIND pearls so arrows
    # appear to emerge from the trunk pearl rather than lay across it)
    for x1, y1, x2, y2 in placed.branch_arrows:
        if y_min <= y1 < y_max:
            parts.append(
                f'<line x1="{x1}" y1="{y1 - y_offset}" x2="{x2}" y2="{y2 - y_offset}" '
                f'stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/>'
            )

    # Layer 6: arrow labels
    for x, y, label in placed.arrow_labels:
        if y_min <= y < y_max:
            parts.append(text_el(x, y - y_offset, label,
                                 font_size=11, font_style='italic',
                                 fill='#5a5a5a', text_anchor='middle'))

    # Layer 7: trunk circles (on top of branch arrows so the arrow
    # appears to emerge from the pearl)
    for x, y, color in placed.trunk_circles:
        if y_min <= y < y_max:
            parts.append(f'<circle cx="{x}" cy="{y - y_offset}" r="{PEARL_R}" fill="{color}"/>')

    # Layer 8: pearls (top)
    for x, y, color in placed.pearls:
        if y_min <= y < y_max:
            parts.append(f'<circle cx="{x}" cy="{y - y_offset}" r="{PEARL_R}" fill="{color}"/>')

    # Optional extras (e.g. climb-back line + label, drawn in local coords)
    if extra_after:
        parts.extend(extra_after)

    return parts


def render_sections() -> dict[str, str]:
    """Render the three map sections. Returns {'dod', 'geh', 'planes'}
    mapped to their standalone SVG strings."""
    return _render(return_sections=True)


def render_svg() -> str:
    """Build the assembled three-section figure as one markdown string."""
    return _render(return_sections=False)


def _render(*, return_sections: bool):
    # === Layout (absolute Y coordinates) ===
    placed = Placed()

    dod_bar_y = 0
    dod_start_y = dod_bar_y + SECT_BAR_H + 16
    dod_end_y = layout_trunk(DOD, dod_start_y, 'dod', placed)

    geh_bar_y = dod_end_y + TRUNK_PADDING
    geh_bar_bottom = geh_bar_y + SECT_BAR_H
    geh_start_y = geh_bar_bottom + TRUNK_PADDING
    geh_end_y = layout_trunk(GEH, geh_start_y, 'geh', placed)

    climb_y_start = geh_end_y + 6
    climb_y_end = climb_y_start + 50
    planes_bar_y = climb_y_end

    placed.trunk_segments = [
        (TRUNK_X, dod_start_y, geh_bar_bottom, COLORS['dod'][1]),
        (TRUNK_X, geh_bar_y, geh_end_y, COLORS['geh'][1]),
    ]

    # === Section 1: DoD ===
    # Spans y=0 to the top of the Geh bar.
    sec_dod_top = 0
    sec_dod_bottom = geh_bar_y
    dod_parts = _section_parts(
        placed, y_min=sec_dod_top, y_max=sec_dod_bottom, y_offset=sec_dod_top,
        bar_label='DUNGEONS OF DOOM', bar_color=TRUNK_DOD,
    )
    dod_svg = _wrap_svg(dod_parts, sec_dod_bottom - sec_dod_top,
                        aria_label='Dungeons of Doom map')

    # === Section 2: Gehennom (includes climb-back at the bottom) ===
    sec_geh_top = geh_bar_y
    sec_geh_bottom = planes_bar_y
    climb_local_start = climb_y_start - sec_geh_top
    climb_local_end = climb_y_end - sec_geh_top
    climb_label_y = (climb_local_start + climb_local_end) // 2 + 5
    climb_extras = [
        f'<line x1="{TRUNK_X}" y1="{climb_local_start}" x2="{TRUNK_X}" y2="{climb_local_end}" '
        f'stroke="#5B8E3A" stroke-width="2.5" stroke-dasharray="7,5" fill="none"/>',
        f'<text x="{TRUNK_X + 20}" y="{climb_label_y}" '
        f'font-size="15" font-weight="600" font-style="italic" fill="#5B8E3A">'
        f'now go <tspan style="font-weight:800;font-size:17px">ALL</tspan> '
        f'the way back up...</text>',
    ]
    geh_parts = _section_parts(
        placed, y_min=sec_geh_top, y_max=sec_geh_bottom, y_offset=sec_geh_top,
        bar_label='GEHENNOM', bar_color=TRUNK_GEH,
        extra_after=climb_extras,
    )
    geh_svg = _wrap_svg(geh_parts, sec_geh_bottom - sec_geh_top,
                        aria_label='Gehennom map')

    # === Section 3: Planes (rendered in its own coord system, bar at y=0) ===
    plane_parts, planes_local_end = render_planes_section(0)
    planes_svg = _wrap_svg(plane_parts, planes_local_end + 10,
                           aria_label='Elemental Planes and Ascension')

    if return_sections:
        return {'dod': dod_svg, 'geh': geh_svg, 'planes': planes_svg}

    # === Assemble the figure ===
    figure = (
        '<div><figure style="margin: 1.5em 0; text-align: center;">'
        + dod_svg + geh_svg + planes_svg
        + '<figcaption style="font-style: italic; color: #5a5a5a; '
          'font-size: 0.9em; margin-top: 0.5em;">'
          'Branches extend left and right of the main trunk. '
          'Pearls (small colored dots) indicate the approximate number of '
          'intervening dungeon levels. ★ marks the three Invocation items '
          '(Bell of Opening, Candelabrum, Book of the Dead) needed to enter '
          "Moloch's Sanctum and claim the Amulet."
        '</figcaption></figure></div>'
    )
    return figure


# ============================================================================
# Inplace replacement
# ============================================================================

MARKER_BEGIN = '<!-- DMAP-BEGIN -->'
MARKER_END = '<!-- DMAP-END -->'


def replace_inplace(target_md: Path) -> None:
    text = target_md.read_text()
    if MARKER_BEGIN not in text or MARKER_END not in text:
        sys.exit(f'Markers not found in {target_md}. Add\n  {MARKER_BEGIN}\n  ...\n  {MARKER_END}\naround the SVG block.')
    new_svg = render_svg()
    pattern = re.compile(re.escape(MARKER_BEGIN) + r'.*?' + re.escape(MARKER_END), re.DOTALL)
    new_text = pattern.sub(MARKER_BEGIN + '\n' + new_svg + '\n' + MARKER_END, text)
    target_md.write_text(new_text)
    print(f'Updated {target_md}', file=sys.stderr)


def write_pdfs(images_dir: Path) -> None:
    """Write each map section as a standalone SVG plus PDF (via rsvg-convert)
    into images_dir/. The PDFs are what the LaTeX print pipeline includes;
    the SVGs are kept alongside for diffability."""
    if shutil.which('rsvg-convert') is None:
        sys.exit('rsvg-convert not found. Install with: brew install librsvg')
    images_dir.mkdir(parents=True, exist_ok=True)
    sections = render_sections()
    for name, svg in sections.items():
        svg_path = images_dir / f'dmap-{name}.svg'
        pdf_path = images_dir / f'dmap-{name}.pdf'
        svg_path.write_text(svg)
        subprocess.run(
            ['rsvg-convert', '-f', 'pdf', '-o', str(pdf_path), str(svg_path)],
            check=True,
        )
        print(f'Wrote {pdf_path}', file=sys.stderr)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == '--inplace':
        here = Path(__file__).parent
        replace_inplace(here / 'companion.md')
        write_pdfs(here / 'images')
    elif len(sys.argv) > 1 and sys.argv[1] == '--pdfs':
        write_pdfs(Path(__file__).parent / 'images')
    else:
        print(render_svg())


if __name__ == '__main__':
    main()
