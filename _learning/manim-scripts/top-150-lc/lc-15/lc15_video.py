from manim import *
import re

# ---- AxioByte v3 palette ----
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; MINT_BG="#0F2A20"; RED_BG="#331617"; VIOLET_BG="#241B3A"

CODEFG="#C7D0DA"; KW_C=CYAN; NUM_C=AMBER; OP_C="#F78CA0"; STR_C=MINT; COM_C=GRAY
KEYWORDS=set("int long char bool void auto for while if else return const unsigned size_t struct".split())
TYPES=set("string vector pair map unordered_map stringstream".split())

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55
ARR_Y=1.65; SZ=0.7; STEP=0.86; TRI_Y=-0.55; CODE_Y=-3.3
READ=0.8; READ_L=1.4

ORIG=[-1,0,1,2,-1,-4]; S=sorted(ORIG); N=len(S)

def glow(shape,color=None,layers=6,spread=0.34,max_op=0.16):
    if color is None: color=shape.get_stroke_color()
    halo=VGroup()
    for i in range(layers):
        f=(i+1)/layers
        c=shape.copy().set_stroke(width=0).set_fill(color,opacity=max_op*(1-f)+0.015)
        c.scale(1+spread*f); halo.add(c)
    halo.set_z_index(shape.get_z_index()-1); return halo

def _char_colors(s):
    col=[None]*len(s); ci=s.find("//")
    for m in re.finditer(r'[A-Za-z_]\w*|\d+|"[^"]*"|\'[^\']*\'|[-+*/%<>=!&|?:]+', s):
        tok=m.group(); a,b=m.start(),m.end()
        if ci!=-1 and a>=ci: continue
        if tok[0].isdigit(): c=NUM_C
        elif tok[0] in '"\'': c=STR_C
        elif tok[0] in "-+*/%<>=!&|?:": c=OP_C
        elif tok in KEYWORDS or tok in TYPES: c=KW_C
        else: c=None
        if c is not None:
            for k in range(a,b): col[k]=c
    if ci!=-1:
        for k in range(ci,len(s)): col[k]=COM_C
    return col

def colorize(s,scale=0.32):
    col=_char_colors(s); t2c={}; i=0
    while i<len(s):
        if col[i] is None: i+=1; continue
        j=i
        while j<len(s) and col[j]==col[i]: j+=1
        t2c["[%d:%d]"%(i,j)]=col[i]; i=j
    return Text(s,font=MN,color=CODEFG,t2c=t2c).scale(scale)

def pill(text,tc,bg,st,s=0.4,h=0.56,glowing=False):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); g=VGroup(box,t)
    if glowing: g.add_to_back(glow(box,st,layers=5,spread=0.5,max_op=0.14))
    return g

def cell(v,size=SZ,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.11,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.5*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def pointer(label,color,up=True,glowing=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.13).set_z_index(4)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.4)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    g=VGroup(tri,lab).set_z_index(8)
    if glowing: g.add_to_back(glow(tri,color,layers=5,spread=0.9,max_op=0.22))
    return g


