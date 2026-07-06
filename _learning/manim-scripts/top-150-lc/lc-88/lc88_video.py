from manim import *

BG      = "#0B0E14"
SURFACE = "#151B26"
BORDER  = "#2A3542"
CYAN    = "#34D8E8"
AMBER   = "#F0A431"
WHITE   = "#E8ECF1"
GRAY    = "#5A6472"
MINT    = "#57E5B0"
RED     = "#F2544D"

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_height = 14.0
config.frame_width  = 7.875
config.background_color = BG

FN = "DejaVu Sans"
MN = "DejaVu Sans Mono"
CW = 0.92
BUF = 0.14

def cell_surface(value, stroke=BORDER, txt_color=WHITE):
    r = RoundedRectangle(width=CW, height=CW, corner_radius=0.13,
                         stroke_color=stroke, stroke_width=3.0,
                         fill_color=SURFACE, fill_opacity=1.0)
    r.set_z_index(1)
    t = Text(str(value), font=FN, weight=BOLD, color=txt_color).scale(0.62)
    t.move_to(r.get_center()).set_z_index(5)
    return VGroup(r, t)

def cell_empty():
    base = RoundedRectangle(width=CW, height=CW, corner_radius=0.13,
                            stroke_color=GRAY, stroke_width=2.4)
    d = DashedVMobject(base, num_dashes=18, dashed_ratio=0.55)
    d.set_stroke(GRAY, 2.4).set_z_index(1)
    return VGroup(d)

def idx_label(i):
    return Text(str(i), font=MN, color=GRAY).scale(0.34)

def pointer(label, color, up=True):
    tri = Triangle(color=color, fill_opacity=1.0, stroke_width=0).scale(0.13)
    if up:
        tri.rotate(PI)
    lab = Text(label, font=MN, weight=BOLD, color=color).scale(0.44)
    lab.next_to(tri, UP if up else DOWN, buff=0.06)
    g = VGroup(tri, lab)
    g.set_z_index(8)
    return g


