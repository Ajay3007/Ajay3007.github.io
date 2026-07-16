# AxioByte — Visual Theme v3

Goal: match the polish level of the algomaster.io reference clips (`assets/videos/`)
while staying a **distinct AxioByte identity** (our cyan+amber brand, not a clone).
Applies to **new episodes from #125 (Valid Palindrome) onward**. Episodes 1–24 stay on v2.

Preview / approve the look by rendering:
```
manim -s -qh axiobyte_theme_v3.py ThemeV3
```

## What changed from v2

1. **Neon glow** — a soft colored halo behind cells, pointers, result blocks, icons,
   and highlighted items. Implemented with `glow(shape, color)`: stacks a few larger,
   semi-transparent fill copies behind the shape (no real blur needed in manim).
   Use glow on *accented* elements (current cell, pointer, answer), not everything —
   restraint keeps it readable.
2. **Code panel** now has:
   - a **line-number gutter** (gray, left of the code),
   - the syntax highlighting from v2 (keywords/types cyan, numbers amber, operators
     rose `#F78CA0`, strings mint, comments gray, default `#C7D0DA`),
   - the active-line **translucent bar** PLUS a **bright cyan left-edge accent** (glowing),
     matching the Tower of Hanoi reference panel.
3. **Punchier palette** — same brand hues, slightly more saturated accents:
   `MINT #4DE6A0` (was `#57E5B0`), deeper `BG #090C13`, added `VIOLET #B79CF0`
   for a second keyword/identifier accent. Brand `CYAN #34D8E8` / `AMBER #F0A431` kept.
4. **Stylized icons** (glowing) for sections that need them — list node (rounded box +
   port + arrow), DB cylinder (ellipse-capped body), tree node (circle). Cell-based
   episodes (arrays/strings/two-pointers) mostly don't need icons.

## Helper API (copy verbatim into each new lc<num>_video.py — still no shared import)

- `glow(shape, color=None, layers=6, spread=0.34, max_op=0.16)` → VGroup halo (add behind).
- `cell(v, size, stroke, fill, tcolor, glowc=None)` — glow only when `glowc` is set.
- `pointer(label, color, up=True, glowing=True)`.
- `pill(text, tc, bg, st, ..., glowing=False)`.
- `colorize(s, scale)` — syntax-highlighted mono `Text` (unchanged from v2).
- Code panel: build lines with `colorize`, add a gutter of gray numbers, a full-width
  translucent bar at the active line, and a thin glowing accent bar at the panel's left
  edge at that line's y. (See `ThemeV3.construct` for the reference implementation.)

## Guardrails

- Keep glow subtle (`max_op ≤ ~0.2`); it should feel like light, not fog.
- Don't glow every cell — only the ones the eye should follow.
- Icons are accents, not the star; the algorithm visualization stays primary.
- Watch render time: glow multiplies mobjects (~6× per glowed shape). Fine for stills
  and short scenes; avoid glowing 30+ elements at once.
