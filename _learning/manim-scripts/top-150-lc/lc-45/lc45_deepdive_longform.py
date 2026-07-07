from manim import *

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"

config.pixel_width=1920
config.pixel_height=1080
config.frame_width=16.0
config.frame_height=9.0
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"
R=1.0; RL=1.8; RX=2.4

def wordmark(s=0.5):
    a=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(s)
    b=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(s)
    return VGroup(a,b).arrange(RIGHT,buff=0.02)

def pill(text,tc,bg,st,s=0.45,h=0.64):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def acell(v,size=0.9,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.12,stroke_color=stroke,stroke_width=3.0,fill_color=fill,fill_opacity=1.0)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center())
    return VGroup(r,t)

def tnode(i,stroke=CYAN,fill=SURFACE):
    r=RoundedRectangle(width=1.4,height=0.8,corner_radius=0.16,stroke_color=stroke,stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(f"mJ({i})",font=MN,weight=BOLD,color=WHITE).scale(0.44).move_to(r.get_center()).set_z_index(3)
    return VGroup(r,t)

# shared tree layout (nums = [2,3,1,4])
TREE={"0":(0,3.0),"1":(-3.8,1.0),"2b":(4.2,1.0),"2a":(-5.6,-1.05),"3b":(-2.2,-1.05),"3c":(4.2,-1.05),"3a":(-5.6,-2.5)}
LBL={"0":"0","1":"1","2b":"2","2a":"2","3b":"3","3c":"3","3a":"3"}
EDGES=[("0","1"),("0","2b"),("1","2a"),("1","3b"),("2a","3a"),("2b","3c")]

class Base(Scene):
    def wm_add(self):
        self.wm=wordmark(0.5).to_corner(UL,buff=0.5); self.add(self.wm)
    def head(self,txt,color=CYAN):
        t=Text(txt,font=FN,weight=BOLD,color=color).scale(0.62).to_edge(UP,buff=0.55)
        self.play(FadeIn(t,shift=DOWN*0.1),run_time=0.4); return t
    def cap(self,txt,color=WHITE,s=0.55,y=-3.7):
        t=Text(txt,font=FN,color=color).scale(s)
        if t.width>14.5: t.scale_to_fit_width(14.5)
        t.move_to([0,y,0]); return t


class Seg1(Base):
    def construct(self):
        self.wm_add()
        # title card
        title=Text("Jump Game II",font=FN,weight=BOLD,color=WHITE).scale(1.3).move_to(UP*1.2)
        sub=Text("from Recursion to Memoization",font=FN,color=CYAN).scale(0.65).next_to(title,DOWN,buff=0.35)
        self.play(FadeIn(title,shift=UP*0.15),run_time=0.7)
        self.play(FadeIn(sub,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(wordmark(0.85).move_to(DOWN*1.7),shift=UP*0.1),run_time=0.5)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)
        # problem
        h=self.head("The problem")
        vals=[2,3,1,4]
        row=VGroup(*[acell(v) for v in vals]).arrange(RIGHT,buff=0.2).move_to(UP*1.9)
        idx=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.42).next_to(row[i],DOWN,buff=0.18) for i in range(4)])
        nlab=Text("nums",font=MN,weight=BOLD,color=WHITE).scale(0.45).next_to(row,LEFT,buff=0.3)
        self.play(FadeIn(nlab),LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in row],lag_ratio=0.1),run_time=0.9)
        self.play(FadeIn(idx),run_time=0.4)
        p1=Text("nums[i] = the max jump length from index i.",font=FN,color=WHITE).scale(0.55).move_to(DOWN*0.2)
        p2=Text("What is the FEWEST jumps to reach the last index?",font=FN,color=MINT).scale(0.55).next_to(p1,DOWN,buff=0.3)
        self.play(FadeIn(p1,shift=UP*0.1),run_time=0.5); self.play(FadeIn(p2,shift=UP*0.1),run_time=0.5)
        self.wait(RL)
        self.play(FadeOut(VGroup(p1,p2)),FadeOut(h),run_time=0.4)
        # intuition
        h2=self.head("The key idea",MINT)
        i1=Text("Say you're standing at index 0.  Its value is 2,",font=FN,color=WHITE).scale(0.55).move_to(UP*0.25)
        i2=Text("so a single jump can land on index 1 or index 2.",font=FN,color=WHITE).scale(0.55).next_to(i1,DOWN,buff=0.25)
        self.play(FadeIn(i1),run_time=0.5); self.play(FadeIn(i2),run_time=0.5)
        row[0][0].set_stroke(CYAN,4.5)
        a1=CurvedArrow(row[0].get_top()+UP*0.03,row[1].get_top()+UP*0.03,angle=-PI*0.6,color=CYAN,stroke_width=4,tip_length=0.18)
        a2=CurvedArrow(row[0].get_top()+UP*0.03,row[2].get_top()+UP*0.03,angle=-PI*0.5,color=AMBER,stroke_width=4,tip_length=0.18)
        self.play(row[0][0].animate.set_stroke(CYAN,4.5),Create(a1),run_time=0.5)
        self.play(Create(a2),run_time=0.5)
        self.wait(R)
        self.play(FadeOut(VGroup(i1,i2)),run_time=0.35)
        i3=Text("Whichever you choose, you still need the fewest jumps",font=FN,color=WHITE).scale(0.55).move_to(UP*0.25)
        i4=Text("to finish FROM THERE.  So:",font=FN,color=WHITE).scale(0.55).next_to(i3,DOWN,buff=0.25)
        self.play(FadeIn(i3),run_time=0.5); self.play(FadeIn(i4),run_time=0.5); self.wait(R)
        eq=VGroup(
            Text("minJump(0)",font=MN,weight=BOLD,color=WHITE).scale(0.6),
            Text("= 1 +",font=MN,weight=BOLD,color=WHITE).scale(0.6),
            Text("min(",font=MN,weight=BOLD,color=WHITE).scale(0.6),
            Text("minJump(1)",font=MN,weight=BOLD,color=CYAN).scale(0.6),
            Text(",",font=MN,weight=BOLD,color=WHITE).scale(0.6),
            Text("minJump(2)",font=MN,weight=BOLD,color=AMBER).scale(0.6),
            Text(")",font=MN,weight=BOLD,color=WHITE).scale(0.6),
        ).arrange(RIGHT,buff=0.18).move_to(DOWN*1.5)
        self.play(FadeOut(VGroup(i3,i4)),run_time=0.3)
        self.play(FadeIn(eq,shift=UP*0.1),run_time=0.7)
        one=Text("the jump you take now",font=FN,color=MINT).scale(0.42).next_to(eq[1],DOWN,buff=0.45)
        self.play(FadeIn(one,shift=UP*0.1),run_time=0.5)
        self.wait(RL)
        self.play(FadeOut(one),run_time=0.3)
        # optimal substructure
        os1=Text("The best way to finish from a square depends only on the square \u2014",font=FN,color=MINT).scale(0.5).move_to(DOWN*2.7)
        os2=Text("not on how you got there.  That's why we can solve it piece by piece.",font=FN,color=MINT).scale(0.5).next_to(os1,DOWN,buff=0.2)
        for g in (os1,os2):
            if g.width>15: g.scale_to_fit_width(15)
        self.play(FadeIn(os1),run_time=0.5); self.play(FadeIn(os2),run_time=0.5)
        self.wait(RX)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)


