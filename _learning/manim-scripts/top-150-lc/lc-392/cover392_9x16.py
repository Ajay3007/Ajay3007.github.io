from manim import *

# ---- AxioByte v3 palette ----
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"
CYAN_BG="#10303A"; MINT_BG="#0F2A20"; RED_BG="#331617"
EASY_T="#4DE6A0"; EASY_B="#0F2A20"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

S="abc"; T="ahbgdc"; SZ=0.72; STEP=0.82
MATCH={0:0,1:2,2:5}   # s index -> t index

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

def mcell(ch,stroke,fill,tcolor,size,glowc=None):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.11,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(ch,font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center()).set_z_index(3)
    g=VGroup(r,t)
    if glowc is not None: g.add_to_back(glow(r,glowc))
    return g

class Cover392(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 392",CYAN,SURFACE,CYAN),pill("Easy",EASY_T,EASY_B,EASY_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Is Subsequence",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(5.4).move_to(UP*4.0)
        self.add(title)
        self.add(pill("Two Pointers",CYAN,SURFACE,CYAN,s=0.36,glowing=True).move_to(UP*3.25))

        sub=Text("scan t once · tick off s in order",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        # s row (all matched -> mint glow)
        sx0=-((len(S)-1)*STEP)/2
        srow_y=1.55
        for c,ch in enumerate(S):
            self.add(mcell(ch,MINT,MINT_BG,MINT,SZ,glowc=MINT).move_to([sx0+c*STEP,srow_y,0]))
        self.add(Text("s",font=MN,weight=BOLD,color=MINT).scale(0.4).move_to([sx0-0.62,srow_y,0]))
        # t row
        tx0=-((len(T)-1)*STEP)/2
        trow_y=0.35
        matched_t=set(MATCH.values())
        for c,ch in enumerate(T):
            if c in matched_t: st,fl,tc,gc=MINT,MINT_BG,MINT,MINT
            else: st,fl,tc,gc=BORDER,SURFACE,GRAY,None
            self.add(mcell(ch,st,fl,tc,SZ,glowc=gc).move_to([tx0+c*STEP,trow_y,0]))
        self.add(Text("t",font=MN,weight=BOLD,color=WHITE).scale(0.4).move_to([tx0-0.62,trow_y,0]))
        # connectors s -> t
        for si,ti in MATCH.items():
            self.add(Line([sx0+si*STEP,srow_y-SZ/2,0],[tx0+ti*STEP,trow_y+SZ/2,0],color=MINT,stroke_width=2.4).set_z_index(0))

        box=RoundedRectangle(width=5.6,height=1.2,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-1.7)
        box.add_to_back(glow(box,MINT,layers=6,spread=0.28,max_op=0.14))
        bval=Text('"abc" ⊆ "ahbgdc" → true',font=MN,weight=BOLD,color=MINT).scale(0.46).move_to(UP*-1.7)
        if bval.width>5.2: bval.scale_to_fit_width(5.2)
        self.add(box,bval)
        self.add(Text("found a, b, c in order",font=MN,color=GRAY).scale(0.34).move_to(UP*-2.7))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.1))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-4.9+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-4.9+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.5))
        self.wait(0.3)
