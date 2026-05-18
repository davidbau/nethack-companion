#!/usr/bin/env python3
"""Inspect the Lulu Novella duplex template by dumping ALL drawings and
text on each page, so we can identify the bleed/trim/safety/fold lines."""

import fitz
from pathlib import Path

PDF = Path(__file__).parent / "template.pdf"

doc = fitz.open(PDF)
for page_num, page in enumerate(doc, start=1):
    print(f"\n=== Page {page_num}: {page.rect.width:.3f} x {page.rect.height:.3f} pts")
    # Try extra=True to get more detail
    drawings = page.get_drawings(extended=True)
    print(f"Drawings: {len(drawings)}")
    for i, d in enumerate(drawings[:30]):
        print(f"  [{i}] type={d.get('type')} color={d.get('color')} fill={d.get('fill')} stroke_opacity={d.get('stroke_opacity')} dashes={d.get('dashes')}")
        r = d.get("rect")
        if r:
            print(f"      rect: ({r.x0:.2f}, {r.y0:.2f}) - ({r.x1:.2f}, {r.y1:.2f})  w={r.width:.2f} h={r.height:.2f}")
        items = d.get("items", [])
        for item in items[:6]:
            print(f"      item: {item[0]}  {[str(x) for x in item[1:4]]}")
    # Also try text — to locate "SPINE" / "BACK COVER" etc.
    print(f"\nText spans:")
    text_dict = page.get_text("dict")
    for block in text_dict.get("blocks", [])[:50]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "").strip()
                if text:
                    bbox = span["bbox"]
                    print(f"  '{text[:40]}' bbox=({bbox[0]:.1f},{bbox[1]:.1f})-({bbox[2]:.1f},{bbox[3]:.1f})")
