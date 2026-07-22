"""
AxioByte Systems -- Ep 01 cover.  1080 x 1920.

    manim -sqh cover_ep01_9x16.py CoverEp01        # the cover image
    manim -qh --fps 60 cover_ep01_9x16.py CoverEp01Intro   # 2.6 s build, then holds

House style: flat background, thin frame, one hero visual, generous air.
Same shape as cover12_9x16.py / cover_sys01_9x16.py -- brand, pill, title, rule
pair, subtitle, the one picture, the payoff, rule pair, handle.

THE ONE PICTURE
    Two bars, ONE scale (0.00205 units per cycle, applied to both). The mint bar
    is the entire per-packet budget at 100 GbE -- 148.8 Mpps on a 3 GHz core is
    ~20 cycles -- and the red-amber stack next to it is what the kernel path
    actually spends. The budget is a hairline because it IS a hairline; that is
    the episode in one frame, and 110x is the number worth putting on a thumbnail.

The four segments and the palette are lifted from ep01_video.py, so the cover and
the film are the same drawing: red IRQ, amber stack, violet copy, red switch.
"""

from manim import *


def _font(*names):
    try:
        import manimpango
        have = set(manimpango.list_fonts())
    except Exception:
        have = set()
    return next((n for n in names if n in have), names[-1])


BG = "#090C13"; SURFACE = "#141B27"; BORDER = "#26344A"
WHITE = "#EAF0F6"; GRAY = "#65728A"
CYAN = "#34D8E8"; AMBER = "#F0A431"; MINT = "#4DE6A0"; VIOLET = "#B79CF0"; RED = "#FF5C55"
CYAN_BG = "#10303A"; AMBER_BG = "#33240F"; RED_BG = "#331617"; MINT_BG = "#0F2A20"

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_height = 14.0
config.frame_width = 7.875
config.background_color = BG
FN = _font("DejaVu Sans", "Helvetica Neue", "Helvetica")
MN = _font("DejaVu Sans Mono", "Menlo", "Andale Mono")

# --- the numbers, from the film -------------------------------------------
SPEND = [("IRQ", 500, RED), ("stack", 700, AMBER),
         ("copy", 400, VIOLET), ("switch", 600, RED)]
TOTAL = sum(c for _, c, _ in SPEND)          # 2200
BUDGET = 20                                  # 148.8 Mpps on one 3.0 GHz core
BAR_TOP, BAR_BOT, BAR_W = 1.9, -2.6, 1.55
CYC = (BAR_TOP - BAR_BOT) / TOTAL            # one scale, both bars


def pill(text, tc, bg, s=0.34, h=0.60):
    t = Text(text, font=MN, weight=BOLD, color=tc).scale(s)
    box = RoundedRectangle(width=t.width + 0.5, height=h, corner_radius=h / 2,
                           stroke_color=tc, stroke_width=2.5, fill_color=bg, fill_opacity=1.0)
    return VGroup(box, t.move_to(box.get_center()))


def rules(y, w=1.45, sw=4):
    return VGroup(Line(LEFT * w, ORIGIN, color=CYAN, stroke_width=sw).move_to(UP * y + LEFT * w / 2),
                  Line(ORIGIN, RIGHT * w, color=AMBER, stroke_width=sw).move_to(UP * y + RIGHT * w / 2))


