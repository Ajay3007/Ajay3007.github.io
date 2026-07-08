from manim import *
import re

BG="#0B0E14"; SURFACE="#151B26"; BORDER="#2A3542"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#E8ECF1"; GRAY="#5A6472"; MINT="#57E5B0"; RED="#F2544D"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; RED_BG="#331617"; MINT_BG="#0F2A20"

# ---- v2 code-panel palette (syntax highlighting) ----
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
TILE_Y=2.4; OUT_Y0=1.35; OUT_STEP=0.66; FORM_Y=-0.75; CODE_Y=-3.05
READ=0.8; READ_L=1.4

WORDS=["This","is","an","example","of","text","justification"]
MAXW=16
LINES=["This    is    an","example  of text","justification   "]
GROUPS=[[0,1,2],[3,4,5],[6]]      # word indices per line
BOXW=6.3                          # visual width representing maxWidth

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

def pill(text,tc,bg,st,s=0.4,h=0.56):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.45,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def wtile(word,tc=WHITE,bg=SURFACE,st=BORDER):
    t=Text(word,font=MN,weight=BOLD,color=tc).scale(0.42)
    box=RoundedRectangle(width=t.width+0.3,height=0.6,corner_radius=0.1,stroke_color=st,stroke_width=2.6,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)

def linebox(s,color=WHITE,edge=BORDER):
    # monospace line rendered flush inside a fixed maxWidth box
    box=RoundedRectangle(width=BOXW,height=0.56,corner_radius=0.08,stroke_color=edge,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0)
    t=Text(s,font=MN,weight=BOLD,color=color).scale(0.44)
    if t.width>BOXW-0.2: t.scale_to_fit_width(BOXW-0.2)
    t.move_to(box.get_center())
    return VGroup(box,t)


