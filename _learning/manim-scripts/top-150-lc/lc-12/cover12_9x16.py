from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"
MED_T="#F0A431"; MED_B="#33240F"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mcell(v,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.1,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover12(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 12",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Integer to Roman",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.0).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("greedy — take the biggest coin that fits",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        num=Text("2024",font=MN,weight=BOLD,color=WHITE).scale(0.9).move_to(UP*1.5)
        self.add(num)
        self.add(Text("↓",font=FN,weight=BOLD,color=AMBER).scale(0.7).move_to(UP*0.55))

        res="MMXXIV"; two={4,5}   # the IV pair at the end
        row=VGroup()
        for i,ch in enumerate(res):
            if i in two: row.add(mcell(ch,AMBER,AMBER_BG,AMBER,0.74))
            else: row.add(mcell(ch,MINT,MINT_BG,MINT,0.74))
        row.arrange(RIGHT,buff=0.14).move_to(UP*-0.4)
        self.add(row)

        steps=Text("+M +M   +X +X   +IV",font=MN,color=GRAY).scale(0.36).move_to(UP*-1.4)
        self.add(steps)

        box=RoundedRectangle(width=5.4,height=1.25,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.7)
        bval=Text("2024 = MMXXIV",font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(box.get_center())
        if bval.width>5.0: bval.scale_to_fit_width(5.0)
        self.add(box,bval)
        self.add(Text("13 fixed values, biggest first",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(1) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.6))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.4+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.4+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-6.0))
        self.wait(0.3)
