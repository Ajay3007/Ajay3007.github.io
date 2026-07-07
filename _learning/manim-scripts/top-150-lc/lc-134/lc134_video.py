from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55
NET_Y=2.15; STAT_Y=0.45; CODE_Y=-3.15
READ=0.8; READ_L=1.4

def cell(v,size=0.8,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def pointer(label,color,up=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.12)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.4)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    return VGroup(tri,lab).set_z_index(8)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def statbox(label,val,color):
    lab=Text(label,font=MN,color=GRAY).scale(0.36)
    v=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62)
    col=VGroup(lab,v).arrange(DOWN,buff=0.1)
    box=RoundedRectangle(width=max(col.width+0.8,1.9),height=col.height+0.6,corner_radius=0.14,
                         stroke_color=color,stroke_width=2.6,fill_color=SURFACE,fill_opacity=1.0)
    col.move_to(box.get_center())
    return VGroup(box,col),v


class LC134(Scene):
    def construct(self):
        self.persistent()
        self.problem_scene()
        self.hint_scene()
        self.approach_scene()
        self.walkthrough()
        self.outro()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.4)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.4)
        self.wm=VGroup(axio,byte).arrange(RIGHT,buff=0.02).move_to(UP*WM_Y)
        badge=pill("# 134",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Gas Station",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3)
        if self.hdr.width>6.5: self.hdr.scale(6.5/self.hdr.width)
        self.hdr.move_to(UP*HDR_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.15),run_time=0.5)
        self.play(FadeIn(self.hdr[0],shift=RIGHT*0.2),Write(self.hdr[1]),run_time=0.9)
        self.wait(0.35); self.cap=None

    def set_cap(self,txt,color=WHITE,scale=0.46,rt=0.45):
        new=Text(txt,font=FN,color=color).scale(scale)
        if new.width>6.7: new.scale_to_fit_width(6.7)
        new.move_to(UP*CAP_Y)
        if self.cap is None:
            self.cap=new; self.play(FadeIn(new,shift=UP*0.1),run_time=rt); return
        self.play(FadeOut(self.cap,shift=UP*0.08),run_time=0.22)
        self.play(FadeIn(new,shift=UP*0.08),run_time=0.32); self.cap=new

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("gas[i] = fuel at station i.  cost[i] = fuel to reach i+1.",font=FN,color=WHITE).scale(0.4)
        t2=Text("The road loops. Find a start you can drive the full circle from.",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.85); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        gas=[1,2,3,4,5]; cost=[3,4,5,1,2]
        grow=VGroup(*[cell(v,0.78) for v in gas]).arrange(RIGHT,buff=0.16).move_to(UP*1.25)
        crow=VGroup(*[cell(v,0.78,stroke=BORDER,tcolor=AMBER) for v in cost]).arrange(RIGHT,buff=0.16).move_to(UP*0.15)
        glab=Text("gas",font=MN,weight=BOLD,color=CYAN).scale(0.38).next_to(grow,LEFT,buff=0.26)
        clab=Text("cost",font=MN,weight=BOLD,color=AMBER).scale(0.38).next_to(crow,LEFT,buff=0.26)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(crow[i],DOWN,buff=0.16) for i in range(5)])
        self.play(FadeIn(glab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in grow],lag_ratio=0.08),run_time=0.9)
        self.play(FadeIn(clab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in crow],lag_ratio=0.08),run_time=0.9)
        self.play(FadeIn(idx),run_time=0.4)
        self.wait(0.4)
        arc=CurvedArrow(crow[4].get_bottom()+DOWN*0.05,crow[0].get_bottom()+DOWN*0.05,angle=PI*0.55,color=MINT,stroke_width=4,tip_length=0.18)
        jl=Text("station 4 wraps back to 0",font=MN,color=MINT).scale(0.34).next_to(arc,DOWN,buff=0.06)
        self.play(Create(arc),FadeIn(jl),run_time=0.7)
        self.wait(0.5)
        q=Text("return the start index, or -1 if impossible",font=MN,weight=BOLD,color=AMBER).scale(0.38).move_to(UP*-2.35)
        if q.width>6.7: q.scale_to_fit_width(6.7)
        self.play(FadeIn(q,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,t2,grow,crow,glab,clab,idx,arc,jl,q)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("First, is it even possible?",font=FN,weight=BOLD,color=WHITE).scale(0.5)
        h2=Text("If total gas < total cost → return -1.",font=FN,color=WHITE).scale(0.44)
        h3=Text("If the tank runs dry at i, no start before i works.",font=FN,color=CYAN).scale(0.44)
        h4=Text("So jump the start to i + 1 and keep going.",font=FN,color=MINT).scale(0.44)
        for h in (h1,h2,h3,h4):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.1); h2.next_to(h1,DOWN,buff=0.24); h3.next_to(h2,DOWN,buff=0.34); h4.next_to(h3,DOWN,buff=0.24)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.35)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h4,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Greedy: one pass",font=FN,weight=BOLD,color=WHITE).scale(0.54).move_to(UP*2.35)
        a1=Text("total = running sum of gas[i] - cost[i]",font=MN,color=WHITE).scale(0.38).move_to(UP*1.5)
        a2=Text("tank = fuel since the current start",font=MN,color=CYAN).scale(0.38).move_to(UP*0.85)
        a3=Text("tank < 0  →  start = i + 1,  tank = 0",font=MN,color=MINT).scale(0.38).move_to(UP*0.2)
        a4=Text("total < 0  →  -1,   else  →  start",font=MN,color=AMBER).scale(0.38).move_to(UP*-0.45)
        for g in (a1,a2,a3,a4):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.42); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        gas=[1,2,3,4,5]; cost=[3,4,5,1,2]; net=[g-c for g,c in zip(gas,cost)]; n=5
        self.cells=[cell(v,0.8,tcolor=(MINT if v>=0 else AMBER)) for v in net]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.16).move_to(UP*NET_Y)
        nlab=Text("gas-cost",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(row,LEFT,buff=0.24)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.34).next_to(self.cells[i],DOWN,buff=0.18) for i in range(n)])

        raw=[(0,"int total=0, tank=0, start=0;"),
             (0,"for (int i = 0; i < n; i++) {"),
             (1,"int d = gas[i] - cost[i];"),
             (1,"total += d;  tank += d;"),
             (1,"if (tank < 0) { start=i+1; tank=0; }"),
             (0,"}"),
             (0,"return total < 0 ? -1 : start;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.35))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>6.0: code.scale(6.0/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in self.cells],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(idx),run_time=0.4)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.85)

        self.tgrp,self.tval=statbox("tank",0,CYAN)
        self.sgrp,self.sval=statbox("start",0,MINT)
        self.togrp,self.toval=statbox("total",0,AMBER)
        stats=VGroup(self.togrp,self.tgrp,self.sgrp).arrange(RIGHT,buff=0.4).move_to(UP*STAT_Y)
        if stats.width>7.0: stats.scale(7.0/stats.width)
        self.play(FadeIn(stats,shift=UP*0.1),run_time=0.5)

        self.pi=pointer("i",CYAN,up=True).next_to(self.cells[0],UP,buff=0.12)
        self.ps=pointer("start",MINT,up=False).next_to(self.cells[0],DOWN,buff=0.62)
        self.play(FadeIn(self.pi,shift=DOWN*0.15),FadeIn(self.ps,shift=UP*0.15),run_time=0.5)
        self.set_cap("total, tank, start all begin at 0"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_i(i): return self.pi.animate.next_to(self.cells[i],UP,buff=0.12)
        def move_start(i): return self.ps.animate.next_to(self.cells[i],DOWN,buff=0.62)
        def set_val(ref,val,color):
            new=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62).move_to(ref)
            return Transform(ref,new)

        total=0; tank=0; start=0
        # walk i = 0..4
        anim_notes=[
            ("i = 0:  d = -2   tank → -2  <0", RED),
            ("i = 1:  d = -2   tank → -2  <0", RED),
            ("i = 2:  d = -2   tank → -2  <0", RED),
            ("i = 3:  d = +3   tank → 3   ✓", MINT),
            ("i = 4:  d = +3   tank → 6   ✓", MINT),
        ]
        for i in range(n):
            d=net[i]; total+=d; tank+=d
            note,c=anim_notes[i]
            self.set_cap(note,color=c)
            self.play(*hl([2,3]),move_i(i),self.cells[i][0].animate.set_stroke(c,4.6),run_time=0.5)
            self.play(set_val(self.toval,total,AMBER),set_val(self.tval,tank,(RED if tank<0 else CYAN)),run_time=0.45)
            self.wait(0.25)
            if tank<0:
                start=i+1; tank=0
                self.set_cap("tank dry → nowhere so far works. start = %d" % start,color=AMBER)
                self.play(*hl([4]),move_start(start if start<n else n-1),run_time=0.5)
                self.play(set_val(self.tval,0,CYAN),set_val(self.sval,start,MINT),run_time=0.4)
                self.wait(0.3)
            self.play(self.cells[i][0].animate.set_stroke(BORDER,3.0),run_time=0.3)
        self.wait(0.3)
        self.start_final=start

    def outro(self):
        self.play(FadeOut(self.pi),*[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.4)
        # highlight the winning suffix 3..4
        self.set_cap("total = 0  ≥ 0  →  a valid start exists",color=MINT)
        self.play(self.cells[3][0].animate.set_stroke(MINT,4.6).set_fill(MINT_BG,1.0),
                  self.cells[4][0].animate.set_stroke(MINT,4.6).set_fill(MINT_BG,1.0),run_time=0.55)
        self.wait(READ_L)
        ans=pill("answer  →  start = 3",MINT,MINT_BG,MINT,s=0.5,h=0.72).move_to(UP*STAT_Y)
        self.play(FadeOut(self.tgrp),FadeOut(self.sgrp),FadeOut(self.togrp),FadeIn(ans,scale=1.05),run_time=0.5)
        self.set_cap("start at 3: fuel never dips below zero all the way round",color=MINT); self.wait(READ_L)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.55)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge=VGroup(cbox,comp).move_to(self.panel.get_center())
        self.play(FadeOut(self.panel),FadeOut(VGroup(*self.code)),run_time=0.35)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.45); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("14 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
        head=Text("LeetCode Top Interview 150",font=FN,weight=BOLD,color=WHITE).scale(0.58)
        if head.width>6.6: head.scale_to_fit_width(6.6)
        head.move_to(UP*1.2)
        sub=Text("every problem, visually explained",font=FN,color=GRAY).scale(0.46).move_to(UP*0.5)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*-0.15+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*-0.15+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center()); cta=VGroup(ctabox,ctatxt).move_to(UP*-1.05)
        nxt=VGroup(Text("↓",font=FN,weight=BOLD,color=AMBER).scale(0.55),
                   Text("comment the next problem",font=FN,color=WHITE).scale(0.46)).arrange(RIGHT,buff=0.2).move_to(UP*-2.35)
        self.play(FadeIn(wm,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(part,shift=UP*0.1),run_time=0.35)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
