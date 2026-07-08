from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; RED_BG="#331617"; MINT_BG="#0F2A20"; AMBER_BG="#33240F"
MED_T="#F0A431"; MED_B="#33240F"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

S="PAYPALISHIRING"; NR=3
ROWCOL={0:CYAN,1:MINT,2:AMBER}; ROWBG={0:CYAN_BG,1:MINT_BG,2:AMBER_BG}

def pill(text,tc,bg,st,s=0.42,h=0.62):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.5,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def gcell(ch,color,bg,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.09,stroke_color=color,stroke_width=2.8,fill_color=bg,fill_opacity=1.0)
    t=Text(ch,font=FN,weight=BOLD,color=color).scale(0.55*size).move_to(r.get_center())
    return VGroup(r,t)

def zigzag(s,nr):
    cur=0;step=1;col=0;pos=[]
    for ch in s:
        pos.append((cur,col))
        if cur==0: step=1
        elif cur==nr-1: step=-1
        cur+=step
        if step==-1: col+=1
    return pos

class Cover6(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 6",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Zigzag Conversion",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.0).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("bucket per row · bounce top ↔ bottom",font=MN,color=GRAY).scale(0.34).move_to(UP*2.45)
        if sub.width>6.6: sub.scale_to_fit_width(6.6)
        self.add(sub)

        pos=zigzag(S,NR); ncols=max(c for _,c in pos)+1
        cw=0.6; cs=0.66
        x0=-(ncols-1)*cs/2; ytop=1.5; ys=0.66
        for (r,c),ch in zip(pos,S):
            self.add(gcell(ch,ROWCOL[r],ROWBG[r],cw).move_to([x0+c*cs,ytop-r*ys,0]))
        for r in range(NR):
            self.add(Text("→",font=FN,weight=BOLD,color=ROWCOL[r]).scale(0.4).move_to([x0-0.7,ytop-r*ys,0]))

        box=RoundedRectangle(width=6.2,height=1.2,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-1.7)
        bval=Text('"PAHNAPLSIIGYIR"',font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(box.get_center())
        if bval.width>5.8: bval.scale_to_fit_width(5.8)
        self.add(box,bval)
        self.add(Text("read row by row, top to bottom",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(n) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-3.9))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-4.7+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-4.7+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.3))
        self.wait(0.3)