class Seg2(Base):
    def construct(self):
        self.wm_add()
        h=self.head("The recurrence")
        base=VGroup(Text("base:",font=MN,weight=BOLD,color=AMBER).scale(0.62),
                    Text("minJump(i) = 0    if i is the last index",font=MN,color=WHITE).scale(0.55)).arrange(RIGHT,buff=0.3).move_to(UP*2.6)
        bnote=Text("already at the goal \u2014 zero jumps needed",font=FN,color=GRAY).scale(0.45).next_to(base,DOWN,buff=0.2)
        rec=VGroup(Text("else:",font=MN,weight=BOLD,color=CYAN).scale(0.62),
                   Text("minJump(i) = 1 + min( minJump(j) )   for every reachable j",font=MN,color=WHITE).scale(0.5)).arrange(RIGHT,buff=0.3).move_to(UP*1.1)
        for g in (base,rec):
            if g.width>15: g.scale_to_fit_width(15)
        self.play(FadeIn(base,shift=UP*0.1),run_time=0.5); self.play(FadeIn(bnote),run_time=0.4); self.wait(R)
        self.play(FadeIn(rec,shift=UP*0.1),run_time=0.5); self.wait(RL)
        self.play(FadeOut(bnote),run_time=0.3)
        # code, explained
        raw=["int minJump(int i) {",
             "    if (i >= n - 1) return 0;",
             "    int best = INT_MAX - 1;",
             "    for (int j = 1; j <= nums[i]; j++)",
             "        if (i + j < n)",
             "            best = min(best, minJump(i + j));",
             "    return best + 1;",
             "}"]
        code=VGroup(*[Text(s,font=MN,color=WHITE).scale(0.46) for s in raw])
        code.arrange(DOWN,aligned_edge=LEFT,buff=0.17)
        if code.width>7.8: code.scale(7.8/code.width)
        panel=RoundedRectangle(corner_radius=0.18,stroke_color=BORDER,stroke_width=2.6,fill_color="#0F1420",fill_opacity=1.0,width=code.width+1.0,height=code.height+0.7)
        grp=VGroup(panel,code); code.move_to(panel.get_center())
        grp.move_to(LEFT*3.2+DOWN*1.3)
        self.play(rec.animate.move_to(UP*3.0),FadeOut(base),run_time=0.5)
        self.play(FadeIn(panel),run_time=0.4)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.1) for l in code],lag_ratio=0.1),run_time=1.1)
        self.wait(0.6)
        notes=[(1,"base case: 0 at the end",AMBER),
               (3,"try every reachable jump",CYAN),
               (5,"keep the cheapest finish",MINT),
               (6,"+1 for this jump",MINT)]
        arrows=[]
        for li,txt,col in notes:
            ln=code[li]
            note=Text(txt,font=FN,color=col).scale(0.46)
            note.next_to(grp,RIGHT,buff=0.7).set_y(ln.get_y())
            ar=Arrow(note.get_left()+LEFT*0.05,ln.get_right()+RIGHT*0.12,buff=0.1,color=col,stroke_width=3,max_tip_length_to_length_ratio=0.35)
            self.play(ln.animate.set_color(col),Create(ar),FadeIn(note,shift=LEFT*0.1),run_time=0.55)
            arrows.append(VGroup(ar,note)); self.wait(0.7)
        self.wait(R)
        end=Text("This is correct... but let's watch it actually run.",font=FN,weight=BOLD,color=WHITE).scale(0.55).move_to(DOWN*3.6)
        self.play(FadeIn(end,shift=UP*0.1),run_time=0.5)
        self.wait(RL)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)


