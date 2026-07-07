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
BASE=-1.05; SCALE=0.47; BW=0.66; PITCH=0.95; X0=-1.9
CODE_Y=-2.75
READ=0.8; READ_L=1.4

def barx(i): return X0+i*PITCH

def acell(v,size=0.78,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=3.0,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center())
    return VGroup(r,t)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC274(Scene):
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
        badge=pill("# 274",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("H-Index",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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
        t1=Text("h-index = h  means:  h papers each cited \u2265 h times.",font=FN,color=WHITE).scale(0.42)
        t2=Text("(and it's the LARGEST such h.)",font=FN,color=GRAY).scale(0.4)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.4); t2.next_to(t1,DOWN,buff=0.2)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        vals=[3,0,6,1,5]
        row=VGroup(*[acell(v) for v in vals]).arrange(RIGHT,buff=0.16).move_to(UP*0.75)
        nlab=Text("citations",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(row,UP,buff=0.22)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=0.9)
        self.wait(0.4)
        q=Text("5 papers \u2014 what's the h-index?",font=FN,color=AMBER).scale(0.44).move_to(UP*-0.6)
        self.play(FadeIn(q,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L)
        self.play(FadeOut(VGroup(lbl,t1,t2,row,nlab,q)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The intuition",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        h1=Text("Sort the papers by citations \u2014 highest first.",font=FN,weight=BOLD,color=WHITE).scale(0.44)
        h2=Text("At rank i, you already have i papers this cited or more.",font=FN,color=WHITE).scale(0.42)
        h3=Text("So if paper i still has \u2265 i citations \u2192 the h-index is \u2265 i.",font=FN,color=CYAN).scale(0.42)
        h4=Text("Take the largest rank where that holds.",font=FN,color=MINT).scale(0.42)
        for h in (h1,h2,h3,h4):
            if h.width>6.9: h.scale_to_fit_width(6.9)
        h1.move_to(UP*2.0); h2.next_to(h1,DOWN,buff=0.28); h3.next_to(h2,DOWN,buff=0.28); h4.next_to(h3,DOWN,buff=0.28)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.2)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.45); self.wait(0.2)
        self.play(FadeIn(h4,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        a0=Text("Sort descending, then find the crossing",font=FN,weight=BOLD,color=WHITE).scale(0.46).move_to(UP*2.2)
        if a0.width>6.9: a0.scale_to_fit_width(6.9)
        a1=Text("walk down the sorted list",font=FN,color=WHITE).scale(0.44).move_to(UP*1.3)
        a2=Text("count papers with  citations \u2265 rank",font=MN,weight=BOLD,color=CYAN).scale(0.42).move_to(UP*0.6)
        a3=Text("that count is the h-index",font=FN,color=MINT).scale(0.44).move_to(UP*-0.05)
        for g in (a2,):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.45); self.wait(0.25)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def make_bar(self,i,cit,fill=SURFACE,stroke=BORDER):
        h=max(cit*SCALE,0.05)
        r=Rectangle(width=BW,height=h,fill_color=fill,fill_opacity=1.0,stroke_color=stroke,stroke_width=2.8).set_z_index(2)
        r.move_to([barx(i),BASE+h/2,0])
        lab=Text(str(cit),font=FN,weight=BOLD,color=WHITE).scale(0.4).next_to(r,UP,buff=0.08).set_z_index(3)
        return VGroup(r,lab)

    def walkthrough(self):
        cits=[6,5,3,1,0]; n=5
        self.bars=[self.make_bar(i,c) for i,c in enumerate(cits)]
        ranks=VGroup(*[Text(str(i+1),font=MN,color=GRAY).scale(0.4).move_to([barx(i),BASE-0.4,0]) for i in range(n)])
        baseline=Line([X0-0.55,BASE,0],[barx(n-1)+0.55,BASE,0],color=BORDER,stroke_width=2.5)
        rlab=Text("rank",font=MN,color=GRAY).scale(0.34).next_to(ranks,DOWN,buff=0.12)
        srt=Text("sorted  \u2193  most-cited first",font=MN,weight=BOLD,color=WHITE).scale(0.34).move_to(UP*2.75)
        # diagonal citations = rank line
        diag=DashedLine([X0-PITCH*0.5,BASE+SCALE*0.5,0],[X0+PITCH*4.5,BASE+SCALE*5.5,0],color=AMBER,stroke_width=3.2,dash_length=0.14).set_z_index(1)
        dlab=Text("citations = rank",font=MN,weight=BOLD,color=AMBER).scale(0.34)
        dlab.move_to([barx(4)+0.1,BASE+SCALE*5.5+0.05,0]).shift(LEFT*0.9+UP*0.05)
        # h counter
        hbx=RoundedRectangle(width=1.5,height=0.8,corner_radius=0.13,stroke_color=MINT,stroke_width=3.0,fill_color=SURFACE,fill_opacity=1.0)
        hvl=Text("0",font=FN,weight=BOLD,color=MINT).scale(0.54).move_to(hbx.get_center())
        hlb=Text("h",font=MN,color=GRAY).scale(0.34).next_to(hbx,UP,buff=0.08)
        htr=VGroup(hlb,hbx,hvl).move_to([2.95,1.7,0])
        self.hbx=hbx; self.hvl=hvl

        raw=[(0,"sort(cit.rbegin(), cit.rend());"),
             (0,"int h = 0;"),
             (0,"while (h < n && cit[h] > h)"),
             (1,"h++;"),
             (0,"return h;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.36))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.14)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>5.6: code.scale(5.6/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(srt),Create(baseline),FadeIn(ranks),FadeIn(rlab),run_time=0.6)
        self.play(LaggedStart(*[GrowFromEdge(b[0],DOWN) for b in self.bars],lag_ratio=0.12),
                  LaggedStart(*[FadeIn(b[1]) for b in self.bars],lag_ratio=0.12),run_time=1.0)
        self.play(FadeIn(htr,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(panel),run_time=0.3)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.7)
        self.play(Create(diag),FadeIn(dlab),run_time=0.6)
        self.set_cap("a paper counts if its bar reaches the line"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def seth(v):
            new=Text(str(v),font=FN,weight=BOLD,color=MINT).scale(0.54).move_to(self.hbx.get_center())
            self.play(FadeOut(self.hvl,scale=0.4),FadeIn(new,scale=1.2),run_time=0.35); self.hvl=new

        cits=[6,5,3,1,0]
        # qualify steps
        for i in range(3):
            self.set_cap(f"rank {i+1}:  {cits[i]} \u2265 {i+1}   \u2713",color=MINT)
            self.play(*hl([2,3]),self.bars[i][0].animate.set_fill(MINT_BG,1.0).set_stroke(MINT,3.6),
                      self.bars[i][1].animate.set_color(MINT),run_time=0.5)
            seth(i+1); self.wait(0.3)
        # fail step
        self.set_cap(f"rank 4:  {cits[3]} \u2265 4 ?  no   \u2192  stop",color=RED)
        self.play(*hl([2]),self.bars[3][0].animate.set_fill(RED_BG,1.0).set_stroke(RED,3.6),
                  self.bars[3][1].animate.set_color(RED),run_time=0.55)
        self.wait(READ_L)
        # h x h square
        self.set_cap("3 papers, each cited \u2265 3 times  \u2192  h = 3",color=MINT)
        sq=Rectangle(width=barx(2)+BW/2-(barx(0)-BW/2),height=3*SCALE,
                     fill_color=MINT,fill_opacity=0.16,stroke_color=MINT,stroke_width=3.0)
        sq.move_to([(barx(0)-BW/2+barx(2)+BW/2)/2,BASE+3*SCALE/2,0]).set_z_index(4)
        sqlab=Text("h \u00d7 h = 3 \u00d7 3",font=MN,weight=BOLD,color=MINT).scale(0.36).move_to(sq.get_center()).set_z_index(6)
        self.play(*hl([4]),FadeIn(sq),self.hbx.animate.set_stroke(MINT,4.2),run_time=0.5)
        self.play(FadeIn(sqlab),run_time=0.4)
        self.wait(READ_L)
        self._sq=VGroup(sq,sqlab); self._extras=VGroup(srt,baseline,ranks,rlab,diag,dlab,htr)

    def outro(self):
        self.play(FadeOut(self._sq),FadeOut(self._extras),FadeOut(self.hvl),
                  *[FadeOut(b) for b in self.bars],
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.5)
        self.set_cap("sort, then find where citations meet rank",color=MINT); self.wait(READ)
        comp=VGroup(Text("Time  O(n log n)",font=MN,weight=BOLD,color=CYAN).scale(0.46),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.46)).arrange(RIGHT,buff=0.45)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge=VGroup(cbox,comp).move_to(UP*0.6)
        note=Text("O(n) with counting sort",font=MN,color=GRAY).scale(0.36).next_to(badge,DOWN,buff=0.3)
        self.play(FadeOut(self.panel),FadeOut(VGroup(*self.code)),run_time=0.35)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.45)
        self.play(FadeIn(note),run_time=0.4); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("11 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
