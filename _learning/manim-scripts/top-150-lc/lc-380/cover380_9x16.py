from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"
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

def mcell(v,stroke,fill,tcolor,size=0.72):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=2.8,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center())
    return VGroup(r,t)

def mentry(k,v):
    kk=Text(str(k),font=MN,weight=BOLD,color=CYAN).scale(0.4)
    ar=Text("\u2192",font=MN,color=GRAY).scale(0.36)
    vv=Text(str(v),font=MN,weight=BOLD,color=AMBER).scale(0.4)
    inner=VGroup(kk,ar,vv).arrange(RIGHT,buff=0.09)
    box=RoundedRectangle(width=inner.width+0.3,height=0.56,corner_radius=0.11,stroke_color=BORDER,stroke_width=2.2,fill_color=SURFACE,fill_opacity=1.0)
    inner.move_to(box.get_center()); return VGroup(box,inner)

class Cover380(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 380",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.15))
        title=Text("Insert Delete GetRandom",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.4).move_to(UP*4.15)
        sub2=Text("O(1)",font=FN,weight=BOLD,color=MINT).scale(0.8).next_to(title,DOWN,buff=0.2)
        self.add(title,sub2)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*2.7+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*2.7+RIGHT*0.75))

        # array
        vals=[1,2,3]
        arr=VGroup(*[mcell(v,BORDER,SURFACE,WHITE) for v in vals]).arrange(RIGHT,buff=0.14).move_to(UP*1.5+RIGHT*0.3)
        self.add(arr,Text("v",font=MN,weight=BOLD,color=WHITE).scale(0.44).next_to(arr,LEFT,buff=0.28))
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(arr[i],DOWN,buff=0.12) for i in range(3)])
        self.add(idx)
        # map
        mp=VGroup(*[mentry(v,i) for i,v in enumerate(vals)]).arrange(RIGHT,buff=0.18).move_to(UP*0.15+RIGHT*0.3)
        self.add(mp,Text("map",font=MN,weight=BOLD,color=WHITE).scale(0.4).next_to(mp,LEFT,buff=0.28))
        self.add(Text("value \u2192 index",font=MN,color=GRAY).scale(0.32).next_to(mp,DOWN,buff=0.14))

        # swap-with-last hint
        hint=Text("remove:  swap with last  \u2192  pop   (O(1))",font=MN,weight=BOLD,color=MINT).scale(0.38).move_to(UP*-1.4)
        if hint.width>6.8: hint.scale_to_fit_width(6.8)
        self.add(hint)
        arc=CurvedArrow(arr[2].get_top()+UP*0.05,arr[1].get_top()+UP*0.05,angle=PI*0.6,color=MINT,stroke_width=3.5,tip_length=0.16)
        self.add(arc)

        hook=Text("array  +  hash map",font=FN,weight=BOLD,color=CYAN).scale(0.5).move_to(UP*-2.5)
        self.add(hook)
        box=RoundedRectangle(width=5.6,height=1.15,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-3.75)
        bval=Text("insert · remove · getRandom",font=MN,weight=BOLD,color=MINT).scale(0.42).move_to(box.get_center())
        if bval.width>5.2: bval.scale_to_fit_width(5.2)
        self.add(box,bval)
        self.add(Text("all  O(1)  average",font=MN,weight=BOLD,color=WHITE).scale(0.42).move_to(UP*-4.95))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-5.75))
        self.wait(0.3)
