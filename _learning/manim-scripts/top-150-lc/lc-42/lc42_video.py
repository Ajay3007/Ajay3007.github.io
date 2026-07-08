from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"
WATER="#4AA8FF"; WATER_BG="#12314F"; TERR="#3A4657"

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55
BASE_Y=-0.55; UH=0.8; BW=0.86; GAP=0.05
STAT_Y=-2.35; CODE_Y=-4.55
READ=0.8; READ_L=1.4

H=[2,1,0,3,0,1,2]; N=len(H)

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
    lab=Text(label,font=MN,color=GRAY).scale(0.34)
    v=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.6)
    col=VGroup(lab,v).arrange(DOWN,buff=0.09)
    box=RoundedRectangle(width=max(col.width+0.75,1.75),height=col.height+0.55,corner_radius=0.14,
                         stroke_color=color,stroke_width=2.6,fill_color=SURFACE,fill_opacity=1.0)
    col.move_to(box.get_center())
    return VGroup(box,col),v


class LC42(Scene):
    def construct(self):
        self.persistent()
        self.problem_scene()
        self.hint_scene()
        self.approach_scene()
        self.prefix_walk()
        self.twopointer_walk()
        self.outro()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.4)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.4)
        self.wm=VGroup(axio,byte).arrange(RIGHT,buff=0.02).move_to(UP*WM_Y)
        badge=pill("# 42",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Trapping Rain Water",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3)
        if self.hdr.width>6.7: self.hdr.scale(6.7/self.hdr.width)
        self.hdr.move_to(UP*HDR_Y)
        self.play(FadeIn(self.wm,shift=DOWN*0.15),run_time=0.5)
        self.play(FadeIn(self.hdr[0],shift=RIGHT*0.2),Write(self.hdr[1]),run_time=0.9)
        self.wait(0.3); self.cap=None

    def set_cap(self,txt,color=WHITE,scale=0.46,rt=0.45):
        new=Text(txt,font=FN,color=color).scale(scale)
        if new.width>6.7: new.scale_to_fit_width(6.7)
        new.move_to(UP*CAP_Y)
        if self.cap is None:
            self.cap=new; self.play(FadeIn(new,shift=UP*0.1),run_time=rt); return
        self.play(FadeOut(self.cap,shift=UP*0.08),run_time=0.22)
        self.play(FadeIn(new,shift=UP*0.08),run_time=0.32); self.cap=new

    # ---------- chart geometry ----------
    def col_x(self,i):
        W=N*BW+(N-1)*GAP
        return -W/2+BW/2+i*(BW+GAP)

    def bar_top(self,i):
        return BASE_Y+H[i]*UH

    def make_bar(self,i):
        h=H[i]
        if h==0:
            r=Rectangle(width=BW,height=0.05,fill_color=TERR,fill_opacity=1.0,stroke_width=0)
            r.move_to([self.col_x(i),BASE_Y+0.025,0])
        else:
            r=Rectangle(width=BW,height=h*UH,fill_color=TERR,fill_opacity=1.0,stroke_color=BORDER,stroke_width=2.2)
            r.move_to([self.col_x(i),BASE_Y+h*UH/2,0])
        r.set_z_index(3); return r

    def water_rect(self,i,level):
        h=H[i]
        if level<=h: return None
        y0=self.bar_top(i); y1=BASE_Y+level*UH
        r=Rectangle(width=BW,height=y1-y0,fill_color=WATER,fill_opacity=0.5,stroke_color=WATER,stroke_width=1.2)
        r.move_to([self.col_x(i),(y0+y1)/2,0]); r.set_z_index(2); return r

    def cap_line(self,i,level,color):
        y=BASE_Y+level*UH
        return DashedLine([self.col_x(i)-BW/2,y,0],[self.col_x(i)+BW/2,y,0],
                          color=color,stroke_width=4,dash_length=0.07).set_z_index(6)

    def build_chart(self):
        self.bars=VGroup(*[self.make_bar(i) for i in range(N)])
        self.ground=Line([self.col_x(0)-BW/2-0.15,BASE_Y,0],[self.col_x(N-1)+BW/2+0.15,BASE_Y,0],
                         color=GRAY,stroke_width=3).set_z_index(1)
        self.hvals=VGroup(*[Text(str(H[i]),font=MN,color=GRAY).scale(0.34).next_to(self.bars[i],UP,buff=0.08)
                            if H[i]>0 else Text("0",font=MN,color=GRAY).scale(0.34).move_to([self.col_x(i),BASE_Y+0.28,0])
                            for i in range(N)]).set_z_index(6)
        self.idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.3).move_to([self.col_x(i),BASE_Y-0.38,0]) for i in range(N)])

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Each bar is a wall of some height.",font=FN,color=WHITE).scale(0.44)
        t2=Text("After it rains, how much water is trapped between them?",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.6); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.45); self.play(FadeIn(t2),run_time=0.45)
        self.wait(0.6)
        self.build_chart()
        hlbl=Text("height",font=MN,weight=BOLD,color=WHITE).scale(0.34).next_to(self.bars,LEFT,buff=0.25)
        self.play(FadeOut(VGroup(t1,t2)),Create(self.ground),run_time=0.45)
        self.play(FadeIn(hlbl),LaggedStart(*[GrowFromEdge(b,DOWN) for b in self.bars],lag_ratio=0.08),run_time=1.1)
        self.play(FadeIn(self.hvals),FadeIn(self.idx),run_time=0.5)
        self.hlbl=hlbl
        self.chart=VGroup(self.ground,self.bars,self.hvals,self.idx,self.hlbl)
        self.wait(0.5)
        # pour water to the final trapped levels
        levels=self.trap_levels()
        waters=[self.water_rect(i,levels[i]) for i in range(N)]
        waters=[w for w in waters if w is not None]
        rain=Text("let it rain — water settles in the dips",font=FN,color=WATER).scale(0.42).move_to(UP*2.6)
        if rain.width>6.9: rain.scale_to_fit_width(6.9)
        self.play(FadeIn(rain,shift=UP*0.1),run_time=0.4)
        self.play(LaggedStart(*[FadeIn(w,shift=DOWN*0.3) for w in waters],lag_ratio=0.12),run_time=1.3)
        self.waters_intro=VGroup(*waters)
        self.wait(0.5)
        ans=pill("6 units trapped  —  but why 6?",WATER,WATER_BG,WATER,s=0.44,h=0.66).move_to(UP*2.6)
        self.play(Transform(rain,ans),run_time=0.5)
        self.wait(READ_L)
        self.play(FadeOut(VGroup(lbl,rain,self.waters_intro)),run_time=0.5)

    def trap_levels(self):
        L=[0]*N; R=[0]*N; m=0
        for i in range(N): m=max(m,H[i]); L[i]=m
        m=0
        for i in range(N-1,-1,-1): m=max(m,H[i]); R[i]=m
        return [min(L[i],R[i]) for i in range(N)]

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        note=Text("water over a bar is capped by its shorter wall",font=FN,color=AMBER).scale(0.42).move_to(UP*2.6)
        if note.width>6.9: note.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),FadeIn(note,shift=UP*0.1),run_time=0.5)
        # focus bar i = 2 (a valley); left wall = 2, right wall = 3
        i=2
        self.play(Indicate(self.hvals[i],color=AMBER,scale_factor=1.6),run_time=0.5)
        lwall=self.cap_line(0,2,MINT)
        rwall=self.cap_line(3,3,CYAN)
        llab=Text("left wall = 2",font=MN,color=MINT).scale(0.32).next_to(lwall,UP,buff=0.08)
        rlab=Text("right wall = 3",font=MN,color=CYAN).scale(0.32).next_to(rwall,UP,buff=0.08)
        self.play(Create(lwall),FadeIn(llab),run_time=0.5)
        self.play(Create(rwall),FadeIn(rlab),run_time=0.5)
        self.wait(0.4)
        w=self.water_rect(i,2)
        formula=pill("min(2, 3) - 0  =  2 units here",WATER,WATER_BG,WATER,s=0.42,h=0.62).move_to(UP*2.6)
        self.play(FadeIn(w,shift=DOWN*0.2),Transform(note,formula),run_time=0.6)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,note,lwall,rwall,llab,rlab,w)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        # clear the chart so the (text-only) approach has a clean screen
        self.play(FadeOut(self.chart),FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        a0=Text("So we need two numbers per bar:",font=FN,weight=BOLD,color=WHITE).scale(0.46).move_to(UP*2.55)
        a1=Text("leftMax[i]  = tallest wall at or left of i",font=MN,color=AMBER).scale(0.36).move_to(UP*1.9)
        a2=Text("rightMax[i] = tallest wall at or right of i",font=MN,color=CYAN).scale(0.36).move_to(UP*1.4)
        a3=Text("water[i] = min(leftMax[i], rightMax[i]) - h[i]",font=MN,weight=BOLD,color=WATER).scale(0.36).move_to(UP*0.75)
        s1=Text("Step 1  ·  build both arrays   →   O(n) space",font=FN,color=GRAY).scale(0.36).move_to(UP*0.0)
        s2=Text("Step 2  ·  drop the arrays with two pointers → O(1)",font=FN,color=MINT).scale(0.36).move_to(UP*-0.5)
        for g in (a1,a2,a3,s1,s2):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.4); self.play(FadeIn(a2,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45); self.wait(0.4)
        self.play(FadeIn(s1,shift=UP*0.1),run_time=0.4); self.play(FadeIn(s2,shift=UP*0.1),run_time=0.4)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,s1,s2)),run_time=0.5)

    def code_panel(self,raw,scale=0.32):
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(scale))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.12)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.28)
        if code.width>6.5: code.scale(6.5/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.3,fill_color="#0F1420",fill_opacity=1.0,
                               width=code.width+0.6,height=code.height+0.4).move_to(UP*CODE_Y)
        code.move_to(panel.get_center())
        return panel,list(code)

    def prefix_walk(self):
        # bring the chart back for the walkthrough
        self.play(FadeIn(self.chart),run_time=0.5)
        seg=pill("Step 1  ·  build the arrays",AMBER,AMBER_BG,AMBER,s=0.4).move_to(UP*2.5)
        self.play(FadeIn(seg,shift=UP*0.1),run_time=0.5)
        raw=[(0,"L[0]=h[0];  for i=1..n-1"),
             (1,"L[i] = max(L[i-1], h[i]);"),
             (0,"R[n-1]=h[n-1];  for i=n-2..0"),
             (1,"R[i] = max(R[i+1], h[i]);"),
             (0,"for i:  res += min(L[i],R[i]) - h[i];")]
        panel,code=self.code_panel(raw)
        self.panel=panel; self.code=code; self._act=[]
        self.play(FadeIn(panel),LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.06),run_time=0.9)

        # leftMax sweep (amber caps), left -> right
        self.set_cap("leftMax: tallest wall seen from the left",color=AMBER)
        Lmax=[0]*N; m=0; lcaps=[]
        for i in range(N):
            m=max(m,H[i]); Lmax[i]=m
            c=self.cap_line(i,m,AMBER); lcaps.append(c)
            self.play(Create(c),run_time=0.22)
        self.lcaps=VGroup(*lcaps); self.wait(0.4)
        # rightMax sweep (cyan caps), right -> left
        self.set_cap("rightMax: tallest wall seen from the right",color=CYAN)
        Rmax=[0]*N; m=0; rcaps=[]
        for i in range(N-1,-1,-1):
            m=max(m,H[i]); Rmax[i]=m
            c=self.cap_line(i,m,CYAN); rcaps.append(c)
            self.play(Create(c),run_time=0.22)
        self.rcaps=VGroup(*rcaps); self.wait(0.4)
        # fill water to min level, accumulate
        self.set_cap("water level = the LOWER of the two caps",color=WATER)
        levels=[min(Lmax[i],Rmax[i]) for i in range(N)]
        total=0; waters=[]
        run=Text("res = 0",font=MN,weight=BOLD,color=WATER).scale(0.42).move_to(UP*2.5)
        self.play(Transform(seg,run),run_time=0.4)
        for i in range(N):
            add=levels[i]-H[i]
            if add>0:
                total+=add
                w=self.water_rect(i,levels[i]); waters.append(w)
                new=Text("res = %d" % total,font=MN,weight=BOLD,color=WATER).scale(0.42).move_to(UP*2.5)
                self.play(FadeIn(w,shift=DOWN*0.2),Transform(seg,new),run_time=0.4)
        self.waters=VGroup(*waters); self.wait(READ)
        done=pill("6 units  —  correct, but we stored 2 arrays",AMBER,AMBER_BG,AMBER,s=0.4,h=0.62).move_to(UP*2.5)
        self.play(Transform(seg,done),run_time=0.5); self.wait(READ_L)
        self.seg=seg
        # clear for optimization: drop caps, water, keep chart
        self.play(FadeOut(self.lcaps),FadeOut(self.rcaps),FadeOut(self.waters),
                  FadeOut(VGroup(*self.code)),FadeOut(self.panel),run_time=0.6)

    def twopointer_walk(self):
        seg=pill("Step 2  ·  two pointers, O(1) space",MINT,MINT_BG,MINT,s=0.4).move_to(UP*2.5)
        self.play(Transform(self.seg,seg),run_time=0.4)
        raw=[(0,"int l=0, r=n-1, lMax=0, rMax=0, res=0;"),
             (0,"while (l < r) {"),
             (1,"if (h[l] < h[r]) { lMax=max(lMax,h[l]); res+=lMax-h[l]; l++; }"),
             (1,"else             { rMax=max(rMax,h[r]); res+=rMax-h[r]; r--; }"),
             (0,"}"),
             (0,"return res;")]
        panel,code=self.code_panel(raw)
        self.panel=panel; self.code=code; self._act=[]
        self.play(FadeIn(panel),LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.06),run_time=0.9)

        self.lm,self.lmv=statbox("lMax",0,AMBER)
        self.rm,self.rmv=statbox("rMax",0,CYAN)
        self.rs,self.rsv=statbox("res",0,WATER)
        stats=VGroup(self.lm,self.rs,self.rm).arrange(RIGHT,buff=0.4).move_to(UP*STAT_Y)
        if stats.width>7.0: stats.scale(7.0/stats.width)
        self.play(FadeIn(stats,shift=UP*0.1),run_time=0.5)

        def set_val(ref,val,color):
            new=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.6).move_to(ref)
            return Transform(ref,new)
        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a

        l=0; r=N-1; lMax=0; rMax=0; res=0
        pl=pointer("l",AMBER,up=False); pr=pointer("r",CYAN,up=False)
        pl.next_to(self.idx[l],DOWN,buff=0.12); pr.next_to(self.idx[r],DOWN,buff=0.12)
        self.play(FadeIn(pl,shift=UP*0.1),FadeIn(pr,shift=UP*0.1),*hl([0]),run_time=0.5)
        self.set_cap("two ends, walk inward toward the taller wall",color=MINT); self.wait(READ)

        step=0
        while l<r:
            step+=1
            if H[l]<H[r]:
                lMax=max(lMax,H[l]); add=lMax-H[l]; res+=add
                self.set_cap("h[l]=%d < h[r]=%d  →  move left;  add %d" % (H[l],H[r],add),
                             color=(WATER if add>0 else GRAY),scale=0.42)
                anims=[*hl([2]),self.bars[l].animate.set_stroke(AMBER,3.6) if H[l]>0 else Wait(0.01)]
                self.play(*anims,run_time=0.4)
                if add>0:
                    w=self.water_rect(l,lMax)
                    self.play(FadeIn(w,shift=DOWN*0.15),set_val(self.lmv,lMax,AMBER),set_val(self.rsv,res,WATER),run_time=0.4)
                else:
                    self.play(set_val(self.lmv,lMax,AMBER),run_time=0.3)
                l+=1
                if l<r:
                    self.play(pl.animate.next_to(self.idx[l],DOWN,buff=0.12),
                              self.bars[l-1].animate.set_stroke(BORDER,2.2) if H[l-1]>0 else Wait(0.01),run_time=0.35)
            else:
                rMax=max(rMax,H[r]); add=rMax-H[r]; res+=add
                self.set_cap("h[r]=%d ≤ h[l]=%d  →  move right;  add %d" % (H[r],H[l],add),
                             color=(WATER if add>0 else GRAY),scale=0.42)
                anims=[*hl([3]),self.bars[r].animate.set_stroke(CYAN,3.6) if H[r]>0 else Wait(0.01)]
                self.play(*anims,run_time=0.4)
                if add>0:
                    w=self.water_rect(r,rMax)
                    self.play(FadeIn(w,shift=DOWN*0.15),set_val(self.rmv,rMax,CYAN),set_val(self.rsv,res,WATER),run_time=0.4)
                else:
                    self.play(set_val(self.rmv,rMax,CYAN),run_time=0.3)
                r-=1
                if l<r:
                    self.play(pr.animate.next_to(self.idx[r],DOWN,buff=0.12),
                              self.bars[r+1].animate.set_stroke(BORDER,2.2) if H[r+1]>0 else Wait(0.01),run_time=0.35)
        self.res_final=res
        self.play(*hl([5]),FadeOut(pl),FadeOut(pr),run_time=0.4)
        self.wait(0.3)

    def outro(self):
        self.set_cap("same 6 units — no arrays, just two counters",color=MINT)
        self.wait(READ_L)
        self.play(*[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.3)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=MINT).scale(0.5)).arrange(RIGHT,buff=0.55)
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
        part=pill("16 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
