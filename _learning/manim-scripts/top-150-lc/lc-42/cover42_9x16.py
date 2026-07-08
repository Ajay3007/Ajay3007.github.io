from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; RED_BG="#331617"; MINT_BG="#0F2A20"
WATER="#4AA8FF"; WATER_BG="#12314F"; TERR="#3A4657"
HARD_T="#F2544D"; HARD_B="#331617"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

BASE_Y=-0.2; UH=0.62; BW=0.82; GAP=0.05
H=[2,1,0,3,0,1,2]; N=len(H)

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def col_x(i):
    W=N*BW+(N-1)*GAP
    return -W/2+BW/2+i*(BW+GAP)

class Cover42(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 42",CYAN,SURFACE,CYAN),pill("Hard",HARD_T,HARD_B,HARD_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Trapping Rain Water",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.2).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.25+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.25+RIGHT*0.75))

        sub=Text("how much water settles between the walls?",font=MN,color=GRAY).scale(0.34).move_to(UP*2.5)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        # trapped levels
        Lm=[0]*N; Rm=[0]*N; m=0
        for i in range(N): m=max(m,H[i]); Lm[i]=m
        m=0
        for i in range(N-1,-1,-1): m=max(m,H[i]); Rm[i]=m
        lvl=[min(Lm[i],Rm[i]) for i in range(N)]

        ground=Line([col_x(0)-BW/2-0.15,BASE_Y,0],[col_x(N-1)+BW/2+0.15,BASE_Y,0],color=GRAY,stroke_width=3)
        self.add(ground)
        for i in range(N):
            if H[i]>0:
                b=Rectangle(width=BW,height=H[i]*UH,fill_color=TERR,fill_opacity=1.0,stroke_color=BORDER,stroke_width=2.2)
                b.move_to([col_x(i),BASE_Y+H[i]*UH/2,0]); b.set_z_index(3); self.add(b)
            if lvl[i]>H[i]:
                w=Rectangle(width=BW,height=(lvl[i]-H[i])*UH,fill_color=WATER,fill_opacity=0.5,stroke_color=WATER,stroke_width=1.2)
                w.move_to([col_x(i),BASE_Y+(H[i]+lvl[i])/2*UH,0]); w.set_z_index(2); self.add(w)
            self.add(Text(str(i),font=MN,color=GRAY).scale(0.3).move_to([col_x(i),BASE_Y-0.35,0]))

        hook=Text("min(leftMax, rightMax) - height",font=MN,color=WATER).scale(0.42).move_to(UP*-2.4)
        if hook.width>6.5: hook.scale_to_fit_width(6.5)
        self.add(hook)

        box=RoundedRectangle(width=5.2,height=1.2,corner_radius=0.18,stroke_color=WATER,stroke_width=3.2,fill_color=WATER_BG,fill_opacity=1.0).move_to(UP*-3.5)
        bval=Text("6 units trapped",font=MN,weight=BOLD,color=WATER).scale(0.52).move_to(box.get_center())
        self.add(box,bval)
        self.add(Text("two pointers  →  O(1) extra space",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-5.05))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.75+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.75+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-6.25))
        self.wait(0.3)
