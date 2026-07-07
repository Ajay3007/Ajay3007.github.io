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

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=1.9; CODE_Y=-1.75
READ=0.8; READ_L=1.4

def cell(v,size=0.8,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.62*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def pointer(label,color,up=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.12)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.42)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    return VGroup(tri,lab).set_z_index(8)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC189(Scene):
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
        badge=pill("# 189",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Rotate Array",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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
        t1=Text("Rotate the array to the right by k steps — in place.",font=FN,color=WHITE).scale(0.4)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t2=Text("The last k values wrap around to the front.",font=FN,color=GRAY).scale(0.38)
        t1.move_to(UP*2.9); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        invals=[1,2,3,4,5]
        inrow=VGroup()
        for i,v in enumerate(invals):
            if i>=3: inrow.add(cell(v,0.72,CYAN,CYAN_BG,WHITE))
            else: inrow.add(cell(v,0.72,BORDER,SURFACE,WHITE))
        inrow.arrange(RIGHT,buff=0.12).move_to(UP*0.95)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.38).next_to(inrow,LEFT,buff=0.26)
        kchip=pill("k = 2",AMBER,SURFACE,AMBER,s=0.36).next_to(inrow,UP,buff=0.22)
        self.play(FadeIn(kchip),run_time=0.35)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.wait(READ_L)
        arr=Arrow(start=[0,0.2,0],end=[0,-0.4,0],buff=0,color=WHITE,stroke_width=5,max_tip_length_to_length_ratio=0.4).move_to(UP*-0.2)
        self.play(GrowArrow(arr),run_time=0.5)
        outvals=[4,5,1,2,3]
        outrow=VGroup()
        for i,v in enumerate(outvals):
            if i<2: outrow.add(cell(v,0.72,MINT,MINT_BG,MINT))
            else: outrow.add(cell(v,0.72,GRAY,SURFACE,WHITE))
        outrow.arrange(RIGHT,buff=0.12).move_to(UP*-1.4)
        ilab=Text("rotated right by 2",font=MN,color=GRAY).scale(0.34).next_to(outrow,DOWN,buff=0.2)
        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in outrow],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(ilab),run_time=0.45)
        self.wait(READ_L+0.7)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,kchip,arr,outrow,ilab)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Rotating right by k moves",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("the last k values to the front.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h3=Text("Three reversals do exactly that — in place.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.22); h3.next_to(h2,DOWN,buff=0.24)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Three reversals",font=FN,weight=BOLD,color=WHITE).scale(0.56).move_to(UP*2.4)
        a1=Text("1.  reverse the whole array",font=FN,color=WHITE).scale(0.44).move_to(UP*1.5)
        a2=Text("2.  reverse the first k",font=FN,color=CYAN).scale(0.44).move_to(UP*0.85)
        a3=Text("3.  reverse the rest",font=FN,color=AMBER).scale(0.44).move_to(UP*0.2)
        a4=Text("(k %= n first, in case k > n)",font=FN,color=GRAY).scale(0.38).move_to(UP*-0.5)
        grp=VGroup(a1,a2,a3)
        for g in grp:
            if g.width>6.8: g.scale_to_fit_width(6.8)
        VGroup(a1,a2,a3).arrange(DOWN,aligned_edge=LEFT,buff=0.28).move_to(UP*0.85)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=RIGHT*0.1),run_time=0.4)
        self.play(FadeIn(a2,shift=RIGHT*0.1),run_time=0.4)
        self.play(FadeIn(a3,shift=RIGHT*0.1),run_time=0.4)
        self.play(FadeIn(a4),run_time=0.4)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        vals=[1,2,3,4,5]; n=5; k=2
        self.cells=[cell(v,0.8) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.13).move_to(UP*ARR_Y)
        kchip=pill("k = 2",AMBER,SURFACE,AMBER,s=0.34).next_to(row,LEFT,buff=0.26)
        raw=[(0,"k %= n;"),(0,"reverse(nums, 0, n-1);"),(0,"reverse(nums, 0, k-1);"),(0,"reverse(nums, k, n-1);")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.4))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.16)
        if code.width>5.4: code.scale(5.4/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.7,height=code.height+0.55)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(kchip),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.08),run_time=0.8)
        self.L=pointer("L",CYAN,up=False); self.R=pointer("R",AMBER,up=False)
        self.L.next_to(self.cells[0],DOWN,buff=0.12); self.R.next_to(self.cells[4],DOWN,buff=0.12)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def hlc(i): return self.cells[i][0].animate.set_stroke(CYAN,4.6)
        def unhlc(i): return self.cells[i][0].animate.set_stroke(BORDER,3.0)
        def set_LR(l,r,rt=0.4):
            return [self.L.animate.next_to(self.cells[l],DOWN,buff=0.12),
                    self.R.animate.next_to(self.cells[r],DOWN,buff=0.12)]
        def swap(l,r):
            pl=self.cells[l].get_center(); pr=self.cells[r].get_center()
            self.play(self.cells[l].animate(path_arc=-PI/2).move_to(pr),
                      self.cells[r].animate(path_arc=-PI/2).move_to(pl),run_time=0.75)
            self.cells[l],self.cells[r]=self.cells[r],self.cells[l]
        def dim(idxs): return [self.cells[i].animate.set_opacity(0.28) for i in idxs]
        def undim(idxs): return [self.cells[i].animate.set_opacity(1.0) for i in idxs]

        # k %= n
        self.set_cap("k %= n   (in case k is larger than n)")
        self.play(*hl([0]),run_time=0.5); self.wait(READ)

        # Phase 1: reverse whole
        self.set_cap("Step 1:  reverse the whole array")
        self.play(*hl([1]),FadeIn(self.L,shift=UP*0.1),FadeIn(self.R,shift=UP*0.1),run_time=0.5)
        self.wait(0.3)
        self.play(hlc(0),hlc(4),run_time=0.3); swap(0,4)
        self.play(unhlc(0),unhlc(4),*set_LR(1,3),run_time=0.45)
        self.play(hlc(1),hlc(3),run_time=0.3); swap(1,3)
        self.play(unhlc(1),unhlc(3),*set_LR(2,2),run_time=0.45)
        self.wait(0.5)   # [5,4,3,2,1]

        # Phase 2: reverse first k
        self.set_cap("Step 2:  reverse the first k = 2")
        self.play(*hl([2]),*dim([2,3,4]),*set_LR(0,1),run_time=0.5)
        self.wait(0.3)
        self.play(hlc(0),hlc(1),run_time=0.3); swap(0,1)
        self.play(unhlc(0),unhlc(1),run_time=0.35)
        self.play(*undim([2,3,4]),run_time=0.4)
        self.wait(0.4)   # [4,5,3,2,1]

        # Phase 3: reverse the rest
        self.set_cap("Step 3:  reverse the rest (n \u2212 k = 3)")
        self.play(*hl([3]),*dim([0,1]),*set_LR(2,4),run_time=0.5)
        self.wait(0.3)
        self.play(hlc(2),hlc(4),run_time=0.3); swap(2,4)
        self.play(unhlc(2),unhlc(4),*set_LR(3,3),run_time=0.45)
        self.play(*undim([0,1]),run_time=0.4)
        self.wait(0.4)   # [4,5,1,2,3]

        self.set_cap("done  \u2192  rotated right by 2",color=MINT)
        self.play(FadeOut(self.L),FadeOut(self.R),run_time=0.4)
        self.wait(READ_L*0.6)

    def outro(self):
        self.play(*[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.35)
        anims=[]
        for c in self.cells:
            anims += [c[0].animate.set_stroke(MINT,3.6), c[1].animate.set_color(MINT)]
        self.play(LaggedStart(*anims,lag_ratio=0.08),run_time=1.0)
        self.set_cap("[4, 5, 1, 2, 3]  \u2014  rotated in place",color=MINT); self.wait(READ)
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
        part=pill("6 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
