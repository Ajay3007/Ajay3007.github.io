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

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=2.05; TRK_Y=0.35; CODE_Y=-2.1
READ=0.8; READ_L=1.4

def cell(v,size=0.78,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center()).set_z_index(5)
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


class LC122(Scene):
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
        badge=pill("# 122",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Buy & Sell Stock II",font=FN,weight=BOLD,color=WHITE).scale(0.58)
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
        t1=Text("Same prices — but now buy & sell as often as you like.",font=FN,color=WHITE).scale(0.4)
        t2=Text("(hold at most one share at a time.)",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.9); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        vals=[7,1,5,3,6,4]
        inrow=VGroup()
        for i,v in enumerate(vals):
            if i in (1,3): inrow.add(cell(v,0.72,AMBER,AMBER_BG,WHITE))
            elif i in (2,4): inrow.add(cell(v,0.72,MINT,MINT_BG,WHITE))
            else: inrow.add(cell(v,0.72,BORDER,SURFACE,WHITE))
        inrow.arrange(RIGHT,buff=0.12).move_to(UP*0.95)
        nlab=Text("prices",font=MN,weight=BOLD,color=WHITE).scale(0.36).next_to(inrow,LEFT,buff=0.24)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.wait(0.4)
        g1=Text("+4",font=MN,weight=BOLD,color=MINT).scale(0.4).next_to(inrow[1:3],UP,buff=0.2)
        g2=Text("+3",font=MN,weight=BOLD,color=MINT).scale(0.4).next_to(inrow[3:5],UP,buff=0.2)
        self.play(FadeIn(g1),FadeIn(g2),run_time=0.5); self.wait(0.4)
        concl=Text("buy 1\u2192sell 5,  buy 3\u2192sell 6   =   7",font=MN,weight=BOLD,color=MINT).scale(0.4).move_to(UP*-1.4)
        if concl.width>6.8: concl.scale_to_fit_width(6.8)
        self.play(FadeIn(concl,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,g1,g2,concl)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("All profit comes from rising runs.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("A rise's profit = the sum of its daily gains.",font=FN,color=WHITE).scale(0.44)
        h3=Text("So just grab every step up.",font=FN,color=CYAN).scale(0.46)
        for h in (h1,h2,h3):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.24); h3.next_to(h2,DOWN,buff=0.24)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Greedy: bank every rise",font=FN,weight=BOLD,color=WHITE).scale(0.54).move_to(UP*2.3)
        a1=Text("walk day by day",font=FN,color=WHITE).scale(0.46).move_to(UP*1.4)
        a2=Text("if prices[i] > prices[i-1]",font=MN,weight=BOLD,color=CYAN).scale(0.44).move_to(UP*0.7)
        a3=Text("add the difference to the profit",font=FN,color=MINT).scale(0.44).move_to(UP*0.05)
        for g in (a2,a3):
            if g.width>6.8: g.scale_to_fit_width(6.8)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.45); self.wait(0.25)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def walkthrough(self):
        vals=[7,1,5,3,6,4]
        self.cells=[cell(v,0.78) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.12).move_to(UP*ARR_Y)
        pbx=RoundedRectangle(width=1.6,height=0.9,corner_radius=0.13,stroke_color=MINT,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        pvl=Text("0",font=FN,weight=BOLD,color=MINT).scale(0.58).move_to(pbx.get_center())
        plb=Text("maxProfit",font=MN,color=GRAY).scale(0.32).next_to(pbx,UP,buff=0.1)
        ptr=VGroup(plb,pbx,pvl).move_to(UP*TRK_Y)
        self.pbx=pbx; self.pvl=pvl; self.tracker=ptr

        raw=[(0,"int maxProfit = 0;"),
             (0,"for (int i = 1; i < n; i++) {"),
             (1,"if (prices[i] > prices[i-1])"),
             (2,"maxProfit += prices[i] - prices[i-1];"),
             (0,"}"),
             (0,"return maxProfit;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.35))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.14)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>5.7: code.scale(5.7/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(ptr,shift=UP*0.1),run_time=0.55)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.85)
        self.pj=pointer("i-1",AMBER,up=True).next_to(self.cells[0],UP,buff=0.12)
        self.pi=pointer("i",CYAN,up=True).next_to(self.cells[1],UP,buff=0.12)
        self.play(FadeIn(self.pj,shift=DOWN*0.12),FadeIn(self.pi,shift=DOWN*0.12),run_time=0.5)
        self.set_cap("maxProfit = 0;   compare each day to the one before"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_pair(i):
            a=[self.pj.animate.next_to(self.cells[i-1],UP,buff=0.12),
               self.pi.animate.next_to(self.cells[i],UP,buff=0.12)]
            return a
        def hp(i,color): return [self.cells[i-1][0].animate.set_stroke(color,4.6),self.cells[i][0].animate.set_stroke(color,4.6)]
        def up(i): return [self.cells[i-1][0].animate.set_stroke(BORDER,3.0),self.cells[i][0].animate.set_stroke(BORDER,3.0)]
        def bank(total,diff,i):
            src=(self.cells[i-1].get_center()+self.cells[i].get_center())/2+UP*0.75
            plus=Text(f"+{diff}",font=FN,weight=BOLD,color=MINT).scale(0.55).move_to(src)
            self.add(plus)
            new=Text(str(total),font=FN,weight=BOLD,color=MINT).scale(0.58).move_to(self.pbx.get_center())
            self.play(plus.animate.move_to(self.pbx.get_center()).set_opacity(0),
                      FadeOut(self.pvl,scale=0.4),FadeIn(new,scale=1.2),run_time=0.6)
            self.pvl=new; self.remove(plus)

        def up_step(i,total,diff):
            self.set_cap(f"day {i}:  {vals[i]} > {vals[i-1]}   \u2192  bank +{diff}",color=MINT)
            self.play(*hl([2,3]),*hp(i,MINT),run_time=0.5); self.wait(0.25)
            bank(total,diff,i)
            self.play(*up(i),run_time=0.3)
            if i<len(vals)-1: self.play(*move_pair(i+1),*hl([1]),run_time=0.5)
            self.wait(0.3)
        def skip_step(i):
            self.set_cap(f"day {i}:  {vals[i]} > {vals[i-1]} ?  no  \u2192  skip",color=GRAY)
            self.play(*hl([2]),*hp(i,RED),run_time=0.5); self.wait(0.35)
            self.play(*up(i),run_time=0.3)
            if i<len(vals)-1: self.play(*move_pair(i+1),*hl([1]),run_time=0.5)
            self.wait(0.3)

        skip_step(1)            # 1 > 7 ? no
        up_step(2,4,4)          # 5 > 1 -> +4
        skip_step(3)            # 3 > 5 ? no
        up_step(4,7,3)          # 6 > 3 -> +3
        skip_step(5)            # 4 > 6 ? no

        self.set_cap("total profit  =  4 + 3  =  7",color=MINT)
        self.play(*hl([5]),self.pbx.animate.set_stroke(MINT,4.2),run_time=0.5)
        self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.pi),FadeOut(self.pj),FadeOut(self.tracker),FadeOut(self.pvl),
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.5)
        ans=pill("max profit = 7",MINT,MINT_BG,MINT,s=0.46,h=0.7).move_to(UP*TRK_Y)
        self.play(FadeIn(ans,scale=1.05),run_time=0.5)
        self.set_cap("grab every rise  \u2192  7  (vs 5 with one trade)",color=MINT); self.wait(READ)
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
        part=pill("8 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
