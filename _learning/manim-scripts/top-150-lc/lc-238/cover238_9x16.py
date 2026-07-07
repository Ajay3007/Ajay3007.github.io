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

def mcell(v,stroke,fill,tcolor,size=0.66):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.46*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover238(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 238",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.15))
        title=Text("Product of Array Except Self",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.7).move_to(UP*4.15)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.45+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.45+RIGHT*0.75))
        sub=Text("answer[i] = product of all except i",font=MN,color=GRAY).scale(0.38).move_to(UP*2.75)
        self.add(sub)

        nums=[1,2,3,4,5,6]; ans=[720,360,240,180,144,120]
        nrow=VGroup(*[mcell(v,BORDER,SURFACE,WHITE) for v in nums]).arrange(RIGHT,buff=0.13).move_to(UP*1.35+RIGHT*0.25)
        self.add(nrow,Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.36).next_to(nrow,LEFT,buff=0.22))
        # prefix arrow above
        pa=Arrow(nrow.get_left()+UP*0.62+LEFT*0.05,nrow.get_right()+UP*0.62+RIGHT*0.05,buff=0,color=CYAN,stroke_width=4,max_tip_length_to_length_ratio=0.06)
        self.add(pa,Text("prefix  \u2192",font=MN,weight=BOLD,color=CYAN).scale(0.34).next_to(pa,UP,buff=0.06))
        # suffix arrow below
        arow=VGroup(*[mcell(v,MINT,MINT_BG,MINT) for v in ans]).arrange(RIGHT,buff=0.13).move_to(DOWN*0.35+RIGHT*0.25)
        for i in range(6): arow[i].move_to([nrow[i].get_center()[0],-0.35,0])
        sa=Arrow(arow.get_right()+DOWN*0.62+RIGHT*0.05,arow.get_left()+DOWN*0.62+LEFT*0.05,buff=0,color=AMBER,stroke_width=4,max_tip_length_to_length_ratio=0.06)
        self.add(arow,Text("ans",font=MN,weight=BOLD,color=WHITE).scale(0.36).next_to(arow,LEFT,buff=0.22))
        self.add(sa,Text("\u2190  suffix",font=MN,weight=BOLD,color=AMBER).scale(0.34).next_to(sa,DOWN,buff=0.06))

        hook=Text("before  \u00d7  after",font=FN,weight=BOLD,color=CYAN).scale(0.6).move_to(UP*-2.55)
        self.add(hook)
        box=RoundedRectangle(width=6.0,height=1.1,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-3.8)
        bval=Text("O(n) time  \u00b7  O(1) space  \u00b7  no division",font=MN,weight=BOLD,color=MINT).scale(0.4).move_to(box.get_center())
        if bval.width>5.6: bval.scale_to_fit_width(5.6)
        self.add(box,bval)
        self.add(Text("two sweeps  \u2014  prefix, then suffix",font=MN,color=WHITE).scale(0.4).move_to(UP*-4.95))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-5.75))
        self.wait(0.3)