class LC15(Scene):
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
        badge=pill("# 15",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("3Sum",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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

    # ---------- v3 code panel ----------
    def build_code(self,raw,scale=0.30,cy=CODE_Y,maxw=6.1):
        lines=[colorize(s,scale) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.12)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.30)
        if block.width>maxw: block.scale(maxw/block.width)
        gut=0.5
        nums=VGroup(*[Text(str(k+1),font=MN,color=GRAY).scale(0.9*scale).move_to([block.get_left()[0]-gut,lines[k].get_center()[1],0]) for k in range(len(lines))])
        content=VGroup(nums,block)
        panelw=content.width+0.7; panelh=content.height+0.5
        panel=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color=SURF2,fill_opacity=1.0,width=panelw,height=panelh).move_to(UP*cy).set_z_index(0)
        content.move_to(panel.get_center()); block.set_z_index(2); nums.set_z_index(2)
        hlbar=RoundedRectangle(width=panelw-0.16,height=lines[0].height+0.13,corner_radius=0.06,stroke_width=0,fill_color=CYAN,fill_opacity=0.0).set_z_index(1)
        accent=RoundedRectangle(width=0.07,height=lines[0].height+0.15,corner_radius=0.03,stroke_width=0,fill_color=CYAN,fill_opacity=0.0).set_z_index(3)
        self.panel=panel; self.code=lines; self.hlbar=hlbar; self.accent=accent; self.content=content
        self._pcx=panel.get_center()[0]; self._plx=panel.get_left()[0]+0.13; self._barvis=False
        return panel,content,hlbar,accent

    def clear_code(self):
        return [FadeOut(self.panel),FadeOut(self.content),FadeOut(self.hlbar),FadeOut(self.accent)]

    def hl(self,i):
        y=self.code[i].get_center()[1]
        if not self._barvis:
            self.hlbar.move_to([self._pcx,y,0]); self.accent.move_to([self._plx,y,0]); self._barvis=True
            return [self.hlbar.animate.set_fill(CYAN,opacity=0.12),self.accent.animate.set_fill(CYAN,opacity=1.0)]
        return [self.hlbar.animate.move_to([self._pcx,y,0]),self.accent.animate.move_to([self._plx,y,0])]

    def cx(self,c):
        x0=-((N-1)*STEP)/2
        return x0+c*STEP

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Find every UNIQUE triplet that sums to 0.",font=FN,weight=BOLD,color=WHITE).scale(0.46)
        t2=Text("no duplicate triplets in the answer",font=FN,color=GRAY).scale(0.4)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.55); t2.next_to(t1,DOWN,buff=0.2)
        self.play(FadeIn(t1),run_time=0.45); self.play(FadeIn(t2),run_time=0.45)
        self.wait(0.4)
        o=Text("nums = [-1, 0, 1, 2, -1, -4]",font=MN,weight=BOLD,color=WHITE).scale(0.5).move_to(UP*1.1)
        self.play(FadeIn(o,shift=UP*0.1),run_time=0.5)
        a1=pill("{-1, -1, 2}",MINT,MINT_BG,MINT,s=0.44,h=0.62,glowing=True)
        a2=pill("{-1, 0, 1}",MINT,MINT_BG,MINT,s=0.44,h=0.62,glowing=True)
        ans=VGroup(a1,a2).arrange(RIGHT,buff=0.4).move_to(UP*-0.2)
        self.play(FadeIn(ans,shift=UP*0.1),run_time=0.6)
        self.wait(READ_L+0.2)
        self.play(FadeOut(VGroup(lbl,t1,t2,o,ans)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("SORT first — it unlocks everything.",font=FN,weight=BOLD,color=WHITE).scale(0.46)
        h2=Text("Fix one number, then it's Two Sum on the rest:",font=FN,color=CYAN).scale(0.4)
        h3=Text("two pointers hunting for -nums[i].",font=FN,color=CYAN).scale(0.42)
        h4=Text("Skip repeats of i, l, r so triplets stay unique.",font=FN,color=MINT).scale(0.4)
        for h in (h1,h2,h3,h4):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.05); h2.next_to(h1,DOWN,buff=0.34)
        h3.next_to(h2,DOWN,buff=0.2); h4.next_to(h3,DOWN,buff=0.34)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.42); self.play(FadeIn(h3,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(h4,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Sort + fix + two-pointer",font=FN,weight=BOLD,color=WHITE).scale(0.52).move_to(UP*2.3)
        a1=Text("sort the array",font=MN,color=WHITE).scale(0.4).move_to(UP*1.45)
        a2=Text("for each i:  l = i+1,  r = n-1",font=MN,color=VIOLET).scale(0.38).move_to(UP*0.8)
        a3=Text("s = nums[i]+nums[l]+nums[r]", font=MN,color=WHITE).scale(0.38).move_to(UP*0.2)
        a4=Text("s<0 → l++    s>0 → r--    s==0 → record",font=MN,color=CYAN).scale(0.36).move_to(UP*-0.4)
        a5=Text("skip duplicate values → unique triplets",font=MN,color=MINT).scale(0.36).move_to(UP*-1.0)
        for g in (a1,a2,a3,a4,a5):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.38)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.4); self.wait(0.15)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a5,shift=UP*0.1),run_time=0.4)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4,a5)),run_time=0.5)

    def walkthrough(self):
        # show unsorted, then sort
        ocells=VGroup(*[cell(v) for v in ORIG]).arrange(RIGHT,buff=STEP-SZ).move_to(UP*ARR_Y)
        self.set_cap("step 1 — sort the array")
        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.1) for c in ocells],lag_ratio=0.06),run_time=0.8)
        self.wait(0.3)
        self.cells=[cell(v) for v in S]
        for c,cc in enumerate(self.cells): cc.move_to([self.cx(c),ARR_Y,0])
        srow=VGroup(*self.cells)
        idx=VGroup(*[Text(str(c),font=MN,color=GRAY).scale(0.3).next_to(self.cells[c],DOWN,buff=0.14) for c in range(N)])
        self.idx=idx
        self.play(FadeOut(ocells,shift=UP*0.2),run_time=0.3)
        self.play(FadeIn(srow,shift=DOWN*0.2),FadeIn(idx),run_time=0.6)
        self.set_cap("sorted → now fix one, two-point the rest",color=CYAN); self.wait(0.4)

        raw=[(0,"// sorted; fix nums[i], two-pointer the rest"),
             (0,"int l = i+1, r = n-1;"),
             (0,"while (l < r) {"),
             (1,"int s = nums[i] + nums[l] + nums[r];"),
             (1,"if (s < 0) l++;"),
             (1,"else if (s > 0) r--;"),
             (1,"else { add(i,l,r); l++; r--; skipDups(); }"),
             (0,"}")]
        panel,content,hlbar,accent=self.build_code(raw)
        self._act=[]
        self.play(FadeIn(panel),run_time=0.35); self.add(hlbar,accent)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in self.code],lag_ratio=0.05),FadeIn(content[0]),run_time=0.85)

        trilbl=Text("triplets:",font=MN,weight=BOLD,color=WHITE).scale(0.34).move_to([-2.9,TRI_Y,0])
        self.trilbl=trilbl; self.play(FadeIn(trilbl),run_time=0.3)
        self.tripills=[]

        self.pi=pointer("i",VIOLET,up=True); self.pl=pointer("l",CYAN,up=False); self.pr=pointer("r",AMBER,up=False)
        self.pi_in=False; self.lr_in=False
        self.glows=[]

        def add_triplet(i,l,r):
            txt="{%d,%d,%d}"%(S[i],S[l],S[r])
            p=pill(txt,MINT,MINT_BG,MINT,s=0.38,h=0.54,glowing=True)
            if not self.tripills: p.next_to(self.trilbl,RIGHT,buff=0.25)
            else: p.next_to(self.tripills[-1],RIGHT,buff=0.2)
            self.tripills.append(p)
            return p

        i=0
        while i<N-2:
            if i>0 and S[i]==S[i-1]:
                self.set_cap("nums[%d]==nums[%d] → skip i (avoid duplicates)"%(i,i-1),color=RED,scale=0.42)
                self.play(self.pi.animate.next_to(self.cells[i],UP,buff=0.14),run_time=0.3)
                self.play(self.cells[i][0].animate.set_stroke(RED,3.6),run_time=0.28)
                self.play(self.cells[i][0].animate.set_stroke(BORDER,3.0),run_time=0.22)
                i+=1; continue
            l=i+1; r=N-1
            # place pointers
            if not self.pi_in:
                self.pi.next_to(self.cells[i],UP,buff=0.14); self.pl.next_to(self.cells[l],DOWN,buff=0.12); self.pr.next_to(self.cells[r],DOWN,buff=0.12)
                self.play(FadeIn(self.pi,shift=DOWN*0.1),FadeIn(self.pl,shift=UP*0.1),FadeIn(self.pr,shift=UP*0.1),*self.hl(3),run_time=0.5)
                self.pi_in=True; self.lr_in=True
            else:
                self.play(self.pi.animate.next_to(self.cells[i],UP,buff=0.14),
                          self.pl.animate.next_to(self.cells[l],DOWN,buff=0.12),
                          self.pr.animate.next_to(self.cells[r],DOWN,buff=0.12),run_time=0.4)
            self.set_cap("fix %d → find two summing to %d"%(S[i],-S[i]),color=VIOLET,scale=0.44)
            self.cells[i][0].set_stroke(VIOLET,4.2)
            self.wait(0.2)
            while l<r:
                s=S[i]+S[l]+S[r]
                if s==0:
                    self.set_cap("%d + %d + %d = 0  ✓"%(S[i],S[l],S[r]),color=MINT,scale=0.46)
                    gi=glow(self.cells[i][0],MINT); gl=glow(self.cells[l][0],MINT); gr=glow(self.cells[r][0],MINT)
                    self.glows+=[gi,gl,gr]
                    self.play(*self.hl(6),
                              self.cells[l][0].animate.set_stroke(MINT,4.6).set_fill(MINT_BG,1.0),
                              self.cells[r][0].animate.set_stroke(MINT,4.6).set_fill(MINT_BG,1.0),
                              self.cells[i][0].animate.set_stroke(MINT,4.6).set_fill(MINT_BG,1.0),
                              FadeIn(gi),FadeIn(gl),FadeIn(gr),run_time=0.55)
                    p=add_triplet(i,l,r); self.play(FadeIn(p,shift=UP*0.1),run_time=0.4)
                    self.play(self.cells[l][0].animate.set_stroke(BORDER,3.0).set_fill(SURFACE,1.0),
                              self.cells[r][0].animate.set_stroke(BORDER,3.0).set_fill(SURFACE,1.0),run_time=0.25)
                    l+=1; r-=1
                    while l<r and S[l]==S[l-1]: l+=1
                    if l<r:
                        self.play(self.pl.animate.next_to(self.cells[l],DOWN,buff=0.12),
                                  self.pr.animate.next_to(self.cells[r],DOWN,buff=0.12),run_time=0.32)
                elif s<0:
                    self.set_cap("%d + %d + %d = %d  < 0  → l++"%(S[i],S[l],S[r],s),color=CYAN,scale=0.42)
                    self.play(*self.hl(4),run_time=0.3); l+=1
                    if l<r: self.play(self.pl.animate.next_to(self.cells[l],DOWN,buff=0.12),run_time=0.26)
                else:
                    self.set_cap("%d + %d + %d = %d  > 0  → r--"%(S[i],S[l],S[r],s),color=AMBER,scale=0.42)
                    self.play(*self.hl(5),run_time=0.3); r-=1
                    if l<r: self.play(self.pr.animate.next_to(self.cells[r],DOWN,buff=0.12),run_time=0.26)
            self.cells[i][0].set_stroke(BORDER,3.0)
            i+=1
        self.wait(READ_L)

    def outro(self):
        self.play(*self.clear_code(),FadeOut(self.pi),FadeOut(self.pl),FadeOut(self.pr),run_time=0.45)
        self.set_cap("two unique triplets sum to zero",color=MINT)
        grp=VGroup(self.trilbl,*self.tripills)
        self.play(grp.animate.move_to(UP*0.9),run_time=0.5)
        self.wait(READ_L)
        comp=VGroup(Text("Time  O(n²)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.5)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color=SURF2,fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        sfx=Text("sort O(n log n) + a two-pointer sweep per i",font=FN,color=GRAY).scale(0.34)
        badge=VGroup(cbox,comp).move_to(UP*-0.9)
        sfx.next_to(badge,DOWN,buff=0.22)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5)
        self.play(FadeIn(sfx),run_time=0.35); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("29 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62,glowing=True).move_to(UP*2.15)
        head=Text("LeetCode Top Interview 150",font=FN,weight=BOLD,color=WHITE).scale(0.58)
        if head.width>6.6: head.scale_to_fit_width(6.6)
        head.move_to(UP*1.2)
        sub=Text("Two Pointers — section complete!",font=FN,color=MINT).scale(0.46).move_to(UP*0.5)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*-0.15+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*-0.15+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center()); cta=VGroup(ctabox,ctatxt).move_to(UP*-1.05)
        cta.add_to_back(glow(ctabox,CYAN,layers=5,spread=0.4,max_op=0.14))
        nxt=VGroup(Text("↓",font=FN,weight=BOLD,color=AMBER).scale(0.55),
                   Text("Sliding Window is next",font=FN,color=WHITE).scale(0.46)).arrange(RIGHT,buff=0.2).move_to(UP*-2.35)
        self.play(FadeIn(wm,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(part,shift=UP*0.1),run_time=0.35)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
