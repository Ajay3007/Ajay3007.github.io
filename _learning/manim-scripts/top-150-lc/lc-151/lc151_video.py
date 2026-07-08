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
RAW_Y=2.5; TILE_Y=1.15; RES_Y=-0.35; CODE_Y=-3.0
READ=0.8; READ_L=1.4

WORDS=["the","sky","is","blue"]
RAW='"  the sky is  blue "'

def _char_colors(s):
    col=[None]*len(s)
    ci=s.find("//")
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

def wtile(word,tc=WHITE,bg=SURFACE,st=BORDER):
    t=Text(word,font=MN,weight=BOLD,color=tc).scale(0.5)
    box=RoundedRectangle(width=t.width+0.42,height=0.72,corner_radius=0.12,stroke_color=st,stroke_width=2.8,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); return VGroup(box,t)


class LC151(Scene):
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
        badge=pill("# 151",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Reverse Words in a String",font=FN,weight=BOLD,color=WHITE).scale(0.6)
        self.hdr=VGroup(badge,title).arrange(RIGHT,buff=0.3)
        if self.hdr.width>6.9: self.hdr.scale(6.9/self.hdr.width)
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
    def build_code(self,raw,scale=0.32,cy=CODE_Y,maxw=6.7):
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

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Reverse the ORDER of the words in a string.",font=FN,color=WHITE).scale(0.44)
        t2=Text("Trim extra spaces — one space between words.",font=FN,color=GRAY).scale(0.4)
        for t in (t1,t2):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        t1.move_to(UP*2.6); t2.next_to(t1,DOWN,buff=0.2)
        self.play(FadeIn(t1),run_time=0.45); self.play(FadeIn(t2),run_time=0.45)
        self.wait(0.5)
        raw=colorize(RAW,0.5).move_to(UP*0.9)
        if raw.width>6.9: raw.scale_to_fit_width(6.9)
        inlbl=Text("in",font=MN,weight=BOLD,color=GRAY).scale(0.36).next_to(raw,LEFT,buff=0.3)
        self.play(FadeIn(inlbl),FadeIn(raw,shift=UP*0.1),run_time=0.6)
        self.wait(0.4)
        out=colorize('"blue is sky the"',0.5).move_to(UP*-0.5)
        outlbl=Text("out",font=MN,weight=BOLD,color=MINT).scale(0.36).next_to(out,LEFT,buff=0.3)
        arrow=Text("↓",font=FN,weight=BOLD,color=AMBER).scale(0.6).move_to(UP*0.2)
        self.play(FadeIn(arrow),run_time=0.3)
        self.play(FadeIn(outlbl),FadeIn(out,shift=UP*0.1),run_time=0.6)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,t2,raw,inlbl,out,outlbl,arrow)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("Three clean steps:",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("1 · pull out the words, skipping the spaces",font=FN,color=CYAN).scale(0.42)
        h3=Text("2 · reverse the list of words",font=FN,color=MINT).scale(0.42)
        h4=Text("3 · glue them back with single spaces",font=FN,color=AMBER).scale(0.42)
        for h in (h1,h2,h3,h4):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.0); h2.next_to(h1,DOWN,buff=0.34)
        h3.next_to(h2,DOWN,buff=0.28); h4.next_to(h3,DOWN,buff=0.28)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.42); self.play(FadeIn(h4,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Tokenize · reverse · join",font=FN,weight=BOLD,color=WHITE).scale(0.52).move_to(UP*2.3)
        a1=Text("stringstream >> word  skips ALL whitespace",font=MN,color=CYAN).scale(0.36).move_to(UP*1.4)
        a2=Text("so extra / leading / trailing spaces vanish for free",font=FN,color=GRAY).scale(0.36).move_to(UP*0.75)
        a3=Text("reverse(words)  then join with ' '",font=MN,color=MINT).scale(0.4).move_to(UP*0.05)
        a4=Text("(in place: reverse all, then flip each word → O(1))",font=FN,color=AMBER).scale(0.36).move_to(UP*-0.7)
        for g in (a1,a2,a3,a4):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.4); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.4)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        raw=colorize(RAW,0.46).move_to(UP*RAW_Y)
        if raw.width>6.9: raw.scale_to_fit_width(6.9)
        self.raw=raw
        self.play(FadeIn(raw,shift=UP*0.1),run_time=0.5)

        raw_code=[(0,'stringstream ss(s);  string t;  vector<string> w;'),
                  (0,'while (ss >> t) w.push_back(t);   // >> skips spaces'),
                  (0,'reverse(w.begin(), w.end());'),
                  (0,'string res;'),
                  (0,'for (auto& x : w) res += (res.empty()?"":" ") + x;'),
                  (0,'return res;')]
        panel,code,hlbar=self.build_code(raw_code)
        self._act=[]
        self.play(FadeIn(panel),run_time=0.35); self.add(hlbar)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.06),run_time=0.85)

        # phase 1: extract word tiles
        self.tiles=[wtile(w,tc=WHITE,bg=SURFACE,st=CYAN) for w in WORDS]
        grp=VGroup(*self.tiles).arrange(RIGHT,buff=0.2).move_to([0,TILE_Y,0])
        self.set_cap("stream out the words — spaces skipped", color=CYAN)
        self.play(*self.hl(1),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(t,shift=DOWN*0.25) for t in self.tiles],lag_ratio=0.18),run_time=1.0)
        self.wait(0.4)

        # phase 2: reverse the tiles (cross inward)
        self.set_cap("reverse the word order", color=MINT)
        rev=list(reversed(self.tiles))
        tmp=VGroup(*[t.copy() for t in rev]).arrange(RIGHT,buff=0.2).move_to([0,TILE_Y,0])
        targets=[tmp[k].get_center() for k in range(len(rev))]
        self.play(*self.hl(2),run_time=0.35)
        self.play(*[rev[k].animate.move_to(targets[k]) for k in range(len(rev))],
                  *[t[0].animate.set_stroke(MINT,3.4) for t in self.tiles],run_time=1.0)
        self.wait(0.4)

        # phase 3: join
        self.set_cap("glue them back with single spaces", color=AMBER)
        res=colorize('"blue is sky the"',0.5).move_to(UP*RES_Y)
        rlbl=Text("res",font=MN,weight=BOLD,color=MINT).scale(0.36).next_to(res,LEFT,buff=0.3)
        self.play(*self.hl(4),run_time=0.35)
        self.play(FadeIn(rlbl),FadeIn(res,shift=UP*0.1),run_time=0.7)
        self.res=VGroup(rlbl,res)
        self.result_str="blue is sky the"
        self.play(*self.hl(5),run_time=0.3); self.wait(READ_L)

    def elegant_card(self):
        self.play(FadeOut(self.hlbar),*[FadeOut(c) for c in self.code],FadeOut(self.panel),
                  FadeOut(VGroup(*self.tiles)),FadeOut(self.raw),run_time=0.5)
        tag=pill("Bonus: cleaner code  ✨",AMBER,AMBER_BG,AMBER,s=0.42,h=0.62).move_to(UP*1.4)
        self.play(FadeIn(tag,scale=1.05),run_time=0.5)
        raw=[(0,'stringstream ss(s);  string w, res;'),
             (0,'while (ss >> w) res = w + (res.empty()?"":" ") + res;'),
             (0,'return res;')]
        panel,code,_=self.build_code(raw,scale=0.32,cy=0.0,maxw=6.7)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.08),run_time=0.8)
        note=Text("read each word and prepend it — no vector, no reverse",font=FN,color=GRAY).scale(0.36).move_to(UP*-1.5)
        if note.width>6.9: note.scale_to_fit_width(6.9)
        self.play(FadeIn(note,shift=UP*0.1),run_time=0.45)
        self.set_cap("prepend as you read — order flips itself",color=AMBER)
        self.wait(READ_L+0.2)
        self.elegant=VGroup(tag,panel,*code,note)

    def outro(self):
        self.play(FadeOut(self.elegant),self.res.animate.move_to(UP*1.2),run_time=0.55)
        self.set_cap("streams skip the messy spaces for you",color=MINT)
        self.wait(READ_L)
        comp=VGroup(Text("Time  O(n)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(n)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.5)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        sfx=Text("O(1) space with the in-place double reverse",font=FN,color=GRAY).scale(0.34)
        badge=VGroup(cbox,comp).move_to(UP*-0.7)
        sfx.next_to(badge,DOWN,buff=0.24)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5)
        self.play(FadeIn(sfx),run_time=0.35); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("21 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
