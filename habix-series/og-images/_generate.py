#!/usr/bin/env python3
"""Generate 1200x630 OG image PNGs for habix-series lectures.

Pipeline:
  - For 7 lectures with existing SVG diagrams: embed the diagram into a
    1200x630 wrapper SVG (centered with wordmark) → cairosvg → PNG.
  - For 10 lectures without diagrams: build a text-card SVG → cairosvg → PNG.

Font: Noto Sans CJK KR (installed via fonts-noto-cjk).
"""
from __future__ import annotations

import json
import re
import os
from pathlib import Path

import cairosvg

ROOT = Path("/home/user/AI_Engineer/habix-series")
DIAG_DIR = ROOT / "diagrams"
META_DIR = ROOT / "metadata"
OUT_DIR = ROOT / "og-images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CANVAS_W, CANVAS_H = 1200, 630
BG = "#faf8f3"
INK = "#1a1a1a"
BLUE = "#1e3a8a"
RED = "#c1121f"
GREEN = "#2d6a4f"
MUTED = "#595959"
FONT_STACK = "'Noto Sans CJK KR','Noto Sans KR','NanumSquare','NanumBarunGothic','Pretendard',sans-serif"

# slug -> diagram SVG filename
DIAGRAM_MAP = {
    "ch01-why-smart-ai-cant-finish": "ch01-barehand-vs-harness.svg",
    "ch02-set-up-the-workshop": "ch02-five-rooms-floorplan.svg",
    "ch04-claude-md-one-page": "ch04-claude-md-3layer.svg",
    "ch06-five-minute-briefing": "ch06-initialization-timeline.svg",
    "ch09-no-victory-without-evidence": "ch09-verification-ladder.svg",
    "ch11-window-into-ai": "ch11-four-windows.svg",
    "capstone-30-day-routine-challenge": "capstone-30day-gantt.svg",
}


def load_meta(slug: str) -> dict:
    return json.loads((META_DIR / f"{slug}.json").read_text(encoding="utf-8"))


def parse_viewbox(svg_text: str) -> tuple[float, float, float, float]:
    m = re.search(r'viewBox\s*=\s*"([^"]+)"', svg_text)
    if not m:
        return (0.0, 0.0, 800.0, 600.0)
    parts = [float(x) for x in m.group(1).split()]
    return tuple(parts)  # type: ignore


def strip_svg_wrapper(svg_text: str) -> str:
    """Return only the inner content of an SVG (children of <svg>)."""
    inner = re.sub(r"^.*?<svg\b[^>]*>", "", svg_text, count=1, flags=re.DOTALL)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.DOTALL)
    return inner


def short_chapter_label(chapter_number: str) -> str:
    # 00a → P-01, 00b → P-02, 00c → P-03 (prelude chapters)
    prelude_map = {"00a": "P-01", "00b": "P-02", "00c": "P-03"}
    if chapter_number in prelude_map:
        return prelude_map[chapter_number]
    if chapter_number == "capstone":
        return "CAPSTONE"
    return f"Ch.{chapter_number}"


# Map of slug -> short chapter tag used in wordmark for diagram cards.
def wordmark_chapter(chapter_number: str) -> str:
    if chapter_number == "capstone":
        return "capstone"
    if chapter_number.startswith("00"):
        return f"p{chapter_number[2:]}" if len(chapter_number) > 2 else "p"
    return f"ch{chapter_number}"


def build_diagram_card(slug: str, meta: dict, svg_path: Path) -> str:
    """Wrap an existing diagram SVG inside a 1200x630 canvas."""
    src = svg_path.read_text(encoding="utf-8")
    # Diagrams reference 'Pretendard' / 'Noto Sans KR' which aren't installed
    # in this environment. cairosvg won't auto-fallback, so rewrite the
    # font-family string to put the available font (Noto Sans CJK KR) first.
    src = re.sub(
        r"font-family:\s*[^;\"}]+",
        f"font-family: {FONT_STACK}",
        src,
    )
    vb = parse_viewbox(src)
    _, _, vw, vh = vb
    inner = strip_svg_wrapper(src)

    # Reserve top/bottom for labels
    margin_top = 30
    margin_bottom = 60
    avail_w = CANVAS_W - 80
    avail_h = CANVAS_H - margin_top - margin_bottom
    scale = min(avail_w / vw, avail_h / vh)
    draw_w = vw * scale
    draw_h = vh * scale
    tx = (CANVAS_W - draw_w) / 2
    ty = margin_top + (avail_h - draw_h) / 2

    chapter = meta.get("chapter_number", "")
    wm = f"habix-series · {wordmark_chapter(chapter)}"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">
  <style>
    .font-base {{ font-family: {FONT_STACK}; }}
    .wm {{ font-size: 18px; font-weight: 600; fill: {MUTED}; letter-spacing: 0.5px; }}
    .wm-dot {{ fill: {BLUE}; }}
  </style>
  <rect width="{CANVAS_W}" height="{CANVAS_H}" fill="{BG}"/>
  <g transform="translate({tx:.2f},{ty:.2f}) scale({scale:.5f})">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" width="{vw}" height="{vh}">{inner}</svg>
  </g>
  <circle cx="60" cy="{CANVAS_H-32}" r="6" class="wm-dot"/>
  <text x="76" y="{CANVAS_H-26}" class="font-base wm">{wm}</text>
  <text x="{CANVAS_W-40}" y="{CANVAS_H-26}" text-anchor="end" class="font-base wm">habix.ai</text>
