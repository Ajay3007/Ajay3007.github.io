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

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55; ARR_Y=2.15; TRK_Y=0.5; CODE_Y=-2.15
READ=0.8; READ_L=1.4

def cell(v,size=0.78,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
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


class LC121(Scene):
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
        badge=pill("# 121",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Buy & Sell Stock",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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
        t1=Text("prices[i] = the stock price on day i.",font=FN,color=WHITE).scale(0.4)
        t2=Text("Buy once, sell later — maximise the profit.",font=FN,color=GRAY).scale(0.38)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.9); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.5); self.play(FadeIn(t2),run_time=0.45)
        self.wait(READ_L)
        vals=[7,1,5,3,6,4]
        inrow=VGroup()
        for i,v in enumerate(vals):
            if i==1: inrow.add(cell(v,0.72,AMBER,AMBER_BG,WHITE))
            elif i==4: inrow.add(cell(v,0.72,MINT,MINT_BG,WHITE))
            else: inrow.add(cell(v,0.72,BORDER,SURFACE,WHITE))
        inrow.arrange(RIGHT,buff=0.12).move_to(UP*0.95)
        nlab=Text("prices",font=MN,weight=BOLD,color=WHITE).scale(0.36).next_to(inrow,LEFT,buff=0.24)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in inrow],lag_ratio=0.1),run_time=1.0)
        self.wait(0.5)
        buy=Text("buy @ 1",font=MN,weight=BOLD,color=AMBER).scale(0.34).next_to(inrow[1],DOWN,buff=0.25)
        sell=Text("sell @ 6",font=MN,weight=BOLD,color=MINT).scale(0.34).next_to(inrow[4],DOWN,buff=0.25)
        self.play(FadeIn(buy),FadeIn(sell),run_time=0.5); self.wait(0.5)
        concl=Text("max profit  =  6 \u2212 1  =  5",font=MN,weight=BOLD,color=MINT).scale(0.44).move_to(UP*-1.5)
        self.play(FadeIn(concl,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,t1,t2,inrow,nlab,buy,sell,concl)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("Hint",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("You must buy before you sell.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("So as you scan, remember the lowest",font=FN,color=WHITE).scale(0.44)
        h3=Text("price so far — the best day to have bought.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*1.9); h2.next_to(h1,DOWN,buff=0.24); h3.next_to(h2,DOWN,buff=0.22)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.wait(0.3)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.5)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("One pass, two trackers",font=FN,weight=BOLD,color=WHITE).scale(0.54).move_to(UP*2.4)
        a1=VGroup(Text("minPrice",font=MN,weight=BOLD,color=AMBER).scale(0.46),
                  Text("lowest price so far",font=FN,color=WHITE).scale(0.42)).arrange(RIGHT,buff=0.3).move_to(UP*1.4)
        a2=VGroup(Text("maxProfit",font=MN,weight=BOLD,color=MINT).scale(0.46),
                  Text("best price \u2212 minPrice",font=FN,color=WHITE).scale(0.42)).arrange(RIGHT,buff=0.3).move_to(UP*0.6)
        a3=Text("each day: update one or the other",font=FN,color=CYAN).scale(0.44).move_to(UP*-0.2)
        for g in (a1,a2,a3):
            if g.width>6.8: g.scale_to_fit_width(6.8)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=RIGHT*0.1),run_time=0.45)
        self.play(FadeIn(a2,shift=RIGHT*0.1),run_time=0.45); self.wait(0.25)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3)),run_time=0.5)

    def walkthrough(self):
        vals=[7,1,5,3,6,4]
        self.cells=[cell(v,0.78) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.12).move_to(UP*ARR_Y)
        # trackers
        mbx=RoundedRectangle(width=1.5,height=0.9,corner_radius=0.13,stroke_color=AMBER,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        mvl=Text("\u221e",font=FN,weight=BOLD,color=AMBER).scale(0.58).move_to(mbx.get_center())
        mlb=Text("minPrice",font=MN,color=GRAY).scale(0.3).next_to(mbx,UP,buff=0.1)
        mtr=VGroup(mlb,mbx,mvl)
        pbx=RoundedRectangle(width=1.5,height=0.9,corner_radius=0.13,stroke_color=MINT,stroke_width=3.2,fill_color=SURFACE,fill_opacity=1.0)
        pvl=Text("0",font=FN,weight=BOLD,color=MINT).scale(0.58).move_to(pbx.get_center())
        plb=Text("maxProfit",font=MN,color=GRAY).scale(0.3).next_to(pbx,UP,buff=0.1)
        ptr=VGroup(plb,pbx,pvl)
        trackers=VGroup(mtr,ptr).arrange(RIGHT,buff=0.9).move_to(UP*TRK_Y)
        self.mbx=mbx; self.mvl=mvl; self.pbx=pbx; self.pvl=pvl; self.trackers=trackers

        raw=[(0,"int minPrice = INT_MAX, maxProfit = 0;"),
             (0,"for (int i = 0; i < n; i++) {"),
             (1,"if (prices[i] < minPrice)"),
             (2,"minPrice = prices[i];"),
             (1,"else if (prices[i] - minPrice > maxProfit)"),
             (2,"maxProfit = prices[i] - minPrice;"),
             (0,"}"),
             (0,"return maxProfit;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.34))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.3)
        if code.width>5.7: code.scale(5.7/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]; self.best_sell=None

        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=1.0)
        self.play(FadeIn(trackers,shift=UP*0.1),run_time=0.6)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in code],lag_ratio=0.06),run_time=0.85)
        self.pf=pointer("i",CYAN,up=True).next_to(self.cells[0],UP,buff=0.12)
        self.play(FadeIn(self.pf,shift=DOWN*0.15),run_time=0.5)
        self.set_cap("minPrice = \u221e,   maxProfit = 0"); self.wait(READ)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def move_i(i):
            if i<len(self.cells): return self.pf.animate.next_to(self.cells[i],UP,buff=0.12)
            return self.pf.animate.next_to(self.cells[-1],UP,buff=0.12).shift(RIGHT*0.7)
        def scan(i): return self.cells[i][0].animate.set_stroke(CYAN,4.6)
        def unscan(i): return self.cells[i][0].animate.set_stroke(BORDER,3.0)
        def pop(box_center,old,newtext):
            self.play(FadeOut(old,scale=0.4),FadeIn(newtext,scale=1.2),run_time=0.38)
        def set_min(v):
            new=Text(str(v),font=FN,weight=BOLD,color=AMBER).scale(0.58).move_to(self.mbx.get_center())
            pop(self.mbx.get_center(),self.mvl,new); self.mvl=new
        def set_profit(v):
            new=Text(str(v),font=FN,weight=BOLD,color=MINT).scale(0.58).move_to(self.pbx.get_center())
            pop(self.pbx.get_center(),self.pvl,new); self.pvl=new
        def mark_buy(i):
            return [self.cells[i][0].animate.set_stroke(AMBER,3.6).set_fill(AMBER_BG,1.0)]
        def unmark(i):
            return [self.cells[i][0].animate.set_stroke(BORDER,3.0).set_fill(SURFACE,1.0),
                    self.cells[i][1].animate.set_color(WHITE)]
        def mark_sell(i):
            return [self.cells[i][0].animate.set_stroke(MINT,3.6).set_fill(MINT_BG,1.0)]

        buy_idx=None
        # i=0 p=7
        self.set_cap("day 0:  price 7  <  minPrice (\u221e)"); self.wait(0.4)
        self.play(*hl([2,3]),scan(0),run_time=0.5); self.wait(0.3)
        set_min(7); self.play(*mark_buy(0),run_time=0.3); buy_idx=0
        self.set_cap("new lowest  \u2192  minPrice = 7",color=AMBER)
        self.play(unscan(0),move_i(1),*hl([1]),run_time=0.55); self.wait(0.35)
        # i=1 p=1
        self.set_cap("day 1:  price 1  <  minPrice (7)"); self.wait(0.4)
        self.play(*hl([2,3]),scan(1),run_time=0.5); self.wait(0.3)
        set_min(1); self.play(*unmark(0),*mark_buy(1),run_time=0.35); buy_idx=1
        self.set_cap("new lowest  \u2192  buy at 1",color=AMBER)
        self.play(unscan(1),move_i(2),*hl([1]),run_time=0.55); self.wait(0.35)
        # i=2 p=5 -> profit 4
        self.set_cap("day 2:  price 5,  profit = 5 \u2212 1 = 4"); self.wait(0.4)
        self.play(*hl([4,5]),scan(2),run_time=0.5); self.wait(0.3)
        set_profit(4); self.play(unscan(2),*mark_sell(2),run_time=0.35); self.best_sell=2
        self.set_cap("4 > 0  \u2192  maxProfit = 4",color=MINT)
        self.play(move_i(3),*hl([1]),run_time=0.55); self.wait(0.35)
        # i=3 p=3 -> profit 2 not better
        self.set_cap("day 3:  price 3,  profit = 2"); self.wait(0.4)
        self.play(*hl([4]),scan(3),run_time=0.5); self.wait(0.3)
        self.set_cap("2 > 4 ?  no  \u2192  keep 4",color=GRAY)
        self.play(unscan(3),move_i(4),*hl([1]),run_time=0.55); self.wait(0.35)
        # i=4 p=6 -> profit 5 new best
        self.set_cap("day 4:  price 6,  profit = 6 \u2212 1 = 5"); self.wait(0.4)
        self.play(*hl([4,5]),scan(4),run_time=0.5); self.wait(0.3)
        set_profit(5); self.play(*unmark(2),*mark_sell(4),run_time=0.35); self.best_sell=4
        self.set_cap("5 > 4  \u2192  maxProfit = 5",color=MINT)
        self.play(move_i(5),*hl([1]),run_time=0.55); self.wait(0.35)
        # i=5 p=4 -> profit 3 not better
        self.set_cap("day 5:  price 4,  profit = 3"); self.wait(0.4)
        self.play(*hl([4]),scan(5),run_time=0.5); self.wait(0.3)
        self.set_cap("3 > 5 ?  no  \u2192  keep 5",color=GRAY)
        self.play(unscan(5),move_i(6),*hl([1]),run_time=0.55); self.wait(0.35)
        # end
        self.set_cap("maxProfit = 5   (buy 1, sell 6)",color=MINT)
        self.play(*hl([7]),self.pbx.animate.set_stroke(MINT,4.2),run_time=0.5)
        self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.pf),FadeOut(self.trackers),FadeOut(self.mvl),FadeOut(self.pvl),
                  *[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.5)
        ans=pill("max profit = 5",MINT,MINT_BG,MINT,s=0.46,h=0.7).move_to(UP*TRK_Y)
        self.play(FadeIn(ans,scale=1.05),run_time=0.5)
        self.set_cap("buy low at 1, sell high at 6  \u2192  5",color=MINT); self.wait(READ)
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
        part=pill("7 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
