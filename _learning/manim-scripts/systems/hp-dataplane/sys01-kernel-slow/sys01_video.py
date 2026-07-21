from manim import *
import re

# ================================================================
# AxioByte Systems — v3 palette + systems diagram toolkit
# Ep 1 · Why the kernel is slow for packets
# ================================================================
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"; WATER="#4AA8FF"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; MINT_BG="#0F2A20"; RED_BG="#331617"; WATER_BG="#12314F"

CODEFG="#C7D0DA"; KW_C=CYAN; NUM_C=AMBER; OP_C="#F78CA0"; STR_C=MINT; COM_C=GRAY
KEYWORDS=set("int for while if else return void struct const char".split())
TYPES=set("uint16_t size_t".split())

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=6.15; BADGE_Y=5.2; TITLE_Y=4.4
SEG_Y=3.45; CAP_Y=2.75
NODE_X=-0.55; NIC_Y=-2.05; KRN_Y=-0.15; APP_Y=1.75
MET_X=2.95; MET_BOT=-2.55; MET_H=4.35; MET_W=0.5
READ=0.8; READ_L=1.4

def glow(shape,color=None,layers=6,spread=0.34,max_op=0.16):
    if color is None: color=shape.get_stroke_color()
    halo=VGroup()
    for i in range(layers):
        f=(i+1)/layers
        c=shape.copy().set_stroke(width=0).set_fill(color,opacity=max_op*(1-f)+0.015)
        c.scale(1+spread*f); halo.add(c)
    halo.set_z_index(shape.get_z_index()-1); return halo

def _char_colors(s):
    col=[None]*len(s); ci=s.find("//")
    for m in re.finditer(r'[A-Za-z_]\w*|\d+|"[^"]*"|\'[^\']*\'|[-+*/%<>=!&|?:]+', s):
        tok=m.group(); a,b=m.start(),m.end()
        if ci!=-1 and a>=ci: continue
        if tok[0].isdigit(): c=NUM_C
        elif tok[0] in '"\'': c=STR_C
        elif tok[0] in "-+*/%<>=!&|?:": c=OP_C
        elif tok in KEYWORDS or tok in TYPES: c=KW_C
        else: c=None
        if c is not None:
            for k in range(a,b): col[k]=c
    if ci!=-1:
        for k in range(ci,len(s)): col[k]=COM_C
    return col

def colorize(s,scale=0.34):
    col=_char_colors(s); t2c={}; i=0
    while i<len(s):
        if col[i] is None: i+=1; continue
        j=i
        while j<len(s) and col[j]==col[i]: j+=1
        t2c["[%d:%d]"%(i,j)]=col[i]; i=j
    return Text(s,font=MN,color=CODEFG,t2c=t2c).scale(scale)

def pill(text,tc,bg,st,s=0.4,h=0.56,glowing=False):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); g=VGroup(box,t)
    if glowing: g.add_to_back(glow(box,st,layers=5,spread=0.5,max_op=0.14))
    return g

def node(title,sub=None,w=2.9,h=0.95,color=CYAN,glowing=True):
    box=RoundedRectangle(width=w,height=h,corner_radius=0.14,stroke_color=color,stroke_width=3.0,
                         fill_color=SURF2,fill_opacity=1.0).set_z_index(2)
    t=Text(title,font=FN,weight=BOLD,color=WHITE).scale(0.48)
    if sub:
        s=Text(sub,font=MN,color=GRAY).scale(0.3)
        inner=VGroup(t,s).arrange(DOWN,buff=0.1)
    else:
        inner=t
    if inner.width>w-0.3: inner.scale_to_fit_width(w-0.3)
    inner.move_to(box.get_center()).set_z_index(5)
    g=VGroup(box,inner)
    if glowing: g.add_to_back(glow(box,color,layers=5,spread=0.2,max_op=0.1))
    g.box=box; return g

def pdot(color=WATER):
    sq=RoundedRectangle(width=0.32,height=0.32,corner_radius=0.07,stroke_color=color,stroke_width=2.0,
                        fill_color=color,fill_opacity=0.9).set_z_index(7)
    g=VGroup(sq); g.add_to_back(glow(sq,color,layers=5,spread=0.9,max_op=0.3))
    return g