</svg>
"""


# -------- Text-card SVG generator --------

# tail tokens to strip from og_title (e.g. " | habix") so the heading is clean
TITLE_TAIL_RE = re.compile(r"\s*\|\s*habix\s*$", re.IGNORECASE)


def clean_title(og_title: str) -> tuple[str, str]:
    """Split og_title into (heading, subline) by the em-dash separator.

    Example: "할 일 한 장이 모든 것을 바꾼다 — 하네스 엔지니어링 Ch.08 | habix"
        ->  ("할 일 한 장이 모든 것을 바꾼다", "하네스 엔지니어링 Ch.08")
    """
    t = TITLE_TAIL_RE.sub("", og_title).strip()
    if "—" in t:
        head, sub = t.split("—", 1)
        return head.strip(), sub.strip()
    return t, ""


def wrap_text(text: str, max_chars: int) -> list[str]:
    """Wrap Korean text into lines without splitting words at spaces if possible.
    Korean lines wrap roughly by character count since no inter-word spacing.
    """
    text = text.strip()
    if not text:
        return []
    # Prefer to break at spaces near max_chars
    lines: list[str] = []
    while len(text) > max_chars:
        cut = max_chars
        # search for a space within the last 8 chars window
        space_idx = text.rfind(" ", max_chars - 8, max_chars + 4)
        if space_idx > 0:
            cut = space_idx
        lines.append(text[:cut].rstrip())
        text = text[cut:].lstrip()
    if text:
        lines.append(text)
    return lines


def build_text_card(slug: str, meta: dict) -> str:
    og_title = meta.get("og_title", "")
    desc = meta.get("og_description", "")
    key_concept = meta.get("key_concept", "")
    chapter = meta.get("chapter_number", "")

    heading, sub = clean_title(og_title)

    # Heading sizing: shrink if long
    heading_lines = wrap_text(heading, 18)
    if len(heading_lines) <= 2:
        h_size = 70
        h_lh = 90
    elif len(heading_lines) <= 3:
        h_size = 60
        h_lh = 78
    else:
        # too long → re-wrap with more chars
        heading_lines = wrap_text(heading, 22)
        h_size = 50
        h_lh = 66

    # Description: wrap to 2-3 lines, shrink font if 3 lines needed
    desc_lines = wrap_text(desc, 38)
    if len(desc_lines) > 2:
        desc_lines = wrap_text(desc, 44)
    if len(desc_lines) > 3:
        desc_lines = desc_lines[:3]

    chap_tag = short_chapter_label(chapter)

    # Vertical layout
    y_chip = 110
    # Approximate chip width: ~14px per character + 36px padding
    chip_w = max(110, len(chap_tag) * 16 + 36)
    # heading start
    total_h_block = h_lh * len(heading_lines)
    y_heading_start = 220
    y_desc_start = y_heading_start + total_h_block + 60

    # build heading tspans
    heading_tspans = []
    for i, line in enumerate(heading_lines):
        dy = 0 if i == 0 else h_lh
        heading_tspans.append(f'<tspan x="80" dy="{dy}">{escape_xml(line)}</tspan>')
    heading_block = "".join(heading_tspans)

    desc_tspans = []
    for i, line in enumerate(desc_lines):
        dy = 0 if i == 0 else 36
        desc_tspans.append(f'<tspan x="80" dy="{dy}">{escape_xml(line)}</tspan>')
    desc_block = "".join(desc_tspans)

    # Key concept ribbon (bottom-left)
    kc_text = escape_xml(key_concept) if key_concept else ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">
  <style>
    .font-base {{ font-family: {FONT_STACK}; }}
    .chip-text {{ font-size: 22px; font-weight: 700; fill: #ffffff; letter-spacing: 1px; }}
    .heading {{ font-size: {h_size}px; font-weight: 800; fill: {INK}; }}
    .desc {{ font-size: 26px; font-weight: 400; fill: {MUTED}; }}
    .sub {{ font-size: 22px; font-weight: 600; fill: {BLUE}; letter-spacing: 0.5px; }}
    .kc {{ font-size: 20px; font-weight: 600; fill: {GREEN}; }}
    .wm {{ font-size: 20px; font-weight: 700; fill: {INK}; letter-spacing: 0.5px; }}
    .wm-muted {{ font-size: 18px; font-weight: 500; fill: {MUTED}; }}
  </style>

  <rect width="{CANVAS_W}" height="{CANVAS_H}" fill="{BG}"/>
  <rect x="0" y="0" width="14" height="{CANVAS_H}" fill="{BLUE}"/>
  <rect x="{CANVAS_W-14}" y="0" width="14" height="{CANVAS_H}" fill="{BLUE}" opacity="0.15"/>

  <!-- chapter chip -->
  <rect x="80" y="{y_chip-36}" rx="6" ry="6" width="{chip_w}" height="48" fill="{BLUE}"/>
  <text x="{80 + chip_w/2:.1f}" y="{y_chip-3}" text-anchor="middle" class="font-base chip-text">{escape_xml(chap_tag)}</text>

  <!-- subtitle (series tag) -->
  <text x="{80 + chip_w + 20}" y="{y_chip-3}" class="font-base sub">{escape_xml(sub) if sub else '하네스 엔지니어링'}</text>

  <!-- heading -->
  <text y="{y_heading_start}" class="font-base heading">{heading_block}</text>

  <!-- description -->
  <text y="{y_desc_start}" class="font-base desc">{desc_block}</text>

  <!-- key concept -->
  <text x="80" y="{CANVAS_H-90}" class="font-base kc">핵심 개념 · {kc_text}</text>

  <!-- wordmarks -->
  <line x1="80" y1="{CANVAS_H-60}" x2="{CANVAS_W-80}" y2="{CANVAS_H-60}" stroke="#d4ccc0" stroke-width="1"/>
  <circle cx="88" cy="{CANVAS_H-28}" r="6" fill="{BLUE}"/>
  <text x="104" y="{CANVAS_H-22}" class="font-base wm">habix-series</text>
  <text x="260" y="{CANVAS_H-22}" class="font-base wm-muted">하네스 엔지니어링</text>
  <text x="{CANVAS_W-80}" y="{CANVAS_H-22}" text-anchor="end" class="font-base wm">habix.ai</text>
</svg>
"""


