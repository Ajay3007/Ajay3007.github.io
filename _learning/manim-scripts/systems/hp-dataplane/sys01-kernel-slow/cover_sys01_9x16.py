from manim import *

BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"; WATER="#4AA8FF"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; MINT_BG="#0F2A20"; RED_BG="#331617"; WATER_BG="#12314F"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

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

def node(title,sub,w,h,color):
    box=RoundedRectangle(width=w,height=h,corner_radius=0.14,stroke_color=color,stroke_width=3.0,fill_color=SURF2,fill_opacity=1.0).set_z_index(2)
    t=Text(title,font=FN,weight=BOLD,color=WHITE).scale(0.5)
    s=Text(sub,font=MN,color=GRAY).scale(0.3)
    VGroup(t,s).arrange(DOWN,buff=0.1).move_to(box.get_center()).set_z_index(3)
    g=VGroup(box,t,s); g.add_to_back(glow(box,color,layers=5,spread=0.22,max_op=0.1)); return g

class CoverSys01(Scene):
    def construct(self):
        self.add(RoundedRectangle(width=7.35,height=13.6,corner_radius=0.4,stroke_color=BORDER,stroke_width=2.0,fill_opacity=0))
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.62)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.62)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03)
        sysx=Text("SYSTEMS",font=MN,weight=BOLD,color=GRAY).scale(0.36).next_to(wm,DOWN,buff=0.08)
        self.add(VGroup(wm,sysx).move_to(UP*5.9))
        self.add(pill("High-Performance Data Plane · #1",CYAN,SURFACE,CYAN,s=0.32,glowing=True).move_to(UP*4.95))

        title=Text("Why the kernel is",font=FN,weight=BOLD,color=WHITE).scale(0.9)
        title2=Text("slow for packets",font=FN,weight=BOLD,color=WHITE).scale(0.9)
        VGroup(title,title2).arrange(DOWN,buff=0.14).move_to(UP*3.7)
        self.add(title,title2)

        # mini stack diagram with a big red BYPASS
        nic=node("NIC","off the wire",3.0,0.9,CYAN).move_to(UP*1.7)
        krn=node("Kernel stack","IRQ · copy · TCP/IP",3.3,1.0,AMBER).move_to(UP*0.35)
        app=node("Your app","recv()",3.0,0.9,MINT).move_to(UP*-1.0)
        self.add(nic,krn,app)
        self.add(Arrow(nic.get_bottom(),krn.get_top(),buff=0.06,color=GRAY,stroke_width=4).set_z_index(1))
        # kernel crossed out
        slash=Line(krn.get_corner(DL),krn.get_corner(UR),color=RED,stroke_width=6).set_z_index(9)
        slash.add_to_back(glow(slash,RED,layers=4,spread=1.0,max_op=0.22))
        self.add(slash)
        krn.set_opacity(0.4)
        # bypass arrow NIC -> app
        by=CurvedArrow(nic.get_left()+LEFT*0.05,app.get_left()+LEFT*0.05,angle=PI*0.7,color=WATER,stroke_width=5,tip_length=0.24).set_z_index(6)
        self.add(by)
        self.add(Text("DPDK bypass",font=MN,weight=BOLD,color=WATER).scale(0.34).next_to(by,LEFT,buff=0.1))

        comp=VGroup(pill("0.5 Mpps",RED,RED_BG,RED,s=0.42,h=0.62,glowing=True),
                    Text("→",font=FN,weight=BOLD,color=WHITE).scale(0.7),
                    pill("15 Mpps",MINT,MINT_BG,MINT,s=0.42,h=0.62,glowing=True)).arrange(RIGHT,buff=0.3).move_to(UP*-2.7)
        self.add(comp)
        self.add(Text("no interrupts · no copies · no syscalls",font=MN,color=GRAY).scale(0.36).move_to(UP*-3.7))

        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(UP*-4.7+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(UP*-4.7+RIGHT*0.7))
        self.add(Text("@axiobyte.systems   ·   from first principles",font=MN,color=GRAY).scale(0.34).move_to(UP*-5.3))
        self.wait(0.3)