class LC68(Scene):
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
        badge=pill("# 68",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Text Justification",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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

    # ---------- v2 code panel ----------
    def build_code(self,raw,scale=0.30,cy=CODE_Y,maxw=6.7):
        lines=[colorize(s,scale) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.11)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.28)
        if block.width>maxw: block.scale(maxw/block.width)
        panel=RoundedRectangle(corner_radius=0.14,stroke_color=BORDER,stroke_width=2.3,
                               fill_color="#0F1420",fill_opacity=1.0,
                               width=block.width+0.6,height=block.height+0.42).move_to(UP*cy).set_z_index(0)
        block.move_to(panel.get_center()); block.set_z_index(2)
        hlbar=RoundedRectangle(width=block.width+0.36,height=lines[0].height+0.11,corner_radius=0.06,
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

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Pack words into lines of EXACTLY maxWidth chars,",font=FN,color=WHITE).scale(0.4)
        t2=Text("padding with spaces so both edges line up.",font=FN,color=GRAY).scale(0.4)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.6); t2.next_to(t1,DOWN,buff=0.18)
        self.play(FadeIn(t1),run_time=0.45); self.play(FadeIn(t2),run_time=0.45)
        self.wait(0.4)
        mw=Text("maxWidth = 16",font=MN,weight=BOLD,color=AMBER).scale(0.42).move_to(UP*1.5)
        self.play(FadeIn(mw),run_time=0.4)
        boxes=VGroup(*[linebox(s,MINT,MINT) for s in LINES]).arrange(DOWN,buff=0.14).move_to(UP*-0.2)
        self.play(LaggedStart(*[FadeIn(b,shift=UP*0.1) for b in boxes],lag_ratio=0.2),run_time=1.1)
        rule=Text("every line is flush left AND right",font=FN,color=CYAN).scale(0.38).next_to(boxes,DOWN,buff=0.35)
        self.play(FadeIn(rule),run_time=0.45)
        self.wait(READ_L+0.2)
        self.play(FadeOut(VGroup(lbl,t1,t2,mw,boxes,rule)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Three rules do it all:",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("1 · greedily pack as many words as fit",font=FN,color=CYAN).scale(0.42)
        h3=Text("2 · spread leftover spaces evenly;",font=FN,color=MINT).scale(0.42)
        h4=Text("    left-hand gaps take the extras",font=FN,color=MINT).scale(0.42)
        h5=Text("3 · last line: single spaces, pad the right",font=FN,color=AMBER).scale(0.42)
        for h in (h1,h2,h3,h4,h5):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.1); h2.next_to(h1,DOWN,buff=0.32)
        h3.next_to(h2,DOWN,buff=0.26); h4.next_to(h3,DOWN,buff=0.12); h5.next_to(h4,DOWN,buff=0.26)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.42); self.play(FadeIn(h4,shift=UP*0.1),run_time=0.3)
        self.play(FadeIn(h5,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4,h5)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Greedy pack, then justify",font=FN,weight=BOLD,color=WHITE).scale(0.52).move_to(UP*2.3)
        a1=Text("add words while  chars + gaps ≤ maxWidth",font=MN,color=WHITE).scale(0.36).move_to(UP*1.4)
        a2=Text("slack = maxWidth − total word chars",font=MN,color=CYAN).scale(0.36).move_to(UP*0.7)
        a3=Text("each gap: slack/gaps  (+1 for the first slack%gaps)",font=MN,color=MINT).scale(0.34).move_to(UP*0.05)
        a4=Text("last line / one word → left-justify + right-pad",font=MN,color=AMBER).scale(0.34).move_to(UP*-0.65)
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
        self.tiles=[wtile(w) for w in WORDS]
        trow=VGroup(*self.tiles).arrange(RIGHT,buff=0.14).move_to(UP*TILE_Y)
        if trow.width>6.95: trow.scale_to_fit_width(6.95)
        self.play(LaggedStart(*[FadeIn(t,shift=DOWN*0.12) for t in self.tiles],lag_ratio=0.08),run_time=1.0)

        raw=[(0,'// words[i..j) are the greedily-packed line'),
             (0,'int gaps = j - i - 1;'),
             (0,'int slack = maxWidth - totalChars;'),
             (0,'string line = words[i];'),
             (0,'for (int k = i+1; k < j; k++) {'),
             (1,'int sp = last ? 1 : slack/gaps + (k-i<=slack%gaps ? 1:0);'),
             (1,'line += string(sp, \' \') + words[k];'),
             (0,'}'),
             (0,'line += string(maxWidth - line.size(), \' \');  // right-pad')]
        panel,code,hlbar=self.build_code(raw)
        self._act=[]
        self.play(FadeIn(panel),run_time=0.35); self.add(hlbar)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.05),run_time=0.85)

        self.outboxes=[]
        caps=[
            ("pack This·is·an (10 ≤ 16); example makes 18 ✗",
             "slack 8 ÷ 2 gaps = 4 + 4  (even)", MINT, 5),
            ("pack example·of·text (15 ≤ 16); next won't fit",
             "slack 3 ÷ 2 gaps = 2 + 1  (left gap extra)", AMBER, 5),
            ("only justification left — the last line",
             "single spaces, then pad the right", CYAN, 8),
        ]
        for li,grp in enumerate(GROUPS):
            headline,formula,fcol,codeline=caps[li]
            self.set_cap(headline,color=WHITE,scale=0.42)
            # highlight the member tiles
            self.play(*[self.tiles[w][0].animate.set_stroke(MINT,4.4).set_fill(MINT_BG,1.0) for w in grp],
                      *self.hl(1 if li<2 else 8),run_time=0.5)
            # flash the first non-fitting tile (if any)
            nxt=grp[-1]+1
            if li<2 and nxt<len(WORDS):
                self.play(self.tiles[nxt][0].animate.set_stroke(RED,4.2),run_time=0.3)
                self.play(self.tiles[nxt][0].animate.set_stroke(BORDER,2.6),run_time=0.25)
            # formula
            fm=Text(formula,font=MN,weight=BOLD,color=fcol).scale(0.4).move_to(UP*FORM_Y)
            if fm.width>6.8: fm.scale_to_fit_width(6.8)
            self.play(*self.hl(codeline),FadeIn(fm,shift=UP*0.1),run_time=0.5)
            # build the justified line box, drop it into the output stack
            box=linebox(LINES[li],MINT,MINT).move_to(UP*(OUT_Y0-li*OUT_STEP))
            self.play(FadeIn(box,shift=DOWN*0.15),run_time=0.5)
            self.outboxes.append(box)
            self.wait(0.4)
            self.play(FadeOut(fm),run_time=0.25)
        self.wait(READ_L)

    def outro(self):
        self.play(FadeOut(self.hlbar),*[FadeOut(c) for c in self.code],FadeOut(self.panel),
                  FadeOut(VGroup(*self.tiles)),run_time=0.5)
        stack=VGroup(*self.outboxes)
        self.play(stack.animate.move_to(UP*1.4),run_time=0.5)
        self.set_cap("every line hits exactly 16 — fully justified",color=MINT)
        self.wait(READ_L)
        comp=VGroup(Text("Time  O(N)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.5)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        sfx=Text("N = total characters (extra space O(1))",font=FN,color=GRAY).scale(0.34)
        badge=VGroup(cbox,comp).move_to(UP*-0.9)
        sfx.next_to(badge,DOWN,buff=0.22)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5)
        self.play(FadeIn(sfx),run_time=0.35); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("24 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
        head=Text("LeetCode Top Interview 150",font=FN,weight=BOLD,color=WHITE).scale(0.58)
        if head.width>6.6: head.scale_to_fit_width(6.6)
        head.move_to(UP*1.2)
        sub=Text("Array / String section — complete!",font=FN,color=MINT).scale(0.46).move_to(UP*0.5)
        dl=Line(LEFT*1.6,ORIGIN,color=CYAN,stroke_width=4).move_to(UP*-0.15+LEFT*0.8)
        dr=Line(ORIGIN,RIGHT*1.6,color=AMBER,stroke_width=4).move_to(UP*-0.15+RIGHT*0.8)
        ctatxt=Text("Follow  @axiobyte",font=FN,weight=BOLD,color=CYAN).scale(0.6)
        ctabox=RoundedRectangle(width=ctatxt.width+0.9,height=1.0,corner_radius=0.5,stroke_color=CYAN,stroke_width=3.0,fill_color=CYAN_BG,fill_opacity=1.0)
        ctatxt.move_to(ctabox.get_center()); cta=VGroup(ctabox,ctatxt).move_to(UP*-1.05)
        nxt=VGroup(Text("↓",font=FN,weight=BOLD,color=AMBER).scale(0.55),
                   Text("Two Pointers is next",font=FN,color=WHITE).scale(0.46)).arrange(RIGHT,buff=0.2).move_to(UP*-2.35)
        self.play(FadeIn(wm,shift=DOWN*0.2),run_time=0.6)
        self.play(FadeIn(part,shift=UP*0.1),run_time=0.35)
        self.play(FadeIn(head,shift=UP*0.1),FadeIn(sub,shift=UP*0.1),run_time=0.55)
        self.play(Create(dl),Create(dr),run_time=0.4)
        self.play(FadeIn(cta,scale=1.06),run_time=0.55)
        self.play(FadeIn(nxt,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.8)
