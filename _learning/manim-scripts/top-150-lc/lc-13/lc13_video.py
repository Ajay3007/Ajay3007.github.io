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
ARR_Y=1.95; TOT_Y=0.35; CODE_Y=-2.6
SZ=0.72
READ=0.8; READ_L=1.4

VAL={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
S="MCMXCIV"

def cell(v,size=SZ,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.62*size).move_to(r.get_center()).set_z_index(5)
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

def statbox(label,val,color):
    lab=Text(label,font=MN,color=GRAY).scale(0.36)
    v=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62)
    col=VGroup(lab,v).arrange(DOWN,buff=0.1)
    box=RoundedRectangle(width=max(col.width+0.8,2.0),height=col.height+0.6,corner_radius=0.14,
                         stroke_color=color,stroke_width=2.6,fill_color=SURFACE,fill_opacity=1.0)
    col.move_to(box.get_center())
    return VGroup(box,col),v


class LC13(Scene):
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
        badge=pill("# 13",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Roman to Integer",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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

    def legend(self):
        items=[("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
        g=VGroup()
        for sym,val in items:
            t=Text("%s = %d" % (sym,val),font=MN,weight=BOLD,color=WHITE).scale(0.34)
            b=RoundedRectangle(width=t.width+0.35,height=0.5,corner_radius=0.1,stroke_color=BORDER,stroke_width=2.0,fill_color=SURFACE,fill_opacity=1.0)
            t.move_to(b.get_center()); g.add(VGroup(b,t))
        top=VGroup(*g[:4]).arrange(RIGHT,buff=0.16)
        bot=VGroup(*g[4:]).arrange(RIGHT,buff=0.16)
        table=VGroup(top,bot).arrange(DOWN,buff=0.18)
        if table.width>6.9: table.scale_to_fit_width(6.9)
        return table

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Convert a Roman numeral to its integer value.",font=FN,color=WHITE).scale(0.44)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t1.move_to(UP*2.7)
        self.play(FadeIn(t1),run_time=0.5)
        table=self.legend().move_to(UP*1.4)
        self.play(FadeIn(table,shift=UP*0.1),run_time=0.8)
        self.wait(READ_L)
        t2=Text("Usually you just add the symbols…",font=FN,color=GRAY).scale(0.42).move_to(UP*-0.3)
        t3=Text("…but a small symbol BEFORE a bigger one means subtract.",font=FN,color=AMBER).scale(0.4).move_to(UP*-0.95)
        for t in (t2,t3):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        self.play(FadeIn(t2,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(t3,shift=UP*0.1),run_time=0.5)
        self.wait(0.4)
        pairs=Text("IV=4   IX=9   XL=40   XC=90   CD=400   CM=900",font=MN,color=CYAN).scale(0.36).move_to(UP*-1.75)
        if pairs.width>6.9: pairs.scale_to_fit_width(6.9)
        self.play(FadeIn(pairs,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,table,t2,t3,pairs)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Scan left to right, one symbol at a time.",font=FN,weight=BOLD,color=WHITE).scale(0.46)
        h2=Text("Add its value…",font=FN,color=MINT).scale(0.46)
        h3=Text("…unless the next symbol is bigger.",font=FN,color=AMBER).scale(0.46)
        h4=Text("Then this one is a discount — subtract it.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3,h4):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.0); h2.next_to(h1,DOWN,buff=0.34)
        h3.next_to(h2,DOWN,buff=0.24); h4.next_to(h3,DOWN,buff=0.34)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45); self.play(FadeIn(h3,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(h4,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("One pass, compare to the neighbor",font=FN,weight=BOLD,color=WHITE).scale(0.5).move_to(UP*2.3)
        if a0.width>6.9: a0.scale_to_fit_width(6.9)
        a1=Text("v[i] = value of symbol i",font=MN,color=WHITE).scale(0.4).move_to(UP*1.4)
        a2=Text("v[i] < v[i+1]   →   total -= v[i]",font=MN,color=AMBER).scale(0.4).move_to(UP*0.7)
        a3=Text("otherwise        →   total += v[i]",font=MN,color=MINT).scale(0.4).move_to(UP*0.0)
        a4=Text("last symbol is always added",font=FN,color=GRAY).scale(0.38).move_to(UP*-0.75)
        for g in (a1,a2,a3,a4):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.45); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.4)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        n=len(S); v=[VAL[ch] for ch in S]
        self.cells=[cell(ch) for ch in S]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.14).move_to(UP*ARR_Y)
        slab=Text("s",font=MN,weight=BOLD,color=WHITE).scale(0.4).next_to(row,LEFT,buff=0.22)
        vlab=VGroup(*[Text(str(v[i]),font=MN,color=GRAY).scale(0.3).next_to(self.cells[i],DOWN,buff=0.16) for i in range(n)])

        raw=[(0,"int total = 0;"),
             (0,"for (int i = 0; i < n; i++)"),
             (1,"if (i+1 < n && v[i] < v[i+1])"),
             (2,"total -= v[i];"),
             (1,"else"),
             (2,"total += v[i];"),
             (0,"return total;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.34))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.12)
        for line,(ind,_) in zip(code,raw): line.shift(RIGHT*ind*0.32)
        if code.width>6.2: code.scale(6.2/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        self.code=list(code); self.panel=panel; self._act=[]

        self.play(FadeIn(slab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in self.cells],lag_ratio=0.08),run_time=1.0)
        self.play(FadeIn(vlab),run_time=0.4)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.06),run_time=0.85)

        self.tg,self.tv=statbox("total",0,CYAN)
        self.tg.move_to(UP*TOT_Y)
        self.play(FadeIn(self.tg,shift=UP*0.1),run_time=0.45)

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a
        def set_total(val,color=CYAN):
            new=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62).move_to(self.tv)
            return Transform(self.tv,new)

        self.pi=pointer("i",CYAN,up=True).next_to(self.cells[0],UP,buff=0.12)
        self.play(FadeIn(self.pi,shift=DOWN*0.15),*hl([0]),run_time=0.5)
        self.set_cap("total starts at 0"); self.wait(READ*0.7)

        total=0
        for i in range(n):
            self.play(self.pi.animate.next_to(self.cells[i],UP,buff=0.12),*hl([2]),run_time=0.4)
            sub=(i+1<n and v[i]<v[i+1])
            if sub:
                total-=v[i]
                self.set_cap("%s(%d) before %s(%d)  →  subtract %d" % (S[i],v[i],S[i+1],v[i+1],v[i]),color=AMBER,scale=0.42)
                self.play(*hl([2,3]),
                          self.cells[i][0].animate.set_stroke(AMBER,4.8).set_fill(AMBER_BG,1.0),
                          self.cells[i+1][0].animate.set_stroke(CYAN,4.2),run_time=0.5)
                self.play(set_total(total,AMBER),run_time=0.4)
                self.play(self.cells[i+1][0].animate.set_stroke(BORDER,3.0),run_time=0.2)
            else:
                total+=v[i]
                self.set_cap("%s = %d  →  add it" % (S[i],v[i]),color=MINT,scale=0.44)
                self.play(*hl([4,5]),
                          self.cells[i][0].animate.set_stroke(MINT,4.8).set_fill(MINT_BG,1.0),run_time=0.5)
                self.play(set_total(total,MINT),run_time=0.4)
            self.play(self.cells[i][0].animate.set_stroke(BORDER,3.0).set_fill(SURFACE,1.0),run_time=0.2)
        self.total_final=total
        self.play(FadeOut(self.pi),*hl([6]),run_time=0.4); self.wait(0.3)

    def outro(self):
        self.play(*[self.code[i].animate.set_color("#9AA6B4") for i in self._act],run_time=0.3)
        self.set_cap("CM=900, XC=90, IV=4 — the three subtractions",color=AMBER)
        ans=pill("MCMXCIV  =  %d" % self.total_final,MINT,MINT_BG,MINT,s=0.5,h=0.72).move_to(UP*TOT_Y)
        self.play(FadeOut(self.tg),FadeIn(ans,scale=1.05),run_time=0.5)
        self.wait(READ_L)
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
        part=pill("17 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
