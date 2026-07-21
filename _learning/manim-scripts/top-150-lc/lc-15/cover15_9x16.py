from manim import *

# ---- AxioByte v3 palette ----
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"
CYAN_BG="#10303A"; MINT_BG="#0F2A20"; VIOLET_BG="#241B3A"
MED_T="#F0A431"; MED_B="#33240F"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

S=[-4,-1,-1,0,1,2]; N=len(S); SZ=0.78; STEP=0.94

def glow(shape,color=None,layers=6,spread=0.34,max_op=0.16):
    if color is None: color=shape.get_stroke_color()
    halo=VGroup()
    for i in range(layers):
        f=(i+1)/layers
        c=shape.copy().set_stroke(width=0).set_fill(color,opacity=max_op*(1-f)+0.015)
        c.scale(1+spread*f); halo.add(c)
    halo.set_z_index(shape.get_z_index()-1); return halo

def pill(text,tc,bg,st,s=0.42,h=0.62,glowing=False):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); g=VGroup(box,t)
    if glowing: g.add_to_back(glow(box,st,layers=5,spread=0.5,max_op=0.14))
    return g

def mcell(v,stroke,fill,tcolor,size,glowc=None):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.11,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.5*size).move_to(r.get_center()).set_z_index(3)
    g=VGroup(r,t)
    if glowc is not None: g.add_to_back(glow(r,glowc))
    return g

def cx(i):
    x0=-((N-1)*STEP)/2
    return x0+i*STEP

class Cover15(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 15",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("3Sum",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(3.4).move_to(UP*4.05)
        self.add(title)
        self.add(pill("Two Pointers",CYAN,SURFACE,CYAN,s=0.36,glowing=True).move_to(UP*3.25))

        sub=Text("sort · fix one · two-pointer the rest",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        # sorted array; highlight the {-1,0,1} triplet (i=1 fixed violet, l=3,r=4 mint)
        FIX,LP,RP=1,3,4
        row_y=1.5
        for i,v in enumerate(S):
            if i==FIX: st,fl,tc,gc=VIOLET,VIOLET_BG,VIOLET,VIOLET
            elif i in (LP,RP): st,fl,tc,gc=MINT,MINT_BG,MINT,MINT
            else: st,fl,tc,gc=BORDER,SURFACE,WHITE,None
            self.add(mcell(v,st,fl,tc,SZ,glowc=gc).move_to([cx(i),row_y,0]))
        self.add(Text("sorted",font=MN,weight=BOLD,color=GRAY).scale(0.3).move_to([cx(0)-0.7,row_y+SZ/2+0.3,0]))
        self.add(Text("i",font=MN,weight=BOLD,color=VIOLET).scale(0.4).move_to([cx(FIX),row_y+SZ/2+0.32,0]))
        self.add(Text("l",font=MN,weight=BOLD,color=MINT).scale(0.4).move_to([cx(LP),row_y-SZ/2-0.32,0]))
        self.add(Text("r",font=MN,weight=BOLD,color=MINT).scale(0.4).move_to([cx(RP),row_y-SZ/2-0.32,0]))

        self.add(Text("-1 + 0 + 1 = 0",font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(UP*-0.05))

        box=RoundedRectangle(width=6.0,height=1.4,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-1.85)
        box.add_to_back(glow(box,MINT,layers=6,spread=0.24,max_op=0.13))
        inner=VGroup(pill("{-1,-1,2}",MINT,SURF2,MINT,s=0.4,h=0.56),pill("{-1,0,1}",MINT,SURF2,MINT,s=0.4,h=0.56)).arrange(RIGHT,buff=0.3).move_to(UP*-1.85)
        self.add(box,inner)
        self.add(Text("skip duplicates → unique triplets",font=MN,color=GRAY).scale(0.34).move_to(UP*-2.95))

        self.add(Text("O(n²) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.2))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.0+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.0+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.6))
        self.wait(0.3)
