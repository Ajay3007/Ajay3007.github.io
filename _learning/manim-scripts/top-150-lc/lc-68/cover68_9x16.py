from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; RED_BG="#331617"; MINT_BG="#0F2A20"
HARD_T="#F2544D"; HARD_B="#331617"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

LINES=["This    is    an","example  of text","justification   "]; BOXW=6.4

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def linebox(s,color,edge):
    box=RoundedRectangle(width=BOXW,height=0.62,corner_radius=0.08,stroke_color=edge,stroke_width=2.6,fill_color="#0F1420",fill_opacity=1.0)
    t=Text(s,font=MN,weight=BOLD,color=color).scale(0.48)
    if t.width>BOXW-0.2: t.scale_to_fit_width(BOXW-0.2)
    t.move_to(box.get_center()); return VGroup(box,t)

class Cover68(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 68",CYAN,SURFACE,CYAN),pill("Hard",HARD_T,HARD_B,HARD_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Text Justification",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.0).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("pack · spread spaces · pad the last line",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        self.add(Text("maxWidth = 16",font=MN,weight=BOLD,color=AMBER).scale(0.42).move_to(UP*1.55))
        boxes=VGroup(*[linebox(s,MINT,MINT) for s in LINES]).arrange(DOWN,buff=0.16).move_to(UP*0.2)
        self.add(boxes)
        # side guides showing flush edges
        self.add(Line(boxes.get_corner(UL)+LEFT*0.12+UP*0.05,boxes.get_corner(DL)+LEFT*0.12+DOWN*0.05,color=CYAN,stroke_width=3))
        self.add(Line(boxes.get_corner(UR)+RIGHT*0.12+UP*0.05,boxes.get_corner(DR)+RIGHT*0.12+DOWN*0.05,color=AMBER,stroke_width=3))

        box=RoundedRectangle(width=5.8,height=1.15,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.1)
        bval=Text("every line = exactly 16",font=MN,weight=BOLD,color=MINT).scale(0.46).move_to(box.get_center())
        if bval.width>5.4: bval.scale_to_fit_width(5.4)
        self.add(box,bval)
        self.add(Text("left gaps take the extra spaces",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.22))

        self.add(Text("O(N) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.2))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.0+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.0+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.6))
        self.wait(0.3)
