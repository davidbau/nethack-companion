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
PEARL_SPACING = 12                    # vertical advance per pearl
PEARL_PADDING = 6                     # pad before first/after last pearl in a gap

GAP_NO_PEARL = 10                     # gap between bubbles when no pearls between

TITLE_Y = 36
SECT_BAR_H = 26
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


@dataclass
class TrunkRow:
    bubble: Optional[Bubble] = None           # None = pure branch point (circle marker)
    branch: Optional[Branch] = None
    pearls_below: int = 0                     # pearls between this row and the next


# ============================================================================
# Dungeon structure
# ============================================================================

DOD: list[TrunkRow] = [
    TrunkRow(bubble=Bubble('Dlvl 1 — Entry', 'up-stair to exit'), pearls_below=2),
    TrunkRow(  # Mines branch LEFT
        branch=Branch(
            side='left', color='mines',
            bubbles=[
                Bubble('Gnomish Mines', '8-10 levels', color='mines'),
                Bubble('Minetown', 'shops, temple', color='mines'),
                Bubble("Mine's End", 'luckstone', color='mines'),
            ],
            pearls=[2, 3],
            attach='top',
        ),
        pearls_below=5,
    ),
    TrunkRow(  # Oracle + Sokoban RIGHT
        bubble=Bubble('The Oracle', 'paid hints'),
        branch=Branch(
            side='right', color='soko',
            bubbles=[
                Bubble('Sokoban prize', 'bag of holding/amulet of reflection', color='soko'),
                Bubble('Sokoban entry ↑', color='soko'),
            ],
            pearls=[2],
            attach='bottom',
        ),
        pearls_below=2,
    ),
    TrunkRow(  # Quest portal + Quest RIGHT
        bubble=Bubble('Quest portal', 'role-specific portal'),
        branch=Branch(
            side='right', color='quest',
            bubbles=[
                Bubble('Quest entry', "your role's dungeon", color='quest'),
                Bubble('Quest goal', 'Bell of Opening, role artifact', color='quest', star=True),
            ],
            pearls=[3],
            attach='top',
        ),
        pearls_below=2,
    ),
    TrunkRow(bubble=Bubble('Big Room (40%)'), pearls_below=2),
    TrunkRow(bubble=Bubble('Rogue Level'), pearls_below=1),
    TrunkRow(  # Fort Ludios branch LEFT
        branch=Branch(
            side='left', color='ludios',
            bubbles=[Bubble('Fort Ludios', 'vault of gold', color='ludios')],
            pearls=[],
            attach='top',
        ),
        pearls_below=3,
    ),
    TrunkRow(bubble=Bubble("Medusa's Island", color='medusa'), pearls_below=2),
    TrunkRow(bubble=Bubble('THE CASTLE', 'wand of wishing', color='castle', is_big=True)),
]

