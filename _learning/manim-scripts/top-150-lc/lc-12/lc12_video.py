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
RES_Y=2.3; MID_Y=0.9; CODE_Y=-2.95
READ=0.8; READ_L=1.4

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

def rcell(v,size=0.6,stroke=BORDER,fill=SURFACE,tcolor=WHITE):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.1,stroke_color=stroke,
                       stroke_width=2.8,fill_color=fill,fill_opacity=1.0).set_z_index(1)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.6*size).move_to(r.get_center()).set_z_index(5)
    return VGroup(r,t)

def statbox(label,val,color):
    lab=Text(label,font=MN,color=GRAY).scale(0.36)
    v=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62)
    col=VGroup(lab,v).arrange(DOWN,buff=0.1)
    box=RoundedRectangle(width=max(col.width+0.8,2.0),height=col.height+0.6,corner_radius=0.14,
                         stroke_color=color,stroke_width=2.6,fill_color=SURFACE,fill_opacity=1.0)
    col.move_to(box.get_center())
    return VGroup(box,col),v

TABLE=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
       (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

def to_roman(n):
    out=""
    for val,sym in TABLE:
        while n>=val: out+=sym; n-=val
    return out

NUM0=2024


class LC12(Scene):
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
        badge=pill("# 12",CYAN,SURFACE,CYAN,s=0.4)
        title=Text("Integer to Roman",font=FN,weight=BOLD,color=WHITE).scale(0.6)
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

    # ---------- v2 code panel with syntax highlighting + active-line bar ----------
    def build_code(self,raw,scale=0.34,cy=CODE_Y,maxw=6.5):
        lines=[colorize(s,scale) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.13)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.32)
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

    def legend_table(self):
        rows=[VGroup() for _ in range(2)]
        for k,(val,sym) in enumerate(TABLE):
            t=Text("%d = %s" % (val,sym),font=MN,weight=BOLD,color=WHITE).scale(0.32)
            b=RoundedRectangle(width=t.width+0.3,height=0.48,corner_radius=0.09,stroke_color=BORDER,stroke_width=2.0,fill_color=SURFACE,fill_opacity=1.0)
            t.move_to(b.get_center()); rows[0 if k<7 else 1].add(VGroup(b,t))
        c1=rows[0].arrange(RIGHT,buff=0.12); c2=rows[1].arrange(RIGHT,buff=0.12)
        table=VGroup(c1,c2).arrange(DOWN,buff=0.16,aligned_edge=LEFT)
        if table.width>6.9: table.scale_to_fit_width(6.9)
        return table

    def problem_scene(self):
        lbl=pill("The problem",CYAN,SURFACE,CYAN).move_to(UP*CAP_Y)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        t1=Text("Convert an integer (1–3999) to a Roman numeral.",font=FN,color=WHITE).scale(0.44)
        if t1.width>6.9: t1.scale_to_fit_width(6.9)
        t1.move_to(UP*2.7)
        self.play(FadeIn(t1),run_time=0.5)
        table=self.legend_table().move_to(UP*1.2)
        self.play(FadeIn(table,shift=UP*0.1),run_time=0.8)
        self.wait(READ_L)
        t2=Text("The 13 building blocks — including the subtractive pairs.",font=FN,color=GRAY).scale(0.38).move_to(UP*-0.5)
        t3=Text("e.g. 2024  →  MMXXIV",font=MN,weight=BOLD,color=MINT).scale(0.46).move_to(UP*-1.3)
        for t in (t2,t3):
            if t.width>6.9: t.scale_to_fit_width(6.9)
        self.play(FadeIn(t2,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(t3,shift=UP*0.1),run_time=0.5)
        self.wait(READ_L+0.3)
        self.play(FadeOut(VGroup(lbl,t1,table,t2,t3)),run_time=0.5)

    def hint_scene(self):
        lbl=pill("The key idea",AMBER,SURFACE,AMBER).move_to(UP*CAP_Y)
        h1=Text("It's just making change with coins.",font=FN,weight=BOLD,color=WHITE).scale(0.48)
        h2=Text("Line the 13 values up, biggest first.",font=FN,color=WHITE).scale(0.44)
        h3=Text("Repeatedly take the biggest one that fits,",font=FN,color=MINT).scale(0.44)
        h4=Text("subtract it, and append its symbol.",font=FN,color=CYAN).scale(0.44)
        for h in (h1,h2,h3,h4):
            if h.width>6.8: h.scale_to_fit_width(6.8)
        h1.move_to(UP*2.0); h2.next_to(h1,DOWN,buff=0.34)
        h3.next_to(h2,DOWN,buff=0.3); h4.next_to(h3,DOWN,buff=0.22)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(h1,shift=UP*0.1),run_time=0.5); self.wait(0.2)
        self.play(FadeIn(h2,shift=UP*0.1),run_time=0.45)
        self.play(FadeIn(h3,shift=UP*0.1),run_time=0.45); self.play(FadeIn(h4,shift=UP*0.1),run_time=0.45)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,h1,h2,h3,h4)),run_time=0.5)

    def approach_scene(self):
        lbl=pill("Approach",MINT,SURFACE,MINT).move_to(UP*CAP_Y)
        a0=Text("Greedy — biggest coin first",font=FN,weight=BOLD,color=WHITE).scale(0.52).move_to(UP*2.3)
        a1=Text("table sorted big → small (M … I)",font=MN,color=WHITE).scale(0.4).move_to(UP*1.4)
        a2=Text("for each (value, symbol):",font=MN,color=CYAN).scale(0.4).move_to(UP*0.7)
        a3=Text("while num ≥ value:  append symbol, num -= value",font=MN,color=MINT).scale(0.36).move_to(UP*0.0)
        a4=Text("sorted order ⇒ the first that fits is the biggest",font=FN,color=AMBER).scale(0.38).move_to(UP*-0.8)
        for g in (a1,a2,a3,a4):
            if g.width>6.9: g.scale_to_fit_width(6.9)
        self.play(FadeIn(lbl,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a0,shift=UP*0.1),run_time=0.5)
        self.play(FadeIn(a1,shift=UP*0.1),run_time=0.4)
        self.play(FadeIn(a2,shift=UP*0.1),run_time=0.42); self.wait(0.2)
        self.play(FadeIn(a3,shift=UP*0.1),run_time=0.42)
        self.play(FadeIn(a4,shift=UP*0.1),run_time=0.42)
        self.wait(READ_L+0.4)
        self.play(FadeOut(VGroup(lbl,a0,a1,a2,a3,a4)),run_time=0.5)

    def walkthrough(self):
        final=to_roman(NUM0); L=len(final)
        cw=0.6; step=0.72; W=L*cw+(L-1)*(step-cw)
        x0=-W/2+cw/2
        xs=[x0+i*step for i in range(L)]
        reslab=Text("result",font=MN,weight=BOLD,color=WHITE).scale(0.34)
        reslab.move_to([xs[0]-0.55,RES_Y,0])
        self.play(FadeIn(reslab),run_time=0.3)

        raw=[(0,'vector<pair<int,string>> t = {{1000,"M"}, ..., {1,"I"}};'),
             (0,'string res;'),
             (0,'for (auto [val, sym] : t)'),
             (1,'while (num >= val) { res += sym; num -= val; }'),
             (0,'return res;')]
        panel,code,hlbar=self.build_code(raw)
        self._act=[]
        self.play(FadeIn(panel),run_time=0.35)
        self.add(hlbar)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.07),run_time=0.9)

        self.ng,self.nv=statbox("num",NUM0,AMBER)
        step_chip=pill("coin  →  symbol",CYAN,CYAN_BG,CYAN,s=0.4,h=0.6)
        mid=VGroup(self.ng,step_chip).arrange(RIGHT,buff=0.6).move_to(UP*MID_Y)
        self.step_chip=step_chip
        self.play(FadeIn(mid,shift=UP*0.1),*self.hl(0),run_time=0.5)
        self.set_cap("num = %d, result empty" % NUM0); self.wait(READ*0.7)

        def set_num(val,color=AMBER):
            new=Text(str(val),font=MN,weight=BOLD,color=color).scale(0.62).move_to(self.nv)
            return Transform(self.nv,new)
        def set_step(txt,color=CYAN):
            new=pill(txt,color,CYAN_BG,color,s=0.4,h=0.6).move_to(self.step_chip)
            return Transform(self.step_chip,new)

        placed=0; num=NUM0
        self.play(*self.hl(2),run_time=0.35)
        for val,sym in TABLE:
            if num<val: continue
            while num>=val:
                num-=val
                self.set_cap("%d ≥ %d  →  take %s" % (num+val,val,sym),color=MINT,scale=0.44)
                new_cells=[]
                for ch in sym:
                    c=rcell(ch,cw,stroke=(AMBER if len(sym)==2 else MINT),
                            fill=(AMBER_BG if len(sym)==2 else MINT_BG),
                            tcolor=(AMBER if len(sym)==2 else MINT)).move_to([xs[placed],RES_Y,0])
                    new_cells.append(c); placed+=1
                self.play(*self.hl(3),set_step("%d  →  %s" % (val,sym),
                          color=(AMBER if len(sym)==2 else MINT)),run_time=0.4)
                self.play(*[FadeIn(c,shift=DOWN*0.25) for c in new_cells],set_num(num),run_time=0.45)
        self.set_cap("num hits 0 — every unit is placed",color=MINT); self.wait(READ)
        self.play(*self.hl(4),run_time=0.4)
        self.final_roman=final
        self.wait(0.2)

    def elegant_card(self):
        self.play(FadeOut(self.hlbar),*[FadeOut(c) for c in self.code],FadeOut(self.panel),run_time=0.45)
        tag=pill("the version pros write  ✨",AMBER,AMBER_BG,AMBER,s=0.42,h=0.62).move_to(UP*MID_Y+UP*0.2)
        self.play(FadeOut(self.ng),FadeOut(self.step_chip),FadeIn(tag,scale=1.05),run_time=0.5)
        raw=[(0,'string th[]={"","M","MM","MMM"};'),
             (0,'string hu[]={"","C", ..., "CM"};   // hundreds'),
             (0,'string te[]={"","X", ..., "XC"};   // tens'),
             (0,'string on[]={"","I", ..., "IX"};   // ones'),
             (0,'return th[n/1000]+hu[n/100%10]+te[n/10%10]+on[n%10];')]
        panel,code,_=self.build_code(raw,scale=0.32,cy=-2.3,maxw=6.7)
        self.play(FadeIn(panel),run_time=0.35)
        self.play(LaggedStart(*[FadeIn(l,shift=RIGHT*0.06) for l in code],lag_ratio=0.07),run_time=0.9)
        note=Text("map each decimal digit straight to its numerals — O(1)",font=FN,color=GRAY).scale(0.36).move_to(UP*-4.4)
        if note.width>6.9: note.scale_to_fit_width(6.9)
        self.play(FadeIn(note,shift=UP*0.1),run_time=0.45)
        self.set_cap("no loop at all — pure lookup",color=AMBER)
        self.wait(READ_L+0.3)
        self.elegant=VGroup(tag,panel,*code,note)

    def outro(self):
        ans=pill("2024  =  %s" % self.final_roman,MINT,MINT_BG,MINT,s=0.5,h=0.72).move_to(UP*MID_Y)
        self.play(FadeOut(self.elegant),FadeIn(ans,scale=1.05),run_time=0.55)
        self.set_cap("greedy is O(1) too — the table has a fixed 13 rows",color=MINT)
        self.wait(READ_L)
        comp=VGroup(Text("Time  O(1)",font=MN,weight=BOLD,color=CYAN).scale(0.5),
                    Text("Space  O(1)",font=MN,weight=BOLD,color=AMBER).scale(0.5)).arrange(RIGHT,buff=0.55)
        cbox=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color="#0F1420",fill_opacity=1.0,width=comp.width+0.7,height=comp.height+0.5)
        comp.move_to(cbox.get_center())
        badge=VGroup(cbox,comp).move_to(UP*-1.4)
        self.play(FadeIn(badge,shift=UP*0.15),run_time=0.5); self.wait(READ_L)

    def end_slide(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=0.55)
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.8)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.8)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*3.4)
        part=pill("18 / 150",MINT,SURFACE,MINT,s=0.44,h=0.62).move_to(UP*2.15)
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
