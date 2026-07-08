from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"
EASY_T="#57E5B0"; EASY_B="#0F2A20"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

VAL={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
S="MCMXCIV"; SUB={1,3,5}   # indices that are subtracted

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mcell(v,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.62*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover13(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 13",CYAN,SURFACE,CYAN),pill("Easy",EASY_T,EASY_B,EASY_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Roman to Integer",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.0).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("add each symbol — unless a smaller one comes first",font=MN,color=GRAY).scale(0.32).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        SZ=0.78
        row=VGroup()
        for i,ch in enumerate(S):
            if i in SUB: row.add(mcell(ch,AMBER,AMBER_BG,AMBER,SZ))
            else: row.add(mcell(ch,MINT,MINT_BG,MINT,SZ))
        row.arrange(RIGHT,buff=0.13).move_to(UP*1.45)
        self.add(row)
        vals=VGroup(*[Text(("-" if i in SUB else "+")+str(VAL[S[i]]),font=MN,color=(AMBER if i in SUB else MINT)).scale(0.3).next_to(row[i],DOWN,buff=0.14) for i in range(len(S))])
        self.add(vals)

        leg=Text("I=1  V=5  X=10  L=50  C=100  D=500  M=1000",font=MN,color=GRAY).scale(0.32).move_to(UP*0.1)
        if leg.width>6.7: leg.scale_to_fit_width(6.7)
        self.add(leg)

        hook=Text("CM=900   XC=90   IV=4",font=MN,weight=BOLD,color=CYAN).scale(0.44).move_to(UP*-0.8)
        self.add(hook)

        box=RoundedRectangle(width=5.4,height=1.25,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.2)
        bval=Text("MCMXCIV = 1994",font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(box.get_center())
        if bval.width>5.0: bval.scale_to_fit_width(5.0)
        self.add(box,bval)
        self.add(Text("one pass, compare each to its neighbor",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.3))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.2+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.2+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8))
        self.wait(0.3)
