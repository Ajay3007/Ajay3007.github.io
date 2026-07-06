from manim import *

BG=" #0B0E14".strip(); BG="#0B0E14"
SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"
CYAN_BG="#10303A"; AMBER_BG="#33240F"
GREEN_T="#4ECB71"; GREEN_B="#12301C"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

def pill(text, tc, bg, st, s=0.42, h=0.62):
    t=Text(text, font=MN, weight=BOLD, color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5, height=h, corner_radius=h/2,
                         stroke_color=st, stroke_width=2.5, fill_color=bg, fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mini_cell(v,color,fill):
    r=RoundedRectangle(width=0.54,height=0.54,corner_radius=0.09,stroke_color=color,
                       stroke_width=2.6,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=color).scale(0.4).move_to(r.get_center())
    return VGroup(r,t)

def mini_empty():
    b=RoundedRectangle(width=0.54,height=0.54,corner_radius=0.09,stroke_color=GRAY,stroke_width=2.0)
    d=DashedVMobject(b,num_dashes=12,dashed_ratio=0.55).set_stroke(GRAY,2.0)
    return VGroup(d)

def ocell(v,origin,size=1.0):
    fill=CYAN_BG if origin=="n1" else AMBER_BG
    st=CYAN if origin=="n1" else AMBER
    r=RoundedRectangle(width=size,height=size,corner_radius=0.14,stroke_color=st,
                       stroke_width=3.4,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=WHITE).scale(0.62*size).move_to(r.get_center())
    return VGroup(r,t)

class Cover88V(Scene):
    def construct(self):
        frame=RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,
                               stroke_color=BORDER,stroke_width=2.0,fill_opacity=0)
        self.add(frame)

        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05)
        self.add(wm)

        meta=VGroup(pill("# 88",CYAN,SURFACE,CYAN), pill("Easy",GREEN_T,GREEN_B,GREEN_T)
                    ).arrange(RIGHT,buff=0.28).move_to(UP*5.1)
        self.add(meta)

        title=Text("Merge Sorted Array",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.5).move_to(UP*3.95)
        self.add(title)

        dl=Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75)
        dr=Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75)
        self.add(dl,dr)

        # input arrays
        n1=VGroup(mini_cell(1,CYAN,CYAN_BG),mini_cell(2,CYAN,CYAN_BG),mini_cell(3,CYAN,CYAN_BG),
                  mini_empty(),mini_empty(),mini_empty()).arrange(RIGHT,buff=0.1)
        n2=VGroup(mini_cell(2,AMBER,AMBER_BG),mini_cell(5,AMBER,AMBER_BG),mini_cell(6,AMBER,AMBER_BG)
                  ).arrange(RIGHT,buff=0.1)
        lab1=Text("nums1",font=MN,weight=BOLD,color=WHITE).scale(0.38)
        lab2=Text("nums2",font=MN,weight=BOLD,color=WHITE).scale(0.38)
        g1=VGroup(lab1,n1).arrange(RIGHT,buff=0.28)
        g2=VGroup(lab2,n2).arrange(RIGHT,buff=0.28)
        inputs=VGroup(g1,g2).arrange(DOWN,aligned_edge=LEFT,buff=0.34).move_to(UP*1.78)
        self.add(inputs)

        arrow=Arrow(start=[0,0.5,0],end=[0,-0.15,0],buff=0,color=CYAN,
                    stroke_width=6,max_tip_length_to_length_ratio=0.4).move_to(UP*0.35)
        self.add(arrow)

        hook=VGroup(Text("\u25C4",font=FN,color=CYAN).scale(0.42),
                    Text("fill from the back",font=FN,color=CYAN).scale(0.46)
                    ).arrange(RIGHT,buff=0.16).move_to(UP*-0.55)
        self.add(hook)

        vals=[1,2,2,3,5,6]; origin=["n1","n1","n2","n1","n2","n2"]
        row=VGroup(*[ocell(v,o,1.0) for v,o in zip(vals,origin)]).arrange(RIGHT,buff=0.12)
        row.move_to(UP*-1.75)
        self.add(row)

        sortd=Text("sorted \u2713",font=FN,weight=BOLD,color=MINT).scale(0.48).move_to(UP*-2.95)
        self.add(sortd)

        tag=Text("O(m + n) time      \u00b7      O(1) space",font=MN,weight=BOLD,color=WHITE
                 ).scale(0.44).move_to(UP*-3.95)
        self.add(tag)

        bl=Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.15+LEFT*0.7)
        br=Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.15+RIGHT*0.7)
        foot=Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.8)
        self.add(bl,br,foot)

        self.wait(0.3)
