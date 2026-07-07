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

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=1.75; IDX_Y=1.2; BAR_Y=0.7; TRK_Y=-0.4; CODE_Y=-2.35
READ=0.8; READ_L=1.4

def cell(v,size=0.8,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def pointer(label,color,up=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.11)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.36)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    return VGroup(tri,lab).set_z_index(8)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC45(Scene):
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
        badge=pill("# 45",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Jump Game II",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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
        t1=Text("nums[i] = max jump from i.  You CAN always reach the end.",font=FN,color=WHITE).scale(0.38)
        t2=Text("Return the FEWEST jumps to get there.",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.9); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        vals=[2,3,1,1,4]
        inrow=VGroup(*[cell(v,0.8) for v in vals]).arrange(RIGHT,buff=0.16).move_to(UP*0.9)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.38).next_to(inrow,LEFT,buff=0.26)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(inrow[i],DOWN,buff=0.16) for i in range(len(vals))])
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(idx),run_time=0.4)
        self.wait(0.4)
        a1=CurvedArrow(inrow[0].get_top()+UP*0.03,inrow[1].get_top()+UP*0.03,angle=-PI*0.6,color=MINT,stroke_width=4,tip_length=0.16)
        a2=CurvedArrow(inrow[1].get_top()+UP*0.03,inrow[4].get_top()+UP*0.03,angle=-PI*0.5,color=MINT,stroke_width=4,tip_length=0.16)
        self.play(Create(a1),run_time=0.5); self.play(Create(a2),run_time=0.5)
        concl=Text("0 \u2192 1 \u2192 4   =   2 jumps",font=MN,weight=BOLD,color=MINT).scale(0.44).move_to(UP*-1.5)
        self.play(FadeIn(concl,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,idx,a1,a2,concl)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Think in levels, like ripples.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("1 jump reaches a range of indices.",font=FN,color=WHITE).scale(0.44)
        h3=Text("2 jumps reach everything the 1st range can.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.24); h3.next_to(h2,DOWN,buff=0.24)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Greedy: expand the frontier",font=FN,weight=BOLD,color=WHITE).scale(0.5).move_to(UP*2.35)
        a1=VGroup(Text("farthest",font=MN,weight=BOLD,color=CYAN).scale(0.44),
                  Text("= how far the NEXT jump can go",font=FN,color=WHITE).scale(0.4)).arrange(RIGHT,buff=0.25).move_to(UP*1.45)
        a2=VGroup(Text("curEnd",font=MN,weight=BOLD,color=AMBER).scale(0.44),
                  Text("= boundary of THIS jump",font=FN,color=WHITE).scale(0.4)).arrange(RIGHT,buff=0.25).move_to(UP*0.7)
        a3=Text("reach the boundary  \u2192  spend a jump",font=FN,color=MINT).scale(0.42).move_to(UP*-0.05)
        for g in (a1,a2,a3):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.45); self.wait(0.25)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def make_bar(self,r):
        left=self.cells[0].get_left()[0]; right=self.cells[r].get_right()[0]
        w=max(right-left,0.2)
        bar=RoundedRectangle(width=w,height=0.2,corner_radius=0.1,stroke_width=0,fill_color=CYAN,fill_opacity=0.85).set_z_index(0)
        bar.move_to([(left+right)/2,BAR_Y,0]); return bar

    def walkthrough(self):
        vals=[2,3,1,1,4]; n=5
        self.cells=[cell(v,0.8) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.16).move_to(UP*ARR_Y)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(row,LEFT,buff=0.22)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(self.cells[i],DOWN,buff=0.16) for i in range(n)])
        rlab=Text("reach",font=MN,weight=BOLD,color=CYAN).scale(0.32)
        rlab.move_to([nlab.get_center()[0],BAR_Y,0])
        # jumps tracker
        jbx=RoundedRectangle(width=1.7,height=0.85,corner_radius=0.13,stroke_color=MINT,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        jvl=Text("0",font=FN,weight=BOLD,color=MINT).scale(0.56).move_to(jbx.get_center())
        jlb=Text("jumps",font=MN,color=GRAY).scale(0.32).next_to(jbx,UP,buff=0.1)
        jtr=VGroup(jlb,jbx,jvl).move_to(UP*TRK_Y)
        self.jbx=jbx; self.jvl=jvl

        raw=[(0,"int jumps=0, curEnd=0, farthest=0;"),
             (0,"for (int i=0; i < n-1; i++) {"),
             (1,"farthest = max(farthest, i+nums[i]);"),
             (1,"if (i == curEnd) { jumps++; curEnd=farthest; }"),
             (0,"}"),
             (0,"return jumps;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.34))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>5.8: code.scale(5.8/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.55,height=code.height+0.4)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in self.cells],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(idx),FadeIn(jtr,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.8)
        self.bar=self.make_bar(0)
        self.pce=pointer("curEnd",AMBER,up=True); self.pce.next_to(self.cells[0],UP,buff=0.1).shift(UP*0.02)
        self.pi=pointer("i",CYAN,up=True).next_to(self.cells[0],UP,buff=0.62)
        self.play(FadeIn(rlab),FadeIn(self.bar),FadeIn(self.pce,shift=DOWN*0.1),run_time=0.5)
        self.play(FadeIn(self.pi,shift=DOWN*0.1),run_time=0.4)
        self.set_cap("farthest & curEnd start at 0"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_i(i): return self.pi.animate.next_to(self.cells[i],UP,buff=0.62)
        def move_ce(i): return self.pce.animate.next_to(self.cells[i],UP,buff=0.1).shift(UP*0.02)
        def extend(r): self.play(Transform(self.bar,self.make_bar(r)),run_time=0.55)
        def set_jumps(v):
            new=Text(str(v),font=FN,weight=BOLD,color=MINT).scale(0.56).move_to(self.jbx.get_center())
            self.play(FadeOut(self.jvl,scale=0.4),FadeIn(new,scale=1.2),run_time=0.35); self.jvl=new

        far=0; curEnd=0
        # i=0
        self.set_cap("i = 0:  farthest = 0 + 2 = 2")
        self.play(*hl([2]),self.cells[0][0].animate.set_stroke(CYAN,4.5),run_time=0.5)
        far=2; extend(far); self.play(self.cells[0][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        self.set_cap("i = curEnd  \u2192  jump!  (curEnd \u2192 2)",color=AMBER)
        self.play(*hl([3]),run_time=0.4); set_jumps(1); curEnd=2
        self.play(move_ce(2),run_time=0.5)
        self.play(move_i(1),*hl([1]),run_time=0.5); self.wait(0.3)
        # i=1
        self.set_cap("i = 1:  farthest = max(2, 1+3) = 4")
        self.play(*hl([2]),self.cells[1][0].animate.set_stroke(CYAN,4.5),run_time=0.5)
        far=4; extend(far); self.play(self.cells[1][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        self.set_cap("i \u2260 curEnd (2)  \u2192  keep going",color=GRAY)
        self.play(*hl([3]),run_time=0.35)
        self.play(move_i(2),*hl([1]),run_time=0.5); self.wait(0.3)
        # i=2
        self.set_cap("i = 2:  farthest = max(4, 2+1) = 4")
        self.play(*hl([2]),self.cells[2][0].animate.set_stroke(CYAN,4.5),run_time=0.5)
        self.play(self.cells[2][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        self.set_cap("i = curEnd  \u2192  jump!  (curEnd \u2192 4)",color=AMBER)
        self.play(*hl([3]),run_time=0.4); set_jumps(2); curEnd=4
        self.play(move_ce(4),run_time=0.5); self.wait(0.2)
        self.play(move_i(3),*hl([1]),run_time=0.5); self.wait(0.3)
        # i=3 (last iteration, no jump)
        self.set_cap("i = 3:  i \u2260 curEnd (4)  \u2192  no jump")
        self.play(*hl([2,3]),self.cells[3][0].animate.set_stroke(CYAN,4.5),run_time=0.5); self.wait(0.3)
        self.play(self.cells[3][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        # end
        self.set_cap("curEnd reached the end  \u2192  2 jumps",color=MINT)
        self.play(*hl([5]),self.jbx.animate.set_stroke(MINT,4.2),
                  self.cells[4][0].animate.set_stroke(MINT,4),run_time=0.5)
        self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.pi),FadeOut(self.pce),FadeOut(self.bar),
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.45)
        self.set_cap("each level = one jump  \u2192  fewest = 2",color=MINT); self.wait(READ)
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
        part=pill("10 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
