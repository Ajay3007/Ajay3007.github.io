from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED="#F2544D"; RED_BG="#331617"; MINT_BG="#0F2A20"
GREEN_T="#4ECB71"; GREEN_B="#12301C"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,
                         stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mcell(v,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,
                       stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center())
    return VGroup(r,t)

def mempty(size):
    b=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=GRAY,stroke_width=2.2)
    d=DashedVMobject(b,num_dashes=14,dashed_ratio=0.55).set_stroke(GRAY,2.2)
    return VGroup(d)

class Cover27(Scene):
    def construct(self):
        frame=RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,
                               stroke_color=BORDER,stroke_width=2.0,fill_opacity=0)
        self.add(frame)

        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))

        self.add(VGroup(pill("# 27",CYAN,SURFACE,CYAN),pill("Easy",GREEN_T,GREEN_B,GREEN_T)
                        ).arrange(RIGHT,buff=0.28).move_to(UP*5.1))

        title=Text("Remove Element",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.4).move_to(UP*3.95)
        self.add(title)

        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))

        # input: val chip + nums row
        self.add(pill("val = 3",AMBER,SURFACE,AMBER,s=0.4).move_to(UP*2.2))
        nums=VGroup(mcell(3,RED,RED_BG,WHITE,0.66),mcell(2,CYAN,CYAN_BG,WHITE,0.66),
                    mcell(2,CYAN,CYAN_BG,WHITE,0.66),mcell(3,RED,RED_BG,WHITE,0.66)).arrange(RIGHT,buff=0.13).move_to(UP*1.45)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.42).next_to(nums,LEFT,buff=0.3)
        self.add(nums,nlab)

        arrow=Arrow(start=[0,0.32,0],end=[0,-0.32,0],buff=0,color=CYAN,stroke_width=6,
                    max_tip_length_to_length_ratio=0.4).move_to(UP*0.5)
        self.add(arrow)

        hook=Text("two pointers  \u00b7  overwrite in place",font=FN,color=CYAN).scale(0.48).move_to(UP*-0.25)
        self.add(hook)

        # result hero row
        res=VGroup(mcell(2,MINT,MINT_BG,MINT,1.0),mcell(2,MINT,MINT_BG,MINT,1.0),
                   mempty(1.0),mempty(1.0)).arrange(RIGHT,buff=0.13).move_to(UP*-1.55)
        self.add(res)

        self.add(VGroup(pill("k = 2",MINT,SURFACE,MINT,s=0.4),
                        Text("the answer",font=MN,color=GRAY).scale(0.4)
                        ).arrange(RIGHT,buff=0.25).move_to(UP*-2.8))

        self.add(Text("O(n) time      \u00b7      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-3.75))

        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.15+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.15+RIGHT*0.7))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8))

        self.wait(0.3)