class LC88(Scene):
    def construct(self):
        self.brand_and_title()
        self.setup_arrays()
        self.naive_fails()
        self.pivot_to_back()
        self.merge_loop()
        self.finish()

    def brand_and_title(self):
        axio = Text("Axio", font=FN, weight=BOLD, color=CYAN).scale(0.44)
        byte = Text("Byte", font=FN, weight=BOLD, color=AMBER).scale(0.44)
        wm = VGroup(axio, byte).arrange(RIGHT, buff=0.02).to_corner(UR, buff=0.32)
        self.wm = wm

        bbox = RoundedRectangle(width=1.2, height=0.56, corner_radius=0.28,
                                stroke_color=CYAN, stroke_width=2.5,
                                fill_color=SURFACE, fill_opacity=1.0)
        btxt = Text("# 88", font=MN, weight=BOLD, color=CYAN).scale(0.42).move_to(bbox.get_center())
        badge = VGroup(bbox, btxt).to_edge(UP, buff=0.55).shift(LEFT*2.4)

        title = Text("Merge Sorted Array", font=FN, weight=BOLD, color=WHITE).scale(0.66)
        title.next_to(badge, DOWN, buff=0.34).set_x(0)

        self.play(FadeIn(wm, shift=DOWN*0.2), run_time=0.5)
        self.play(FadeIn(badge, shift=RIGHT*0.3), Write(title), run_time=0.9)
        self.wait(0.3)
        self.badge, self.title = badge, title

    def setup_arrays(self):
        row1 = VGroup(*[cell_surface(v) for v in [1, 2, 3]],
                      *[cell_empty() for _ in range(3)]).arrange(RIGHT, buff=BUF)
        row1.move_to(UP*2.8)
        self.cells1 = list(row1)

        idxs1 = VGroup()
        for i, c in enumerate(row1):
            idxs1.add(idx_label(i).next_to(c, DOWN, buff=0.12))

        lab1 = Text("nums1", font=MN, weight=BOLD, color=WHITE).scale(0.5)
        lab1.next_to(row1, UP, buff=0.85).align_to(row1, LEFT)
        sub1 = Text("m = 3", font=MN, color=GRAY).scale(0.36)
        sub1.next_to(row1, UP, buff=0.9).align_to(row1, RIGHT)

        row2 = VGroup(*[cell_surface(v) for v in [2, 5, 6]]).arrange(RIGHT, buff=BUF)
        row2.move_to(UP*0.35).align_to(row1, LEFT)
        self.cells2 = list(row2)

        idxs2 = VGroup()
        for i, c in enumerate(row2):
            idxs2.add(idx_label(i).next_to(c, DOWN, buff=0.12))

        lab2 = Text("nums2", font=MN, weight=BOLD, color=WHITE).scale(0.5)
        lab2.next_to(row2, UP, buff=0.3).align_to(row2, LEFT)
        sub2 = Text("n = 3", font=MN, color=GRAY).scale(0.36)
        sub2.next_to(row2, UP, buff=0.32).align_to(row2, RIGHT)

        self.row1, self.row2 = row1, row2

        self.play(FadeIn(lab1), FadeIn(sub1),
                  LaggedStart(*[FadeIn(c, shift=UP*0.15) for c in row1], lag_ratio=0.08),
                  run_time=1.1)
        self.play(FadeIn(idxs1), run_time=0.3)
        self.play(FadeIn(lab2), FadeIn(sub2),
                  LaggedStart(*[FadeIn(c, shift=UP*0.15) for c in row2], lag_ratio=0.08),
                  run_time=0.9)
        self.play(FadeIn(idxs2), run_time=0.3)

        self.caption = Text("Merge nums2 into nums1, in place", font=FN, color=WHITE).scale(0.5)
        self.caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(self.caption, shift=UP*0.2), run_time=0.6)
        self.wait(0.7)

    def set_caption(self, txt, color=WHITE, scale=0.5, rt=0.55):
        new = Text(txt, font=FN, color=color).scale(scale).to_edge(DOWN, buff=0.6)
        self.play(FadeOut(self.caption, shift=DOWN*0.12),
                  FadeIn(new, shift=UP*0.12), run_time=rt)
        self.caption = new

    def naive_fails(self):
        self.set_caption("Naive: fill from the front", color=CYAN)
        wf = pointer("write", AMBER, up=True).next_to(self.cells1[0], UP, buff=0.12)
        self.play(FadeIn(wf, shift=DOWN*0.2), run_time=0.45)

        ghost = self.cells2[0][1].copy().set_z_index(9)
        self.play(Indicate(self.cells2[0][0], color=AMBER, scale_factor=1.12), run_time=0.4)
        self.play(ghost.animate.move_to(self.cells1[0].get_center()).set_color(AMBER), run_time=0.7)

        xmark = Text("\u2715", font=FN, weight=BOLD, color=RED).scale(0.85)
        xmark.move_to(self.cells1[0].get_center()).set_z_index(11)
        self.play(self.cells1[0][0].animate.set_stroke(RED, 4),
                  FadeIn(xmark),
                  Flash(self.cells1[0].get_center(), color=RED, line_length=0.18, num_lines=12),
                  run_time=0.6)
        self.set_caption("clobbers the unread 1", color=RED)
        self.wait(0.8)

        self.play(FadeOut(ghost), FadeOut(xmark), FadeOut(wf),
                  self.cells1[0][0].animate.set_stroke(BORDER, 3),
                  run_time=0.5)

    def pivot_to_back(self):
        self.set_caption("So fill from the back", color=MINT)

        raw = [
            (0, "i = m-1,  j = n-1"),
            (0, "k = m+n-1"),
            (0, "while (j >= 0 && i >= 0)"),
            (1, "if (nums1[i] \u2264 nums2[j])"),
            (2, "nums1[k--] = nums2[j--]"),
            (1, "else"),
            (2, "nums1[k--] = nums1[i--]"),
        ]
        code = VGroup()
        for _, s in raw:
            code.add(Text(s, font=MN, color="#9AA6B4").scale(0.40))
        code.arrange(DOWN, aligned_edge=LEFT, buff=0.17)
        for line, (ind, _) in zip(code, raw):
            line.shift(RIGHT * ind * 0.34)
        panel = RoundedRectangle(corner_radius=0.14, stroke_color=BORDER, stroke_width=2.5,
                                 fill_color="#0F1420", fill_opacity=1.0,
                                 width=code.width + 0.7, height=code.height + 0.5)
        panel.move_to(DOWN*3.35)
        shift = panel.get_center() - code.get_center()
        code.shift(shift)
        for line, (ind, _) in zip(code, raw):
            pass
        self.code_lines = list(code)
        self.code_panel = panel

        self.play(FadeIn(panel), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT*0.1) for l in code], lag_ratio=0.06),
                  run_time=1.0)

        self.pi = pointer("i", CYAN, up=True).next_to(self.cells1[2], UP, buff=0.12)
        self.pk = pointer("k", AMBER, up=True).next_to(self.cells1[5], UP, buff=0.12)
        self.pj = pointer("j", CYAN, up=False).next_to(self.cells2[2], DOWN, buff=0.12)
        self.play(FadeIn(self.pi, shift=DOWN*0.2), FadeIn(self.pk, shift=DOWN*0.2),
                  FadeIn(self.pj, shift=UP*0.2), run_time=0.7)
        self.wait(0.4)
        self._active = []

    def hl(self, idxs):
        anims = [self.code_lines[i].animate.set_color("#9AA6B4") for i in self._active]
        anims += [self.code_lines[i].animate.set_color(CYAN) for i in idxs]
        self._active = idxs
        return anims

    def move_ptr(self, ptr, cell, up=True):
        return ptr.animate.next_to(cell, UP if up else DOWN, buff=0.12)

    def write_value(self, value, from_cell, k_index):
        dest = self.cells1[k_index]
        flyer = Text(str(value), font=FN, weight=BOLD, color=AMBER).scale(0.62)
        flyer.move_to(from_cell.get_center()).set_z_index(9)
        self.add(flyer)
        self.play(flyer.animate.move_to(dest.get_center()), run_time=0.55)
        new_rect = RoundedRectangle(width=CW, height=CW, corner_radius=0.13,
                                    stroke_color=AMBER, stroke_width=3.5,
                                    fill_color=SURFACE, fill_opacity=1.0).set_z_index(1)
        new_rect.move_to(dest.get_center())
        new_txt = Text(str(value), font=FN, weight=BOLD, color=AMBER).scale(0.62)
        new_txt.move_to(dest.get_center()).set_z_index(5)
        self.play(FadeOut(dest), FadeIn(new_rect), FadeOut(flyer, run_time=0.01), run_time=0.3)
        self.add(new_txt)
        self.cells1[k_index] = VGroup(new_rect, new_txt)

    def compare(self, i, j):
        self.play(self.cells1[i][0].animate.set_stroke(CYAN, 4.5),
                  self.cells2[j][0].animate.set_stroke(CYAN, 4.5), run_time=0.4)
        self.wait(0.12)

    def uncompare(self, i=None, j=None):
        a = []
        if i is not None and i >= 0:
            a.append(self.cells1[i][0].animate.set_stroke(BORDER, 3))
        if j is not None and j >= 0:
            a.append(self.cells2[j][0].animate.set_stroke(BORDER, 3))
        if a:
            self.play(*a, run_time=0.28)

    def merge_loop(self):
        i, j, k = 2, 2, 5

        self.set_caption("compare  nums1[i]  vs  nums2[j]", rt=0.5)
        self.play(*self.hl([2, 3]), run_time=0.4)
        self.compare(i, j)
        self.set_caption("6 > 3   \u2192   place 6", color=AMBER, rt=0.5)
        self.play(*self.hl([4]), run_time=0.3)
        self.uncompare(i, j)
        self.write_value(6, self.cells2[j], k)
        j, k = 1, 4
        self.play(self.move_ptr(self.pj, self.cells2[j], up=False),
                  self.move_ptr(self.pk, self.cells1[k], up=True), run_time=0.55)

        self.set_caption("5 > 3   \u2192   place 5", color=AMBER, rt=0.5)
        self.play(*self.hl([2, 3]), run_time=0.3)
        self.compare(i, j)
        self.play(*self.hl([4]), run_time=0.3)
        self.uncompare(i, j)
        self.write_value(5, self.cells2[j], k)
        j, k = 0, 3
        self.play(self.move_ptr(self.pj, self.cells2[j], up=False),
                  self.move_ptr(self.pk, self.cells1[k], up=True), run_time=0.55)

        self.set_caption("3 > 2   \u2192   place 3  (from nums1)", color=CYAN, rt=0.5)
        self.play(*self.hl([2, 3]), run_time=0.3)
        self.compare(i, j)
        self.play(*self.hl([5, 6]), run_time=0.3)
        self.uncompare(i, j)
        self.write_value(3, self.cells1[i], k)
        i, k = 1, 2
        self.play(self.move_ptr(self.pi, self.cells1[i], up=True),
                  self.move_ptr(self.pk, self.cells1[k], up=True), run_time=0.55)

        self.set_caption("2 = 2   \u2192   \u2264 picks nums2", color=AMBER, rt=0.5)
        self.play(*self.hl([2, 3]), run_time=0.3)
        self.compare(i, j)
        self.play(*self.hl([4]), run_time=0.3)
        self.uncompare(i, j)
        self.write_value(2, self.cells2[j], k)
        j, k = -1, 1
        self.play(self.move_ptr(self.pk, self.cells1[k], up=True),
                  FadeOut(self.pj, shift=DOWN*0.2), *self.hl([2]), run_time=0.55)

    def finish(self):
        self.set_caption("j < 0  \u2192  loop ends.  1, 2 already in place", color=MINT, rt=0.6)
        self.play(Indicate(self.cells1[0][0], color=CYAN, scale_factor=1.1),
                  Indicate(self.cells1[1][0], color=CYAN, scale_factor=1.1), run_time=0.7)
        self.play(FadeOut(self.pi), FadeOut(self.pk), *self.hl([]), run_time=0.4)

        sweep = []
        for c in self.cells1:
            sweep.append(c[0].animate.set_stroke(MINT, 3.5))
            sweep.append(c[1].animate.set_color(MINT))
        self.play(LaggedStart(*sweep, lag_ratio=0.06), run_time=1.0)

        self.set_caption("sorted, in place", color=MINT, rt=0.5)

        comp = VGroup(
            Text("Time  O(m + n)", font=MN, weight=BOLD, color=CYAN).scale(0.5),
            Text("Space  O(1)", font=MN, weight=BOLD, color=AMBER).scale(0.5),
        ).arrange(RIGHT, buff=0.55)
        cbox = RoundedRectangle(corner_radius=0.16, stroke_color=BORDER, stroke_width=2.5,
                                fill_color="#0F1420", fill_opacity=1.0,
                                width=comp.width+0.7, height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge = VGroup(cbox, comp).move_to(self.code_panel.get_center())
        self.play(FadeOut(self.code_panel), FadeOut(VGroup(*self.code_lines)),
                  FadeIn(badge, shift=UP*0.2), run_time=0.7)
        self.wait(1.1)
        self.play(Indicate(self.wm, color=CYAN, scale_factor=1.15), run_time=0.8)
        self.wait(0.6)
