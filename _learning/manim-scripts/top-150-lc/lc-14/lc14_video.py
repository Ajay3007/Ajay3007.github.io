from manim import *
import re

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"

# ---- v2 code-panel palette (syntax highlighting) ----
CODEFG="#C7D0DA"; KW_C=CYAN; NUM_C=AMBER; OP_C="#F78CA0"; STR_C=MINT; COM_C=GRAY
KEYWORDS=set("int long char bool void auto for while if else return const unsigned size_t struct".split())
TYPES=set("string vector pair map unordered_map".split())

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"

WM_Y=5.05; HDR_Y=4.3; CAP_Y=3.55
ROW_Y0=2.15; ROW_STEP=0.8; PRE_Y=-0.55; CODE_Y=-3.0
CW=0.62; CSTEP=0.74
READ=0.8; READ_L=1.4

WORDS=["flower","flow","flight"]

def _char_colors(s):
    col=[None]*len(s)
    ci=s.find("//")
    for m in re.finditer(r'[A-Za-z_]\w*|\d+|"[^"]*"|\'[^\']*\'|[-+*/%<>=!&|]+', s):
        tok=m.group(); a,b=m.start(),m.end()
        if ci!=-1 and a>=ci: continue
        if tok[0].isdigit(): c=NUM_C
        elif tok[0] in '"\'': c=STR_C
        elif tok[0] in "-+*/%<>=!&|": c=OP_C
        elif tok in KEYWORDS or tok in TYPES: c=KW_C
        else: c=None
        if c is not None:
            for k in range(a,b): col[k]=c
    if ci!=-1:
        for k in range(ci,len(s)): col[k]=COM_C
    return col

