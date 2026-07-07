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

class Cover274(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.6)
        self.add(VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.05))
        self.add(VGroup(pill("# 274",CYAN,SURFACE,CYAN),pill("Medium",MED_T,MED_B,MED_T)).arrange(RIGHT,buff=0.28).move_to(UP*5.1))
        title=Text("H-Index",font=FN,weight=BOLD,color=WHITE)
        title.scale_to_fit_width(4.4).move_to(UP*3.95)
        self.add(title)
        self.add(Line(LEFT*1.5,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*3.15+LEFT*0.75))
        self.add(Line(ORIGIN,RIGHT*1.5,color=AMBER,stroke_width=4).move_to(UP*3.15+RIGHT*0.75))
        sub=Text("h papers each cited \u2265 h times",font=MN,color=GRAY).scale(0.38).move_to(UP*2.4)
        self.add(sub)

        # mini bar chart
        cits=[6,5,3,1,0]; SC=0.3; BASE=-1.0; BW=0.56; PITCH=0.8; X0=-1.6
        def bx(i): return X0+i*PITCH
        self.add(Line([X0-0.5,BASE,0],[bx(4)+0.5,BASE,0],color=BORDER,stroke_width=2.5))
        for i,c in enumerate(cits):
            h=max(c*SC,0.05)
            green=(i<3)
            r=Rectangle(width=BW,height=h,fill_color=MINT_BG if green else (RED_BG if c==1 else SURFACE),
                        fill_opacity=1.0,stroke_color=MINT if green else (RED if c==1 else BORDER),stroke_width=2.6).set_z_index(2)
            r.move_to([bx(i),BASE+h/2,0])
            self.add(r,Text(str(c),font=FN,weight=BOLD,color=MINT if green else WHITE).scale(0.36).next_to(r,UP,buff=0.06).set_z_index(3))
            self.add(Text(str(i+1),font=MN,color=GRAY).scale(0.34).move_to([bx(i),BASE-0.35,0]))
        diag=DashedLine([X0-PITCH*0.5,BASE+SC*0.5,0],[X0+PITCH*4.5,BASE+SC*5.5,0],color=AMBER,stroke_width=3.0,dash_length=0.12).set_z_index(1)
        self.add(diag)
        self.add(Text("citations = rank",font=MN,weight=BOLD,color=AMBER).scale(0.32).move_to([bx(4)-0.5,BASE+SC*5.5+0.1,0]))
        # h x h square
        sq=Rectangle(width=bx(2)+BW/2-(bx(0)-BW/2),height=3*SC,fill_color=MINT,fill_opacity=0.16,stroke_color=MINT,stroke_width=2.6)
        sq.move_to([(bx(0)-BW/2+bx(2)+BW/2)/2,BASE+3*SC/2,0]).set_z_index(4)
        self.add(sq,Text("3\u00d73",font=MN,weight=BOLD,color=MINT).scale(0.34).move_to(sq.get_center()).set_z_index(6))

        hook=Text("sort  \u2192  where citations meet rank",font=FN,color=CYAN).scale(0.42).move_to(UP*-2.5)
        if hook.width>6.6: hook.scale_to_fit_width(6.6)
        self.add(hook)
        box=RoundedRectangle(width=3.0,height=1.1,corner_radius=0.18,stroke_color=MINT,stroke_width=3.2,fill_color=MINT_BG,fill_opacity=1.0).move_to(UP*-3.7)
        self.add(box,Text("h = 3",font=MN,weight=BOLD,color=MINT).scale(0.6).move_to(box.get_center()))
        self.add(Text("O(n log n)  \u00b7  O(1)",font=MN,weight=BOLD,color=WHITE).scale(0.42).move_to(UP*-4.9))
        self.add(Text("@axiobyte   \u00b7   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-5.75))
        self.wait(0.3)
