from manim import *

# ---- AxioByte v3 palette ----
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"
CYAN_BG="#10303A"; MINT_BG="#0F2A20"
WATER="#4AA8FF"; WATER_BG="#12314F"; TERR="#3A4657"
MED_T="#F0A431"; MED_B="#33240F"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

H=[1,8,6,2,5,4,8,3,7]; N=len(H); BL,BR=1,8
BW=0.56; STEPX=0.62; UH=0.34; BASE_Y=0.4

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

def cx(i):
    x0=-((N-1)*STEPX)/2
    return x0+i*STEPX

class Cover11(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 11",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Container With Most Water",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.6).move_to(UP*4.0)
        self.add(title)
        self.add(pill("Two Pointers",CYAN,SURFACE,CYAN,s=0.36,glowing=True).move_to(UP*3.25))

        sub=Text("area = min(left, right) × width",font=MN,color=GRAY).scale(0.36).move_to(UP*2.4)
        self.add(sub)

        ground=Line([cx(0)-BW/2-0.15,BASE_Y,0],[cx(N-1)+BW/2+0.15,BASE_Y,0],color=GRAY,stroke_width=3)
        self.add(ground)
        # water for the winning pair
        xL=cx(BL); xR=cx(BR); lvl=min(H[BL],H[BR]); y1=BASE_Y+lvl*UH
        w=Rectangle(width=xR-xL,height=y1-BASE_Y,fill_color=WATER,fill_opacity=0.42,stroke_color=WATER,stroke_width=1.4).move_to([(xL+xR)/2,(BASE_Y+y1)/2,0]).set_z_index(1)
        self.add(glow(w,WATER,layers=6,spread=0.1,max_op=0.12),w)
        for i in range(N):
            col=MINT if i in (BL,BR) else BORDER
            b=Rectangle(width=BW,height=H[i]*UH,fill_color=TERR,fill_opacity=1.0,stroke_color=col,stroke_width=(3.4 if i in (BL,BR) else 2.0)).move_to([cx(i),BASE_Y+H[i]*UH/2,0]).set_z_index(3)
            if i in (BL,BR): self.add(glow(b,MINT,layers=4,spread=0.12,max_op=0.1))
            self.add(b)
            self.add(Text(str(H[i]),font=MN,color=GRAY).scale(0.28).move_to([cx(i),BASE_Y+H[i]*UH+0.2,0]))

        box=RoundedRectangle(width=5.2,height=1.2,corner_radius=0.18,stroke_color=WATER,stroke_width=3.2,fill_color=WATER_BG,fill_opacity=1.0).move_to(UP*-3.0)
        box.add_to_back(glow(box,WATER,layers=6,spread=0.26,max_op=0.14))
        bval=Text("max area = 49",font=MN,weight=BOLD,color=WATER).scale(0.54).move_to(UP*-3.0)
        self.add(box,bval)
        self.add(Text("min(8,7) × 7  ·  lines 1 and 8",font=MN,color=GRAY).scale(0.34).move_to(UP*-3.95))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.85))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.55+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.55+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-6.05))
        self.wait(0.3)
