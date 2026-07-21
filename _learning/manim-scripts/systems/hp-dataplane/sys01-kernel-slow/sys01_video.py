from manim import *
import re

# ================================================================
# AxioByte Systems — Ep 1 (DEEP DIVE ~3 min)
# Why the kernel is slow for packets
# v3 palette + systems diagram toolkit
# ================================================================
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"; WATER="#4AA8FF"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; MINT_BG="#0F2A20"; RED_BG="#331617"; WATER_BG="#12314F"

CODEFG="#C7D0DA"; KW_C=CYAN; NUM_C=AMBER; OP_C="#F78CA0"; STR_C=MINT; COM_C=GRAY
KEYWORDS=set("int for while if else return void struct const char uint16_t uint32_t size_t".split())
TYPES=set("rte_mbuf".split())

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=6.35; SEG_Y=5.2; CAP_Y=4.35
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

def colorize(s,scale=0.32):
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
    t=Text(title,font=FN,weight=BOLD,color=WHITE).scale(0.46)
    if sub:
        s=Text(sub,font=MN,color=GRAY).scale(0.3); inner=VGroup(t,s).arrange(DOWN,buff=0.1)
    else: inner=t
    if inner.width>w-0.3: inner.scale_to_fit_width(w-0.3)
    inner.move_to(box.get_center()).set_z_index(5)
    g=VGroup(box,inner)
    if glowing: g.add_to_back(glow(box,color,layers=5,spread=0.2,max_op=0.1))
    g.box=box; return g

def pdot(color=WATER,r=0.16):
    sq=RoundedRectangle(width=2*r,height=2*r,corner_radius=0.06,stroke_color=color,stroke_width=2.0,
                        fill_color=color,fill_opacity=0.9).set_z_index(7)
    g=VGroup(sq); g.add_to_back(glow(sq,color,layers=5,spread=0.9,max_op=0.3)); return g

def timebar(ns,color,unit=0.052,h=0.42):
    w=max(0.2,ns*unit)
    b=RoundedRectangle(width=w,height=h,corner_radius=0.08,stroke_width=0,fill_color=color,fill_opacity=0.9).set_z_index(3)
    b.add_to_back(glow(b,color,layers=4,spread=0.2,max_op=0.1)); return b,w