def escape_xml(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
              .replace('"', "&quot;").replace("'", "&apos;"))


# -------- Main --------

def render_png(svg_str: str, out_path: Path) -> None:
    cairosvg.svg2png(
        bytestring=svg_str.encode("utf-8"),
        write_to=str(out_path),
        output_width=CANVAS_W,
        output_height=CANVAS_H,
    )


def main() -> None:
    index = json.loads((META_DIR / "index.json").read_text(encoding="utf-8"))
    lectures = index["lectures"]

    results: list[tuple[str, str, int]] = []  # (slug, kind, bytes)
    for lec in lectures:
        slug = lec["slug"]
        meta = load_meta(slug)
        out_png = OUT_DIR / f"{slug}.png"

        if slug in DIAGRAM_MAP:
            svg_src = DIAG_DIR / DIAGRAM_MAP[slug]
            svg_str = build_diagram_card(slug, meta, svg_src)
            kind = "diagram"
        else:
            svg_str = build_text_card(slug, meta)
            kind = "text"

        # also persist the wrapper SVG alongside for debug
        # (kept out by default; uncomment if needed)
        # (OUT_DIR / f"{slug}.svg").write_text(svg_str, encoding="utf-8")
        render_png(svg_str, out_png)
        size = out_png.stat().st_size
        results.append((slug, kind, size))
        print(f"  [{kind:7s}] {slug}.png  {size/1024:6.1f} KB")

    total = sum(r[2] for r in results)
    print(f"\nGenerated {len(results)} files, avg {total/len(results)/1024:.1f} KB")


if __name__ == "__main__":
    main()
