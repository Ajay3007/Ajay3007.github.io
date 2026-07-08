from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; RED_BG="#331617"; MINT_BG="#0F2A20"
EASY_T="#57E5B0"; EASY_B="#0F2A20"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WORDS=["flower","flow","flight"]; CW=0.66; CSTEP=0.78

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mcell(ch,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.1,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(ch,font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover14(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 14",CYAN,SURFACE,CYAN),pill("Easy",EASY_T,EASY_B,EASY_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Longest Common Prefix",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.4).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("stack them, scan down the columns",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        maxlen=max(len(w) for w in WORDS)
        x0=-((maxlen-1)*CSTEP)/2
        row_y0=1.4; row_step=0.82
        for r,w in enumerate(WORDS):
            for j,ch in enumerate(w):
                if j<2: st,fl,tc=MINT,MINT_BG,MINT           # matching prefix columns
                elif j==2: st,fl,tc=RED,RED_BG,RED           # first disagreeing column
                else: st,fl,tc=BORDER,SURFACE,WHITE
                self.add(mcell(ch,st,fl,tc,CW).move_to([x0+j*CSTEP,row_y0-r*row_step,0]))
        # column markers
        self.add(Text("✓",font=FN,weight=BOLD,color=MINT).scale(0.5).move_to([x0+0*CSTEP,row_y0+0.6,0]))
        self.add(Text("✓",font=FN,weight=BOLD,color=MINT).scale(0.5).move_to([x0+1*CSTEP,row_y0+0.6,0]))
        self.add(Text("✗",font=FN,weight=BOLD,color=RED).scale(0.5).move_to([x0+2*CSTEP,row_y0+0.6,0]))

        box=RoundedRectangle(width=5.0,height=1.25,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-1.85)
        bval=Text('prefix = "fl"',font=MN,weight=BOLD,color=MINT).scale(0.54).move_to(box.get_center())
        self.add(box,bval)
        self.add(Text("stop at the first column that disagrees",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(S) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-3.95))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-4.75+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-4.75+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.35))
        self.wait(0.3)
