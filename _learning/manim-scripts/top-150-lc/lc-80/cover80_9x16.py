from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED="#F2544D"; RED_BG="#331617"; MINT_BG="#0F2A20"
MED_T="#F0A431"; MED_B="#33240F"

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

class Cover80(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 80",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Remove Duplicates II",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.4).move_to(UP*3.95)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))

        note=Text("red = 3rd copy",font=MN,color=RED).scale(0.36).move_to(UP*2.25)
        self.add(note)
        cols=[(1,CYAN,CYAN_BG),(1,CYAN,CYAN_BG),(1,RED,RED_BG),(2,CYAN,CYAN_BG),(2,CYAN,CYAN_BG)]
        nums=VGroup(*[mcell(v,st,fl,WHITE,0.62) for v,st,fl in cols]).arrange(RIGHT,buff=0.12).move_to(UP*1.5)
        self.add(nums,Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.4).next_to(nums,LEFT,buff=0.28))

        self.add(Arrow(start=[0,0.32,0],end=[0,-0.32,0],buff=0,color=CYAN,stroke_width=6,max_tip_length_to_length_ratio=0.4).move_to(UP*0.5))

        hook=Text("at most twice  \u00b7  look two slots back",font=FN,color=CYAN).scale(0.48)
        if hook.width>6.5: hook.scale_to_fit_width(6.5)
        hook.move_to(UP*-0.25); self.add(hook)

        res=VGroup(mcell(1,MINT,MINT_BG,MINT,0.92),mcell(1,MINT,MINT_BG,MINT,0.92),mcell(2,MINT,MINT_BG,MINT,0.92),mcell(2,MINT,MINT_BG,MINT,0.92),
                   mempty(0.92)).arrange(RIGHT,buff=0.12).move_to(UP*-1.6)
        self.add(res)
        self.add(VGroup(pill("k = 4",MINT,SURFACE,MINT,s=0.4),Text("at most twice",font=MN,color=GRAY).scale(0.4)
                        ).arrange(RIGHT,buff=0.25).move_to(UP*-2.85))
        self.add(Text("O(n) time      \u00b7      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-3.8))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.15+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.15+RIGHT*0.7))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8))
        self.wait(0.3)
