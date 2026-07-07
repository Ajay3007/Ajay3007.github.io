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
RAT_Y=2.3; CAND_Y=1.05; SUM_Y=-0.2; CODE_Y=-3.05
SZ=0.72
READ=0.8; READ_L=1.4

def cell(v,size=SZ,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center()).set_z_index(5)
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


class LC135(Scene):
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
        badge=pill("# 135",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Candy",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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
        t1=Text("Children in a row, each with a rating.",font=FN,color=WHITE).scale(0.44)
        t2=Text("Give the fewest candies so that:",font=FN,color=GRAY).scale(0.4)
        r1=Text("• every child gets at least 1",font=FN,color=WHITE).scale(0.4)
        r2=Text("• a higher rating than a neighbor → more candy",font=FN,color=CYAN).scale(0.4)
        for t in (t1,t2,r1,r2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.75); t2.next_to(t1,DOWN,buff=0.2)
        r1.next_to(t2,DOWN,buff=0.28); r2.next_to(r1,DOWN,buff=0.2)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.4)
        self.play(FadeIn(r1,shift=RIGHT*0.1),run_time=0.4); self.play(FadeIn(r2,shift=RIGHT*0.1),run_time=0.45)
        self.wait(READ_L)
        vals=[2,3,4,3,2,1]
        row=VGroup(*[cell(v) for v in vals]).arrange(RIGHT,buff=0.16).move_to(UP*-1.3)
        rlab=Text("ratings",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(row,LEFT,buff=0.22)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).next_to(row[i],DOWN,buff=0.16) for i in range(len(vals))])
        self.play(FadeIn(rlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.09),run_time=1.0)
        self.play(FadeIn(idx),run_time=0.4)
        peak=Text("index 2 is a peak — it must beat both sides",font=MN,color=AMBER).scale(0.34).next_to(idx,DOWN,buff=0.35)
        if peak.width>6.7: peak.scale_to_fit_width(6.7)
        self.play(row[2][0].animate.set_stroke(AMBER,4.4),FadeIn(peak,shift=UP*0.1),run_time=0.6)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,t2,r1,r2,row,rlab,idx,peak)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("One scan can't satisfy both neighbors.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("So do two greedy passes:",font=FN,color=WHITE).scale(0.44)
        h3=Text("left → right fixes the up-slopes,",font=FN,color=CYAN).scale(0.44)
        h4=Text("right → left fixes the down-slopes.",font=FN,color=MINT).scale(0.44)
        h5=Text("At each child, keep the larger of the two.",font=FN,color=AMBER).scale(0.44)
        for h in (h1,h2,h3,h4,h5):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.2); h2.next_to(h1,DOWN,buff=0.3)
        h3.next_to(h2,DOWN,buff=0.26); h4.next_to(h3,DOWN,buff=0.2); h5.next_to(h4,DOWN,buff=0.3)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.42); self.play(FadeIn(h4,shift=UP*0.1),run_time=0.42)
        self.wait(0.2); self.play(FadeIn(h5,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4,h5)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Two passes, then sum",font=FN,weight=BOLD,color=WHITE).scale(0.54).move_to(UP*2.35)
        a1=Text("candy[i] = 1 for everyone",font=MN,color=WHITE).scale(0.4).move_to(UP*1.5)
        a2=Text("L→R:  r[i] > r[i-1]  ⇒  candy[i] = candy[i-1] + 1",font=MN,color=CYAN).scale(0.36).move_to(UP*0.8)
        a3=Text("R→L:  r[i] > r[i+1]  ⇒  candy[i] = max(candy[i], candy[i+1]+1)",font=MN,color=MINT).scale(0.34).move_to(UP*0.1)
        a4=Text("answer = sum(candy)",font=MN,color=AMBER).scale(0.4).move_to(UP*-0.6)
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

    def bump(self,i,val,color=MINT,override=False):
        tgt=self.cands[i]
        new=Text(str(val),font=FN,weight=BOLD,color=WHITE).scale(0.58*SZ).move_to(tgt[1])
        fill=AMBER_BG if override else MINT_BG
        edge=AMBER if override else color
        self.play(Transform(tgt[1],new),tgt[0].animate.set_stroke(edge,4.8).set_fill(fill,1.0),run_time=0.45)
        self.play(tgt[0].animate.set_stroke(BORDER,3.0).set_fill(SURFACE,1.0),run_time=0.25)

    def walkthrough(self):
        r=[2,3,4,3,2,1]; n=6; c=[1]*n
        self.rats=[cell(v) for v in r]
        rrow=VGroup(*self.rats).arrange(RIGHT,buff=0.16).move_to(UP*RAT_Y)
        rlab=Text("ratings",font=MN,weight=BOLD,color=WHITE).scale(0.32).next_to(rrow,LEFT,buff=0.2)
        self.cands=[cell(1,tcolor=MINT) for _ in range(n)]
        crow=VGroup(*self.cands).arrange(RIGHT,buff=0.16)
        crow.move_to([rrow.get_center()[0],CAND_Y,0])
        clab=Text("candy",font=MN,weight=BOLD,color=MINT).scale(0.32).next_to(crow,LEFT,buff=0.2)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.3).next_to(self.cands[i],DOWN,buff=0.14) for i in range(n)])

        raw=[(0,"vector<int> c(n, 1);"),
             (0,"for (int i = 1; i < n; i++)"),
             (1,"if (r[i] > r[i-1]) c[i] = c[i-1] + 1;"),
             (0,"for (int i = n-2; i >= 0; i--)"),
             (1,"if (r[i] > r[i+1]) c[i] = max(c[i], c[i+1]+1);"),
             (0,"return accumulate(c, 0);")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.32))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>6.4: code.scale(6.4/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(rlab),LaggedStart(*[FadeIn(x,shift=UP*0.1) for x in self.rats],lag_ratio=0.08),run_time=0.9)
        self.play(FadeIn(clab),LaggedStart(*[FadeIn(x,shift=UP*0.1) for x in self.cands],lag_ratio=0.08),FadeIn(idx),run_time=0.9)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.8)
        self.set_cap("everyone starts with 1 candy"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a

        # scanning pointer above ratings
        self.pi=pointer("i",CYAN,up=True).next_to(self.rats[1],UP,buff=0.12)
        # ---------- Pass 1: left -> right ----------
        p1=pill("① left → right",CYAN,CYAN_BG,CYAN,s=0.4).move_to(UP*SUM_Y)
        self.play(FadeIn(self.pi,shift=DOWN*0.15),FadeIn(p1,shift=UP*0.1),*hl([1,2]),run_time=0.55)
        for i in range(1,n):
            self.play(self.pi.animate.next_to(self.rats[i],UP,buff=0.12),
                      self.rats[i][0].animate.set_stroke(CYAN,4.4),
                      self.rats[i-1][0].animate.set_stroke(GRAY,3.4),run_time=0.4)
            if r[i]>r[i-1]:
                c[i]=c[i-1]+1
                self.set_cap("r[%d]>r[%d]  ✓  candy = %d" % (i,i-1,c[i]),color=CYAN,scale=0.44)
                self.bump(i,c[i],color=CYAN)
            else:
                self.set_cap("r[%d] ≤ r[%d]  —  leave at 1" % (i,i-1),color=GRAY,scale=0.44)
                self.wait(0.25)
            self.play(self.rats[i][0].animate.set_stroke(BORDER,3.0),
                      self.rats[i-1][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        self.set_cap("left pass done — up-slopes are correct",color=CYAN); self.wait(READ)

        # ---------- Pass 2: right -> left ----------
        p2=pill("② right → left",MINT,MINT_BG,MINT,s=0.4).move_to(UP*SUM_Y)
        self.play(Transform(p1,p2),self.pi.animate.next_to(self.rats[n-2],UP,buff=0.12),*hl([3,4]),run_time=0.5)
        for i in range(n-2,-1,-1):
            self.play(self.pi.animate.next_to(self.rats[i],UP,buff=0.12),
                      self.rats[i][0].animate.set_stroke(MINT,4.4),
                      self.rats[i+1][0].animate.set_stroke(GRAY,3.4),run_time=0.4)
            if r[i]>r[i+1]:
                want=c[i+1]+1
                if want>c[i]:
                    over=(i==2)
                    c[i]=want
                    if over:
                        self.set_cap("r[2]>r[3] and the drop is long → max bumps it to %d" % c[i],color=AMBER,scale=0.42)
                    else:
                        self.set_cap("r[%d]>r[%d]  ✓  candy = %d" % (i,i+1,c[i]),color=MINT,scale=0.44)
                    self.bump(i,c[i],color=MINT,override=over)
                else:
                    self.set_cap("r[%d]>r[%d] but %d already ≥ %d — keep it" % (i,i+1,c[i],want),color=GRAY,scale=0.4)
                    self.wait(0.3)
            else:
                self.set_cap("r[%d] ≤ r[%d]  —  no change" % (i,i+1),color=GRAY,scale=0.44)
                self.wait(0.25)
            self.play(self.rats[i][0].animate.set_stroke(BORDER,3.0),
                      self.rats[i+1][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
        self.final_c=c
        self.play(FadeOut(self.pi),FadeOut(p1),run_time=0.35)

    def outro(self):
        c=self.final_c; total=sum(c)
        self.play(*[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.3)
        self.set_cap("add them up  →  the minimum total",color=MINT)
        expr=Text("  +  ".join(str(x) for x in c),font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(UP*SUM_Y)
        if expr.width>6.8: expr.scale_to_fit_width(6.8)
        self.play(FadeIn(expr,shift=UP*0.1),run_time=0.5); self.wait(READ)
        ans=pill("minimum candies  =  %d" % total,MINT,MINT_BG,MINT,s=0.5,h=0.72).move_to(UP*SUM_Y)
        self.play(Transform(expr,ans),run_time=0.5); self.wait(READ_L)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(n)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.55)
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
        part=pill("15 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