class Sys01(Scene):
    def construct(self):
        self.persistent()
        self.act1_budget()
        self.act2_kernel()
        self.act3_dpdk_ideas()
        self.act3_code()
        self.act4_numbers()
        self.recap()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.36)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.36)
        row=VGroup(axio,byte).arrange(RIGHT,buff=0.02)
        sysx=Text("SYSTEMS",font=MN,weight=BOLD,color=GRAY).scale(0.26).next_to(row,RIGHT,buff=0.12)
        self.wm=VGroup(row,sysx).move_to(UP*WM_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.1),run_time=0.5)
        self.seg=None; self.cap=None

    def set_seg(self,text,color,bg):
        nl=pill(text,color,bg,color,s=0.36,glowing=True).move_to(UP*SEG_Y)
        if self.seg is None:
            self.seg=nl; return [FadeIn(nl,shift=UP*0.1)]
        old=self.seg; self.seg=nl; return [FadeOut(old,shift=UP*0.08),FadeIn(nl,shift=DOWN*0.08)]

    def clear_cap(self):
        if self.cap is not None:
            self.play(FadeOut(self.cap),run_time=0.2); self.cap=None

    def set_cap(self,txt,color=WHITE,scale=0.44,rt=0.4):
        new=Text(txt,font=FN,color=color).scale(scale)
        if new.width>7.1: new.scale_to_fit_width(7.1)
        new.move_to(UP*CAP_Y)
        if self.cap is None:
            self.cap=new; self.play(FadeIn(new,shift=UP*0.1),run_time=rt); return
        self.play(FadeOut(self.cap,shift=UP*0.08),run_time=0.2)
        self.play(FadeIn(new,shift=UP*0.08),run_time=0.3); self.cap=new

    def clear_body(self,keep=()):
        drop=[m for m in self.mobjects if m not in (self.wm,self.seg,self.cap) and m not in keep]
        if drop: self.play(*[FadeOut(m) for m in drop],run_time=0.5)

    # ---------- v3 code panel ----------
    def build_code(self,raw,scale=0.3,cy=-3.4,maxw=6.4):
        lines=[colorize(s,scale) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.12)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.30)
        if block.width>maxw: block.scale(maxw/block.width)
        gut=0.5
        nums=VGroup(*[Text(str(k+1),font=MN,color=GRAY).scale(0.9*scale).move_to([block.get_left()[0]-gut,lines[k].get_center()[1],0]) for k in range(len(lines))])
        content=VGroup(nums,block)
        pw=content.width+0.7; ph=content.height+0.5
        panel=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color=SURF2,fill_opacity=1.0,width=pw,height=ph).move_to(UP*cy).set_z_index(0)
        content.move_to(panel.get_center()); block.set_z_index(2); nums.set_z_index(2)
        hlbar=RoundedRectangle(width=pw-0.16,height=lines[0].height+0.13,corner_radius=0.06,stroke_width=0,fill_color=CYAN,fill_opacity=0.0).set_z_index(1)
        acc=RoundedRectangle(width=0.07,height=lines[0].height+0.15,corner_radius=0.03,stroke_width=0,fill_color=CYAN,fill_opacity=0.0).set_z_index(3)
        self.panel=panel; self.code=lines; self.hlbar=hlbar; self.acc=acc; self.content=content
        self._pcx=panel.get_center()[0]; self._plx=panel.get_left()[0]+0.13; self._bv=False
        return panel,content,hlbar,acc

    def hl(self,i):
        y=self.code[i].get_center()[1]
        if not self._bv:
            self.hlbar.move_to([self._pcx,y,0]); self.acc.move_to([self._plx,y,0]); self._bv=True
            return [self.hlbar.animate.set_fill(CYAN,opacity=0.12),self.acc.animate.set_fill(CYAN,opacity=1.0)]
        return [self.hlbar.animate.move_to([self._pcx,y,0]),self.acc.animate.move_to([self._plx,y,0])]

    # ============================================================
    # ACT 1 — the budget
    # ============================================================
    def act1_budget(self):
        self.play(*self.set_seg("① the budget nobody mentions",CYAN,CYAN_BG),run_time=0.45)
        self.set_cap("10 GbE, smallest (64-byte) packets…",color=WATER)
        big=Text("14.88 Mpps",font=MN,weight=BOLD,color=WATER).scale(1.05).move_to(UP*3.1)
        self.play(FadeIn(big,scale=1.1),run_time=0.7)
        l2=Text("÷ a 3.0 GHz core",font=MN,color=GRAY).scale(0.5).move_to(UP*2.0)
        self.play(FadeIn(l2,shift=UP*0.1),run_time=0.5)
        eq=Text("≈ 201 cycles  (~67 ns)  per packet",font=MN,weight=BOLD,color=AMBER).scale(0.54).move_to(UP*1.15)
        if eq.width>7.1: eq.scale_to_fit_width(7.1)
        self.play(Write(eq),run_time=0.8); self.wait(0.4)
        self.set_cap("that's your ENTIRE time budget per packet",color=AMBER)

        # budget vs a cache miss — bars anchored left
        bx=-2.6
        bud,bw=timebar(67,MINT); bud.move_to([bx+bw/2,0.0,0])
        budl=Text("budget  67 ns",font=MN,weight=BOLD,color=MINT).scale(0.34).next_to(bud,RIGHT,buff=0.2)
        miss,mw=timebar(95,RED); miss.move_to([bx+mw/2,-1.0,0])
        missl=Text("1 cache miss  ~95 ns",font=MN,weight=BOLD,color=RED).scale(0.34).next_to(miss,RIGHT,buff=0.2)
        line=DashedLine([bx+bw,0.6,0],[bx+bw,-1.6,0],color=MINT,stroke_width=3)
        self.play(GrowFromEdge(bud,LEFT),FadeIn(budl),run_time=0.6)
        self.play(Create(line),run_time=0.3)
        self.play(GrowFromEdge(miss,LEFT),FadeIn(missl),run_time=0.7)
        self.wait(0.3)
        pun=pill("one cache miss and the budget is already gone",RED,RED_BG,RED,s=0.4,h=0.62,glowing=True).move_to(UP*-2.5)
        if pun.width>7.2: pun.scale_to_fit_width(7.2)
        self.play(FadeIn(pun,scale=1.05),run_time=0.6); self.wait(READ_L)
        self.clear_body()

    # ============================================================
    # ACT 2 — the kernel path, costed
    # ============================================================
    def build_stack(self,nic_y,krn_y,app_y,x=-0.55):
        self.nic=node("NIC","DMA + rx ring",color=CYAN).move_to([x,nic_y,0])
        self.krn=node("Kernel stack","IRQ · sk_buff · TCP/IP",w=3.3,h=1.05,color=AMBER).move_to([x,krn_y,0])
        self.app=node("Your app","recv()",color=MINT).move_to([x,app_y,0])
        self.a1=Arrow(self.nic.get_top(),self.krn.get_bottom(),buff=0.08,color=GRAY,stroke_width=4,max_tip_length_to_length_ratio=0.3).set_z_index(1)
        self.a2=Arrow(self.krn.get_top(),self.app.get_bottom(),buff=0.08,color=GRAY,stroke_width=4,max_tip_length_to_length_ratio=0.3).set_z_index(1)

    def act2_kernel(self):
        self.play(*self.set_seg("② where the kernel spends your budget",AMBER,AMBER_BG),run_time=0.45)
        self.build_stack(-2.15,-0.15,1.75)
        self.play(FadeIn(self.nic),FadeIn(self.krn),FadeIn(self.app),GrowArrow(self.a1),GrowArrow(self.a2),run_time=0.9)
        budchip=pill("budget  ~200 cyc",MINT,MINT_BG,MINT,s=0.36,h=0.54).move_to([-1.7,3.55,0])
        self.used=pill("used  0",GRAY,SURFACE,GRAY,s=0.36,h=0.54).move_to([1.7,3.55,0])
        self.play(FadeIn(budchip),FadeIn(self.used),run_time=0.5)
        self.tot=0
        d=pdot(WATER).move_to([-0.55,-3.3,0])
        self.play(FadeIn(d),d.animate.move_to(self.nic.get_center()),run_time=0.6)

        def add_cost(cyc,txt,color=RED,flash_at=None):
            self.tot+=cyc
            over=self.tot>200
            nu=pill("used  ~%d"%self.tot,(RED if over else AMBER),(RED_BG if over else AMBER_BG),(RED if over else AMBER),s=0.36,h=0.54).move_to([1.7,3.55,0])
            self.set_cap(txt,color=color)
            anims=[Transform(self.used,nu)]
            if flash_at is not None: anims.append(Flash(flash_at,color=color,line_length=0.2,num_lines=12,flash_radius=0.6))
            self.play(*anims,run_time=0.6)

        add_cost(300,"DMA lands the packet in a kernel sk_buff (~200-byte alloc)",flash_at=self.nic.get_center())
        self.play(d.animate.move_to(self.krn.get_center()),self.krn.box.animate.set_stroke(AMBER,4.6),run_time=0.5)
        add_cost(500,"interrupt fires — save/restore state; at 15 Mpps it becomes livelock",flash_at=self.krn.get_center())
        add_cost(400,"run the TCP/IP stack + free the sk_buff → cache pollution")
        self.play(d.animate.move_to(self.app.get_center()),run_time=0.5)
        add_cost(600,"context switch + copy AGAIN into user space on recv()",flash_at=self.app.get_center())
        self.wait(0.3)
        self.set_cap("~1800 cycles for a 200-cycle budget — ~9× over, every packet",color=RED)
        napi=pill("even Linux gives up: NAPI switches to POLLING under load",VIOLET,SURF2,VIOLET,s=0.34,h=0.56).move_to([-0.55,-3.35,0])
        if napi.width>7.2: napi.scale_to_fit_width(7.2)
        self.play(FadeOut(d),FadeIn(napi,shift=UP*0.1),run_time=0.6)
        self.wait(READ_L)
        self.clear_body()

    # ============================================================
    # ACT 3a — what makes it fast (ideas)
    # ============================================================
    def act3_dpdk_ideas(self):
        self.play(*self.set_seg("③ what actually makes it fast",MINT,MINT_BG),run_time=0.45)
        self.set_cap("DPDK deletes each cost — here's the map",color=MINT)
        rows=[("poll-mode driver","no interrupts, no livelock"),
              ("hugepages (2M/1G)","far fewer TLB misses"),
              ("mbuf + mempool","buffers pre-allocated, per-core cache — no per-packet alloc"),
              ("zero-copy","the packet is a pointer; process it in place"),
              ("burst of 32","per-packet overhead ÷ 32"),
              ("prefetch next mbuf","hide memory latency behind work")]
        items=VGroup()
        for mech,why in rows:
            chk=Text("✓",font=FN,weight=BOLD,color=MINT).scale(0.5)
            m=Text(mech,font=MN,weight=BOLD,color=WHITE).scale(0.4)
            w=Text("→ "+why,font=FN,color=GRAY).scale(0.36)
            rowg=VGroup(chk,m,w).arrange(RIGHT,buff=0.22)
            if rowg.width>7.2: rowg.scale_to_fit_width(7.2)
            items.add(rowg)
        items.arrange(DOWN,aligned_edge=LEFT,buff=0.34).move_to(UP*0.6)
        for r in items:
            self.play(FadeIn(r,shift=RIGHT*0.12),run_time=0.4)
        self.wait(READ_L)
        note=pill("each line removes a cost from Act 2",MINT,MINT_BG,MINT,s=0.38,h=0.6,glowing=True).move_to(UP*-3.0)
        self.play(FadeIn(note,scale=1.05),run_time=0.5); self.wait(READ)
        self.clear_body()

    # ============================================================
    # ACT 3b — the code
    # ============================================================
    def act3_code(self):
        self.play(*self.set_seg("③ the receive loop, for real",MINT,MINT_BG),run_time=0.4)
        self.set_cap("no syscalls — you just poll a burst and read in place",color=MINT)
        raw=[(0,'struct rte_mbuf *bufs[32];'),
             (0,'uint16_t n = rte_eth_rx_burst(port, q, bufs, 32);'),
             (0,'for (uint16_t i = 0; i < n; i++) {'),
             (1,'rte_prefetch0(next_mbuf(bufs, i));   // hide latency'),
             (1,'process(bufs[i]);   // packet = pointer, zero copy'),
             (0,'}')]
        panel,content,hlbar,acc=self.build_code(raw,scale=0.32,cy=0.4,maxw=6.6)
        self.play(FadeIn(panel),FadeIn(content),run_time=0.6); self.add(hlbar,acc)
        self.play(*self.hl(1),run_time=0.4); self.wait(0.3)
        self.set_cap("rx_burst: grab up to 32 packets, one poll — no interrupt",color=CYAN)
        self.wait(0.6)
        self.play(*self.hl(3),run_time=0.4)
        self.set_cap("prefetch the next while you work on this one",color=VIOLET)
        self.wait(0.6)
        self.play(*self.hl(4),run_time=0.4)
        self.set_cap("process in place — the mbuf is just a pointer",color=MINT)
        self.wait(READ_L)
        self.clear_body()

    # ============================================================
    # ACT 4 — numbers + when NOT to
    # ============================================================
    def act4_numbers(self):
        self.clear_cap()
        self.play(*self.set_seg("④ the payoff — and the price",AMBER,AMBER_BG),run_time=0.45)
        comp=VGroup(pill("kernel  ~0.5 Mpps",RED,RED_BG,RED,s=0.42,h=0.64,glowing=True),
                    Text("→",font=FN,weight=BOLD,color=WHITE).scale(0.7),
                    pill("DPDK  ~15–30 Mpps / core",MINT,MINT_BG,MINT,s=0.42,h=0.64,glowing=True)).arrange(RIGHT,buff=0.28).move_to(UP*3.0)
        if comp.width>7.3: comp.scale_to_fit_width(7.3)
        self.play(FadeIn(comp,scale=1.05),run_time=0.6)
        price=Text("the price:",font=FN,weight=BOLD,color=AMBER).scale(0.5).move_to(UP*1.7)
        p1=Text("• a whole core pinned at 100%, polling forever",font=FN,color=WHITE).scale(0.4)
        p2=Text("• no kernel stack — you rebuild TCP/ARP/… yourself",font=FN,color=WHITE).scale(0.4)
        for p in (p1,p2):
            if p.width>7.1: p.scale_to_fit_width(7.1)
        p1.move_to(UP*0.9); p2.next_to(p1,DOWN,buff=0.28)
        self.play(FadeIn(price,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(p1,shift=RIGHT*0.1),run_time=0.45); self.play(FadeIn(p2,shift=RIGHT*0.1),run_time=0.45)
        self.wait(READ)
        use=Text("use it:  routers · firewalls · load-balancers · NFV",font=FN,weight=BOLD,color=MINT).scale(0.42).move_to(UP*-1.1)
        dont=Text("skip it:  a normal web app — the kernel is fine there",font=FN,weight=BOLD,color=GRAY).scale(0.4).move_to(UP*-1.9)
        for t in (use,dont):
            if t.width>7.2: t.scale_to_fit_width(7.2)
        self.play(FadeIn(use,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(dont,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L)
        self.clear_body()

    # ============================================================
    # RECAP
    # ============================================================
    def recap(self):
        self.clear_cap()
        self.play(*self.set_seg("recap",CYAN,CYAN_BG),run_time=0.4)
        r1=Text("① you get ~67 ns — one cache miss — per packet",font=FN,color=WHITE).scale(0.42)
        r2=Text("② the kernel spends ~9× that on IRQ, copies, syscalls",font=FN,color=WHITE).scale(0.42)
        r3=Text("③ DPDK removes each cost: poll, hugepages, mbuf, burst",font=FN,color=WHITE).scale(0.42)
        r4=Text("→ ~0.5 Mpps becomes tens of Mpps per core",font=FN,weight=BOLD,color=MINT).scale(0.44)
        for r in (r1,r2,r3,r4):
            if r.width>7.2: r.scale_to_fit_width(7.2)
        g=VGroup(r1,r2,r3,r4).arrange(DOWN,aligned_edge=LEFT,buff=0.4).move_to(UP*0.6)
        for r in g[:3]: self.play(FadeIn(r,shift=RIGHT*0.1),run_time=0.45)
        self.play(Write(g[3]),run_time=0.7)
        self.wait(READ_L+0.3)
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.5)
        self.seg=None; self.cap=None

    def end_slide(self):
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