class Seg3(Base):
    def construct(self):
        self.wm_add()
        self.h=self.head("Trace it:  the recursion tree")
        self.nodes={}; self.edges={}; self.vals={}
        for k,(x,y) in TREE.items():
            self.nodes[k]=tnode(LBL[k]).move_to([x,y,0])
        for a,b in EDGES:
            self.edges[(a,b)]=Line(self.nodes[a].get_bottom(),self.nodes[b].get_top(),color=BORDER,stroke_width=2.6).set_z_index(1)
        self.capm=None

        def setcap(txt,color=WHITE):
            new=self.cap(txt,color,y=-4.0)
            if self.capm is None: self.capm=new; self.play(FadeIn(new),run_time=0.35); return
            self.play(FadeOut(self.capm),run_time=0.18); self.play(FadeIn(new),run_time=0.28); self.capm=new
        def enter(k,parent=None,color=CYAN):
            anims=[FadeIn(self.nodes[k],scale=0.7)]
            if parent is not None: anims.append(Create(self.edges[(parent,k)]))
            self.play(*anims,run_time=0.45)
            self.play(self.nodes[k][0].animate.set_stroke(color,4.6),run_time=0.25)
        def base0(k):
            b=self.badge(k,"0",AMBER); return b
        def ret(k,val,color=MINT):
            self.badge(k,str(val),color)
            self.play(self.nodes[k][0].animate.set_stroke(BORDER,3.0),run_time=0.2)

        enter("0"); setcap("call minJump(0)")
        self.wait(0.5)
        setcap("from 0 you can reach index 1  \u2192  call minJump(1)",CYAN)
        enter("1","0"); self.wait(0.4)
        setcap("from 1 you can reach index 2  \u2192  call minJump(2)")
        enter("2a","1"); self.wait(0.4)
        setcap("from 2 you can reach index 3  \u2192  call minJump(3)")
        enter("3a","2a"); self.wait(0.3)
        setcap("index 3 is the last index  \u2192  base case = 0",AMBER)
        base0("3a"); self.wait(0.6)
        setcap("so minJump(2) = 1 + 0 = 1",MINT)
        ret("2a",1); self.wait(0.6)
        setcap("back in minJump(1): also try index 3  \u2192  minJump(3) again")
        enter("3b","1"); base0("3b"); self.wait(0.5)
        setcap("minJump(1) = 1 + min(1, 0) = 1",MINT)
        ret("1",1); self.wait(0.6)
        setcap("back in minJump(0): try index 2  \u2192  minJump(2) again")
        enter("2b","0"); self.wait(0.4)
        setcap("...which calls minJump(3) yet again")
        enter("3c","2b"); base0("3c"); self.wait(0.4)
        setcap("minJump(2) = 1 + 0 = 1",MINT); ret("2b",1); self.wait(0.5)
        setcap("minJump(0) = 1 + min(1, 1) = 2",MINT)
        self.play(self.nodes["0"][0].animate.set_stroke(MINT,4.8),run_time=0.3)
        self.badge("0","2",MINT)
        ans=pill("answer = 2",MINT,MINT_BG,MINT,s=0.55,h=0.72).next_to(self.nodes["0"],RIGHT,buff=0.6)
        self.play(FadeIn(ans,scale=1.05),run_time=0.5); self.wait(RL)
        # repeated work
        self.play(FadeOut(self.h),run_time=0.2)
        h2=Text("Notice the waste",font=FN,weight=BOLD,color=RED).scale(0.62).to_edge(UP,buff=0.55)
        self.play(FadeIn(h2,shift=DOWN*0.1),run_time=0.4)
        setcap("minJump(3) solved 3 times  \u00b7  minJump(2) solved twice",RED)
        self.play(self.nodes["3a"][0].animate.set_stroke(RED,4.4),self.nodes["3b"][0].animate.set_stroke(RED,4.4),
                  self.nodes["3c"][0].animate.set_stroke(RED,4.4),run_time=0.5)
        self.play(self.nodes["2a"][0].animate.set_stroke(RED,4.4),self.nodes["2b"][0].animate.set_stroke(RED,4.4),run_time=0.5)
        self.wait(RL)
        setcap("more indices  \u2192  the same work repeats exponentially",RED)
        self.wait(RX)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)

    def badge(self,k,val,color):
        nd=self.nodes[k]
        b=Text(f"= {val}",font=MN,weight=BOLD,color=color).scale(0.44)
        b.move_to(nd.get_center()+RIGHT*0.62+DOWN*0.64)
        dot=RoundedRectangle(width=b.width+0.2,height=0.44,corner_radius=0.1,stroke_color=color,stroke_width=2.0,fill_color=BG,fill_opacity=0.95).move_to(b.get_center()).set_z_index(4)
        b.set_z_index(5)
        self.play(FadeIn(dot,scale=0.8),FadeIn(b,scale=0.8),run_time=0.3)
        return VGroup(dot,b)


