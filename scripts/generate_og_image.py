#!/usr/bin/env python3
"""
Generates assets/images/og-default.png — the site-wide Open Graph card.

`_config.yml` sets `og_image: /assets/images/og-default.png`, and every page
emits it as `og:image` / `twitter:image`. The file was referenced but had never
been created, so every social preview on the site resolved to a 404.

Kept as a script rather than a committed-only binary so the design stays
editable in source control: change a colour or a line here, not in an image
editor. The output is committed too, because the GitHub Pages build is Jekyll
and does not run Python.

    python3 scripts/generate_og_image.py

Colours are the site design tokens from assets/css/base.css `:root`.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ── Design tokens (assets/css/base.css) ──────────────────────────────────────
BG = (6, 8, 13)  # --bg      #06080d
PANEL = (13, 18, 27)  # --panel   #0d121b
RULE = (26, 32, 48)  # --rule    #1a2030
INK = (230, 235, 242)  # --ink     #e6ebf2
BODY = (170, 180, 194)  # --body    #aab4c2
DIM = (106, 115, 136)  # --dim     #6a7388
ACCENT = (34, 211, 238)  # --accent  #22d3ee

W, H = 1200, 630
MARGIN = 88

SANS = "/System/Library/Fonts/SFNS.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "og-default.png"


def font(path: str, size: int, weight: str | None = None) -> ImageFont.FreeTypeFont:
    """Loads a font, selecting a named variation when the face is variable."""
    f = ImageFont.truetype(path, size)
    if weight:
        try:
            f.set_variation_by_name(weight)
        except (OSError, AttributeError):
            pass  # static face, or FreeType without variable-font support
    return f


def brand_mark(d: ImageDraw.ImageDraw, x: int, y: int, s: int) -> None:
    """The nested-squares mark from the header SVG in _layouts/default.html."""
    d.rectangle([x, y, x + s, y + s], outline=(14, 116, 144), width=2)
    inset = s * 4 // 22
    d.rectangle(
        [x + inset, y + inset, x + s - inset, y + s - inset], outline=ACCENT, width=2
    )
    c, r = x + s / 2, s / 11
    d.ellipse([c - r, y + s / 2 - r, c + r, y + s / 2 + r], fill=ACCENT)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Panel band behind the content, and a hairline grid echoing the site shell.
    d.rectangle([0, 0, W, H], fill=BG)
    d.rectangle([MARGIN - 32, 0, W, H], fill=PANEL)
    for gx in range(MARGIN - 32, W, 120):
        d.line([(gx, 0), (gx, H)], fill=RULE, width=1)
    d.line([(0, H - 96), (W, H - 96)], fill=RULE, width=1)

    # Accent rail on the left edge — the "signal" motif.
    d.rectangle([0, 0, 5, H], fill=ACCENT)

    brand_mark(d, MARGIN, 92, 44)
    d.text((MARGIN + 64, 100), "ajdevhub", font=font(SANS, 30, "Bold"), fill=INK)

    d.text(
        (MARGIN, 214),
        "// SOFTWARE ENGINEER · DATA PLANE",
        font=font(MONO, 22),
        fill=DIM,
    )

    d.text((MARGIN, 262), "Ajay Kumar Gupt", font=font(SANS, 76, "Bold"), fill=INK)

    d.text(
        (MARGIN, 372),
        "Notes, projects and roadmaps across networking,",
        font=font(SANS, 32),
        fill=BODY,
    )
    d.text(
        (MARGIN, 416),
        "systems, compilers and AI. A notebook in public.",
        font=font(SANS, 32),
        fill=BODY,
    )

    d.text((MARGIN, H - 66), "ajay3007.github.io", font=font(MONO, 24), fill=ACCENT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT.relative_to(Path.cwd())} ({OUT.stat().st_size:,} bytes, {W}x{H})")


if __name__ == "__main__":
    main()