class Sys01(Scene):
    def construct(self):
        self.persistent()
        self.hook()
        self.slow_path()
        self.fast_path()
        self.payoff()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.42)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.42)
        row=VGroup(axio,byte).arrange(RIGHT,buff=0.02)
        sysx=Text("SYSTEMS",font=MN,weight=BOLD,color=GRAY).scale(0.28).next_to(row,DOWN,buff=0.05)
        self.wm=VGroup(row,sysx).move_to(UP*WM_Y)
        self.badge=pill("High-Perf Data Plane · #1",CYAN,SURFACE,CYAN,s=0.34).move_to(UP*BADGE_Y)
        self.title=Text("Why the kernel is slow for packets",font=FN,weight=BOLD,color=WHITE).scale(0.54)
        if self.title.width>7.1: self.title.scale_to_fit_width(7.1)
        self.title.move_to(UP*TITLE_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.15),run_time=0.6)
        self.play(FadeIn(self.badge,shift=UP*0.1),run_time=0.4)
        self.play(Write(self.title),run_time=0.9)
        self.wait(0.3); self.cap=None; self.seg=None

    def set_cap(self,txt,color=WHITE,scale=0.44,rt=0.45):
        new=Text(txt,font=FN,color=color).scale(scale)
        if new.width>7.1: new.scale_to_fit_width(7.1)
        new.move_to(UP*CAP_Y)
        if self.cap is None:
            self.cap=new; self.play(FadeIn(new,shift=UP*0.1),run_time=rt); return
        self.play(FadeOut(self.cap,shift=UP*0.08),run_time=0.2)
        self.play(FadeIn(new,shift=UP*0.08),run_time=0.3); self.cap=new

    def set_seg(self,text,color,bg):
        nl=pill(text,color,bg,color,s=0.36,glowing=True).move_to(UP*SEG_Y)
        if self.seg is None:
            self.seg=nl; return [FadeIn(nl,shift=UP*0.1)]
        old=self.seg; self.seg=nl; return [Transform(old,nl)]

    # ---------- latency meter (right side) ----------
    def build_meter(self):
        out=RoundedRectangle(width=MET_W,height=MET_H,corner_radius=0.1,stroke_color=BORDER,stroke_width=2.4,
                             fill_color=SURF2,fill_opacity=1.0).move_to([MET_X,MET_BOT+MET_H/2,0]).set_z_index(1)
        lab=Text("latency",font=MN,weight=BOLD,color=GRAY).scale(0.3).next_to(out,DOWN,buff=0.12)
        self.met_out=out; self.met_lab=lab; self.met_fill=None
        return VGroup(out,lab)

    def set_meter(self,frac,color):
        frac=max(0.03,min(1.0,frac)); hh=frac*(MET_H-0.14)
        nf=RoundedRectangle(width=MET_W-0.14,height=hh,corner_radius=0.07,stroke_width=0,fill_color=color,fill_opacity=0.9)
        nf.move_to([MET_X,MET_BOT+0.07+hh/2,0]).set_z_index(2)
        nf.add_to_back(glow(nf,color,layers=4,spread=0.22,max_op=0.12))
        if self.met_fill is None:
            self.met_fill=nf; return [FadeIn(nf)]
        old=self.met_fill; self.met_fill=nf; return [FadeOut(old),FadeIn(nf)]

    def build_stack(self):
        self.nic=node("NIC","off the wire",color=CYAN).move_to([NODE_X,NIC_Y,0])
        self.krn=node("Kernel stack","IRQ · copy · TCP/IP",w=3.3,h=1.1,color=AMBER).move_to([NODE_X,KRN_Y,0])
        self.app=node("Your app","recv()",color=MINT).move_to([NODE_X,APP_Y,0])
        self.a1=Arrow(self.nic.get_top(),self.krn.get_bottom(),buff=0.08,color=GRAY,stroke_width=4,max_tip_length_to_length_ratio=0.3).set_z_index(1)
        self.a2=Arrow(self.krn.get_top(),self.app.get_bottom(),buff=0.08,color=GRAY,stroke_width=4,max_tip_length_to_length_ratio=0.3).set_z_index(1)
        self.wire=Line([NODE_X,NIC_Y-1.9,0],self.nic.get_bottom()+DOWN*0.02,color=WATER,stroke_width=4).set_z_index(0)
        self.wlabel=Text("10 GbE  ·  ~14.8 Mpps",font=MN,color=WATER).scale(0.32).next_to(self.wire,DOWN,buff=0.1)

    def hook(self):
        self.build_stack()
        self.play(Create(self.wire),FadeIn(self.wlabel),run_time=0.6)
        self.play(FadeIn(self.nic,shift=UP*0.1),run_time=0.5)
        dots=VGroup(*[pdot(WATER).move_to([NODE_X,NIC_Y-1.9-0.42*i,0]) for i in range(4)])
        self.set_cap("a 10-gig link fires ~15 million packets a second",color=WATER)
        self.play(LaggedStart(*[d.animate.move_to(self.nic.get_center()) for d in dots],lag_ratio=0.12),run_time=1.0)
        self.play(FadeOut(dots),run_time=0.2)
        self.set_cap("can the kernel keep up with each one?")
        self.wait(READ)

    def slow_path(self):
        self.play(*self.set_seg("The slow path — through the kernel",AMBER,AMBER_BG),run_time=0.45)
        self.play(FadeIn(self.krn,shift=UP*0.1),FadeIn(self.app,shift=UP*0.1),
                  GrowArrow(self.a1),GrowArrow(self.a2),run_time=0.8)
        meter=self.build_meter()
        self.play(FadeIn(meter),*self.set_meter(0.05,MINT),run_time=0.5)

        d=pdot(WATER).move_to([NODE_X,NIC_Y-1.4,0])
        self.play(FadeIn(d),d.animate.move_to(self.nic.get_center()),run_time=0.5)

        # tax 1 — interrupt
        self.set_cap("① the NIC fires an interrupt — the CPU drops everything",color=RED)
        self.play(Flash(self.nic.get_center(),color=RED,line_length=0.22,num_lines=12,flash_radius=0.7),
                  *self.set_meter(0.24,AMBER),run_time=0.7)
        # tax 2 — copy + stack
        self.play(d.animate.move_to(self.krn.get_center()),self.krn.box.animate.set_stroke(AMBER,4.8),run_time=0.6)
        self.set_cap("② copy into a kernel buffer, then run the whole TCP/IP stack",color=RED)
        self.play(*self.set_meter(0.55,AMBER),run_time=0.6)
        # tax 3 — context switch
        self.set_cap("③ context switch: kernel → your app",color=RED)
        self.play(Flash(self.a2.get_center(),color=RED,line_length=0.18,num_lines=10,flash_radius=0.5),
                  d.animate.move_to(self.app.get_center()),*self.set_meter(0.78,AMBER),run_time=0.75)
        # tax 4 — copy again
        self.set_cap("④ copy AGAIN into your buffer, on recv()",color=RED)
        self.play(self.app.box.animate.set_stroke(MINT,4.8),*self.set_meter(0.96,RED),run_time=0.7)
        self.slow_dot=d
        self.tput=pill("throughput  ~ 0.5 Mpps",RED,RED_BG,RED,s=0.4,h=0.6,glowing=True).move_to([NODE_X,NIC_Y-1.4,0])
        self.play(FadeOut(self.wlabel),FadeOut(self.wire),FadeIn(self.tput,shift=UP*0.1),run_time=0.5)
        self.set_cap("every packet pays this tax — the kernel tops out",color=RED)
        self.wait(READ_L)

    def fast_path(self):
        self.play(*self.set_seg("The fast path — bypass the kernel (DPDK)",MINT,MINT_BG),
                  FadeOut(self.slow_dot),run_time=0.5)
        slash=Line(self.krn.box.get_corner(DL),self.krn.box.get_corner(UR),color=RED,stroke_width=6).set_z_index(9)
        slash.add_to_back(glow(slash,RED,layers=4,spread=1.0,max_op=0.22))
        self.play(self.krn.animate.set_opacity(0.28),FadeOut(self.a1),FadeOut(self.a2),Create(slash),run_time=0.7)
        self.krn_slash=slash
        direct=CurvedArrow(self.nic.get_left()+LEFT*0.05,self.app.get_left()+LEFT*0.05,angle=PI*0.75,
                           color=WATER,stroke_width=5,tip_length=0.22).set_z_index(6)
        dlab=Text("DMA to\nuser space",font=MN,weight=BOLD,color=WATER).scale(0.3).move_to([-3.05,0.55,0])
        self.play(Create(direct),FadeIn(dlab),run_time=0.8)
        self.direct=direct; self.dlab=dlab
        self.set_cap("the NIC writes straight into your memory — poll-mode, zero-copy",color=WATER)
        d=pdot(WATER).move_to(self.nic.get_center())
        self.play(FadeIn(d),run_time=0.2)
        self.play(d.animate.move_to(self.app.get_center()),*self.set_meter(0.18,MINT),run_time=0.8)
        self.fast_dot=d
        nt=pill("throughput  ~ 15 Mpps / core",MINT,MINT_BG,MINT,s=0.4,h=0.6,glowing=True).move_to([NODE_X,NIC_Y-1.4,0])
        self.play(Transform(self.tput,nt),run_time=0.5)
        self.wait(0.3)
        c1=colorize("recv(fd, buf, len, 0);            // syscall + copy",0.3).move_to([0,NIC_Y-2.35,0])
        c2=colorize("rte_eth_rx_burst(port, q, m, 32); // just poll, 0-copy",0.3).next_to(c1,DOWN,buff=0.16,aligned_edge=LEFT)
        cg=VGroup(c1,c2)
        if cg.width>7.3: cg.scale_to_fit_width(7.3)
        cg.move_to([0,NIC_Y-2.6,0])
        self.play(FadeIn(c1,shift=UP*0.08),run_time=0.45)
        self.play(FadeIn(c2,shift=UP*0.08),run_time=0.45)
        self.wait(READ_L)

    def payoff(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.6)
        self.cap=None; self.seg=None
        title=pill("the trade-off",AMBER,AMBER_BG,AMBER,s=0.42,glowing=True).move_to(UP*2.7)
        self.play(FadeIn(title,shift=UP*0.1),run_time=0.4)
        t1=Text("a whole core spins at 100% — polling, never sleeping",font=FN,color=WHITE).scale(0.42)
        t2=Text("and you give up the kernel's stack — you build what you need",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>7.1: t.scale_to_fit_width(7.1)
        t1.move_to(UP*1.5); t2.next_to(t1,DOWN,buff=0.28)
        self.play(FadeIn(t1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(t2,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L)
        comp=VGroup(pill("kernel  ~0.5 Mpps",RED,RED_BG,RED,s=0.42,h=0.64,glowing=True),
                    Text("→",font=FN,weight=BOLD,color=WHITE).scale(0.7),
                    pill("DPDK  ~15 Mpps",MINT,MINT_BG,MINT,s=0.42,h=0.64,glowing=True)).arrange(RIGHT,buff=0.3).move_to(UP*-0.35)
        if comp.width>7.3: comp.scale_to_fit_width(7.3)
        self.play(FadeIn(comp,scale=1.05),run_time=0.6)
        take=Text("skip the kernel → reach line rate",font=FN,weight=BOLD,color=CYAN).scale(0.5).move_to(UP*-1.9)
        if take.width>7.1: take.scale_to_fit_width(7.1)
        self.play(Write(take),run_time=0.7)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(title,t1,t2,comp,take)),run_time=0.5)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.5)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        row=VGroup(axio,byte).arrange(RIGHT,buff=0.03)
        sysx=Text("SYSTEMS",font=MN,weight=BOLD,color=GRAY).scale(0.44).next_to(row,DOWN,buff=0.12)
        brand=VGroup(row,sysx).move_to(UP*3.2)
        head=Text("High-Performance Data Plane",font=FN,weight=BOLD,color=WHITE).scale(0.56)
        if head.width>6.8: head.scale_to_fit_width(6.8)
        head.move_to(UP*1.6)
        sub=Text("systems, from first principles",font=FN,color=GRAY).scale(0.46).move_to(UP*0.9)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*0.3+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*0.3+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte.systems",font=FN,weight=BOLD,color=CYAN).scale(0.54)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center()); cta=VGroup(ctabox,ctatxt).move_to(UP*-0.7)
        cta.add_to_back(glow(ctabox,CYAN,layers=5,spread=0.4,max_op=0.14))
        nxt=VGroup(Text("next ↓",font=FN,weight=BOLD,color=AMBER).scale(0.5),
                   Text("zero-copy: a packet is just a pointer",font=FN,color=WHITE).scale(0.42)).arrange(RIGHT,buff=0.25).move_to(UP*-2.1)
        if nxt.width>7.1: nxt.scale_to_fit_width(7.1)
        self.play(FadeIn(brand,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
