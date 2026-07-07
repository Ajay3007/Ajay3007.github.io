from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"
CYAN_BG="#10303A"; RED="#F2544D"; MINT_BG="#0F2A20"
GREEN_T="#4ECB71"; GREEN_B="#12301C"

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
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover169(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 169",CYAN,SURFACE,CYAN),pill("Easy",GREEN_T,GREEN_B,GREEN_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Majority Element",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.2).move_to(UP*3.95)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))

        note=Text("green = appears > n/2 times",font=MN,color=MINT).scale(0.34).move_to(UP*2.3)
        self.add(note)
        cols=[(2,MINT,MINT_BG),(2,MINT,MINT_BG),(1,GRAY,SURFACE),(1,GRAY,SURFACE),(2,MINT,MINT_BG)]
        nums=VGroup(*[mcell(v,st,fl,WHITE,0.66) for v,st,fl in cols]).arrange(RIGHT,buff=0.12).move_to(UP*1.55)
        self.add(nums,Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.4).next_to(nums,LEFT,buff=0.28))

        self.add(Arrow(start=[0,0.3,0],end=[0,-0.3,0],buff=0,color=CYAN,stroke_width=6,max_tip_length_to_length_ratio=0.4).move_to(UP*0.55))

        hook=Text("Boyer-Moore voting  \u00b7  cancel the pairs",font=FN,color=CYAN).scale(0.46)
        if hook.width>6.5: hook.scale_to_fit_width(6.5)
        hook.move_to(UP*-0.2); self.add(hook)

        box=RoundedRectangle(width=1.35,height=1.35,corner_radius=0.16,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-1.55)
        bval=Text("2",font=FN,weight=BOLD,color=MINT).scale(0.9).move_to(box.get_center())
        blab=Text("majority",font=MN,color=GRAY).scale(0.34).next_to(box,UP,buff=0.12)
        self.add(box,bval,blab)
        self.add(Text("appears 3 of 5",font=MN,color=GRAY).scale(0.36).next_to(box,DOWN,buff=0.22))

        self.add(Text("O(n) time      \u00b7      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-3.95))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.15+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.15+RIGHT*0.7))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8))
        self.wait(0.3)
