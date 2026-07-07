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
ARR_Y=2.2; IDX_Y=1.62; MAP_Y=0.45; CODE_Y=-2.3
READ=0.8; READ_L=1.4

def acell(v,size=0.8,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center()).set_z_index(4)
    return VGroup(r,t)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def mentry(k,v,kc=CYAN):
    kk=Text(str(k),font=MN,weight=BOLD,color=kc).scale(0.42)
    ar=Text("\u2192",font=MN,color=GRAY).scale(0.4)
    vv=Text(str(v),font=MN,weight=BOLD,color=AMBER).scale(0.42)
    inner=VGroup(kk,ar,vv).arrange(RIGHT,buff=0.1)
    box=RoundedRectangle(width=inner.width+0.34,height=0.6,corner_radius=0.12,stroke_color=BORDER,stroke_width=2.2,fill_color=SURFACE,fill_opacity=1.0)
    inner.move_to(box.get_center())
    return VGroup(box,inner)


class LC380(Scene):
    def construct(self):
        self.persistent()
        self.problem_scene()
        self.intuition_scene()
        self.walkthrough()
        self.outro()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.4)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.4)
        self.wm=VGroup(axio,byte).arrange(RIGHT,buff=0.02).move_to(UP*WM_Y)
        badge=pill("# 380",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Insert Delete GetRandom O(1)",font=FN,weight=BOLD,color=WHITE).scale(0.52)
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
        intro=Text("Design a set with three operations:",font=FN,color=WHITE).scale(0.46).move_to(UP*2.5)
        self.play(FadeIn(intro,shift=UP*0.1),run_time=0.5)
        def opline(sig,desc,col,y):
            s=Text(sig,font=MN,weight=BOLD,color=col).scale(0.44)
            d=Text(desc,font=FN,color=GRAY).scale(0.38)
            g=VGroup(s,d).arrange(RIGHT,buff=0.25)
            if g.width>6.9: g.scale_to_fit_width(6.9)
            return g.move_to(UP*y)
        o1=opline("insert(val)","add if not already present",MINT,1.5)
        o2=opline("remove(val)","delete if present",RED,0.75)
        o3=opline("getRandom()","return a uniformly random element",CYAN,0.0)
        self.play(FadeIn(o1,shift=RIGHT*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(o2,shift=RIGHT*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(o3,shift=RIGHT*0.1),run_time=0.5)
        self.wait(READ)
        catch=Text("...and EVERY operation must run in O(1) average.",font=FN,weight=BOLD,color=AMBER).scale(0.46)
        if catch.width>6.6: catch.scale_to_fit_width(6.6)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=AMBER,stroke_width=2.8,fill_color=AMBER_BG,fill_opacity=0.5,width=catch.width+0.6,height=0.95).move_to(UP*-1.35)
        catch.move_to(cbox.get_center())
        self.play(FadeIn(cbox),FadeIn(catch),run_time=0.6)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,intro,o1,o2,o3,cbox,catch)),run_time=0.5)

    def intuition_scene(self):
        lbl=pill("The intuition",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        i1=VGroup(Text("getRandom",font=MN,weight=BOLD,color=CYAN).scale(0.44),
                  Text("uniform  \u2192  an ARRAY (random index)",font=FN,color=WHITE).scale(0.4)).arrange(RIGHT,buff=0.2)
        i2=VGroup(Text("find fast",font=MN,weight=BOLD,color=AMBER).scale(0.44),
                  Text("\u2192  a HASH MAP:  value \u2192 index",font=FN,color=WHITE).scale(0.4)).arrange(RIGHT,buff=0.2)
        for g in (i1,i2):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        i1.move_to(UP*2.3); i2.move_to(UP*1.55)
        self.play(FadeIn(i1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(i2,shift=UP*0.1),run_time=0.5)
        self.wait(READ)
        prob=Text("but deleting from the middle of an array is O(n)...",font=FN,color=RED).scale(0.42).move_to(UP*0.6)
        if prob.width>6.9: prob.scale_to_fit_width(6.9)
        self.play(FadeIn(prob,shift=UP*0.1),run_time=0.5)
        self.wait(READ)
        trick1=Text("the trick:  swap the target with the LAST element,",font=FN,weight=BOLD,color=MINT).scale(0.44)
        trick2=Text("then pop.  Order doesn't matter in a set!",font=FN,weight=BOLD,color=MINT).scale(0.44)
        for g in (trick1,trick2):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        trick1.move_to(UP*-0.4); trick2.next_to(trick1,DOWN,buff=0.22)
        self.play(FadeIn(trick1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(trick2,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,i1,i2,prob,trick1,trick2)),run_time=0.5)

    def walkthrough(self):
        vlab=Text("v",font=MN,weight=BOLD,color=WHITE).scale(0.5)
        mlab=Text("map",font=MN,weight=BOLD,color=WHITE).scale(0.42)
        vals=[1,2,3]
        self.cells=[acell(v) for v in vals]
        row=VGroup(*self.cells).arrange(RIGHT,buff=0.16).move_to([0.35,ARR_Y,0])
        vlab.next_to(row,LEFT,buff=0.3)
        self.idxs=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.36).move_to([self.cells[i].get_center()[0],IDX_Y,0]) for i in range(3)])
        self.mp={}
        for i,v in enumerate(vals): self.mp[v]=mentry(v,i)
        maprow=VGroup(*[self.mp[v] for v in vals]).arrange(RIGHT,buff=0.2).move_to([0.35,MAP_Y,0])
        mlab.next_to(maprow,LEFT,buff=0.3)

        rlbl=Text("remove(val)",font=MN,weight=BOLD,color=WHITE).scale(0.38)
        raw=[(0,"if (!idx.count(val)) return false;"),
             (0,"int i = idx[val];"),
             (0,"v[i] = v.back();  idx[v[i]] = i;"),
             (0,"v.pop_back();  idx.erase(val);"),
             (0,"return true;")]
        code=VGroup()
        for _,s in raw: code.add(Text(s,font=MN,color="#9AA6B4").scale(0.35))
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.14)
        if code.width>5.6: code.scale(5.6/code.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=code.width+0.6,height=code.height+0.45)
        panel.move_to(UP*CODE_Y); code.move_to(panel.get_center())
        rlbl.next_to(panel,UP,buff=0.14)
        self.code=list(code); self.panel=panel; self.rlbl=rlbl; self._act=[]

        def hl(idxs):
            a=[self.code[i].animate.set_color("#9AA6B4") for i in self._act]
            a+=[self.code[i].animate.set_color(CYAN) for i in idxs]; self._act=idxs; return a

        # insert (build)
        self.set_cap("insert:  append to the array + record its index")
        self.play(FadeIn(vlab),FadeIn(mlab),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in self.cells],lag_ratio=0.15),FadeIn(self.idxs),run_time=0.9)
        self.play(LaggedStart(*[FadeIn(self.mp[k],shift=UP*0.1) for k in vals],lag_ratio=0.15),run_time=0.8)
        self.wait(READ)
        # getRandom
        self.set_cap("getRandom:  v[ random index ]  \u2014  O(1)",color=CYAN)
        self.play(self.cells[2][0].animate.set_stroke(CYAN,4.6),run_time=0.4)
        gr=Text("\u2192 3",font=MN,weight=BOLD,color=CYAN).scale(0.5).next_to(row,RIGHT,buff=0.45)
        self.play(FadeIn(gr,shift=RIGHT*0.1),run_time=0.4); self.wait(0.5)
        self.play(FadeOut(gr),self.cells[2][0].animate.set_stroke(BORDER,3.0),run_time=0.4)
        # show remove code
        self.play(FadeIn(panel),FadeIn(rlbl),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.08) for l in self.code],lag_ratio=0.07),run_time=0.7)

        # remove(2)
        self.set_cap("remove(2):  the map says it's at index 1",color=AMBER)
        self.play(*hl([0,1]),self.mp[2][0].animate.set_stroke(AMBER,4.0),
                  self.cells[1][0].animate.set_stroke(AMBER,4.6),run_time=0.55)
        self.wait(0.5)
        self.set_cap("swap the LAST element (3) into that slot",color=MINT)
        self.play(self.cells[2][0].animate.set_stroke(MINT,4.6),run_time=0.35)
        old2=self.cells[1][1]; last3=self.cells[2][1]
        self.play(*hl([2]),last3.animate.move_to(self.cells[1][0].get_center()),
                  old2.animate.set_opacity(0),run_time=0.7)
        self.remove(old2)
        self.cells[1]=VGroup(self.cells[1][0],last3)
        self.play(self.cells[1][0].animate.set_stroke(MINT,4.0),run_time=0.2)
        new3=mentry(3,1).move_to(self.mp[3].get_center())
        self.play(FadeOut(self.mp[3]),FadeIn(new3),run_time=0.4)
        self.mp[3]=new3
        self.wait(0.4)
        self.set_cap("pop the last slot  \u2014  O(1), no shifting",color=MINT)
        self.play(*hl([3]),FadeOut(self.cells[2][0]),FadeOut(self.idxs[2]),run_time=0.55)
        self.cells=self.cells[:2]
        # erase map[2], slide 3 into its slot
        pos2=self.mp[2].get_center()
        self.set_cap("erase 2 from the map",color=RED)
        self.play(FadeOut(self.mp[2]),self.mp[3].animate.move_to(pos2),run_time=0.5)
        del self.mp[2]
        self.play(*hl([4]),self.cells[1][0].animate.set_stroke(BORDER,3.0),run_time=0.4)
        self.set_cap("done in O(1)  \u2014  v = [1, 3],  map = {1\u21920, 3\u21921}",color=MINT)
        self.wait(READ_L)
        self._extras=VGroup(vlab,mlab,self.idxs[0],self.idxs[1],row,self.mp[1],self.mp[3])

    def outro(self):
        self.play(*[FadeOut(m) for m in [self.panel,self.rlbl]+self.code],run_time=0.35)
        self.set_cap("array for random access  +  map for O(1) lookup",color=MINT); self.wait(READ)
        rows=VGroup(
            Text("insert      O(1)",font=MN,weight=BOLD,color=MINT).scale(0.46),
            Text("remove      O(1)",font=MN,weight=BOLD,color=RED).scale(0.46),
            Text("getRandom   O(1)",font=MN,weight=BOLD,color=CYAN).scale(0.46),
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=rows.width+0.8,height=rows.height+0.6)
        rows.move_to(cbox.get_center())
        badge=VGroup(cbox,rows).move_to(UP*-1.4)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("12 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
