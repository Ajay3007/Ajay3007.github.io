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

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=2.15; TRK_Y=0.55; CODE_Y=-2.05
READ=0.8; READ_L=1.4

def cell(v,size=0.85,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def pointer(label,color,up=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.12)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.42)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    return VGroup(tri,lab).set_z_index(8)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,
                         stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC169(Scene):
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
        badge=pill("# 169",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Majority Element",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3)
        if self.hdr.width>6.5: self.hdr.scale(6.5/self.hdr.width)
        self.hdr.move_to(UP*HDR_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.15),run_time=0.5)
        self.play(FadeIn(self.hdr[0],shift=RIGHT*0.2),Write(self.hdr[1]),run_time=0.9)
        self.wait(0.35); self.cap=None

    def set_cap(self,txt,color=WHITE,scale=0.48,rt=0.45):
        new=Text(txt,font=FN,color=color).scale(scale)
        if new.width>6.6: new.scale_to_fit_width(6.6)
        new.move_to(UP*CAP_Y)
        if self.cap is None:
            self.cap=new; self.play(FadeIn(new,shift=UP*0.1),run_time=rt); return
        self.play(FadeOut(self.cap,shift=UP*0.08),run_time=0.22)
        self.play(FadeIn(new,shift=UP*0.08),run_time=0.32); self.cap=new

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Return the value that appears more than n / 2 times —",font=FN,color=WHITE).scale(0.4)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t2=Text("the majority element (it always exists).",font=FN,color=GRAY).scale(0.38)
        t1.move_to(UP*2.9); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        cols=[(2,MINT,MINT_BG),(2,MINT,MINT_BG),(1,GRAY,SURFACE),(1,GRAY,SURFACE),(2,MINT,MINT_BG)]
        inrow=VGroup(*[cell(v,0.78,st,fl,WHITE) for v,st,fl in cols]).arrange(RIGHT,buff=0.13).move_to(UP*1.05)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.38).next_to(inrow,LEFT,buff=0.28)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.wait(0.5)
        tally=Text("2 appears 3 times   \u00b7   1 appears 2 times",font=MN,color=WHITE).scale(0.38)
        if tally.width>6.7: tally.scale_to_fit_width(6.7)
        tally.move_to(UP*-0.3)
        concl=Text("3  >  5 / 2      \u2192      majority = 2",font=MN,weight=BOLD,color=MINT).scale(0.42).move_to(UP*-1.35)
        self.play(FadeIn(tally),run_time=0.5); self.wait(0.6)
        self.play(FadeIn(concl,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.6)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,tally,concl)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Counting with a hash map costs O(n) space.",font=FN,color=WHITE).scale(0.44)
        h2=Text("Smarter: pair up different values and cancel them.",font=FN,color=WHITE).scale(0.44)
        h3=Text("The majority is > half, so it always survives.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.26); h3.next_to(h2,DOWN,buff=0.22)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.5); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.6)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Boyer-Moore Voting",font=FN,weight=BOLD,color=WHITE).scale(0.56).move_to(UP*2.4)
        a1=Text("keep a candidate + a count",font=FN,color=WHITE).scale(0.44).move_to(UP*1.5)
        a2=VGroup(Text("match  \u2192  +1",font=FN,color=MINT).scale(0.44),
                  Text("mismatch  \u2192  \u22121",font=FN,color=RED).scale(0.44)).arrange(RIGHT,buff=0.5).move_to(UP*0.75)
        a3=Text("count hits 0  \u2192  pick a new candidate",font=FN,color=CYAN).scale(0.44).move_to(UP*0.0)
        for g in (a2,a3):
            if g.width>6.8: g.scale_to_fit_width(6.8)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.45); self.wait(0.25)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.6)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def walkthrough(self):
        vals=[2,2,1,1,2]
        self.cells=[cell(v,0.85) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.13).move_to(UP*ARR_Y)
        # trackers
        cbx=RoundedRectangle(width=1.15,height=0.9,corner_radius=0.13,stroke_color=AMBER,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        cvl=Text("?",font=FN,weight=BOLD,color=GRAY).scale(0.6).move_to(cbx.get_center())
        clb=Text("candidate",font=MN,color=GRAY).scale(0.32).next_to(cbx,UP,buff=0.1)
        cand=VGroup(clb,cbx,cvl)
        nbx=RoundedRectangle(width=1.15,height=0.9,corner_radius=0.13,stroke_color=CYAN,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        nvl=Text("0",font=FN,weight=BOLD,color=WHITE).scale(0.6).move_to(nbx.get_center())
        nlb=Text("count",font=MN,color=GRAY).scale(0.32).next_to(nbx,UP,buff=0.1)
        cnt=VGroup(nlb,nbx,nvl)
        trackers=VGroup(cand,cnt).arrange(RIGHT,buff=0.9).move_to(UP*TRK_Y)
        self.cbx=cbx; self.cvl=cvl; self.nbx=nbx; self.nvl=nvl; self.trackers=trackers

        raw=[(0,"int count = 0, cand = 0;"),
             (0,"for (int f = 0; f < n; f++) {"),
             (1,"if (count == 0) cand = nums[f];"),
             (1,"count += (nums[f]==cand) ? 1 : -1;"),
             (0,"}"),
             (0,"return cand;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.37))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.14)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.32)
        if code.width>5.5: code.scale(5.5/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.5)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(trackers,shift=UP*0.1),run_time=0.6)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.07),run_time=0.85)
        self.pf=pointer("f",CYAN,up=True).next_to(self.cells[0],UP,buff=0.12)
        self.play(FadeIn(self.pf,shift=DOWN*0.15),run_time=0.5)
        self.set_cap("candidate = none,   count = 0"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_f(f):
            if f<len(self.cells): return self.pf.animate.next_to(self.cells[f],UP,buff=0.12)
            return self.pf.animate.next_to(self.cells[-1],UP,buff=0.12).shift(RIGHT*0.7)
        def scan(f): return self.cells[f][0].animate.set_stroke(CYAN,4.5)
        def tint(f,ok): return self.cells[f][0].animate.set_stroke(MINT if ok else RED,4.5)
        def unscan(f): return self.cells[f][0].animate.set_stroke(BORDER,3.0)
        def set_cand(v):
            new=Text(str(v),font=FN,weight=BOLD,color=AMBER).scale(0.6).move_to(self.cbx.get_center())
            self.play(FadeOut(self.cvl,scale=0.4),FadeIn(new,scale=1.2),self.cbx.animate.set_stroke(AMBER,4.2),run_time=0.4)
            self.cvl=new
        def bump(n,delta):
            color=MINT if delta>0 else RED
            new=Text(str(n),font=FN,weight=BOLD,color=WHITE).scale(0.6).move_to(self.nbx.get_center())
            vote=Text(("+1" if delta>0 else "\u22121"),font=FN,weight=BOLD,color=color).scale(0.46).next_to(self.nbx,RIGHT,buff=0.12)
            self.add(vote)
            self.play(FadeOut(self.nvl,scale=0.4),FadeIn(new,scale=1.2),vote.animate.shift(UP*0.55).set_opacity(0),run_time=0.42)
            self.nvl=new; self.remove(vote)

        # f=0  count==0 -> cand=2 -> +1
        self.set_cap("count = 0  \u2192  nums[0] becomes the candidate")
        self.play(*hl([1,2]),scan(0),run_time=0.5); self.wait(0.3)
        set_cand(2)
        self.set_cap("2 matches the candidate  \u2192  count + 1",color=MINT)
        self.play(*hl([3]),tint(0,True),run_time=0.4); bump(1,1)
        self.play(unscan(0),move_f(1),*hl([1]),run_time=0.5); self.wait(0.35)
        # f=1  match -> +1
        self.set_cap("nums[1] = 2  matches the candidate")
        self.play(*hl([1,3]),scan(1),run_time=0.5); self.wait(0.3)
        self.set_cap("match  \u2192  count + 1",color=MINT)
        self.play(tint(1,True),run_time=0.35); bump(2,1)
        self.play(unscan(1),move_f(2),*hl([1]),run_time=0.5); self.wait(0.35)
        # f=2  mismatch -> -1
        self.set_cap("nums[2] = 1  \u2260  the candidate")
        self.play(*hl([1,3]),scan(2),run_time=0.5); self.wait(0.3)
        self.set_cap("mismatch  \u2192  count \u2212 1",color=RED)
        self.play(tint(2,False),run_time=0.35); bump(1,-1)
        self.play(unscan(2),move_f(3),*hl([1]),run_time=0.5); self.wait(0.35)
        # f=3  mismatch -> -1 -> 0
        self.set_cap("nums[3] = 1  \u2260  the candidate")
        self.play(*hl([1,3]),scan(3),run_time=0.5); self.wait(0.3)
        self.set_cap("mismatch  \u2192  count \u2212 1  \u2192  0",color=RED)
        self.play(tint(3,False),run_time=0.35); bump(0,-1)
        self.play(unscan(3),move_f(4),*hl([1]),run_time=0.5); self.wait(0.35)
        # f=4  count==0 -> cand=2 -> +1
        self.set_cap("count = 0  \u2192  nums[4] becomes the candidate")
        self.play(*hl([1,2]),scan(4),run_time=0.5); self.wait(0.3)
        set_cand(2)
        self.set_cap("2 matches  \u2192  count + 1",color=MINT)
        self.play(*hl([3]),tint(4,True),run_time=0.4); bump(1,1)
        self.play(unscan(4),move_f(5),*hl([1]),run_time=0.5); self.wait(0.35)
        # end
        self.set_cap("candidate = 2  \u2192  the majority element",color=MINT)
        self.play(*hl([5]),self.cbx.animate.set_stroke(MINT,4.2),self.cvl.animate.set_color(MINT),run_time=0.5)
        self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.pf),FadeOut(self.trackers),FadeOut(self.cvl),FadeOut(self.nvl),
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.5)
        anims=[]
        for i in (0,1,4):
            anims += [self.cells[i][0].animate.set_stroke(MINT,3.6), self.cells[i][1].animate.set_color(MINT)]
        for i in (2,3):
            anims += [self.cells[i][0].animate.set_stroke(GRAY,2.2).set_fill(SURFACE,0.4), self.cells[i][1].animate.set_color(GRAY).set_opacity(0.5)]
        self.play(LaggedStart(*anims,lag_ratio=0.06),run_time=1.0)
        ans=pill("majority = 2",MINT,MINT_BG,MINT,s=0.46,h=0.7).move_to(UP*TRK_Y)
        self.play(FadeIn(ans,scale=1.05),run_time=0.5)
        self.set_cap("2 appears 3 of 5  \u2192  the majority element",color=MINT); self.wait(READ)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.55)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge=VGroup(cbox,comp).move_to(self.panel.get_center())
        self.play(FadeOut(self.panel),FadeOut(VGroup(*self.code)),run_time=0.35)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.45); self.wait(READ_L)
        self.ans=ans

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("5 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
        head=Text("LeetCode Top Interview 150",font=FN,weight=BOLD,color=WHITE).scale(0.58)
        if head.width>6.6: head.scale_to_fit_width(6.6)
        head.move_to(UP*1.2)
        sub=Text("every problem, visually explained",font=FN,color=GRAY).scale(0.46).move_to(UP*0.5)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*-0.15+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*-0.15+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center()); cta=VGroup(ctabox,ctatxt).move_to(UP*-1.05)
        nxt=VGroup(Text("\u2193",font=FN,weight=BOLD,color=AMBER).scale(0.55),
                   Text("comment the next problem",font=FN,color=WHITE).scale(0.46)).arrange(RIGHT,buff=0.2).move_to(UP*-2.35)
        self.play(FadeIn(wm,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(part,shift=UP*0.1),run_time=0.35)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
