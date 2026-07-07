from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=1.9; CODE_Y=-1.5
READ=0.8; READ_L=1.4

def cell(v,size=0.9,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def empty_cell(size=0.9):
    b=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=GRAY,stroke_width=2.2)
    d=DashedVMobject(b,num_dashes=16,dashed_ratio=0.55).set_stroke(GRAY,2.2).set_z_index(1)
    return VGroup(d)

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


class LC26(Scene):
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
        badge=pill("# 26",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Remove Duplicates",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3).move_to(UP*HDR_Y)
        if self.hdr.width>6.5: self.hdr.scale(6.5/self.hdr.width)
        self.hdr.move_to(UP*HDR_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.15),run_time=0.5)
        self.play(FadeIn(self.hdr[0],shift=RIGHT*0.2),Write(self.hdr[1]),run_time=0.9)
        self.wait(0.35)
        self.cap=None

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
        t1=Text("nums is sorted. Remove duplicates in place, so each value appears once.",font=FN,color=WHITE).scale(0.4)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t2=Text("Return k = the number of unique values.",font=FN,color=GRAY).scale(0.38)
        t1.move_to(UP*2.85); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        # input [1,1,2,2,3]: first occurrences cyan, duplicates red
        cols=[(1,CYAN,CYAN_BG),(1,RED,RED_BG),(2,CYAN,CYAN_BG),(2,RED,RED_BG),(3,CYAN,CYAN_BG)]
        inrow=VGroup(*[cell(v,0.72,st,fl,WHITE) for v,st,fl in cols]).arrange(RIGHT,buff=0.12).move_to(UP*0.95)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.38).next_to(inrow,LEFT,buff=0.28)
        dupnote=Text("red = duplicate",font=MN,color=RED).scale(0.32).next_to(inrow,UP,buff=0.2)
        self.play(FadeIn(dupnote),run_time=0.35)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.wait(READ_L)
        arr=Arrow(start=[0,0.2,0],end=[0,-0.4,0],buff=0,color=WHITE,stroke_width=5,max_tip_length_to_length_ratio=0.4).move_to(UP*-0.2)
        self.play(GrowArrow(arr),run_time=0.5)
        outrow=VGroup(cell(1,0.72,MINT,SURFACE,MINT),cell(2,0.72,MINT,SURFACE,MINT),cell(3,0.72,MINT,SURFACE,MINT),
                      empty_cell(0.72),empty_cell(0.72)).arrange(RIGHT,buff=0.12).move_to(UP*-1.4)
        klab=pill("k = 3",MINT,SURFACE,MINT,s=0.36).next_to(outrow,LEFT,buff=0.28)
        ilab=Text("rest is ignored",font=MN,color=GRAY).scale(0.34).next_to(outrow,DOWN,buff=0.2)
        self.play(FadeIn(klab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in outrow],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(ilab),run_time=0.45)
        self.wait(READ_L+0.7)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,dupnote,arr,outrow,klab,ilab)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("The array is sorted.",font=FN,weight=BOLD,color=WHITE).scale(0.5)
        h2=Text("So duplicates are always next to each other —",font=FN,color=WHITE).scale(0.44)
        h3=Text("compare each value to the last unique one.",font=FN,color=CYAN).scale(0.44)
        for h in (h2,h3):
            if h.width>6.7: h.scale_to_fit_width(6.7)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.28); h3.next_to(h2,DOWN,buff=0.2)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.5); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Two pointers",font=FN,weight=BOLD,color=WHITE).scale(0.6).move_to(UP*2.4)
        af=VGroup(Text("f",font=MN,weight=BOLD,color=CYAN).scale(0.52),
                  Text("fast  —  scans every element",font=FN,color=CYAN).scale(0.44)).arrange(RIGHT,buff=0.25).move_to(UP*1.3)
        asl=VGroup(Text("s",font=MN,weight=BOLD,color=AMBER).scale(0.52),
                   Text("slow  —  marks the last unique value",font=FN,color=AMBER).scale(0.44)).arrange(RIGHT,buff=0.25).move_to(UP*0.55)
        for g in (af,asl):
            if g.width>6.7: g.scale_to_fit_width(6.7)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(af,shift=RIGHT*0.1),run_time=0.5); self.wait(0.35)
        self.play(FadeIn(asl,shift=RIGHT*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,a0,af,asl)),run_time=0.5)

    def walkthrough(self):
        vals=[1,1,2,2,3]
        self.cells=[cell(v,0.9) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.14).move_to(UP*ARR_Y)
        raw=[(0,"int n = nums.size(), s = 0;"),
             (0,"for (int f = 1; f < n; f++) {"),
             (1,"if (nums[f] != nums[s])"),
             (2,"nums[++s] = nums[f];"),
             (0,"}"),
             (0,"return s + 1;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.38))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.16)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.34)
        if code.width>5.4: code.scale(5.4/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,
                               fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.7,height=code.height+0.5)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.07),run_time=0.9)
        self.pf=pointer("f",CYAN,up=True).next_to(self.cells[1],UP,buff=0.12)
        self.ps=pointer("s",AMBER,up=False).next_to(self.cells[0],DOWN,buff=0.12)
        self.play(FadeIn(self.pf,shift=DOWN*0.15),FadeIn(self.ps,shift=UP*0.15),run_time=0.6)
        self.set_cap("s = last unique (index 0);  f scans from 1")
        self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_f(f):
            if f<len(self.cells): return self.pf.animate.next_to(self.cells[f],UP,buff=0.12)
            return self.pf.animate.next_to(self.cells[-1],UP,buff=0.12).shift(RIGHT*0.7)
        def move_s(si): return self.ps.animate.next_to(self.cells[si],DOWN,buff=0.12)
        def comp(f,s): return [self.cells[f][0].animate.set_stroke(CYAN,4.5),self.cells[s][0].animate.set_stroke(CYAN,4.5)]
        def unc(f,s): return [self.cells[f][0].animate.set_stroke(BORDER,3.0),self.cells[s][0].animate.set_stroke(BORDER,3.0)]
        def write(si,f):
            fl=Text(str(vals[f]),font=FN,weight=BOLD,color=AMBER).scale(0.54).move_to(self.cells[f].get_center()).set_z_index(9)
            self.add(fl); self.play(fl.animate.move_to(self.cells[si].get_center()),run_time=0.65)
            nr=RoundedRectangle(width=0.9,height=0.9,corner_radius=0.13,stroke_color=AMBER,stroke_width=3.4,fill_color=SURFACE,fill_opacity=1.0).set_z_index(1).move_to(self.cells[si].get_center())
            nt=Text(str(vals[f]),font=FN,weight=BOLD,color=AMBER).scale(0.54).move_to(self.cells[si].get_center()).set_z_index(5)
            self.play(FadeOut(self.cells[si]),FadeIn(nr),FadeOut(fl,run_time=0.01),run_time=0.35)
            self.add(nt); self.cells[si]=VGroup(nr,nt)

        s=0
        # f=1
        self.set_cap("f = 1:  compare nums[1] with nums[s]"); self.wait(0.5)
        self.play(*hl([1,2]),*comp(1,s),run_time=0.55); self.wait(0.4)
        self.set_cap("1 == 1   \u2192   duplicate, skip",color=RED); self.wait(READ)
        self.play(*unc(1,s),run_time=0.3); self.play(move_f(2),*hl([1]),run_time=0.55); self.wait(0.4)
        # f=2
        self.set_cap("f = 2:  compare nums[2] with nums[s]"); self.wait(0.5)
        self.play(*hl([1,2]),*comp(2,s),run_time=0.55); self.wait(0.4)
        self.set_cap("2 \u2260 1   \u2192   new unique",color=MINT); self.wait(READ)
        self.play(*hl([3]),*unc(2,s),run_time=0.4)
        self.play(move_s(1),run_time=0.45); write(1,2); s=1
        self.play(move_f(3),*hl([1]),run_time=0.55); self.wait(0.5)
        # f=3
        self.set_cap("f = 3:  compare nums[3] with nums[s]"); self.wait(0.5)
        self.play(*hl([1,2]),*comp(3,s),run_time=0.55); self.wait(0.4)
        self.set_cap("2 == 2   \u2192   duplicate, skip",color=RED); self.wait(READ)
        self.play(*unc(3,s),run_time=0.3); self.play(move_f(4),*hl([1]),run_time=0.55); self.wait(0.4)
        # f=4
        self.set_cap("f = 4:  compare nums[4] with nums[s]"); self.wait(0.5)
        self.play(*hl([1,2]),*comp(4,s),run_time=0.55); self.wait(0.4)
        self.set_cap("3 \u2260 2   \u2192   new unique",color=MINT); self.wait(READ)
        self.play(*hl([3]),*unc(4,s),run_time=0.4)
        self.play(move_s(2),run_time=0.45); write(2,4); s=2
        self.play(move_f(5),*hl([1]),run_time=0.55); self.wait(0.5)
        # end
        self.set_cap("loop ends   \u2192   k = s + 1 = 3",color=MINT)
        self.play(*hl([5]),run_time=0.45); self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.pf),FadeOut(self.ps),
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.45)
        anims=[]
        for c in (self.cells[0],self.cells[1],self.cells[2]):
            anims += [c[0].animate.set_stroke(MINT,3.6), c[1].animate.set_color(MINT)]
        for c in (self.cells[3],self.cells[4]):
            anims += [c[0].animate.set_stroke(GRAY,2.2).set_fill(SURFACE,0.4), c[1].animate.set_color(GRAY).set_opacity(0.5)]
        self.play(LaggedStart(*anims,lag_ratio=0.06),run_time=1.0)
        self.set_cap("first k = 3 unique values",color=MINT); self.wait(READ)
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
        part=pill("3 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
        head=Text("LeetCode Top Interview 150",font=FN,weight=BOLD,color=WHITE).scale(0.58)
        if head.width>6.6: head.scale_to_fit_width(6.6)
        head.move_to(UP*1.2)
        sub=Text("every problem, visually explained",font=FN,color=GRAY).scale(0.46).move_to(UP*0.5)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*-0.15+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*-0.15+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,
                                stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center())
        cta=VGroup(ctabox,ctatxt).move_to(UP*-1.05)
        nxt=VGroup(Text("\u2193",font=FN,weight=BOLD,color=AMBER).scale(0.55),
                   Text("comment the next problem",font=FN,color=WHITE).scale(0.46)).arrange(RIGHT,buff=0.2).move_to(UP*-2.35)
        self.play(FadeIn(wm,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(part,shift=UP*0.1),run_time=0.35)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
