from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; RED_BG="#331617"; MINT_BG="#0F2A20"
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

def mcell(v,stroke,fill,tcolor,size):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover134(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 134",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Gas Station",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(5.4).move_to(UP*3.95)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))

        sub=Text("net[i] = gas[i] - cost[i]",font=MN,color=GRAY).scale(0.36).move_to(UP*2.35)
        self.add(sub)
        net=[-2,-2,-2,3,3]
        row=VGroup()
        for i,v in enumerate(net):
            if v>=0: row.add(mcell(v,MINT,MINT_BG,MINT,0.72))
            else: row.add(mcell(v,BORDER,SURFACE,AMBER,0.72))
        row.arrange(RIGHT,buff=0.16).move_to(UP*1.4)
        self.add(row,Text("gas-cost",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(row,LEFT,buff=0.22))
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(row[i],DOWN,buff=0.16) for i in range(5)])
        self.add(idx)
        # start marker under index 3
        st=Triangle(color=MINT,fill_opacity=1.0,stroke_width=0).scale(0.14).next_to(idx[3],DOWN,buff=0.16)
        stl=Text("start",font=MN,weight=BOLD,color=MINT).scale(0.32).next_to(st,DOWN,buff=0.06)
        self.add(st,stl)

        hook=Text("greedy  ·  where does the tank never run dry?",font=FN,color=CYAN).scale(0.42)
        if hook.width>6.6: hook.scale_to_fit_width(6.6)
        hook.move_to(UP*-0.85); self.add(hook)

        box=RoundedRectangle(width=5.0,height=1.2,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.2)
        bval=Text("start = 3",font=MN,weight=BOLD,color=MINT).scale(0.52).move_to(box.get_center())
        self.add(box,bval)
        self.add(Text("total gas ≥ total cost, so a start exists",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(1) space",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.25))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.2+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.2+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8))
        self.wait(0.3)
