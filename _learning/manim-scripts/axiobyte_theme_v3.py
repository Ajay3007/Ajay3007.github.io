"""
AxioByte — Theme v3 style sheet (a single still frame to approve the look).

Render:
  manim -s -qh axiobyte_theme_v3.py ThemeV3
  -> media/images/axiobyte_theme_v3/ThemeV3_ManimCE_v0.20.1.png

This is NOT an episode — it's a preview of the v3 upgrades (neon glow, code
panel with line numbers + left-edge accent, punchier-but-branded palette,
stylized icons). Once approved, these helpers get copied into each new
lc<num>_video.py (from #125 onward). Finished episodes 1-24 stay on v2.
"""
from manim import *
import re

# ---- AxioByte v3 palette (our identity: cyan+amber brand, punchier accents) ----
BG="#090C13"; SURFACE="#141B27"; SURF2="#0F1420"; BORDER="#26344A"
CYAN="#34D8E8"; AMBER="#F0A431"; WHITE="#EAF0F6"; GRAY="#65728A"
MINT="#4DE6A0"; RED="#FF5C55"; VIOLET="#B79CF0"
CYAN_BG="#10303A"; AMBER_BG="#33240F"; MINT_BG="#0F2A20"; RED_BG="#331617"

# code-panel syntax colors
CODEFG="#C7D0DA"; KW_C=CYAN; NUM_C=AMBER; OP_C="#F78CA0"; STR_C=MINT; COM_C=GRAY
KEYWORDS=set("int long char bool void auto for while if else return const unsigned size_t struct".split())
TYPES=set("string vector pair map unordered_map stringstream".split())

config.pixel_width=1080
config.pixel_height=1920
config.frame_height=14.0
config.frame_width=7.875
config.background_color=BG
FN="DejaVu Sans"; MN="DejaVu Sans Mono"


# ---------- v3 GLOW: soft neon halo behind any shape ----------
def glow(shape,color=None,layers=6,spread=0.34,max_op=0.16):
    if color is None: color=shape.get_stroke_color()
    halo=VGroup()
    for i in range(layers):
        f=(i+1)/layers
        c=shape.copy().set_stroke(width=0).set_fill(color,opacity=max_op*(1-f)+0.015)
        c.scale(1+spread*f)
        halo.add(c)
    halo.set_z_index(shape.get_z_index()-1)
    return halo


# ---------- v3 cell with optional glow ----------
def cell(v,size=0.8,stroke=BORDER,fill=SURFACE,tcolor=WHITE,glowc=None):
    r=RoundedRectangle(width=size,height=size,corner_radius=0.13,stroke_color=stroke,
                       stroke_width=3.0,fill_color=fill,fill_opacity=1.0).set_z_index(2)
    t=Text(str(v),font=FN,weight=BOLD,color=tcolor).scale(0.58*size).move_to(r.get_center()).set_z_index(5)
    grp=VGroup(r,t)
    if glowc is not None:
        grp.add_to_back(glow(r,glowc))
    return grp

def pointer(label,color,up=True,glowing=True):
    tri=Triangle(color=color,fill_opacity=1.0,stroke_width=0).scale(0.13).set_z_index(3)
    if up: tri.rotate(PI)
    lab=Text(label,font=MN,weight=BOLD,color=color).scale(0.4)
    lab.next_to(tri,UP if up else DOWN,buff=0.05)
    g=VGroup(tri,lab).set_z_index(8)
    if glowing: g.add_to_back(glow(tri,color,layers=5,spread=0.9,max_op=0.22))
    return g

def pill(text,tc,bg,st,s=0.4,h=0.56,glowing=False):
    t=Text(text,font=MN,weight=BOLD,color=tc).scale(s)
    box=RoundedRectangle(width=t.width+0.5,height=h,corner_radius=h/2,stroke_color=st,stroke_width=2.4,fill_color=bg,fill_opacity=1.0)
    t.move_to(box.get_center()); g=VGroup(box,t)
    if glowing: g.add_to_back(glow(box,st,layers=5,spread=0.5,max_op=0.14))
    return g