def colorize(s,scale=0.34):
    col=_char_colors(s); t2c={}; i=0
    while i<len(s):
        if col[i] is None: i+=1; continue
        j=i
        while j<len(s) and col[j]==col[i]: j+=1
        t2c["[%d:%d]"%(i,j)]=col[i]; i=j
    return Text(s,font=MN,color=CODEFG,t2c=t2c).scale(scale)

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def cell(ch,size=CW,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.1,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(ch,font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)


class LC14(Scene):
    def construct(self):
        self.persistent()
        self.problem_scene()
        self.hint_scene()
        self.approach_scene()
        self.walkthrough()
        self.elegant_card()
        self.outro()
        self.end_slide()

    def persistent(self):
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.4)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.4)
        self.wm=VGroup(axio,byte).arrange(RIGHT,buff=0.02).move_to(UP*WM_Y)
        badge=pill("# 14",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Longest Common Prefix",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3)
        if self.hdr.width>6.8: self.hdr.scale(6.8/self.hdr.width)
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

    # ---------- v2 code panel: syntax highlighting + active-line bar ----------
    def build_code(self,raw,scale=0.34,cy=CODE_Y,maxw=6.6):
        lines=[colorize(s,scale) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.30)
        if block.width>maxw: block.scale(maxw/block.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.3,
                               fill_color="#0F1420",fill_opacity=1.0,
                               width=block.width+0.6,height=block.height+0.45).move_to(UP*cy).set_z_index(0)
        block.move_to(panel.get_center()); block.set_z_index(2)
        hlbar=RoundedRectangle(width=block.width+0.36,height=lines[0].height+0.12,corner_radius=0.07,
                               stroke_width=0,fill_color=CYAN,fill_opacity=0.0).set_z_index(1)
        hlbar.move_to([panel.get_center()[0],lines[0].get_center()[1],0])
        self.panel=panel; self.code=lines; self.hlbar=hlbar; self._barvis=False
        return panel,lines,hlbar

    def hl(self,i):
        target=[self.panel.get_center()[0],self.code[i].get_center()[1],0]
        if not self._barvis:
            self.hlbar.move_to(target); self._barvis=True
            return [self.hlbar.animate.set_fill(CYAN,opacity=0.15)]
        return [self.hlbar.animate.move_to(target)]

    # ---------- grid geometry ----------
    def col_x(self,j):
        maxlen=max(len(w) for w in WORDS)
        x0=-((maxlen-1)*CSTEP)/2
        return x0+j*CSTEP

    def row_y(self,r):
        return ROW_Y0-r*ROW_STEP

    def build_grid(self):
        self.grid=[]
        gob=VGroup()
        for r,w in enumerate(WORDS):
            rowcells=[]
            for j,ch in enumerate(w):
                c=cell(ch).move_to([self.col_x(j),self.row_y(r),0])
                rowcells.append(c); gob.add(c)
            self.grid.append(rowcells)
        return gob

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Given a list of strings,",font=FN,color=WHITE).scale(0.46)
        t2=Text("find their longest common prefix.",font=FN,color=GRAY).scale(0.44)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.6); t2.next_to(t1,DOWN,buff=0.2)
        self.play(FadeIn(t1),run_time=0.45); self.play(FadeIn(t2),run_time=0.45)
        self.wait(0.5)
        lst=Text('["flower", "flow", "flight"]',font=MN,weight=BOLD,color=WHITE).scale(0.46).move_to(UP*0.9)
        if lst.width>6.9: lst.scale_to_fit_width(6.9)
        self.play(FadeIn(lst,shift=UP*0.1),run_time=0.6)
        self.wait(0.4)
        ans=pill('common prefix  =  "fl"',MINT,MINT_BG,MINT,s=0.46,h=0.66).move_to(UP*-0.4)
        self.play(FadeIn(ans,scale=1.05),run_time=0.5)
        note=Text('"fl"ower · "fl"ow · "fl"ight',font=MN,color=CYAN).scale(0.4).next_to(ans,DOWN,buff=0.3)
        if note.width>6.7: note.scale_to_fit_width(6.7)
        self.play(FadeIn(note),run_time=0.45)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,t2,lst,ans,note)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Stack the words and read DOWN the columns.",font=FN,weight=BOLD,color=WHITE).scale(0.44)
        h2=Text("Column 0 all match? keep it.",font=FN,color=MINT).scale(0.44)
        h3=Text("Column 1 all match? keep it.",font=FN,color=MINT).scale(0.44)
        h4=Text("First column that disagrees →",font=FN,color=AMBER).scale(0.44)
        h5=Text("the prefix ends right there.",font=FN,color=RED).scale(0.44)
        for h in (h1,h2,h3,h4,h5):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.1); h2.next_to(h1,DOWN,buff=0.3)
        h3.next_to(h2,DOWN,buff=0.2); h4.next_to(h3,DOWN,buff=0.3); h5.next_to(h4,DOWN,buff=0.2)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.4); self.play(FadeIn(h3,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(h4,shift=UP*0.1),run_time=0.42); self.play(FadeIn(h5,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4,h5)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Vertical scanning",font=FN,weight=BOLD,color=WHITE).scale(0.54).move_to(UP*2.3)
        a1=Text("take column j of the first word: c = strs[0][j]",font=MN,color=WHITE).scale(0.36).move_to(UP*1.4)
        a2=Text("check every other word at column j",font=MN,color=CYAN).scale(0.38).move_to(UP*0.7)
        a3=Text("hit the word's end, or a different char → stop",font=MN,color=AMBER).scale(0.36).move_to(UP*0.0)
        a4=Text("answer = strs[0] up to that column",font=MN,color=MINT).scale(0.38).move_to(UP*-0.75)
        for g in (a1,a2,a3,a4):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.42); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.4)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        gob=self.build_grid()
        collabs=VGroup(*[Text(str(j),font=MN,color=GRAY).scale(0.3).move_to([self.col_x(j),self.row_y(0)+0.5,0])
                         for j in range(max(len(w) for w in WORDS))])
        self.play(LaggedStart(*[FadeIn(c,shift=UP*0.08) for row in self.grid for c in row],lag_ratio=0.03),run_time=1.1)
        self.play(FadeIn(collabs),run_time=0.35)

        raw=[(0,'for (int j = 0; j < strs[0].size(); j++) {'),
             (1,'char c = strs[0][j];'),
             (1,'for (auto& s : strs)'),
             (2,'if (j == s.size() || s[j] != c) return strs[0].substr(0, j);'),
             (0,'}'),
             (0,'return strs[0];')]
        panel,code,hlbar=self.build_code(raw)
        self._act=[]
        self.play(FadeIn(panel),run_time=0.35); self.add(hlbar)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.06),run_time=0.85)

        # column scanning bar
        top=self.row_y(0)+CW/2+0.05; bot=self.row_y(len(WORDS)-1)-CW/2-0.05
        self.colbar=RoundedRectangle(width=CW+0.16,height=top-bot,corner_radius=0.09,stroke_width=0,
                                     fill_color=CYAN,fill_opacity=0.0).set_z_index(0)
        self.colbar.move_to([self.col_x(0),(top+bot)/2,0])
        self.add(self.colbar)

        pre=pill('prefix = ""',MINT,MINT_BG,MINT,s=0.42,h=0.6).move_to(UP*PRE_Y)
        self.pre=pre
        self.play(FadeIn(pre,shift=UP*0.1),*self.hl(0),run_time=0.5)
        self.set_cap("scan the columns left to right"); self.wait(READ*0.7)

        def set_pre(txt):
            new=pill('prefix = "%s"'%txt,MINT,MINT_BG,MINT,s=0.42,h=0.6).move_to(self.pre)
            return Transform(self.pre,new)

        prefix=""
        c0=WORDS[0]
        stopped=False
        for j in range(len(c0)):
            self.play(self.colbar.animate.move_to([self.col_x(j),self.colbar.get_center()[1],0]).set_fill(CYAN,opacity=0.16),
                      *self.hl(1),run_time=0.4)
            ch=c0[j]
            # find first mismatch
            bad=None
            for r,w in enumerate(WORDS):
                if j>=len(w) or w[j]!=ch: bad=r; break
            self.play(*self.hl(3),self.grid[0][j][0].animate.set_stroke(CYAN,4.4),run_time=0.35)
            if bad is None:
                prefix+=ch
                self.set_cap("column %d — all '%s'  ✓" % (j,ch),color=MINT,scale=0.46)
                self.play(*[self.grid[r][j][0].animate.set_stroke(MINT,4.8).set_fill(MINT_BG,1.0) for r in range(len(WORDS))],run_time=0.4)
                self.play(set_pre(prefix),run_time=0.35)
            else:
                self.set_cap("column %d — '%s' ≠ '%s'  → stop" % (j,WORDS[bad][j] if j<len(WORDS[bad]) else '_',ch),color=RED,scale=0.44)
                self.play(self.grid[bad][j][0].animate.set_stroke(RED,4.8).set_fill(RED_BG,1.0),
                          self.grid[bad][j][1].animate.set_color(RED),
                          self.colbar.animate.set_fill(RED,opacity=0.14),run_time=0.5)
                stopped=True
                break
        self.prefix_final=prefix
        self.play(*self.hl(3),run_time=0.3); self.wait(READ_L)

    def elegant_card(self):
        self.play(FadeOut(self.hlbar),*[FadeOut(c) for c in self.code],FadeOut(self.panel),run_time=0.45)
        tag=pill("Bonus: cleaner code  ✨",AMBER,AMBER_BG,AMBER,s=0.42,h=0.62).move_to(UP*PRE_Y+UP*0.15)
        self.play(FadeOut(self.pre),FadeIn(tag,scale=1.05),run_time=0.5)
        raw=[(0,'auto [lo, hi] = minmax_element(begin(strs), end(strs));'),
             (0,'int i = 0;'),
             (0,'while (i < lo->size() && (*lo)[i] == (*hi)[i]) i++;'),
             (0,'return lo->substr(0, i);')]
        panel,code,_=self.build_code(raw,scale=0.32,cy=-2.35,maxw=6.7)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.07),run_time=0.9)
        note=Text("only the lexicographic min & max strings matter",font=FN,color=GRAY).scale(0.36).move_to(UP*-4.35)
        if note.width>6.9: note.scale_to_fit_width(6.9)
        self.play(FadeIn(note,shift=UP*0.1),run_time=0.45)
        self.set_cap("compare just the smallest and largest words",color=AMBER)
        self.wait(READ_L+0.2)
        self.elegant=VGroup(tag,panel,*code,note)

    def outro(self):
        ans=pill('answer  =  "%s"'%self.prefix_final,MINT,MINT_BG,MINT,s=0.5,h=0.72).move_to(UP*PRE_Y)
        self.play(FadeOut(self.elegant),FadeIn(ans,scale=1.05),run_time=0.55)
        self.set_cap("stop at the first column that disagrees",color=MINT)
        self.wait(READ_L)
        comp=VGroup(Text("Time  O(S)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.5)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        sfx=Text("S = total characters across all words",font=FN,color=GRAY).scale(0.34)
        badge=VGroup(cbox,comp).move_to(UP*-1.75)
        sfx.next_to(badge,DOWN,buff=0.22)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5)
        self.play(FadeIn(sfx),run_time=0.35); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("20 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
