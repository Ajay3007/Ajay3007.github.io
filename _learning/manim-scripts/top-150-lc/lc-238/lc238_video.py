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
NUMS_Y=2.7; ANS_Y=1.5; IDX_Y=0.88; TRK_Y=0.0; CODE_Y=-2.35
READ=0.8; READ_L=1.4

def cell(v,size=0.72,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    if v is None:
        return VGroup(r)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.5*size).move_to(r.get_center()).set_z_index(4)
    return VGroup(r,t)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC238(Scene):
    def construct(self):
        self.persistent()
        self.problem_scene()
        self.intuition_scene()
        self.approach_scene()
        self.walkthrough()
        self.outro()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.4)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.4)
        self.wm=VGroup(axio,byte).arrange(RIGHT,buff=0.02).move_to(UP*WM_Y)
        badge=pill("# 238",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Product of Array Except Self",font=FN,weight=BOLD,color=WHITE).scale(0.52)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.28)
        if self.hdr.width>6.7: self.hdr.scale(6.7/self.hdr.width)
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
        t1=Text("Return answer[i] = product of ALL other elements.",font=FN,color=WHITE).scale(0.44)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t1.move_to(UP*2.4)
        self.play(FadeIn(t1,shift=UP*0.1),run_time=0.5)
        vals=[1,2,3,4,5,6]
        row=VGroup(*[cell(v) for v in vals]).arrange(RIGHT,buff=0.14).move_to(UP*1.15)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.36).next_to(row,LEFT,buff=0.24)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.08),run_time=0.9)
        self.wait(0.4)
        c1=Text("the catch:  O(n) time  \u00b7  and NO division",font=FN,weight=BOLD,color=AMBER).scale(0.46)
        if c1.width>6.9: c1.scale_to_fit_width(6.9)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=AMBER,stroke_width=2.6,fill_color=AMBER_BG,fill_opacity=0.5,width=c1.width+0.6,height=0.9).move_to(UP*-0.5)
        c1.move_to(cbox.get_center())
        self.play(FadeIn(cbox),FadeIn(c1),run_time=0.55)
        note=Text("(division would break on zeros anyway)",font=FN,color=GRAY).scale(0.38).next_to(cbox,DOWN,buff=0.3)
        self.play(FadeIn(note),run_time=0.45)
        self.wait(READ_L)
        self.play(FadeOut(VGroup(lbl,t1,row,nlab,cbox,c1,note)),run_time=0.5)

    def intuition_scene(self):
        lbl=pill("The intuition",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        i1=Text("answer[i]  =  (everything BEFORE i) \u00d7 (everything AFTER i)",font=FN,weight=BOLD,color=WHITE).scale(0.44)
        if i1.width>7.0: i1.scale_to_fit_width(7.0)
        i1.move_to(UP*2.35)
        self.play(FadeIn(i1,shift=UP*0.1),run_time=0.5)
        vals=[1,2,3,4,5,6]
        row=VGroup(*[cell(v) for v in vals]).arrange(RIGHT,buff=0.14).move_to(UP*1.05)
        self.play(FadeIn(row),run_time=0.5)
        self.wait(0.3)
        self.play(row[2][0].animate.set_stroke(CYAN,4.6),run_time=0.4)
        pick=Text("take i = 2",font=MN,weight=BOLD,color=CYAN).scale(0.4).next_to(row,UP,buff=0.2)
        self.play(FadeIn(pick),run_time=0.4)
        # before bracket
        bef=VGroup(row[0],row[1])
        bbr=Brace(bef,DOWN,color=MINT,buff=0.12)
        bl=Text("before: 1\u00d72 = 2",font=MN,weight=BOLD,color=MINT).scale(0.36).next_to(bbr,DOWN,buff=0.08)
        aft=VGroup(row[3],row[4],row[5])
        abr=Brace(aft,DOWN,color=AMBER,buff=0.12)
        al=Text("after: 4\u00d75\u00d76 = 120",font=MN,weight=BOLD,color=AMBER).scale(0.36).next_to(abr,DOWN,buff=0.08)
        self.play(GrowFromCenter(bbr),FadeIn(bl),run_time=0.5)
        self.play(GrowFromCenter(abr),FadeIn(al),run_time=0.5)
        self.wait(0.4)
        res=Text("answer[2] = 2 \u00d7 120 = 240",font=MN,weight=BOLD,color=WHITE).scale(0.46).move_to(UP*-2.2)
        self.play(FadeIn(res,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L)
        conc=Text("prefix products, then suffix products",font=FN,color=MINT).scale(0.44).move_to(UP*-3.0)
        self.play(FadeIn(conc),run_time=0.5)
        self.wait(READ)
        self.play(FadeOut(VGroup(lbl,i1,row,pick,bbr,bl,abr,al,res,conc)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        a0=Text("Two sweeps, in place",font=FN,weight=BOLD,color=WHITE).scale(0.52).move_to(UP*2.3)
        a1=VGroup(Text("Pass 1  \u2192",font=MN,weight=BOLD,color=CYAN).scale(0.46),
                  Text("fill each ans[i] with the product BEFORE it",font=FN,color=WHITE).scale(0.38)).arrange(RIGHT,buff=0.22)
        a2=VGroup(Text("Pass 2  \u2190",font=MN,weight=BOLD,color=MINT).scale(0.46),
                  Text("multiply each by the product AFTER it",font=FN,color=WHITE).scale(0.38)).arrange(RIGHT,buff=0.22)
        for g in (a1,a2):
            if g.width>7.0: g.scale_to_fit_width(7.0)
        a1.move_to(UP*1.2); a2.move_to(UP*0.4)
        a3=Text("O(1) extra space  \u00b7  no division",font=MN,weight=BOLD,color=AMBER).scale(0.42).move_to(UP*-0.6)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=RIGHT*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(a2,shift=RIGHT*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def walkthrough(self):
        vals=[1,2,3,4,5,6]; n=6
        self.nc=[cell(v) for v in vals]
        nrow=VGroup(*self.nc).arrange(RIGHT,buff=0.14).move_to(UP*NUMS_Y)
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(nrow,LEFT,buff=0.22)
        self.ac=[cell(None) for _ in vals]
        arow=VGroup(*self.ac).arrange(RIGHT,buff=0.14)
        for i in range(n): self.ac[i].move_to([self.nc[i].get_center()[0],ANS_Y,0])
        alab=Text("ans",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(VGroup(*self.ac),LEFT,buff=0.22)
        self.acv=[None]*n
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.32).move_to([self.nc[i].get_center()[0],IDX_Y,0]) for i in range(n)])
        # tracker
        tbx=RoundedRectangle(width=1.7,height=0.78,corner_radius=0.13,stroke_color=CYAN,stroke_width=3.0,fill_color=SURFACE,fill_opacity=1.0)
        tvl=Text("1",font=FN,weight=BOLD,color=CYAN).scale(0.5).move_to(tbx.get_center())
        tlb=Text("prefix P",font=MN,color=GRAY).scale(0.34).next_to(tbx,LEFT,buff=0.22)
        trk=VGroup(tlb,tbx,tvl).move_to([0.4,TRK_Y,0])
        tlb.next_to(tbx,LEFT,buff=0.22)
        self.tbx=tbx; self.tvl=tvl; self.tlb=tlb

        raw=[(0,"int P = 1;"),
             (0,"for (i=0; i<n; i++) { ans[i]=P; P*=nums[i]; }"),
             (0,"int R = 1;"),
             (0,"for (i=n-1; i>=0; i--) { ans[i]*=R; R*=nums[i]; }"),
             (0,"return ans;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.34))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.15)
        if code.width>6.0: code.scale(6.0/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.55,height=code.height+0.4)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(nlab),FadeIn(alab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in self.nc],lag_ratio=0.06),run_time=0.8)
        self.play(FadeIn(idx),LaggedStart(*[FadeIn(c) for c in self.ac],lag_ratio=0.06),run_time=0.6)
        self.play(FadeIn(trk,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(panel),run_time=0.3)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in self.code],lag_ratio=0.06),run_time=0.7)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def set_ans(i,val,color=WHITE):
            new=Text(str(val),font=FN,weight=BOLD,color=color).scale(0.5*0.72).move_to(self.ac[i][0].get_center()).set_z_index(4)
            if self.acv[i] is None:
                self.acv[i]=new; return FadeIn(new,scale=1.2)
            old=self.acv[i]; self.acv[i]=new; return AnimationGroup(FadeOut(old,scale=0.4),FadeIn(new,scale=1.2))
        def set_trk(val,color=CYAN):
            new=Text(str(val),font=FN,weight=BOLD,color=color).scale(0.5).move_to(self.tbx.get_center())
            old=self.tvl; self.tvl=new; return AnimationGroup(FadeOut(old,scale=0.4),FadeIn(new,scale=1.2))

        # PASS 1 (prefix, left->right)
        self.set_cap("Pass 1 \u2192 :  each ans[i] = product BEFORE it",color=CYAN)
        self.play(*hl([0,1]),run_time=0.4)
        P=1
        pref=[1,1,2,6,24,120]
        for i in range(n):
            self.play(set_ans(i,pref[i],CYAN),self.ac[i][0].animate.set_stroke(CYAN,4.2),run_time=0.42)
            P*=vals[i]
            self.play(set_trk(P,CYAN),self.nc[i][0].animate.set_stroke(CYAN,4.0),run_time=0.34)
            self.play(self.nc[i][0].animate.set_stroke(BORDER,3.0),self.ac[i][0].animate.set_stroke(BORDER,3.0),run_time=0.18)
        self.wait(READ)
        # relabel tracker for suffix
        self.set_cap("Pass 2 \u2190 :  multiply by the product AFTER it",color=MINT)
        newlb=Text("suffix R",font=MN,color=GRAY).scale(0.34).move_to(self.tlb.get_center())
        self.play(*hl([2,3]),FadeOut(self.tlb),FadeIn(newlb),
                  self.tbx.animate.set_stroke(MINT,3.0),set_trk(1,MINT),run_time=0.5)
        self.tlb=newlb
        R=1
        ansf=[720,360,240,180,144,120]
        for i in range(n-1,-1,-1):
            self.play(set_ans(i,ansf[i],MINT),self.ac[i][0].animate.set_stroke(MINT,4.2),run_time=0.42)
            R*=vals[i]
            self.play(set_trk(R,MINT),self.nc[i][0].animate.set_stroke(MINT,4.0),run_time=0.34)
            self.play(self.nc[i][0].animate.set_stroke(BORDER,3.0),self.ac[i][0].animate.set_stroke(MINT if True else BORDER,3.2),run_time=0.18)
        self.play(*hl([4]),run_time=0.3)
        self.set_cap("answer = product of everything except self  \u2713",color=MINT)
        self.play(*[self.ac[i][0].animate.set_stroke(MINT,3.6) for i in range(n)],run_time=0.4)
        self.wait(READ_L)
        self._extras=VGroup(nlab,alab,idx,trk,self.tlb,nrow,VGroup(*self.ac))

    def outro(self):
        self.play(FadeOut(self.panel),FadeOut(VGroup(*self.code)),FadeOut(self.tvl),FadeOut(self.tbx),FadeOut(self.tlb),run_time=0.35)
        self.set_cap("before \u00d7 after  \u2014  two sweeps, no division",color=MINT); self.wait(READ)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Extra space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.5)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge=VGroup(cbox,comp).move_to(UP*-1.3)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.45); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("13 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