class Seg4(Base):
    def construct(self):
        self.wm_add()
        self.h=self.head("The fix:  memoize",MINT)
        # memo table top-right
        cells=[]; labels=[]
        for i in range(4):
            c=acell("-1",0.85,BORDER,SURFACE,GRAY)
            cells.append(c)
        table=VGroup(*cells).arrange(RIGHT,buff=0.12).to_corner(UR,buff=0.7).shift(DOWN*0.3+LEFT*0.2)
        idxs=VGroup(*[Text(str(i),font=MN,color=GRAY).scale(0.36).next_to(cells[i],UP,buff=0.12) for i in range(4)])
        mlab=Text("memo",font=MN,weight=BOLD,color=MINT).scale(0.42).next_to(table,LEFT,buff=0.3)
        self.cells=cells
        self.play(FadeIn(mlab),FadeIn(table),FadeIn(idxs),run_time=0.6)
        note=Text("store each answer the first time; reuse it after",font=FN,color=MINT).scale(0.5).move_to([-2.5,3.0,0])
        if note.width>9: note.scale_to_fit_width(9)
        self.play(FadeIn(note),run_time=0.5); self.wait(R)

        # tree (memoized, DFS) on left/center
        self.nodes={}; self.edges={}
        for k,(x,y) in TREE.items():
            xx=x*0.78-1.2; yy=y*0.92-0.4
            self.nodes[k]=tnode(LBL[k]).move_to([xx,yy,0])
        for a,b in EDGES:
            self.edges[(a,b)]=Line(self.nodes[a].get_bottom(),self.nodes[b].get_top(),color=BORDER,stroke_width=2.4).set_z_index(1)
        self.capm=None
        def setcap(txt,color=WHITE):
            new=self.cap(txt,color,s=0.52,y=-3.9)
            if self.capm is None: self.capm=new; self.play(FadeIn(new),run_time=0.3); return
            self.play(FadeOut(self.capm),run_time=0.16); self.play(FadeIn(new),run_time=0.26); self.capm=new
        def enter(k,parent=None):
            anims=[FadeIn(self.nodes[k],scale=0.7)]
            if parent is not None: anims.append(Create(self.edges[(parent,k)]))
            self.play(*anims,run_time=0.4)
        def store(i,val):
            new=Text(str(val),font=FN,weight=BOLD,color=MINT).scale(0.5).move_to(self.cells[i][0].get_center())
            self.play(self.cells[i][0].animate.set_stroke(MINT,4.0),FadeOut(self.cells[i][1]),FadeIn(new,scale=1.2),run_time=0.45)
            self.cells[i][1]=new
        def hit(i):
            self.play(Indicate(self.cells[i],color=CYAN,scale_factor=1.25),run_time=0.6)

        enter("0"); enter("1","0"); enter("2a","1"); enter("3a","2a")
        setcap("first time reaching index 3  \u2192  compute 0, store memo[3]",AMBER)
        b=self.badge("3a","0",AMBER); store(3,0); self.wait(0.5)
        setcap("minJump(2)=1, store memo[2]",MINT); self.badge("2a","1",MINT); store(2,1); self.wait(0.5)
        # cache hit for mJ(3) under mJ(1)
        setcap("minJump(1) also needs minJump(3) \u2014 but it's in memo!",CYAN)
        gh=tnode("3",GRAY,SURFACE).move_to([self.nodes["1"].get_center()[0]+1.6,self.nodes["1"].get_center()[1]-1.9,0]).set_opacity(0.5)
        ge=Line(self.nodes["1"].get_bottom(),gh.get_top(),color=BORDER,stroke_width=2.0).set_z_index(1)
        self.play(Create(ge),FadeIn(gh),run_time=0.4)
        hit(3)
        ct=Text("cached \u2192 0",font=MN,weight=BOLD,color=GRAY).scale(0.36).next_to(gh,DOWN,buff=0.12)
        self.play(FadeIn(ct),run_time=0.3); self.wait(0.6)
        setcap("minJump(1)=1, store memo[1]",MINT); self.badge("1","1",MINT); store(1,1); self.wait(0.5)
        # cache hit for mJ(2) under mJ(0) -> prunes whole subtree
        setcap("minJump(0) needs minJump(2) \u2014 already in memo, skip the whole subtree",CYAN)
        gh2=tnode("2",GRAY,SURFACE).move_to([self.nodes["0"].get_center()[0]+2.6,self.nodes["0"].get_center()[1]-1.9,0]).set_opacity(0.5)
        ge2=Line(self.nodes["0"].get_bottom(),gh2.get_top(),color=BORDER,stroke_width=2.0).set_z_index(1)
        self.play(Create(ge2),FadeIn(gh2),run_time=0.4)
        hit(2)
        ct2=Text("cached \u2192 1",font=MN,weight=BOLD,color=GRAY).scale(0.36).next_to(gh2,DOWN,buff=0.12)
        self.play(FadeIn(ct2),run_time=0.3); self.wait(0.6)
        setcap("minJump(0) = 1 + min(1,1) = 2, store memo[0]",MINT)
        self.play(self.nodes["0"][0].animate.set_stroke(MINT,4.8),run_time=0.3)
        self.badge("0","2",MINT); store(0,2); self.wait(0.8)
        setcap("every index solved once \u2014 the grey calls were free",MINT)
        self.wait(RL)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)
        self.capm=None
        # complexity + memo code lines
        h2=Text("Why O(n\u00b2)?",font=FN,weight=BOLD,color=CYAN).scale(0.62).to_edge(UP,buff=0.55)
        self.play(FadeIn(h2,shift=DOWN*0.1),run_time=0.4)
        c1=Text("n subproblems (one per index)",font=FN,color=WHITE).scale(0.55).move_to(UP*2.0)
        c2=Text("\u00d7  up to n work each (the loop over jumps)",font=FN,color=WHITE).scale(0.55).next_to(c1,DOWN,buff=0.28)
        c3=Text("=  O(n\u00b2) time,   O(n) space for the memo",font=MN,weight=BOLD,color=MINT).scale(0.58).next_to(c2,DOWN,buff=0.4)
        for g in (c1,c2,c3):
            if g.width>14: g.scale_to_fit_width(14)
        self.play(FadeIn(c1),run_time=0.5); self.play(FadeIn(c2),run_time=0.5); self.wait(0.5)
        self.play(FadeIn(c3,scale=1.03),run_time=0.6); self.wait(R)
        add=Text("the two lines that make it a DP:",font=FN,color=GRAY).scale(0.5).move_to(DOWN*0.6)
        l1=Text("if (memo[i] != -1) return memo[i];",font=MN,weight=BOLD,color=CYAN).scale(0.55).next_to(add,DOWN,buff=0.3)
        l2=Text("memo[i] = best + 1;",font=MN,weight=BOLD,color=MINT).scale(0.55).next_to(l1,DOWN,buff=0.25)
        self.play(FadeIn(add),run_time=0.4)
        self.play(FadeIn(l1,shift=UP*0.1),run_time=0.45); self.play(FadeIn(l2,shift=UP*0.1),run_time=0.45)
        self.wait(RX)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)

    def badge(self,k,val,color):
        nd=self.nodes[k]
        b=Text(f"={val}",font=MN,weight=BOLD,color=color).scale(0.4)
        b.move_to(nd.get_center()+RIGHT*0.55+DOWN*0.6)
        dot=RoundedRectangle(width=b.width+0.16,height=0.4,corner_radius=0.09,stroke_color=color,stroke_width=2.0,fill_color=BG,fill_opacity=0.95).move_to(b.get_center()).set_z_index(4)
        b.set_z_index(5)
        self.play(FadeIn(dot,scale=0.8),FadeIn(b,scale=0.8),run_time=0.28)
        return VGroup(dot,b)