def build():
    """Every part of the cover, named. The still adds them all; the intro plays
    them in six beats and lands on exactly the same frame."""
    p = {}
    p["frame"] = RoundedRectangle(width=7.35, height=13.6, corner_radius=0.4,
                                  stroke_color=BORDER, stroke_width=2.0, fill_opacity=0)
    p["brand"] = VGroup(Text("Axio", font=FN, weight=BOLD, color=CYAN).scale(0.6),
                        Text("Byte", font=FN, weight=BOLD, color=AMBER).scale(0.6)) \
        .arrange(RIGHT, buff=0.03).move_to(UP * 6.05)
    p["pill"] = pill("High-Performance Data Plane  ·  Ep 01", CYAN, SURFACE, s=0.32) \
        .move_to(UP * 5.15)

    title = VGroup(Text("Why the kernel is", font=FN, weight=BOLD, color=WHITE),
                   Text("slow for packets", font=FN, weight=BOLD, color=WHITE)) \
        .arrange(DOWN, buff=0.18)
    title.scale_to_fit_width(6.1).move_to(UP * 3.85)
    p["title"] = title
    p["rules_top"] = rules(2.65)

    sub = Text("100 GbE  ·  64-byte frames  ·  one 3 GHz core", font=MN, color=GRAY).scale(0.32)
    if sub.width > 6.4:
        sub.scale_to_fit_width(6.4)
    p["sub"] = sub.move_to(UP * 2.2)

    # ---- the hero: what one packet costs, against what one packet is worth ----
    bar, labels, y = VGroup(), VGroup(), BAR_TOP
    for name, cyc, col in SPEND:
        h = cyc * CYC
        cy = y - h / 2
        seg = Rectangle(width=BAR_W, height=h, stroke_color=BG, stroke_width=1.5,
                        fill_color=col, fill_opacity=0.95).move_to([1.05, cy, 0])
        bar.add(VGroup(seg, Text(str(cyc), font=MN, weight=BOLD, color=BG)
                       .scale(0.36).move_to(seg.get_center())).set_z_index(len(bar)))
        labels.add(Text(name, font=MN, weight=BOLD, color=col).scale(0.32)
                   .move_to([2.02, cy, 0], aligned_edge=LEFT))
        y -= h
    p["bar"], p["bar_labels"] = bar, labels
    p["spend_total"] = Text(f"≈ {TOTAL:,} cycles".replace(",", " "), font=MN, weight=BOLD,
                            color=RED).scale(0.36).move_to([1.05, BAR_BOT - 0.42, 0])

    bh = BUDGET * CYC                                   # ~0.04 units. Yes, that small.
    bud = Rectangle(width=BAR_W, height=bh, stroke_width=0, fill_color=MINT,
                    fill_opacity=1.0).move_to([-1.92, BAR_BOT + bh / 2, 0])
    halo = VGroup(*[Rectangle(width=BAR_W + 0.10, height=bh * k, stroke_width=0,
                              fill_color=MINT, fill_opacity=op).move_to(bud.get_center())
                    for k, op in ((7, 0.10), (3.5, 0.18))])
    p["budget"] = VGroup(halo, bud)
    p["budget_label"] = VGroup(
        Text("20 cycles", font=MN, weight=BOLD, color=MINT).scale(0.34),
        Text("the whole budget", font=MN, color=GRAY).scale(0.30),
    ).arrange(DOWN, buff=0.10).move_to([-1.92, BAR_BOT - 0.55, 0])

    p["ratio"] = VGroup(
        Text("110×", font=FN, weight=BOLD, color=RED).scale(1.7),
        Text("over budget", font=MN, weight=BOLD, color=RED).scale(0.36),
    ).arrange(DOWN, buff=0.18).move_to([-1.92, -0.15, 0])

    # ---- the payoff ------------------------------------------------------
    row = VGroup(pill("kernel  0.5 Mpps", RED, RED_BG, s=0.32),
                 Text("→", font=FN, weight=BOLD, color=WHITE).scale(0.6),
                 pill("DPDK  15–30 Mpps", MINT, MINT_BG, s=0.32)) \
        .arrange(RIGHT, buff=0.24)
    if row.width > 6.9:
        row.scale_to_fit_width(6.9)
    p["payoff"] = row.move_to(UP * -4.15)
    p["caption"] = Text("no interrupts  ·  no copies  ·  no syscalls", font=MN, color=GRAY) \
        .scale(0.32).move_to(UP * -4.95)

    p["rules_bot"] = rules(-5.7, w=1.3, sw=3)
    p["handle"] = Text("@axiobyte.systems   ·   from first principles", font=MN, color=GRAY) \
        .scale(0.32).move_to(UP * -6.25)
    return p


class CoverEp01(Scene):
    def construct(self):
        p = build()
        self.add(*p.values())
        self.wait(0.3)


class CoverEp01Intro(Scene):
    """The same cover, drawn in 2.6 s and held. Nothing ever leaves, so the last
    frame IS the cover -- verified pixel-identical to CoverEp01, which is why the
    bands carry explicit z-indices: without them the seam strokes land in
    whichever order the bands happened to be added."""

    def construct(self):
        p = build()
        self.add(p["frame"])
        self.play(FadeIn(p["brand"], shift=DOWN * 0.15), FadeIn(p["pill"], scale=1.06),
                  run_time=0.35)
        self.play(FadeIn(p["title"], shift=UP * 0.12), Create(p["rules_top"]),
                  FadeIn(p["sub"]), run_time=0.45)

        # the budget lands first, so the stack has something to be measured against
        self.play(FadeIn(p["budget"], scale=1.4), FadeIn(p["budget_label"]), run_time=0.30)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in p["bar"][::-1]],
                              lag_ratio=0.18),
                  LaggedStart(*[FadeIn(l, shift=RIGHT * 0.12) for l in p["bar_labels"][::-1]],
                              lag_ratio=0.18),
                  run_time=0.75)
        self.play(FadeIn(p["spend_total"]), FadeIn(p["ratio"], scale=1.12), run_time=0.35)
        self.play(FadeIn(p["payoff"], shift=UP * 0.10), FadeIn(p["caption"]),
                  Create(p["rules_bot"]), FadeIn(p["handle"]), run_time=0.40)
        self.wait(2.0)
