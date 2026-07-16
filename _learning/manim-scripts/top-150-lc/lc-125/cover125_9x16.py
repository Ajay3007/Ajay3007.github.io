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

S="race a car"; STEP=0.72; SZ=0.66

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
    disp="·" if ch==" " else ch
    r=RoundedRectangle(width=size,height=size,corner_radius=0.11,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(disp,font=FN,weight=BOLD,color=(GRAY if ch==" " else tcolor)).scale(0.58*size).move_to(r.get_center()).set_z_index(3)
    g=VGroup(r,t)
    if glowc is not None: g.add_to_back(glow(r,glowc))
    return g

class Cover125(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 125",CYAN,SURFACE,CYAN),pill("Easy",EASY_T,EASY_B,EASY_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Valid Palindrome",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(5.6).move_to(UP*4.0)
        self.add(title)
        self.add(pill("Two Pointers",CYAN,SURFACE,CYAN,s=0.36,glowing=True).move_to(UP*3.25))

        sub=Text("one pointer each end · skip non-alnum · compare",font=MN,color=GRAY).scale(0.32).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        n=len(S); x0=-((n-1)*STEP)/2
        # matched prefix (0..2 and 7..9) mint-glow; mismatch e(3) vs a(5) red-glow
        matched={0,9,1,8,2,7}; mism={3,5}
        for c,ch in enumerate(S):
            if c in matched: st,fl,tc,gc=MINT,MINT_BG,MINT,MINT
            elif c in mism: st,fl,tc,gc=RED,RED_BG,RED,RED
            else: st,fl,tc,gc=BORDER,SURFACE,WHITE,None
            self.add(mcell(ch,st,fl,tc,SZ,glowc=gc).move_to([x0+c*STEP,1.45,0]))
        # pointers l/r stopped at mismatch
        self.add(Text("l",font=MN,weight=BOLD,color=CYAN).scale(0.4).move_to([x0+3*STEP,1.45+SZ/2+0.3,0]))
        self.add(Text("r",font=MN,weight=BOLD,color=AMBER).scale(0.4).move_to([x0+5*STEP,1.45-SZ/2-0.3,0]))

        eq=Text("'e'  ≠  'a'",font=MN,weight=BOLD,color=RED).scale(0.5).move_to(UP*0.1)
        self.add(eq)

        box=RoundedRectangle(width=5.4,height=1.2,corner_radius=0.18,stroke_color=RED,stroke_width=3.2,fill_color=RED_BG,fill_opacity=1.0).move_to(UP*-1.5)
        box.add_to_back(glow(box,RED,layers=6,spread=0.28,max_op=0.14))
        bval=Text('"race a car" → false',font=MN,weight=BOLD,color=RED).scale(0.5).move_to(UP*-1.5)
        if bval.width>5.0: bval.scale_to_fit_width(5.0)
        self.add(box,bval)
        self.add(Text('("...Panama" would be true)',font=MN,color=GRAY).scale(0.34).move_to(UP*-2.5))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.0))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-4.85+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-4.85+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.45))
        self.wait(0.3)