class Seg5(Base):
    def construct(self):
        self.wm_add()
        steps=VGroup(
            Text("1.  intuition:  1 jump  +  best finish from where you land",font=FN,color=WHITE).scale(0.55),
            Text("2.  recurrence:  minJump(i) = 1 + min(minJump(reachable))",font=FN,color=WHITE).scale(0.55),
            Text("3.  plain recursion re-solves subproblems  \u2192  exponential",font=FN,color=RED).scale(0.55),
            Text("4.  memoize  \u2192  each index once  \u2192  O(n\u00b2) time, O(n) space",font=FN,color=MINT).scale(0.55),
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.4).move_to(UP*1.2)
        for g in steps:
            if g.width>14.5: g.scale_to_fit_width(14.5)
        self.head("The journey")
        for s in steps:
            self.play(FadeIn(s,shift=RIGHT*0.1),run_time=0.5); self.wait(0.35)
        self.wait(R)
        g=Text("the greedy \"jump levels\" trick then reaches O(n) \u2014 see the short.",font=FN,weight=BOLD,color=CYAN).scale(0.55).move_to(DOWN*1.6)
        if g.width>14.5: g.scale_to_fit_width(14.5)
        self.play(FadeIn(g,shift=UP*0.1),run_time=0.6)
        self.wait(RL)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.wm],run_time=0.5)
        wm=wordmark(1.05).move_to(UP*0.6)
        cta=Text("Subscribe to @axiobyte  \u00b7  LeetCode Top Interview 150, visually explained",font=FN,weight=BOLD,color=CYAN).scale(0.5).next_to(wm,DOWN,buff=0.5)
        if cta.width>15: cta.scale_to_fit_width(15)
        self.play(FadeIn(wm,shift=UP*0.1),run_time=0.6)
        self.play(FadeIn(cta),run_time=0.5)
        self.wait(RL)