GEH: list[TrunkRow] = [
    TrunkRow(bubble=Bubble('Valley of the Dead', "Gehennom's entrance", color='geh'), pearls_below=1),
    TrunkRow(bubble=Bubble("Asmodeus's Lair", color='geh'), pearls_below=1),
    TrunkRow(bubble=Bubble("Juiblex's Swamp", color='geh'), pearls_below=1),
    TrunkRow(bubble=Bubble("Baalzebub's Lair", color='geh'), pearls_below=1),
    TrunkRow(  # Vlad's Tower branch RIGHT (attaches at bottom; tower goes UP)
        branch=Branch(
            side='right', color='vlad',
            bubbles=[
                Bubble('Candelabrum', color='vlad', star=True),
                Bubble("Vlad's Tower ↑", color='vlad'),
            ],
            pearls=[1],
            attach='bottom',
        ),
        pearls_below=1,
    ),
    TrunkRow(bubble=Bubble('Orcus-Town', 'wand of death · Eye of the Aethiopica', color='geh'), pearls_below=2),
    TrunkRow(bubble=Bubble("The Wizard's Tower", '★ Book of the Dead', color='geh'), pearls_below=3),
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
            # Pure branch point — circle marker on trunk
            attach_y = cur_y + BUBBLE_H // 2  # treat as a normal row height advance
            placed.trunk_circles.append((TRUNK_X, attach_y, COLORS[trunk_color_key][1]))
            row_h = BUBBLE_H

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
        f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>'
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
    parts.append(f'<rect x="40" y="{bar_y}" width="680" height="{SECT_BAR_H}" rx="4" fill="{TRUNK_PLANES}"/>')
    parts.append(text_el(WIDTH // 2, bar_y + 18, 'THE ELEMENTAL PLANES',
                         font_size=15, font_weight=600, fill='#fff',
                         text_anchor='middle', letter_spacing='0.08em'))

    # Planes row: Earth, Air, Fire, Water (4 boxes, centered)
    plane_w = 120
    plane_h = 40
    gap_x = 40
    n = 4
    row_total = n * plane_w + (n - 1) * gap_x   # 4*120 + 3*40 = 600
    row_x_start = (WIDTH - row_total) // 2       # 80
    row_y = bar_bottom + 50                      # leave space for curved arrow

    # Curved arrow from bar bottom-center to Earth top-center
    earth_cx = row_x_start + plane_w // 2
    parts.append(
        f'<path d="M {WIDTH//2} {bar_bottom} '
        f'C {WIDTH//2} {row_y - 6} {earth_cx} {row_y - 6} {earth_cx} {row_y - 2} '
        f'L {earth_cx} {row_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

    # Each plane box
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
        if i < len(plane_data) - 1:
            x1 = x + plane_w
            x2 = row_x_start + (i + 1) * (plane_w + gap_x)
            arr_y = row_y + plane_h // 2
            parts.append(
                f'<line x1="{x1}" y1="{arr_y}" x2="{x2}" y2="{arr_y}" '
                f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
            )

    water_bottom = row_y + plane_h
    water_cx = plane_cx[-1]

    # Curved arrow from Water bottom-center to Astral top-center
    astral_y = water_bottom + 50
    astral_h = 42
    astral_w = 240
    astral_x = (WIDTH - astral_w) // 2
    astral_cx = WIDTH // 2

    parts.append(
        f'<path d="M {water_cx} {water_bottom} '
        f'C {water_cx} {astral_y - 6} {astral_cx} {astral_y - 6} {astral_cx} {astral_y - 2} '
        f'L {astral_cx} {astral_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

    # Astral
    fill, stroke = COLORS['astral']
    parts.append(f'<rect x="{astral_x}" y="{astral_y}" width="{astral_w}" height="{astral_h}" rx="6" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    parts.append(text_el(astral_cx, astral_y + 18, 'Astral Plane',
                         font_size=15, font_weight=600, fill='#1f2933', text_anchor='middle'))
    parts.append(text_el(astral_cx, astral_y + 34, 'three altars · pick yours',
                         font_size=12, font_style='italic', fill='#555', text_anchor='middle'))

    # Arrow Astral → Ascension
    astral_bottom = astral_y + astral_h
    asc_y = astral_bottom + 18
    parts.append(
        f'<line x1="{astral_cx}" y1="{astral_bottom}" x2="{astral_cx}" y2="{asc_y}" '
        f'stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>'
    )

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

    return parts, asc_y + asc_h


# ============================================================================
# Main SVG assembly
# ============================================================================

def render_section_bar(y: int, label: str, color: str) -> list[str]:
    parts = [
        f'<rect x="{SECT_BAR_MARGIN}" y="{y}" width="{WIDTH - 2 * SECT_BAR_MARGIN}" '
        f'height="{SECT_BAR_H}" rx="4" fill="{color}"/>',
        text_el(WIDTH // 2, y + 18, label,
                font_size=15, font_weight=600, fill='#fff',
                text_anchor='middle', letter_spacing='0.08em'),
    ]
    return parts


def render_svg() -> str:
    # Lay out DoD
    placed = Placed()

    dod_start_y = 92
    dod_bar_y = dod_start_y - 16 - SECT_BAR_H
    # DoD bar above trunk
    bar_parts = render_section_bar(dod_bar_y, 'DUNGEONS OF DOOM', TRUNK_DOD)

    dod_end_y = layout_trunk(DOD, dod_start_y, 'dod', placed)

    # Geh bar
    geh_bar_y = dod_end_y + TRUNK_PADDING
    geh_bar_bottom = geh_bar_y + SECT_BAR_H
    geh_start_y = geh_bar_bottom + TRUNK_PADDING
    geh_end_y = layout_trunk(GEH, geh_start_y, 'geh', placed)

    # Climb-back dashed line
    climb_y_start = geh_end_y + 6
    climb_y_end = climb_y_start + 50
    planes_bar_y = climb_y_end

    # Extend trunk segments to touch the bars (so the bars cover the transition)
    # DoD trunk should extend down into the bar
    # Geh trunk should extend down past Sanctum to climb-back start
    # We'll handle this by overwriting the placed trunk_segments
    placed.trunk_segments = []
    placed.trunk_segments.append((TRUNK_X, dod_start_y, geh_bar_bottom, COLORS['dod'][1]))
    placed.trunk_segments.append((TRUNK_X, geh_bar_y, geh_end_y, COLORS['geh'][1]))

    # Assemble SVG
    parts = []

    # Title
    parts.append(text_el(WIDTH // 2, TITLE_Y, 'The Dungeon',
                         font_size=24, font_weight=600, fill='#1f2933', text_anchor='middle'))

    # Trunk segments (drawn first so bubbles render on top)
    parts.extend(render_trunk_segments(placed.trunk_segments))

    # DoD bar
    parts.extend(bar_parts)

    # Bubbles
    for b, x, y in placed.bubbles:
        parts.extend(render_bubble(b, x, y))

    # Trunk circles
    parts.extend(render_trunk_circles(placed.trunk_circles))

    # Geh bar (drawn after bubbles? actually it should cover trunk between DoD/Geh)
    parts.extend(render_section_bar(geh_bar_y, 'GEHENNOM', TRUNK_GEH))

    # Branch connectors
    parts.extend(render_branch_connectors(placed.branch_connectors))

    # Branch arrows
    parts.extend(render_branch_arrows(placed.branch_arrows))

    # Pearls (rendered last so they're on top)
    parts.extend(render_pearls(placed.pearls))

    # Climb-back dashed line
    parts.append(
        f'<line x1="{TRUNK_X}" y1="{climb_y_start}" x2="{TRUNK_X}" y2="{climb_y_end}" '
        f'stroke="#5B8E3A" stroke-width="2.5" stroke-dasharray="7,5" fill="none"/>'
    )
    parts.append(text_el(TRUNK_X + 20, climb_y_start + (climb_y_end - climb_y_start) // 2 + 5,
                         '',
                         font_size=15, font_weight=600,
                         font_style='italic', fill='#5B8E3A',
                         text_anchor='start'))
    # Replace above empty content with proper tspan for "ALL" emphasis
    parts[-1] = (f'<text x="{TRUNK_X + 20}" '
                 f'y="{climb_y_start + (climb_y_end - climb_y_start) // 2 + 5}" '
                 f'font-size="15" font-weight="600" font-style="italic" '
                 f'fill="#5B8E3A">'
                 f'now go <tspan style="font-weight:800;font-size:17px">ALL</tspan> '
                 f'the way back up...</text>')

    # Planes section
    plane_parts, total_y = render_planes_section(planes_bar_y)
    parts.extend(plane_parts)

    # Wrap in SVG container
    view_h = total_y + 20
    svg_open = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {view_h}" '
        f'role="img" aria-label="The dungeon overview map" '
        f'style="max-width: {WIDTH}px; width: 100%; height: auto; '
        f"font-family: 'EB Garamond', 'Garamond', 'Georgia', serif;\">"
    )
    defs = (
        '<defs>'
        '<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/>'
        '</marker>'
        '</defs>'
    )
    title_el = '<title>The Dungeon Overview Map</title>'
    body = ''.join(parts)
    svg = svg_open + title_el + defs + body + '</svg>'

    figure = (
        '<div><figure style="margin: 1.5em 0; text-align: center;">'
        + svg
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


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == '--inplace':
        target = Path(__file__).parent / 'companion.md'
        replace_inplace(target)
    else:
        print(render_svg())


if __name__ == '__main__':
    main()
