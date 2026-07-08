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

def wtile(word,tc,bg,st,scale=0.5):
    t=Text(word,font=MN,weight=BOLD,color=tc).scale(scale)
    box=RoundedRectangle(width=t.width+0.42,height=0.78,corner_radius=0.12,stroke_color=st,stroke_width=2.8,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

class Cover151(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 151",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("Reverse Words in a String",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(6.4).move_to(UP*4.0)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.2+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.2+RIGHT*0.75))

        sub=Text("tokenize · reverse · join",font=MN,color=GRAY).scale(0.36).move_to(UP*2.45)
        self.add(sub)

        raw=Text('"  the sky is  blue "',font=MN,weight=BOLD,color=GRAY).scale(0.5).move_to(UP*1.6)
        if raw.width>6.8: raw.scale_to_fit_width(6.8)
        self.add(Text("in",font=MN,weight=BOLD,color=GRAY).scale(0.34).next_to(raw,LEFT,buff=0.25),raw)

        top=VGroup(*[wtile(w,WHITE,SURFACE,CYAN) for w in ["the","sky","is","blue"]]).arrange(RIGHT,buff=0.18).move_to(UP*0.55)
        self.add(top)
        self.add(Text("↓ reverse",font=MN,weight=BOLD,color=MINT).scale(0.36).move_to(UP*-0.35))
        bot=VGroup(*[wtile(w,MINT,MINT_BG,MINT) for w in ["blue","is","sky","the"]]).arrange(RIGHT,buff=0.18).move_to(UP*-1.25)
        self.add(bot)

        box=RoundedRectangle(width=5.6,height=1.2,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-2.75)
        bval=Text('"blue is sky the"',font=MN,weight=BOLD,color=MINT).scale(0.5).move_to(box.get_center())
        if bval.width>5.2: bval.scale_to_fit_width(5.2)
        self.add(box,bval)
        self.add(Text("stringstream >> skips extra spaces",font=MN,color=GRAY).scale(0.34).next_to(box,DOWN,buff=0.24))

        self.add(Text("O(n) time      ·      O(1) in place",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*-4.55))
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-5.35+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-5.35+RIGHT*0.7))
        self.add(Text("@axiobyte   ·   from first principles",font=MN,color=GRAY).scale(0.36).move_to(UP*-5.95))
        self.wait(0.3)
