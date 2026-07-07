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

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mcell(v,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover135(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 135",CYAN,SURFACE,CYAN),pill("Hard",HARD_T,HARD_B,HARD_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Candy",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(4.2).move_to(UP*3.95)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))

        sub=Text("higher rating than a neighbor → more candy",font=MN,color=GRAY).scale(0.32).move_to(UP*2.4)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        rats=[2,3,4,3,2,1]; cands=[1,2,4,3,2,1]; SZ=0.72
        rrow=VGroup(*[mcell(v,(AMBER if i==2 else BORDER),SURFACE,(AMBER if i==2 else WHITE),SZ) for i,v in enumerate(rats)])
        rrow.arrange(RIGHT,buff=0.15).move_to(UP*1.5)
        self.add(rrow,Text("ratings",font=MN,weight=BOLD,color=WHITE).scale(0.3).next_to(rrow,LEFT,buff=0.18))
        crow=VGroup(*[mcell(v,(AMBER if i==2 else MINT),(RED_BG if i==2 else MINT_BG),(AMBER if i==2 else MINT),SZ) for i,v in enumerate(cands)])
        crow.arrange(RIGHT,buff=0.15)
        crow.move_to([rrow.get_center()[0],0.5,0])
        self.add(crow,Text("candy",font=MN,weight=BOLD,color=MINT).scale(0.3).next_to(crow,LEFT,buff=0.18))
        # spotlight the peak override
        star=Text("max(3, 4) = 4",font=MN,weight=BOLD,color=AMBER).scale(0.34).next_to(crow[2],UP,buff=0.12)
        self.add(star)

        hook=Text("two passes  ·  L→R then R→L",font=FN,color=CYAN).scale(0.46)
        if hook.width>6.5: hook.scale_to_fit_width(6.5)
        hook.move_to(UP*-1.0); self.add(hook)

        box=RoundedRectangle(width=5.4,height=1.2,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.3)
        bval=Text("min candies = 13",font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(box.get_center())
        self.add(box,bval)
        self.add(Text("keep the larger of the two passes",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(n) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.35))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.25+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.25+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.85))
        self.wait(0.3)