# ---------- v3 code panel: syntax highlight + line numbers + active-line bar w/ left accent ----------
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

def colorize(s,scale=0.34):
    col=_char_colors(s); t2c={}; i=0
    while i<len(s):
        if col[i] is None: i+=1; continue
        j=i
        while j<len(s) and col[j]==col[i]: j+=1
        t2c["[%d:%d]"%(i,j)]=col[i]; i=j
    return Text(s,font=MN,color=CODEFG,t2c=t2c).scale(scale)


class ThemeV3(Scene):
    def construct(self):
        # ---- branding ----
        axio=Text("Axio",font=FN,weight=BOLD,color=CYAN).scale(0.55)
        byte=Text("Byte",font=FN,weight=BOLD,color=AMBER).scale(0.55)
        wm=VGroup(axio,byte).arrange(RIGHT,buff=0.03).move_to(UP*6.15)
        self.add(wm)
        self.add(pill("theme v3  ·  neon + icons",CYAN,SURFACE,CYAN,s=0.38).move_to(UP*5.5))

        # ---- 1. glowing cells + glowing pointer ----
        self.add(Text("cells + pointer (glow)",font=MN,color=GRAY).scale(0.34).move_to(UP*4.55+LEFT*2.0))
        vals=[3,2,1,0,4]
        row=VGroup()
        for i,v in enumerate(vals):
            gc=CYAN if i==1 else (MINT if i==4 else None)
            st=CYAN if i==1 else (MINT if i==4 else BORDER)
            fl=CYAN_BG if i==1 else (MINT_BG if i==4 else SURFACE)
            tc=CYAN if i==1 else (MINT if i==4 else WHITE)
            row.add(cell(v,0.8,stroke=st,fill=fl,tcolor=tc,glowc=gc))
        row.arrange(RIGHT,buff=0.16).move_to(UP*3.7)
        self.add(row)
        self.add(pointer("i",CYAN,up=True).next_to(row[1],UP,buff=0.14))

        # ---- 2. upgraded code panel ----
        self.add(Text("code panel: numbers + active-line accent",font=MN,color=GRAY).scale(0.32).move_to(UP*2.55+LEFT*0.6))
        raw=[(0,"int l=0, r=n-1, res=0;"),
             (0,"while (l < r) {"),
             (1,"if (h[l] < h[r]) res += h[l++];"),
             (1,"else             res += h[r--];"),
             (0,"}"),
             (0,"return res;")]
        active=2
        lines=[colorize(s) for _,s in raw]
        block=VGroup(*lines).arrange(DOWN,aligned_edge=LEFT,buff=0.14)
        for ln,(ind,_) in zip(lines,raw): ln.shift(RIGHT*ind*0.34)
        gut=0.42  # gutter width for line numbers
        block.shift(RIGHT*gut/2)
        nums=VGroup(*[Text(str(k+1),font=MN,color=GRAY).scale(0.30).move_to([block.get_left()[0]-gut, lines[k].get_center()[1],0]) for k in range(len(lines))])
        panelw=block.width+gut+0.7; panelh=block.height+0.5
        panel=RoundedRectangle(corner_radius=0.16,stroke_color=BORDER,stroke_width=2.4,fill_color=SURF2,fill_opacity=1.0,width=panelw,height=panelh).set_z_index(0)
        content=VGroup(nums,block); content.move_to(ORIGIN)
        grp=VGroup(panel,content).move_to(UP*1.15)
        # active-line highlight bar + bright left accent
        y=lines[active].get_center()[1]
        bar=RoundedRectangle(width=panelw-0.16,height=lines[0].height+0.14,corner_radius=0.06,stroke_width=0,fill_color=CYAN,fill_opacity=0.12).set_z_index(1)
        bar.move_to([panel.get_center()[0],y,0])
        accent=RoundedRectangle(width=0.07,height=lines[0].height+0.16,corner_radius=0.03,stroke_width=0,fill_color=CYAN,fill_opacity=1.0).set_z_index(2)
        accent.move_to([panel.get_left()[0]+0.12,y,0])
        accent.add_to_back(glow(accent,CYAN,layers=4,spread=1.6,max_op=0.3))
        self.add(panel,bar,accent,content)

        # ---- 3. stylized icons (glow) ----
        self.add(Text("stylized icons (for later sections)",font=MN,color=GRAY).scale(0.32).move_to(DOWN*1.3+LEFT*1.0))
        # list node
        node=self.list_node("val", MINT)
        node.move_to(DOWN*2.2+LEFT*2.1)
        self.add(node)
        # database cylinder
        db=self.db_icon(CYAN).move_to(DOWN*2.15)
        self.add(db)
        # tree node (circle)
        tn=self.tree_node("7",AMBER).move_to(DOWN*2.2+RIGHT*2.1)
        self.add(tn)

        # ---- 4. palette swatches ----
        self.add(Text("palette",font=MN,color=GRAY).scale(0.32).move_to(DOWN*3.7+LEFT*2.6))
        sw=VGroup()
        for name,c in [("cyan",CYAN),("amber",AMBER),("mint",MINT),("red",RED),("violet",VIOLET)]:
            dot=RoundedRectangle(width=0.6,height=0.6,corner_radius=0.14,stroke_width=0,fill_color=c,fill_opacity=1.0)
            dot.add_to_back(glow(dot,c,layers=5,spread=0.5,max_op=0.18))
            lab=Text(name,font=MN,color=c).scale(0.28)
            sw.add(VGroup(dot,lab).arrange(DOWN,buff=0.12))
        sw.arrange(RIGHT,buff=0.55).move_to(DOWN*4.5)
        self.add(sw)

        # footer
        self.add(Line(LEFT*1.4,ORIGIN,color=CYAN,stroke_width=3).move_to(DOWN*5.6+LEFT*0.7))
        self.add(Line(ORIGIN,RIGHT*1.4,color=AMBER,stroke_width=3).move_to(DOWN*5.6+RIGHT*0.7))
        self.add(Text("@axiobyte  ·  from first principles",font=MN,color=GRAY).scale(0.34).move_to(DOWN*6.1))
        self.wait(0.3)

    # ----- icon builders -----
    def list_node(self,text,color):
        box=RoundedRectangle(width=1.1,height=0.7,corner_radius=0.12,stroke_color=color,stroke_width=2.8,fill_color=SURFACE,fill_opacity=1.0).set_z_index(2)
        t=Text(text,font=MN,weight=BOLD,color=color).scale(0.34).move_to(box.get_center()).set_z_index(3)
        port=Circle(radius=0.09,color=color,fill_opacity=1.0,stroke_width=0).move_to(box.get_right()+LEFT*0.18).set_z_index(3)
        arr=Arrow(port.get_center(),port.get_center()+RIGHT*0.5,buff=0,color=color,stroke_width=4,max_tip_length_to_length_ratio=0.4).set_z_index(3)
        g=VGroup(box,t,port,arr); g.add_to_back(glow(box,color)); return g

    def db_icon(self,color):
        body=RoundedRectangle(width=1.0,height=0.9,corner_radius=0.05,stroke_color=color,stroke_width=2.8,fill_color=SURFACE,fill_opacity=1.0)
        top=Ellipse(width=1.0,height=0.32,color=color,stroke_width=2.8,fill_color=SURF2,fill_opacity=1.0).move_to(body.get_top())
        m1=Ellipse(width=1.0,height=0.32,color=color,stroke_width=2.0,fill_opacity=0).move_to(body.get_center()+UP*0.12)
        g=VGroup(body,m1,top).set_z_index(2); g.add_to_back(glow(body,color)); return g

    def tree_node(self,text,color):
        c=Circle(radius=0.42,color=color,stroke_width=2.8,fill_color=SURFACE,fill_opacity=1.0).set_z_index(2)
        t=Text(text,font=FN,weight=BOLD,color=color).scale(0.4).move_to(c.get_center()).set_z_index(3)
        g=VGroup(c,t); g.add_to_back(glow(c,color)); return g
