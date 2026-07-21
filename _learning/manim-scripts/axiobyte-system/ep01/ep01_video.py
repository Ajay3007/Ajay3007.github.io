"""
AXIOBYTE SYSTEMS -- Episode 01
"Why the kernel cannot keep up with a 100 Gb NIC"   (135.6 s, 9:16 portrait)

Render (video):   manim -qh --fps 60 ep01_video.py FullVideo
Render (draft):   manim -ql --fps 30 ep01_video.py FullVideo
Layout check:     manim -sqh ep01_video.py StillStage      (the machine, at rest)
                  manim -sqh ep01_video.py StillCost       (the cost column, full)

Act previews (each seeds the state it inherits and starts near t=0):
    manim -pql ep01_video.py ActArrival     # 14.5 - 34.7   packet -> IRQ -> CPU
    manim -pql ep01_video.py ActStack       # 34.5 - 59.0   layers, sk_buff, copies
    manim -pql ep01_video.py ActSwitch      # 58.8 - 87.1   wake-up, switch, bottleneck
    manim -pql ep01_video.py ActDPDK        # 86.8 - end    poll mode, hugepages

---------------------------------------------------------------------------
THE ONE RULE
---------------------------------------------------------------------------
Nothing here is eyeballed. Every beat is a WORD START looked up in timeline.json
by W(word, sentence). The whole cue table is resolved at IMPORT, so a typo -- or
a re-cut voiceover that no longer contains the word -- fails immediately instead
of drifting silently out of sync. The film has 120+ cues and not one wait() with
a hand-guessed number in it.

---------------------------------------------------------------------------
TWO LANES, ONE MACHINE
---------------------------------------------------------------------------
The frame is split, and it stays split for the whole film:

    LEFT LANE   -- WHERE THE PACKET IS.   NIC -> kernel stack -> your app, with
                   the kernel/user boundary drawn as a real line the packet has
                   to cross.

    RIGHT LANE  -- WHAT THE CORE IS DOING.  A vertical execution timeline, time
                   flowing DOWNWARD, one band per thing the CPU actually ran:
                   your app, the IRQ, the stack, the copy, the switch. Its
                   height is CYCLES, at a fixed 0.20 px per cycle.

Because both lanes run top-to-bottom they read as one picture: the packet
descends on the left exactly as the core burns cycles on the right. That column
is the whole argument of the episode -- built band by band through the kernel
half, then demolished band by band through the DPDK half, on the words
"no ... no ... almost no". The closing line, "once you understand where the time
is actually spent", is not a claim laid over a diagram. It IS the diagram, and it
has been on screen for ninety seconds.

The mint hairline at the top of that column is the budget: 100 Gb/s of 64-byte
frames is 148.8 Mpps, which on one 3 GHz core is ~20 cycles per packet. The
kernel path costs ~2,200. That is why the hairline is a hairline.

---------------------------------------------------------------------------
COLOUR IS MEANING -- and nothing borrows a hue it does not own
---------------------------------------------------------------------------
    green  NIC          amber  Linux kernel      blue   user space
    yellow DMA/hardware purple memory            red    overhead / bottleneck
    grey   idle         cyan   DPDK (and the brand)
The packet itself is white: it is the thing moving THROUGH all of them.
"""

from manim import *
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# CANVAS -- 1080 x 1920 design space, 1 unit == 100 px
# ---------------------------------------------------------------------------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 10.8
config.frame_height = 19.2

DW, DH = 1080, 1920
CXP, CYP = DW / 2, DH / 2
FH = DH / 100.0                        # full frame height in manim units (19.2)


def P(px, py):
    """Design-space pixel (top-left origin) -> Manim coords."""
    return np.array([(px - CXP) / 100.0, (CYP - py) / 100.0, 0.0])


def U(px):
    """Design-space length -> Manim units."""
    return px / 100.0


def X(px):
    return (px - CXP) / 100.0


# ---------------------------------------------------------------------------
# FONTS -- DejaVu if the machine has it (what the reference episodes render
# with), else the macOS pair the project's own setup guide names as the
# sanctioned substitute. Choosing at import beats silent Pango fallback, which
# would change every measured width in this file.
# ---------------------------------------------------------------------------
def _font(*names):
    try:
        import manimpango
        have = set(manimpango.list_fonts())
    except Exception:
        have = set()
    for n in names:
        if n in have:
            return n
    return names[-1]


FN = _font("DejaVu Sans", "Helvetica Neue", "Helvetica")
MN = _font("DejaVu Sans Mono", "Menlo", "Andale Mono")


# ===========================================================================
# TIMELINE CONTROLLER -- the film is driven by timeline.json, never by guesses
# ===========================================================================
class Timeline:
    """word-level timeline.json, indexed for lookup.

    W("interrupt", s=5) -> the START of the word "interrupt" in sentence 5.
    Raises if it is not there, which is the whole point: a cue can never
    silently point at nothing.
    """

    def __init__(self, path):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        self.words = d["words"]
        self.sentences = d["sentences"]
        self.duration = d["meta"]["duration"]

    @staticmethod
    def _norm(w):
        return w.strip().strip(".,?!;:—–\"'").lower()

    def word(self, text, s=None, occ=0):
        key = self._norm(text)
        hits = [w for w in self.words
                if self._norm(w["word"]) == key
                and (s is None or w["sentence_index"] == s)]
        if len(hits) <= occ:
            where = "" if s is None else f" in sentence {s}"
            raise KeyError(f"timeline.json has no word {text!r}{where} (occurrence {occ})")
        return hits[occ]["start"]


TL = Timeline(os.path.join(HERE, "timeline.json"))
W = TL.word
VOICEOVER_SECONDS = TL.duration        # 135.628


# ---------------------------------------------------------------------------
# THE CUE TABLE -- every beat in the film, resolved from the timeline at IMPORT.
# This is the script. Read it top to bottom and you have read the video.
# ---------------------------------------------------------------------------
CUE = {
    # -- HOOK  "Have you ever wondered why modern servers can have a 100 gigabit
    #           network card, but still struggle to process every packet at line
    #           rate?"
    "hk_open":       W("Have", 0),            #   0.03  the NIC lights up
    "hk_100":        W("100", 0),             #   2.33  100 GbE -- the flood starts
    "hk_struggle":   W("struggle", 0),        #   4.54  the throat appears; jam
    "hk_line":       W("line", 0),            #   6.30  148.8 Mpps -> 20 cycles

    # -- "The answer isn't that Linux is slow."
    "an_linux":      W("Linux", 1),           #   8.34  the throat IS the kernel
    "an_slow":       W("slow", 1),            #   8.76  "SLOW", struck out

    # -- "It's that the traditional networking path does a lot of work for every
    #     single packet."
    "tp_traditional": W("traditional", 2),    #  10.04  the path unfolds: 5 layers
    "tp_path":       W("path", 2),            #  11.00  ...down to your app
    "tp_work":       W("work", 2),            #  12.10  every layer pulses
    "tp_every":      W("every", 2),           #  12.56  x EVERY PACKET
    "tp_packet":     W("packet", 2),          #  13.47

    # -- "Let's see what actually happens."
    "ls_see":        W("see", 3),             #  14.75  the storm clears
    "ls_happens":    W("happens", 3),         #  15.37  one packet, followed

    # -- "A packet arrives at the network card."
    "ar_packet":     W("packet", 4),          #  16.55  it flies in from the wire
    "ar_arrives":    W("arrives", 4),         #  16.87  lands in the rx ring
    "ar_card":       W("card", 4),            #  17.67  DMA into host memory

    # -- "Instead of your application receiving it immediately, the network card
    #     first raises an interrupt to tell the CPU, a packet has arrived."
    "ir_instead":    W("Instead", 5),         #  18.49  the naive straight line
    "ir_app":        W("application", 5),     #  19.03
    "ir_immediately": W("immediately", 5),    #  20.09  ...and it is crossed out
    "ir_first":      W("first", 5),           #  21.95  pull back: the CPU appears
    "ir_interrupt":  W("interrupt", 5),       #  22.88  THE IRQ FIRES
    "ir_cpu":        W("CPU", 5),             #  23.74  [HIGH] the core is hit
    "ir_arrived":    W("arrived", 5),         #  25.26  the message lands

    # -- "The CPU stops whatever it was doing, switches into kernel mode, and
    #     starts running the network driver."
    "cs_stops":      W("stops", 6),           #  26.82  your app's band is cut off
    "cs_switches":   W("switches", 6),        #  28.30  ring 3 -> ring 0
    "cs_kernel":     W("kernel", 6),          #  28.88  the core turns amber
    "cs_driver":     W("driver", 6),          #  30.46  the driver row lights

    # -- "That interruption alone has a cost."
    "ct_that":       W("That", 7),            #  32.03  the IRQ band, isolated
    "ct_cost":       W("cost", 7),            #  33.49  ~500 cyc vs a 20 cyc budget

    # -- "Next, the packet travels through multiple layers of the Linux
    #     networking stack."
    "st_next":       W("Next", 8),            #  34.69
    "st_travels":    W("travels", 8),         #  35.65  the packet enters the stack
    "st_layers":     W("layers", 8),          #  36.69  layer by layer, lit in turn
    "st_stack":      W("stack", 8),           #  37.99  + ~700 cycles

    # -- "During this journey, the packet is wrapped in kernel data structures,
    #     inspected, and often copied into different memory buffers before it
    #     finally reaches your application."
    "jr_during":     W("During", 9),          #  39.08  push in on the packet
    "jr_wrapped":    W("wrapped", 9),         #  40.68  the sk_buff closes around it
    "jr_structures": W("structures", 9),      #  41.72
    "jr_inspected":  W("inspected", 9),       #  42.44  a scan sweeps it
    "jr_copied":     W("copied", 9),          #  43.98  THE COPY
    "jr_buffers":    W("buffers", 9),         #  45.32  kernel buffer / user buffer
    "jr_reaches":    W("reaches", 9),         #  46.72
    "jr_app":        W("application", 9),     #  47.19  it finally lands

    # -- "And that's another source of overhead -- memory copies."
    "ov_another":    W("another", 10),        #  48.97
    "ov_overhead":   W("overhead", 10),       #  49.77  [HIGH pause on the dash]
    "ov_copies":     W("copies", 10),         #  50.85  + ~400 cycles

    # -- "Copying thousands or even millions of packets every second consumes
    #     valuable CPU cycles and memory bandwidth."
    "cp_copying":    W("Copying", 11),        #  51.79  the copy repeats, and repeats
    "cp_millions":   W("millions", 11),       #  53.35  the counter runs
    "cp_second":     W("second", 11),         #  54.80
    "cp_cpu":        W("CPU", 11),            #  56.26  the overhead bands flare
    "cp_bandwidth":  W("bandwidth", 11),      #  57.80  memory bandwidth saturates

    # -- "Finally, your application has to wake up to process the packet."
    "wk_finally":    W("Finally", 12),        #  59.02
    "wk_app":        W("application", 12),    #  59.89  the app is asleep (grey)
    "wk_wake":       W("wake", 12),           #  60.73  ...and wakes (blue)
    "wk_process":    W("process", 12),        #  61.29

    # -- "That means another context switch, from the kernel back to user space."
    "sw_context":    W("context", 13),        #  63.53  the switch band opens
    "sw_switch":     W("switch", 13),         #  63.95
    "sw_kernel":     W("kernel", 13),         #  64.78  the packet crosses the line
    "sw_user":       W("user", 13),           #  65.72

    # -- "Context switches save and restore CPU state, flush caches, and add more
    #     latency."
    "cx_context":    W("Context", 14),        #  66.88  the register file appears
    "cx_save":       W("save", 14),           #  67.78  registers out
    "cx_restore":    W("restore", 14),        #  68.24  registers in
    "cx_state":      W("state", 14),          #  69.08
    "cx_flush":      W("flush", 14),          #  69.64  the cache goes cold
    "cx_caches":     W("caches", 14),         #  69.94
    "cx_latency":    W("latency", 14),        #  71.33  + ~600 cycles

    # -- "Now imagine this happening not once, but millions of times every second."
    "mn_now":        W("Now", 15),            #  72.31  go and live in the column
    "mn_once":       W("once", 15),           #  73.95  ONE packet, bracketed
    "mn_millions":   W("millions", 15),       #  74.94  ...tiled, over and over
    "mn_second":     W("second", 15),         #  76.40  all of it red

    # -- "Interrupts, memory copies, context switches."
    "th_interrupts": W("Interrupts", 16),     #  77.62  three chips, one per word
    "th_copies":     W("copies", 16),         #  78.76
    "th_switches":   W("switches", 16),       #  79.84

    # -- "Individually, they seem small."
    "iv_indiv":      W("Individually", 17),   #  80.97  push in until they look tiny
    "iv_small":      W("small", 17),          #  82.05

    # -- "Together, they become the biggest bottleneck in high-performance
    #     networking."
    "tg_together":   W("Together", 18),       #  82.81  they stack into one bar
    "tg_biggest":    W("biggest", 18),        #  84.01
    "tg_bottleneck": W("bottleneck", 18),     #  84.47  the hook's throat returns
    "tg_networking": W("networking", 18),     #  85.83

    # -- "This is where DPDK changes everything."
    "dp_this":       W("This", 19),           #  87.06  title card
    "dp_changes":    W("changes", 19),        #  88.12

    # -- "Instead of waiting for interrupts, DPDK continuously polls the network
    #     card."
    "pl_interrupts": W("interrupts", 20),     #  90.58  the IRQ line is cut
    "pl_dpdk":       W("DPDK", 20),           #  91.27  [HIGH] the app becomes a PMD
    "pl_polls":      W("polls", 20),          #  92.63  the poll loop spins
    "pl_card":       W("card", 20),           #  93.47  a burst comes back

    # -- "It maps packet buffers directly into user space memory using huge pages,
    #     allowing the application to access packets without the traditional
    #     kernel networking stack."
    "mp_maps":       W("maps", 21),           #  94.49  the kernel steps aside
    "mp_buffers":    W("buffers", 21),        #  95.19  the straight lane draws
    "mp_directly":   W("directly", 21),       #  95.59  the packet takes it
    "mp_user":       W("user", 21),           #  96.28  the mbuf pool, in user space
    "mp_huge":       W("huge", 21),           #  97.68  4K pages...
    "mp_pages":      W("pages", 21),          #  98.04  ...merge into 2 MB pages
    "mp_allowing":   W("allowing", 21),       #  99.02  the app reaches in
    "mp_access":     W("access", 21),         # 100.24  read in place -- zero copy
    "mp_without":    W("without", 21),        # 101.12
    "mp_stack":      W("stack", 21),          # 103.01  the stack sits idle

    # -- "The result?"
    "rs_result":     W("result", 22),         # 103.97  back to the cost column

    # -- "No per-packet interrupts, no unnecessary memory copies, almost no
    #     context switches."
    "no_irq":        W("No", 23),             # 104.97  [HIGH] the IRQ band goes
    "no_irq_w":      W("interrupts", 23),     # 105.81
    "no_copy":       W("no", 23, 1),          # 106.57  [HIGH] the copy band goes
    "no_copy_w":     W("copies", 23),         # 107.78
    "no_almost":     W("almost", 23),         # 108.64
    "no_switch":     W("no", 23, 2),          # 109.14  the switch band goes
    "no_switch_w":   W("switches", 23),       # 109.86

    # -- "The CPU spends its time processing packets instead of managing operating
    #     system overhead."
    "cy_cpu":        W("CPU", 24),            # 111.02  [HIGH] the reclaimed time...
    "cy_processing": W("processing", 24),     # 112.25  ...becomes packet processing
    "cy_instead":    W("instead", 24),        # 113.39
    "cy_overhead":   W("overhead", 24),       # 115.17

    # -- "That's why technologies like DPDK power high-performance firewalls, load
    #     balancers, telecom systems, and modern cloud networking."
    "ap_dpdk":       W("DPDK", 25),           # 117.70  [HIGH] four fan-outs
    "ap_firewalls":  W("firewalls", 25),      # 119.56
    "ap_balancers":  W("balancers", 25),      # 120.66
    "ap_telecom":    W("telecom", 25),        # 121.64
    "ap_cloud":      W("cloud", 25),          # 123.39

    # -- "Where processing millions of packets per second isn't just an
    #     optimization, it's a requirement."
    "rq_millions":   W("millions", 26),       # 125.61  148.8 Mpps
    "rq_second":     W("second", 26),         # 126.74
    "rq_optimization": W("optimization", 26), # 127.88  struck out
    "rq_requirement": W("requirement", 26),   # 129.18  stamped

    # -- "Once you understand where the time is actually spent, the performance
    #     difference becomes obvious."
    "cl_once":       W("Once", 27),           # 130.72  the two columns, side by side
    "cl_spent":      W("spent", 27),          # 132.67
    "cl_difference": W("difference", 27),     # 134.03  ~0.5 Mpps -> 15-30 Mpps
    "cl_obvious":    W("obvious", 27),        # 134.81
}


# ---------------------------------------------------------------------------
# VOICEOVER
# ---------------------------------------------------------------------------
AUDIO_CANDIDATES = [os.path.join(HERE, n) for n in
                    ("voiceover.mp3", "voiceover.mpeg", "voiceover.wav")]


def _add_voiceover(scene):
    for p in AUDIO_CANDIDATES:
        if os.path.exists(p):
            scene.add_sound(p)
            return
    print("[VO] narration audio not found -- rendering silent.")


class VOScene(MovingCameraScene):
    """Scene whose cue(t) anchors beats to voiceover timestamps.

    The authoritative clock is manim's own renderer.time, and cue(t) inserts
    exactly enough dead time to reach absolute time t (minus a small lead, so
    motion is already underway when the word is heard). `epoch` shifts the whole
    timeline so one act can be previewed starting near t=0.

    Do NOT override play()/wait() to keep a private clock -- manim's wait() is
    implemented on top of play(), so a naive override double-counts every wait.
    """

    epoch = 0.0
    LEAD = 0.22        # begin each beat ~0.22 s before its spoken word

    def now(self):
        return self.renderer.time

    def cue(self, t, lead=None):
        lead = self.LEAD if lead is None else lead
        gap = (t - self.epoch - lead) - self.now()
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.06:
            print(f"[SYNC] behind by {-gap:5.2f}s at t={t:7.2f} "
                  f"(clock={self.now():7.2f}, epoch={self.epoch})")

    def at(self, key, lead=None):
        self.cue(CUE[key], lead=lead)


# ---------------------------------------------------------------------------
# PALETTE -- one hue per idea, for the whole film, and nothing borrows.
# ---------------------------------------------------------------------------
BG      = "#090C13"
SURFACE = "#141B27"
SURF2   = "#0F1420"
BORDER  = "#26344A"

INK     = "#EAF0F6"    # WHITE   -- the packet, and headline type
SUBTLE  = "#9AA6BC"
IDLE    = "#65728A"    # GREY    -- idle / parked
USER    = "#4AA8FF"    # BLUE    -- user space
KERN    = "#F0A431"    # ORANGE  -- the Linux kernel
NIC_C   = "#4DE6A0"    # GREEN   -- the NIC
HW      = "#F5D14F"    # YELLOW  -- DMA / hardware
MEM     = "#B79CF0"    # PURPLE  -- memory
BAD     = "#FF5C55"    # RED     -- overhead / bottleneck
DPDK_C  = "#34D8E8"    # CYAN    -- DPDK (and the AxioByte mark)

KERN_BG = "#33240F"
BAD_BG  = "#331617"
DPDK_BG = "#10303A"
NIC_BG  = "#0F2A20"
MEM_BG  = "#221B38"

Z_GLOW, Z_ZONE, Z_NODE, Z_LINE, Z_LABEL, Z_PKT, Z_CARD = 0, 1, 2, 3, 5, 7, 9
Z_SCRIM, Z_TITLE, Z_KEY = 20, 21, 25

# type ladder (font_size ~= on-screen pixel height at this canvas)
KEY_SIZE, TITLE_SIZE, CAP_SIZE = 38, 66, 30
NODE_T, NODE_S, ROW_T, TAG_T, MONO_S = 33, 21, 24, 22, 18


# ---------------------------------------------------------------------------
# LAYOUT -- two lanes, fixed for the whole film (design px).
#   LEFT  x 148..596   the packet's journey
#   RIGHT x 640..1040  the core's execution timeline
# The keyword and the caption are pinned to the CAMERA FRAME, not to the world,
# because this film pushes the camera into single objects and a world-anchored
# header would be cropped the instant it did.
# ---------------------------------------------------------------------------
SPINE_X, SPINE_W = 372, 448
NIC_Y,  NIC_H = 430, 190          #  335 .. 525
KRN_Y,  KRN_H = 856, 476          #  618 .. 1094
BOUND_Y = 1148                    # the kernel / user line
APP_Y,  APP_H = 1272, 168         # 1188 .. 1356
FLOOR_Y = 1500                    # scratch band for temporary props

KROWS = [("IRQ + softirq", 742), ("driver (NAPI)", 812), ("sk_buff alloc", 882),
         ("IP / TCP stack", 952), ("copy to socket", 1022)]

CPU_X, CPU_W = 840, 400           #  640 .. 1040
CPU_TOP, CPU_BOT = 322, 1330
BAR_X, BAR_W = 753, 170           # the execution bar: 668 .. 838
LBL_X = 856                       # its labels, left-aligned
TL_TOP = 480                      # the first band starts here
CYC_PX = 0.20                     # 1 cycle == 0.20 px of column. Never changes.

BUDGET_CYC = 20                   # 148.8 Mpps on one 3 GHz core
FULL_FRAME = (CXP, 930, 1.00)     # the whole machine
LEFT_FRAME = (400, 880, 0.78)     # just the packet's lane


# ===========================================================================
# DRAWING TOOLKIT
# ===========================================================================
def glow(shape, color=None, layers=5, spread=0.24, max_op=0.13):
    """A soft halo: nested translucent copies. Cheap, and it survives a camera
    push far better than a fat stroke does."""
    if color is None:
        color = shape.get_stroke_color()
    halo = VGroup()
    for i in range(layers):
        f = (i + 1) / layers
        c = shape.copy().set_stroke(width=0).set_fill(color, opacity=max_op * (1 - f) + 0.012)
        c.scale(1 + spread * f)
        halo.add(c)
    return halo.set_z_index(Z_GLOW)


def T(txt, size=ROW_T, color=INK, font=None, bold=True):
    return Text(txt, font=font or FN, weight=(BOLD if bold else NORMAL),
                color=color, font_size=size)


def box(w, h, color, fill=SURF2, fill_op=1.0, r=0.16, sw=3.0):
    return RoundedRectangle(width=U(w), height=U(h), corner_radius=r,
                            stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=fill_op)


def node(title, sub=None, w=SPINE_W, h=NIC_H, color=NIC_C, px=None, py=None,
         glowing=True, tsize=NODE_T):
    """A labelled component of the machine."""
    b = box(w, h, color).set_z_index(Z_NODE)
    t = T(title, tsize, INK)
    inner = t
    if sub:
        inner = VGroup(t, T(sub, NODE_S, IDLE, font=MN, bold=False)).arrange(DOWN, buff=0.09)
    if inner.width > U(w) - 0.30:
        inner.scale_to_fit_width(U(w) - 0.30)
    inner.move_to(b.get_center()).set_z_index(Z_LABEL)
    g = VGroup(b, inner)
    if glowing:
        g.add_to_back(glow(b, color, layers=5, spread=0.14, max_op=0.09))
    g.box, g.label = b, inner
    if px is not None:
        g.move_to(P(px, py))
    return g


def pill(txt, color, bg=None, size=TAG_T, h=56, glowing=False, mono=False):
    t = T(txt, size, color, font=(MN if mono else FN))
    b = RoundedRectangle(width=t.width + 0.44, height=U(h), corner_radius=U(h) / 2,
                         stroke_color=color, stroke_width=2.4,
                         fill_color=(bg or SURF2), fill_opacity=1.0).set_z_index(Z_CARD)
    t.move_to(b.get_center()).set_z_index(Z_CARD + 1)
    g = VGroup(b, t)
    if glowing:
        g.add_to_back(glow(b, color, layers=5, spread=0.34, max_op=0.14))
    return g


def tag(txt, color, size=TAG_T, mono=False):
    """A small plated label -- readable over anything it is dropped on."""
    t = T(txt, size, color, font=(MN if mono else FN))
    plate = SurroundingRectangle(t, buff=0.13, corner_radius=0.09, stroke_width=0,
                                 fill_color=BG, fill_opacity=0.88)
    return VGroup(plate, t).set_z_index(Z_LABEL)


def packet(color=INK, s=26, glowing=False):
    """One packet. White, because it is the thing moving THROUGH the machine."""
    sq = RoundedRectangle(width=U(s), height=U(s), corner_radius=U(s) / 4,
                          stroke_color=color, stroke_width=1.8,
                          fill_color=color, fill_opacity=0.92).set_z_index(Z_PKT)
    g = VGroup(sq)
    if glowing:
        g.add_to_back(glow(sq, color, layers=5, spread=0.9, max_op=0.30))
    return g


def vlink(py0, py1, px=SPINE_X, color=IDLE, sw=5):
    return Arrow(P(px, py0), P(px, py1), buff=0.02, color=color, stroke_width=sw,
                 max_tip_length_to_length_ratio=0.28,
                 max_stroke_width_to_length_ratio=999).set_z_index(Z_LINE)


def bolt(p0, p1, color=BAD, sw=6, n=5, amp=26):
    """An interrupt line: a zig-zag, because an IRQ is not a polite arrow."""
    pts = []
    for i in range(n + 1):
        f = i / n
        base = p0 + (p1 - p0) * f
        off = 0.0 if i in (0, n) else (amp / 100.0) * (1 if i % 2 else -1)
        pts.append(base + np.array([0.0, off, 0.0]))
    return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners(pts) \
        .set_z_index(Z_LINE)


def strike(mob, color=BAD, sw=5, pad=0.10):
    return Line(mob.get_left() + LEFT * pad, mob.get_right() + RIGHT * pad,
                color=color, stroke_width=sw).set_z_index(Z_CARD + 2)


def _dimmed(m, f):
    """A copy of `m` with every fill and stroke opacity SCALED by f.

    set_opacity(0.16) would be wrong here and wrong in a way that is easy to miss:
    these groups carry glow halos whose layers sit at 1-13% opacity, so assigning
    them 16% makes the halo BRIGHTER and the node turns into a solid colour block.
    Scaling preserves the relationship between a shape and its own halo."""
    c = m.copy()
    for sm in c.family_members_with_points():
        sm.set_fill(opacity=sm.get_fill_opacity() * f)
        sm.set_stroke(opacity=sm.get_stroke_opacity() * f)
    return c


def dim(mobs, f=0.20):
    """Step back, reversibly: each mobject saves its state so undim() can Restore
    it exactly, halos included."""
    out = []
    for m in mobs:
        m.save_state()
        out.append(Transform(m, _dimmed(m, f)))
    return out


def undim(mobs):
    return [Restore(m) for m in mobs if getattr(m, "saved_state", None) is not None]


def cam(scene, window):
    px, py, k = window
    return scene.camera.frame.animate.scale_to_fit_height(FH * k).move_to(P(px, py))


def set_cam(scene, window):
    px, py, k = window
    scene.camera.frame.scale_to_fit_height(FH * k).move_to(P(px, py))


# ===========================================================================
# THE PINNED CHROME -- chapter keyword (top) and caption (bottom)
# ===========================================================================
class _Pinned:
    """Base for the two bars that ride the camera frame. An updater re-solves
    both the position AND the on-screen size from the live frame every frame, so
    a push-in from 1.0x to 0.42x neither crops the bar nor doubles its size."""

    EDGE = UP

    def __init__(self, scene, pad=0.95):
        self.scene, self.pad, self.mob = scene, pad, None

    def _apply(self, m):
        f = self.scene.camera.frame
        k = f.height / FH
        want = m._base_w * k
        if abs(m.width - want) > 1e-4:
            m.scale_to_fit_width(want)
        y = (f.get_top()[1] - k * self.pad - m.height / 2) if self.EDGE is UP else \
            (f.get_bottom()[1] + k * self.pad + m.height / 2)
        m.move_to([f.get_center()[0], y, 0])

    def _place(self, m):
        m._base_w = m.width
        self._apply(m)
        return m

    def _pin(self, m):
        m.add_updater(self._apply)
        self.mob = m


class KeywordBar(_Pinned):
    """The chapter indicator: ONE keyword at a time, never popped on."""

    EDGE = UP
    MAXW = 6.2

    def _build(self, label, color):
        t = T(label, KEY_SIZE, color).set_z_index(Z_KEY)
        if t.width > self.MAXW:
            t.scale_to_fit_width(self.MAXW)
        return self._place(t)

    def to(self, label, color, run_time=0.7, extra=None):
        new = self._build(label, color)
        if self.mob is None:
            self.scene.play(FadeIn(new, shift=DOWN * 0.14), *(extra or []), run_time=run_time)
        else:
            self.mob.clear_updaters()
            self.scene.play(FadeTransform(self.mob, new), *(extra or []), run_time=run_time)
        self._pin(new)

    def hide(self, run_time=0.5, extra=None):
        """Step the chapter indicator out. A deep push-in re-solves the pin from
        the new frame, and at 0.44x the slot lands inside the panel it is meant to
        label -- so the label leaves rather than sit on top of its own subject."""
        if self.mob is None:
            if extra:
                self.scene.play(*extra, run_time=run_time)
            return
        self.mob.clear_updaters()
        self.scene.play(FadeOut(self.mob, shift=UP * 0.16), *(extra or []),
                        run_time=run_time)
        self.mob = None

    def morph_from(self, title, label, color, run_time=0.85, extra=None):
        """A full-screen title card SHRINKS into the slot and becomes the keyword."""
        new = self._build(label, color)
        anims = [ReplacementTransform(title, new)]
        if self.mob is not None:
            self.mob.clear_updaters()
            anims.append(FadeOut(self.mob, shift=UP * 0.18))
        self.scene.play(*anims, *(extra or []), run_time=run_time)
        self._pin(new)


class CaptionBar(_Pinned):
    """One caption at a time, on a soft plate so it stays legible over anything."""

    EDGE = DOWN
    MAXW = 8.6

    def _build(self, txt, color):
        t = T(txt, CAP_SIZE, color)
        if t.width > self.MAXW:
            t.scale_to_fit_width(self.MAXW)
        plate = SurroundingRectangle(t, buff=0.22, corner_radius=0.14, stroke_width=0,
                                     fill_color=SURF2, fill_opacity=0.94)
        acc = RoundedRectangle(width=0.09, height=t.height + 0.16, corner_radius=0.045,
                               stroke_width=0, fill_color=color, fill_opacity=1.0)
        g = VGroup(plate, acc, t).set_z_index(Z_CARD)
        acc.next_to(plate.get_left(), RIGHT, buff=0.14)
        t.next_to(acc, RIGHT, buff=0.16)
        g._base_w = g.width
        self._apply(g)
        return g

    def show(self, txt, color=SUBTLE, run_time=0.45, extra=None):
        new = self._build(txt, color)
        if self.mob is None:
            self.scene.play(FadeIn(new, shift=UP * 0.10), *(extra or []), run_time=run_time)
        else:
            self.mob.clear_updaters()
            self.scene.play(FadeTransform(self.mob, new), *(extra or []), run_time=run_time)
        new.add_updater(self._apply)
        self.mob = new

    def clear(self, run_time=0.35, extra=None):
        if self.mob is None:
            if extra:
                self.scene.play(*extra, run_time=run_time)
            return
        self.mob.clear_updaters()
        self.scene.play(FadeOut(self.mob, shift=DOWN * 0.10), *(extra or []), run_time=run_time)
        self.mob = None


def make_scrim(op=0.88):
    return Rectangle(width=config.frame_width * 1.4, height=config.frame_height * 1.4,
                     fill_color=BG, fill_opacity=op, stroke_width=0) \
        .move_to(ORIGIN).set_z_index(Z_SCRIM)


def title_card(scene, kb, label, color, t_in, t_out, sub=None, extra_out=None):
    """The film's one title grammar. The card does not simply leave: it shrinks
    into the top of the frame and BECOMES the chapter keyword it just opened."""
    sc = make_scrim()
    f = scene.camera.frame
    ttl = T(label, TITLE_SIZE, color).move_to(f.get_center() + UP * 0.6).set_z_index(Z_TITLE)
    rule = Line(ttl.get_left(), ttl.get_right(), color=color, stroke_width=3.5) \
        .next_to(ttl, DOWN, buff=0.24).set_opacity(0.65).set_z_index(Z_TITLE)
    extra_in, sub_m = [], None
    if sub:
        sub_m = T(sub, CAP_SIZE, SUBTLE, bold=False).next_to(rule, DOWN, buff=0.26) \
            .set_z_index(Z_TITLE)
        extra_in = [FadeIn(sub_m, shift=UP * 0.1)]
    scene.cue(t_in)
    scene.play(FadeIn(sc), Write(ttl), Create(rule), *extra_in, run_time=0.72)
    scene.cue(t_out)
    out = [FadeOut(sc), FadeOut(rule, scale=0.6)] + \
          ([FadeOut(sub_m, scale=0.6)] if sub_m else []) + list(extra_out or [])
    kb.morph_from(ttl, label, color, run_time=0.85, extra=out)


# ===========================================================================
# THE LEFT LANE -- the machine the packet travels through
# ===========================================================================
class Stage:
    """Every persistent mobject in the film, in one place, so an act preview can
    rebuild exactly what it inherits."""

    def __init__(self):
        self.__dict__["_d"] = {}

    def __getattr__(self, k):
        try:
            return self.__dict__["_d"][k]
        except KeyError:
            raise AttributeError(k)

    def __setattr__(self, k, v):
        self.__dict__["_d"][k] = v


def build_nic():
    """The NIC, with a visible rx ring: five descriptors the DMA engine fills."""
    b = box(SPINE_W, NIC_H, NIC_C).move_to(P(SPINE_X, NIC_Y)).set_z_index(Z_NODE)
    ttl = T("NIC", NODE_T, INK).move_to(P(SPINE_X - 130, NIC_Y - 46)).set_z_index(Z_LABEL)
    sub = T("100 GbE", NODE_S, NIC_C, font=MN).move_to(P(SPINE_X + 120, NIC_Y - 44)) \
        .set_z_index(Z_LABEL)
    slots = VGroup(*[
        box(54, 44, NIC_C, fill=SURF2, r=0.05, sw=2.0)
        .move_to(P(SPINE_X + 46 + (i - 2) * 62, NIC_Y + 44))
        for i in range(5)]).set_z_index(Z_NODE)
    ring = T("rx ring", MONO_S, IDLE, font=MN, bold=False) \
        .move_to(P(SPINE_X - 168, NIC_Y + 44)).set_z_index(Z_LABEL)
    g = VGroup(b, ttl, sub, slots, ring)
    g.add_to_back(glow(b, NIC_C, layers=5, spread=0.13, max_op=0.09))
    g.box, g.slots = b, slots
    return g


def build_kernel():
    """The Linux networking stack, as five real stages -- not a grey rectangle."""
    b = box(SPINE_W, KRN_H, KERN).move_to(P(SPINE_X, KRN_Y)).set_z_index(Z_NODE)
    ttl = T("LINUX KERNEL", NODE_T, KERN).move_to(P(SPINE_X, 668)).set_z_index(Z_LABEL)
    rows = VGroup()
    for name, y in KROWS:
        rb = box(380, 58, KERN, fill=SURFACE, r=0.08, sw=1.8).move_to(P(SPINE_X, y))
        rt = T(name, ROW_T, SUBTLE, bold=False).move_to(P(SPINE_X, y))
        r = VGroup(rb, rt).set_z_index(Z_NODE + 1)
        r.box = rb
        rows.add(r)
    g = VGroup(b, ttl, rows)
    g.add_to_back(glow(b, KERN, layers=5, spread=0.10, max_op=0.08))
    g.box, g.title, g.rows = b, ttl, rows
    return g


def build_app():
    return node("YOUR APP", "recv()", SPINE_W, APP_H, USER, SPINE_X, APP_Y)


def build_boundary():
    ln = DashedLine(P(120, BOUND_Y), P(624, BOUND_Y), color=IDLE, stroke_width=2.6,
                    dash_length=0.14).set_z_index(Z_LINE)
    a = T("kernel space", MONO_S, IDLE, font=MN, bold=False) \
        .move_to(P(232, BOUND_Y - 28)).set_z_index(Z_LABEL)
    bl = T("user space", MONO_S, USER, font=MN, bold=False) \
        .move_to(P(224, BOUND_Y + 30)).set_z_index(Z_LABEL)
    g = VGroup(ln, a, bl)
    g.line = ln
    return g


def throat_shape(op=0.30):
    """The constriction from the hook -- and, seventy-five seconds later, the
    thing it was always a picture of. The waist is 84 px against a 30 px packet:
    wide enough that one gets through, narrow enough that the rest do not."""
    lf = Polygon(P(112, 700), P(330, 862), P(330, 948), P(112, 1110),
                 stroke_color=BAD, stroke_width=3, fill_color=BAD, fill_opacity=op)
    rt = Polygon(P(632, 700), P(414, 862), P(414, 948), P(632, 1110),
                 stroke_color=BAD, stroke_width=3, fill_color=BAD, fill_opacity=op)
    return VGroup(lf, rt).set_z_index(Z_ZONE)


# ===========================================================================
# THE RIGHT LANE -- what the core is actually executing.
#
# Time flows DOWNWARD and height is CYCLES, at a fixed 0.20 px per cycle. That
# constant is the reason the column can be trusted: the interrupt band is taller
# than the copy band because 500 > 400, not because it looked better that way.
# ===========================================================================
class CPUColumn:
    def __init__(self, scene):
        self.scene = scene
        self.y = TL_TOP
        self.segs = []

    # -- chrome ------------------------------------------------------------
    def chrome(self):
        b = box(CPU_W, CPU_BOT - CPU_TOP, BORDER, fill=SURF2, fill_op=0.94, sw=2.2) \
            .move_to(P(CPU_X, (CPU_TOP + CPU_BOT) / 2)).set_z_index(Z_ZONE)
        ttl = T("CPU CORE", NODE_T - 3, INK).move_to(P(CPU_X - 78, CPU_TOP + 46)) \
            .set_z_index(Z_LABEL)
        ghz = T("3.0 GHz", MONO_S, IDLE, font=MN, bold=False) \
            .move_to(P(CPU_X + 118, CPU_TOP + 46)).set_z_index(Z_LABEL)
        g = VGroup(b, ttl, ghz)
        g.box = b
        return g

    def budget_mark(self):
        """The whole per-packet budget: 148.8 Mpps on one 3 GHz core = ~20 cycles.
        Drawn to the same scale as everything else, which is why it is a hairline."""
        h = max(BUDGET_CYC * CYC_PX, 5)
        r = Rectangle(width=U(BAR_W), height=U(h), stroke_width=0,
                      fill_color=NIC_C, fill_opacity=1.0) \
            .move_to(P(BAR_X, TL_TOP - 20)).set_z_index(Z_LABEL)
        halo = Rectangle(width=U(BAR_W + 8), height=U(h * 5), stroke_width=0,
                         fill_color=NIC_C, fill_opacity=0.13) \
            .move_to(r.get_center()).set_z_index(Z_GLOW)
        lab = T("your whole budget: 20 cyc", MONO_S, NIC_C, font=MN, bold=False) \
            .move_to(P(CPU_X, TL_TOP - 54)).set_z_index(Z_LABEL)
        return VGroup(halo, r, lab)

    # -- bands -------------------------------------------------------------
    def band(self, name, cyc=None, px=None, color=USER, sub=None):
        """Build (do not play) the next band. Height is cycles unless px is given."""
        h = px if px is not None else cyc * CYC_PX
        cy = self.y + h / 2
        r = Rectangle(width=U(BAR_W), height=U(h), stroke_width=1.4,
                      stroke_color=color, fill_color=color, fill_opacity=0.80) \
            .move_to(P(BAR_X, cy)).set_z_index(Z_NODE)
        parts = [T(name, TAG_T, color)]
        if cyc is not None:
            parts.append(T(f"{cyc} cyc", MONO_S, color, font=MN, bold=False))
        if sub is not None:
            parts.append(T(sub, MONO_S - 2, IDLE, font=MN, bold=False))
        lab = VGroup(*parts).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        maxw = U(CPU_X + CPU_W / 2 - 16 - LBL_X)
        if lab.width > maxw:
            lab.scale_to_fit_width(maxw)
        lab.move_to(P(LBL_X, cy), aligned_edge=LEFT).set_z_index(Z_LABEL)
        seg = VGroup(r, lab)
        seg.rect, seg.lab, seg.h, seg.color = r, lab, h, color
        self.y += h
        self.segs.append(seg)
        return seg

    @staticmethod
    def anim(seg):
        return [GrowFromEdge(seg.rect, UP), FadeIn(seg.lab, shift=RIGHT * 0.12)]

    def below(self, seg):
        i = self.segs.index(seg)
        return self.segs[i + 1:]

    def collapse(self, seg, run_time=0.6, extra=None):
        """Remove a band and pull everything under it up by exactly its height --
        the column shrinks by the cycles that were removed, and by nothing else."""
        dy = UP * U(seg.h)
        below = self.below(seg)
        self.segs.remove(seg)
        self.y -= seg.h
        self.scene.play(FadeOut(seg.rect, scale=0.85), FadeOut(seg.lab, shift=RIGHT * 0.2),
                        *[b.animate.shift(dy) for b in below], *(extra or []),
                        run_time=run_time)


# ===========================================================================
# ACT 0 -- THE HOOK   (0.0 - 9.6 s)
#   "Have you ever wondered why modern servers can have a 100 gigabit network
#    card, but still struggle to process every packet at line rate?"
#   "The answer isn't that Linux is slow."
# ===========================================================================
def act_hook(scene, st, kb, cap):
    set_cam(scene, LEFT_FRAME)

    # 0.03  the NIC, alone, with its rx ring already drawn: everything that
    # follows happens because of what lands in those five descriptors.
    st.nic = build_nic()
    scene.at("hk_open", lead=0.0)
    scene.play(FadeIn(st.nic, shift=DOWN * 0.2), run_time=0.7)

    # 2.33  "a 100 GIGABIT network card"  -- and the wire opens. The packets are
    # released with a long lag so that something is ALWAYS in flight: this is the
    # one shot in the film where the frame should feel like it cannot keep up.
    st.pkts = VGroup(*[packet(INK, 30) for _ in range(10)])
    for i, p in enumerate(st.pkts):
        p.move_to(P(SPINE_X + (i % 5 - 2) * 62, NIC_Y + 44))
    rate = pill("148.8 Mpps  ·  64-byte frames", NIC_C, NIC_BG, TAG_T, glowing=True) \
        .move_to(P(SPINE_X, 196))
    scene.at("hk_100")
    scene.play(FadeIn(rate, scale=1.08), run_time=0.35)
    scene.play(LaggedStart(*[p.animate.move_to(P(SPINE_X + (i % 5 - 2) * 62, 1740))
                             for i, p in enumerate(st.pkts)], lag_ratio=0.12),
               run_time=1.85, rate_func=linear)

    # 4.54  "...but still STRUGGLE..."  -- the throat. Fifteen more arrive and
    # stack up against it; exactly one gets through. This shape is the film's
    # thesis, and it comes back at 84.47 under its real name.
    st.throat = throat_shape()
    jam = VGroup(*[packet(INK, 30) for _ in range(15)])
    for i, p in enumerate(jam):
        p.move_to(P(SPINE_X + (i % 5 - 2) * 62, NIC_Y + 44))
    scene.at("hk_struggle")
    scene.play(FadeIn(st.throat), run_time=0.25)
    scene.play(LaggedStart(*[p.animate.move_to(P(SPINE_X + (i % 5 - 2) * 56,
                                                 668 - (i // 5) * 38))
                             for i, p in enumerate(jam)], lag_ratio=0.055),
               run_time=1.05)
    trickle = packet(INK, 30).move_to(P(SPINE_X, 760))
    scene.play(FadeIn(trickle), trickle.animate.move_to(P(SPINE_X, 1740)),
               run_time=0.30, rate_func=linear)
    st.pkts = jam

    # 6.30  "...at LINE RATE?"  -- the number that governs the rest of the film.
    # 100 Gb/s of 64-byte frames is 148.8 Mpps; one 3 GHz core therefore owes a
    # packet every ~20 cycles. Everything after this is measured against that.
    bud = pill("≈ 20 cycles per packet", KERN, KERN_BG, TAG_T + 2, h=62, glowing=True) \
        .move_to(P(SPINE_X, 1330))
    scene.at("hk_line")
    scene.play(FadeTransform(rate.copy(), bud), run_time=0.55)
    cap.show("one 3 GHz core · that is the whole budget", KERN)

    # 8.34  "The answer isn't that LINUX is SLOW."  -- the throat was never a
    # metaphor. It is the kernel, and it is about to be named.
    st.krn = build_kernel()
    for r in st.krn.rows:
        r.set_opacity(0.0)
    keep = st.pkts[:5]
    scene.at("an_linux", lead=0.30)
    scene.play(ReplacementTransform(st.throat, st.krn),
               FadeOut(bud, shift=DOWN * 0.2), FadeOut(rate, shift=UP * 0.2),
               *[FadeOut(p, scale=0.5) for p in st.pkts[5:]],
               *[p.animate.move_to(P(SPINE_X + (i - 2) * 56, 570)).scale(0.8)
                 for i, p in enumerate(keep)], run_time=0.45)
    st.pkts = keep
    slow = tag("SLOW", BAD, TAG_T + 4).move_to(P(SPINE_X + 292, 668))
    sl = strike(slow)
    scene.at("an_slow")
    scene.play(FadeIn(slow, scale=1.2), run_time=0.3)
    scene.play(Create(sl), slow.animate.set_opacity(0.4), run_time=0.45)
    st.slow = VGroup(slow, sl)


# ===========================================================================
# ACT 1 -- THE PATH   (9.6 - 16.5 s)
#   "It's that the traditional networking path does a lot of work for every
#    single packet."
#   "Let's see what actually happens."
# ===========================================================================
def act_path(scene, st, kb, cap):
    # 10.04  the kernel is not one box. It is five stages, and the packet is
    # obliged to visit all of them.
    scene.at("tp_traditional")
    scene.play(FadeOut(st.slow),
               LaggedStart(*[r.animate.set_opacity(1.0) for r in st.krn.rows],
                           lag_ratio=0.14), run_time=0.9)

    # 11.00  "...networking PATH..."  -- and it ends somewhere: your process, on
    # the far side of a boundary the packet cannot cross for free.
    st.app = build_app()
    st.bound = build_boundary()
    st.a1 = vlink(NIC_Y + NIC_H / 2 + 8, KRN_Y - KRN_H / 2 - 8)
    st.a2 = vlink(KRN_Y + KRN_H / 2 + 8, APP_Y - APP_H / 2 - 8)
    scene.at("tp_path")
    scene.play(GrowArrow(st.a1), GrowArrow(st.a2), FadeIn(st.bound),
               FadeIn(st.app, shift=UP * 0.15), run_time=0.7)

    # 12.10  "...does a LOT OF WORK..."  -- each stage flares in turn. Work is
    # not narrated here, it is watched.
    scene.at("tp_work")
    scene.play(LaggedStart(*[Indicate(r, color=KERN, scale_factor=1.06)
                             for r in st.krn.rows], lag_ratio=0.11), run_time=0.45)

    # 12.56  "...for EVERY SINGLE PACKET."  -- and the jam dives in, all of it.
    ev = pill("× every single packet", BAD, BAD_BG, TAG_T + 2, h=60, glowing=True) \
        .move_to(P(SPINE_X, 1420))
    scene.at("tp_every")
    scene.play(LaggedStart(*[p.animate.move_to(P(SPINE_X + (i % 3 - 1) * 46, KRN_Y))
                             .set_opacity(0.22)
                             for i, p in enumerate(st.pkts)], lag_ratio=0.06),
               run_time=0.65)
    scene.at("tp_packet")
    scene.play(FadeIn(ev, scale=1.08), run_time=0.45)

    # 14.75  "Let's see what ACTUALLY HAPPENS."  -- the storm clears, and the
    # film slows down to follow exactly one of them.
    scene.at("ls_see")
    scene.play(FadeOut(ev, shift=DOWN * 0.2),
               *[FadeOut(p, scale=0.4) for p in st.pkts],
               st.krn.rows.animate.set_opacity(0.35), run_time=0.6)
    st.pkt = packet(INK, 30, glowing=True).move_to(P(920, 250))
    scene.at("ls_happens")
    kb.to("THE PACKET PATH", NIC_C, run_time=0.5)
    cap.show("one packet, from wire to process", SUBTLE)


# ===========================================================================
# ACT 2 -- ARRIVAL AND THE INTERRUPT   (16.5 - 34.7 s)
#   "A packet arrives at the network card."
#   "Instead of your application receiving it immediately, the network card
#    first raises an interrupt to tell the CPU, a packet has arrived."
#   "The CPU stops whatever it was doing, switches into kernel mode, and starts
#    running the network driver."
#   "That interruption alone has a cost."
# ===========================================================================
def act_arrival(scene, st, kb, cap):
    # 16.55  off the wire and into a descriptor of the rx ring.
    scene.at("ar_packet")
    scene.add(st.pkt)
    scene.play(st.pkt.animate.move_to(P(SPINE_X + 170, NIC_Y + 44)), run_time=0.3,
               rate_func=rush_from)
    scene.at("ar_arrives")
    scene.play(Indicate(st.nic.slots[4], color=NIC_C, scale_factor=1.25),
               Flash(P(SPINE_X + 170, NIC_Y + 44), color=NIC_C, line_length=0.14,
                     num_lines=10, flash_radius=0.30), run_time=0.5)

    # 17.67  the DMA engine writes it into host memory before software sees it.
    # Yellow, because this is hardware doing the work -- no CPU involved yet.
    dma = vlink(NIC_Y + NIC_H / 2 + 8, KRN_Y - KRN_H / 2 - 8, color=HW, sw=6)
    dmat = tag("DMA", HW, TAG_T).move_to(P(SPINE_X + 118, 572))
    scene.at("ar_card")
    scene.play(FadeOut(st.a1), GrowArrow(dma), FadeIn(dmat, shift=RIGHT * 0.1),
               st.pkt.animate.move_to(P(SPINE_X, 600)), run_time=0.6)
    st.dma, st.dmat = dma, dmat

    # 18.49  "INSTEAD of your application receiving it IMMEDIATELY..."
    # The straight line is drawn precisely so it can be taken away: this is the
    # thing every viewer assumes happens, and it does not.
    wish = DashedLine(P(560, NIC_Y + 70), P(560, APP_Y - 40), color=USER,
                      stroke_width=4, dash_length=0.16).set_z_index(Z_LINE)
    wisht = tag("straight to my app?", USER, TAG_T - 2).move_to(P(520, 1120))
    scene.at("ir_instead")
    scene.play(Create(wish), run_time=0.45)
    scene.at("ir_app")
    scene.play(Indicate(st.app, color=USER, scale_factor=1.05),
               FadeIn(wisht, shift=UP * 0.1), run_time=0.45)
    scene.at("ir_immediately")
    x = VGroup(Line(P(524, 856), P(596, 928), color=BAD, stroke_width=7),
               Line(P(524, 928), P(596, 856), color=BAD, stroke_width=7)).set_z_index(Z_CARD)
    scene.play(Create(x), wish.animate.set_opacity(0.25), run_time=0.4)
    scene.play(FadeOut(x), FadeOut(wish), FadeOut(wisht), run_time=0.3)

    # 21.95  "...the network card FIRST raises..."  -- the camera pulls back and
    # the other half of the machine walks into frame. From here to the end of the
    # film the right lane is the core, and it is never off screen for long.
    st.cpu = CPUColumn(scene)
    st.cpu_chrome = st.cpu.chrome()
    scene.at("ir_first")
    scene.play(cam(scene, FULL_FRAME), FadeIn(st.cpu_chrome), run_time=0.55)
    st.seg_app0 = st.cpu.band("YOUR APP", px=190, color=USER, sub="running")
    scene.play(*CPUColumn.anim(st.seg_app0), run_time=0.3)

    # 22.88  "...an INTERRUPT..."  A zig-zag, not an arrow. It is a wire being
    # yanked, and it lands on the core in mid-instruction.
    st.irq = bolt(P(600, NIC_Y), P(CPU_X - CPU_W / 2 - 6, 470))
    scene.at("ir_interrupt")
    kb.to("THE INTERRUPT", BAD, run_time=0.4)
    scene.play(Create(st.irq), run_time=0.4)

    # 23.74  "...to tell the CPU"  [HIGH]  -- the strongest beat so far.
    scene.at("ir_cpu")
    scene.play(Flash(P(CPU_X, 470), color=BAD, line_length=0.30, num_lines=16,
                     flash_radius=0.75),
               st.cpu_chrome.box.animate.set_stroke(BAD, 3.4), run_time=0.55)

    # 25.26  "...a packet has arrived."  The message rides the wire it just cut.
    msg = tag("packet has arrived", BAD, TAG_T - 3).move_to(P(560, NIC_Y - 78))
    scene.at("ir_arrived")
    scene.play(FadeIn(msg, shift=RIGHT * 0.1), run_time=0.3)
    scene.play(msg.animate.move_to(P(CPU_X - 30, 396)).set_opacity(0.0), run_time=0.55)

    # 26.82  "The CPU STOPS whatever it was doing"  -- your app's band is cut off
    # mid-flight. That red rule is the instant your process stopped running.
    cut = Line(P(BAR_X - BAR_W / 2 - 14, 0), P(BAR_X + BAR_W / 2 + 14, 0), color=BAD,
               stroke_width=5).move_to([X(BAR_X), st.seg_app0.rect.get_bottom()[1], 0]) \
        .set_z_index(Z_CARD)
    scene.at("cs_stops")
    scene.play(Create(cut), st.seg_app0.rect.animate.set_fill(USER, 0.32), run_time=0.5)
    st.cut = cut

    # 28.30  "...SWITCHES into KERNEL MODE..."  ring 3 -> ring 0, and the core
    # itself changes colour. From here on amber is the kernel, in both lanes.
    ring = tag("ring 3 → ring 0", KERN, TAG_T - 2, mono=True).move_to(P(CPU_X, 372))
    scene.at("cs_switches")
    scene.play(FadeIn(ring, shift=DOWN * 0.1),
               st.cpu_chrome.box.animate.set_stroke(KERN, 3.4), run_time=0.45)
    st.seg_irq = st.cpu.band("IRQ", 500, color=BAD, sub="save state")
    scene.at("cs_kernel")
    scene.play(*CPUColumn.anim(st.seg_irq), run_time=0.6)
    cap.show("the core's time, flowing downward", SUBTLE)

    # 30.46  "...and starts running the network DRIVER."  Left lane and right
    # lane light together: the row it is executing, and the time it costs.
    scene.at("cs_driver")
    scene.play(Indicate(st.krn.rows[0], color=BAD, scale_factor=1.06),
               st.krn.rows[1].animate.set_opacity(1.0), run_time=0.5)
    scene.play(Indicate(st.krn.rows[1], color=KERN, scale_factor=1.06),
               FadeOut(ring), run_time=0.5)

    # 32.03  "That interruption alone has a COST."  -- and the budget is finally
    # drawn to scale beside it. Five hundred cycles against twenty. The hairline
    # IS the point.
    scene.at("ct_that")
    scene.play(Indicate(st.seg_irq.rect, color=BAD, scale_factor=1.06),
               FadeOut(st.cut), run_time=0.5)
    st.budget = st.cpu.budget_mark()
    scene.at("ct_cost")
    scene.play(FadeIn(st.budget, shift=DOWN * 0.1), run_time=0.5)
    cap.show("500 cycles, just to be told a packet exists", BAD)


# ===========================================================================
# ACT 3 -- THE STACK, AND THE COPIES   (34.7 - 59.0 s)
#   "Next, the packet travels through multiple layers of the Linux networking
#    stack."
#   "During this journey, the packet is wrapped in kernel data structures,
#    inspected, and often copied into different memory buffers before it finally
#    reaches your application."
#   "And that's another source of overhead -- memory copies."
#   "Copying thousands or even millions of packets every second consumes valuable
#    CPU cycles and memory bandwidth."
# ===========================================================================
def act_stack(scene, st, kb, cap):
    # 34.69  a new chapter, and the packet starts down the stack.
    scene.at("st_next")
    kb.to("THE KERNEL STACK", KERN, run_time=0.5)
    scene.at("st_travels")
    scene.play(st.pkt.animate.move_to(P(SPINE_X, KROWS[0][1])),
               st.krn.rows.animate.set_opacity(1.0), run_time=0.55)

    # 36.69  "...MULTIPLE LAYERS..."  The packet is carried down and each layer
    # lights as it is entered. Five stops, every packet, forever.
    st.seg_stack = st.cpu.band("STACK", 700, color=KERN, sub="sk_buff + TCP/IP")
    scene.at("st_layers")
    scene.play(LaggedStart(*[Indicate(r, color=KERN, scale_factor=1.05)
                             for r in st.krn.rows], lag_ratio=0.22),
               st.pkt.animate.move_to(P(SPINE_X, KROWS[3][1])),
               *CPUColumn.anim(st.seg_stack), run_time=1.2)
    scene.at("st_stack")
    cap.show("five layers · ~700 more cycles", KERN)

    # 39.08  "DURING this journey..."  -- push in. The next eight seconds happen
    # inside one kernel buffer, and they deserve to be seen at that size. The
    # window is framed to hold the sk_buff AND the process it is copied to, so
    # the copy can be watched crossing the kernel/user line; the five stack rows
    # step back to 12% because the buffer is about to be drawn on top of them.
    scene.at("jr_during")
    kb.hide(run_time=0.8, extra=[cam(scene, (SPINE_X + 10, 1090, 0.60)),
                                 st.krn.rows.animate.set_opacity(0.12)])

    # 40.68  "...the packet is WRAPPED in kernel DATA STRUCTURES..."
    # The sk_buff closes around the packet: headroom, metadata, then the bytes
    # that actually came off the wire. ~200 bytes of bookkeeping per packet.
    skb = box(320, 132, KERN, fill=SURFACE, fill_op=1.0, r=0.10, sw=2.6) \
        .move_to(P(SPINE_X, 900)).set_z_index(Z_NODE + 2)
    cells = VGroup(*[box(88, 60, KERN, fill=SURF2, r=0.06, sw=1.6)
                     .move_to(P(SPINE_X + (i - 1) * 98, 918)) for i in range(3)]) \
        .set_z_index(Z_NODE + 3)
    cnames = VGroup(*[T(n, MONO_S - 3, IDLE, font=MN, bold=False)
                      .move_to(P(SPINE_X + (i - 1) * 98, 934))
                      for i, n in enumerate(("head", "meta", "data"))]).set_z_index(Z_LABEL + 1)
    skbt = T("sk_buff", TAG_T, KERN, font=MN).move_to(P(SPINE_X, 856)).set_z_index(Z_LABEL + 1)
    st.skb = VGroup(skb, cells, cnames, skbt)
    scene.at("jr_wrapped")
    scene.play(st.pkt.animate.move_to(P(SPINE_X + 98, 904)).scale(0.78),
               FadeIn(skb, scale=1.3), FadeIn(cells), FadeIn(cnames), run_time=0.7)
    scene.at("jr_structures")
    scene.play(Indicate(VGroup(cells[0], cells[1]), color=KERN, scale_factor=1.08),
               FadeIn(skbt, shift=UP * 0.08), run_time=0.55)

    # 42.44  "...INSPECTED..."  a scan sweeps the buffer: netfilter, routing,
    # checksums. Every one of them touches memory the core does not have cached.
    scan = Line(P(SPINE_X - 170, 838), P(SPINE_X + 170, 838), color=DPDK_C,
                stroke_width=3.4).set_z_index(Z_CARD)
    scene.at("jr_inspected")
    scene.play(Create(scan), run_time=0.25)
    scene.play(scan.animate.move_to(P(SPINE_X, 962)), run_time=0.55)
    scene.play(FadeOut(scan), run_time=0.2)

    # 43.98  "...and often COPIED into different memory BUFFERS..."
    # THE copy: the same bytes, written a second time, into a second buffer on
    # the other side of the kernel/user line. Purple is memory, and it is not free.
    # The destination is inside YOUR PROCESS, on the far side of the boundary --
    # so the arrow visibly crosses that line. A copy between two kernel buffers
    # would be a detail; this one is the reason recv() costs what it costs.
    ubuf = box(300, 52, MEM, fill=MEM_BG, fill_op=0.85, r=0.07, sw=2.2) \
        .move_to(P(SPINE_X, 1318)).set_z_index(Z_NODE + 2)
    ubt = T("user buffer", MONO_S - 2, MEM, font=MN, bold=False) \
        .move_to(P(SPINE_X, 1318)).set_z_index(Z_LABEL + 1)
    kbt = T("kernel buffer", MONO_S, KERN, font=MN, bold=False) \
        .move_to(P(SPINE_X - 30, 992)).set_z_index(Z_LABEL + 1)
    copy_arrow = Arrow(P(SPINE_X + 132, 976), P(SPINE_X + 132, 1288), buff=0.0,
                       color=MEM, stroke_width=6, max_tip_length_to_length_ratio=0.14) \
        .set_z_index(Z_LINE)
    dup = packet(INK, 24).move_to(P(SPINE_X + 98, 904))
    scene.at("jr_copied")
    scene.play(FadeIn(ubuf, shift=UP * 0.1), FadeIn(ubt), FadeIn(kbt),
               st.app.label.animate.shift(UP * U(34)), run_time=0.4)
    scene.play(GrowArrow(copy_arrow), FadeIn(dup),
               dup.animate.move_to(P(SPINE_X - 110, 1318)), run_time=0.7)
    scene.at("jr_buffers")
    scene.play(Indicate(ubuf, color=MEM, scale_factor=1.06),
               Indicate(skb, color=KERN, scale_factor=1.03), run_time=0.55)
    cap.show("the same bytes, written twice", MEM)
    st.copy_group = VGroup(ubuf, ubt, kbt, copy_arrow)
    st.dup = dup

    # 46.72  "...before it finally REACHES YOUR APPLICATION."  Pull back out, and
    # the copy lands where the viewer was promised, thirty seconds ago, it would.
    scene.at("jr_reaches")
    scene.play(cam(scene, FULL_FRAME), st.krn.rows.animate.set_opacity(1.0), run_time=0.45)
    scene.at("jr_app")
    scene.play(Indicate(st.app, color=USER, scale_factor=1.06),
               Flash(P(SPINE_X, APP_Y), color=USER, line_length=0.22, num_lines=12,
                     flash_radius=0.7), run_time=0.7)

    # 49.77  "...another source of OVERHEAD -- MEMORY COPIES."  The dash is the
    # loudest moment in the sentence, so the frame goes quiet for it and only the
    # copy is left lit.
    scene.at("ov_another")
    kb.to("MEMORY COPIES", MEM, run_time=0.45)
    scene.at("ov_overhead")
    scene.play(copy_arrow.animate.set_color(BAD).set_stroke(width=9),
               Flash(P(SPINE_X + 132, 1130), color=BAD, line_length=0.24, num_lines=14,
                     flash_radius=0.6), run_time=0.5)
    st.seg_copy = st.cpu.band("COPY", 400, color=MEM, sub="to user space")
    scene.at("ov_copies")
    scene.play(*CPUColumn.anim(st.seg_copy), run_time=0.55)

    # 51.79  "COPYING thousands or even MILLIONS of packets every second..."
    # One copy is a detail. The rate is the problem -- so the rate is what runs.
    scene.at("cp_copying")
    ghosts = VGroup(*[packet(INK, 22).move_to(P(SPINE_X + 132, 980)) for _ in range(5)])
    scene.play(LaggedStart(*[g.animate.move_to(P(SPINE_X + 132, 1290)).set_opacity(0.0)
                             for g in ghosts], lag_ratio=0.18), run_time=1.0)
    counter = T("1 000 / s", TITLE_SIZE - 22, MEM, font=MN).move_to(P(CXP, FLOOR_Y))
    scene.at("cp_millions")
    scene.play(FadeIn(counter, scale=1.1), run_time=0.35)
    for txt in ("1 000 000 / s", "148 800 000 / s"):
        nxt = T(txt, TITLE_SIZE - 22, BAD, font=MN).move_to(P(CXP, FLOOR_Y))
        scene.play(FadeTransform(counter, nxt), run_time=0.42)
        counter = nxt
    scene.at("cp_second")
    scene.play(Flash(P(CXP, FLOOR_Y), color=BAD, line_length=0.3, num_lines=16,
                     flash_radius=1.1), run_time=0.5)

    # 56.26  "...consumes valuable CPU CYCLES and MEMORY BANDWIDTH."
    scene.at("cp_cpu")
    scene.play(Indicate(st.seg_copy.rect, color=BAD, scale_factor=1.08),
               Indicate(st.seg_stack.rect, color=BAD, scale_factor=1.04), run_time=0.6)
    bwbox = box(420, 40, MEM, fill=SURFACE, r=0.06, sw=1.8).move_to(P(SPINE_X, FLOOR_Y + 112))
    bwfill = Rectangle(width=U(414), height=U(34), stroke_width=0, fill_color=BAD,
                       fill_opacity=0.85).move_to(P(SPINE_X - 207, FLOOR_Y + 112),
                                                  aligned_edge=LEFT).set_z_index(Z_NODE)
    bwlab = T("memory bandwidth", MONO_S, MEM, font=MN, bold=False) \
        .move_to(P(SPINE_X, FLOOR_Y + 64)).set_z_index(Z_LABEL)
    scene.at("cp_bandwidth")
    scene.play(FadeIn(bwbox), FadeIn(bwlab), GrowFromEdge(bwfill, LEFT), run_time=0.8)
    st.bw = VGroup(bwbox, bwfill, bwlab, counter)


# ===========================================================================
# ACT 4 -- THE CONTEXT SWITCH   (59.0 - 72.3 s)
#   "Finally, your application has to wake up to process the packet."
#   "That means another context switch, from the kernel back to user space."
#   "Context switches save and restore CPU state, flush caches, and add more
#    latency."
# ===========================================================================
def act_switch(scene, st, kb, cap):
    # 59.02  clear the floor: the next idea needs the space.
    scene.at("wk_finally")
    scene.play(FadeOut(st.bw, shift=DOWN * 0.2), run_time=0.5)

    # 59.89  the app has been grey this whole time and nobody said so. Say it by
    # showing it: blocked in recv(), off the run queue, holding nothing.
    sleep = tag("blocked in recv()", IDLE, TAG_T - 2, mono=True).move_to(P(SPINE_X, 1400))
    scene.at("wk_app")
    scene.play(st.app.box.animate.set_stroke(IDLE, 3.0),
               st.app.label.animate.set_opacity(0.5),
               FadeIn(sleep, shift=UP * 0.08), run_time=0.5)

    # 60.73  "...has to WAKE UP..."  The scheduler has to put it back on a core.
    scene.at("wk_wake")
    scene.play(st.app.box.animate.set_stroke(USER, 3.4),
               st.app.label.animate.set_opacity(1.0),
               FadeOut(sleep, shift=UP * 0.1),
               Flash(P(SPINE_X, APP_Y), color=USER, line_length=0.26, num_lines=14,
                     flash_radius=0.8), run_time=0.55)
    scene.at("wk_process")
    cap.show("the scheduler has to run first", USER)

    # 63.53  "...another CONTEXT SWITCH, from the KERNEL back to USER SPACE."
    # The band opens on the right; the packet crosses the line on the left. Same
    # event, both lanes, same instant.
    st.seg_ctx = st.cpu.band("SWITCH", 600, color=BAD, sub="ring 0 → ring 3")
    scene.at("sw_context")
    kb.to("CONTEXT SWITCH", BAD, run_time=0.45)
    scene.at("sw_switch")
    scene.play(*CPUColumn.anim(st.seg_ctx),
               st.cpu_chrome.box.animate.set_stroke(USER, 3.4), run_time=0.55)
    scene.at("sw_kernel")
    scene.play(Indicate(st.bound.line, color=BAD, scale_factor=1.0),
               st.dup.animate.move_to(P(SPINE_X - 110, 1318)), run_time=0.6)
    scene.at("sw_user")
    scene.play(Indicate(st.app, color=USER, scale_factor=1.05), run_time=0.45)

    # 66.88  "CONTEXT SWITCHES SAVE and RESTORE CPU state..."  Eight registers
    # out, eight back in. None of this work has anything to do with your packet.
    regs = VGroup(*[box(64, 34, USER, fill=SURFACE, r=0.05, sw=1.6)
                    .move_to(P(210 + (i % 4) * 76, FLOOR_Y + (i // 4) * 46))
                    for i in range(8)]).set_z_index(Z_NODE)
    rlab = T("CPU state", MONO_S, SUBTLE, font=MN, bold=False) \
        .move_to(P(286, FLOOR_Y - 54)).set_z_index(Z_LABEL)
    vault = box(150, 120, IDLE, fill=SURF2, r=0.08, sw=2.2).move_to(P(560, FLOOR_Y + 22))
    vlab = T("saved", MONO_S, IDLE, font=MN, bold=False).move_to(P(560, FLOOR_Y - 54)) \
        .set_z_index(Z_LABEL)
    scene.at("cx_context")
    scene.play(FadeIn(regs), FadeIn(rlab), FadeIn(vault), FadeIn(vlab), run_time=0.4)
    scene.at("cx_save")
    scene.play(LaggedStart(*[r.animate.move_to(P(560, FLOOR_Y + 22)).scale(0.4)
                             .set_opacity(0.2) for r in regs], lag_ratio=0.05),
               run_time=0.5)
    scene.at("cx_restore")
    scene.play(LaggedStart(*[r.animate.move_to(P(210 + (i % 4) * 76, FLOOR_Y + (i // 4) * 46))
                             .scale(2.5).set_opacity(1.0) for i, r in enumerate(regs)],
                           lag_ratio=0.05), run_time=0.55)
    scene.at("cx_state")
    scene.play(FadeOut(VGroup(regs, rlab, vault, vlab), shift=DOWN * 0.15), run_time=0.4)

    # 69.64  "...FLUSH CACHES..."  The real bill for a context switch is not the
    # register file. It is that the core comes back to a cold cache and pays for
    # every line all over again.
    grid = VGroup(*[box(46, 34, MEM, fill=MEM_BG, fill_op=0.85, r=0.05, sw=1.4)
                    .move_to(P(196 + (i % 8) * 54, FLOOR_Y - 20 + (i // 8) * 44))
                    for i in range(24)]).set_z_index(Z_NODE)
    glab = T("L1 / L2 cache", MONO_S, MEM, font=MN, bold=False) \
        .move_to(P(386, FLOOR_Y - 76)).set_z_index(Z_LABEL)
    scene.at("cx_flush")
    scene.play(FadeIn(grid), FadeIn(glab), run_time=0.26)
    scene.at("cx_caches")
    scene.play(LaggedStart(*[c.animate.set_fill(SURF2, 1.0).set_stroke(IDLE, 1.0)
                             for c in grid], lag_ratio=0.02), run_time=0.9)
    cold = tag("cold — every line must be fetched again", IDLE, TAG_T - 3) \
        .move_to(P(386, FLOOR_Y + 148))
    scene.play(FadeIn(cold, shift=UP * 0.08), run_time=0.35)

    # 71.33  "...and add more LATENCY."
    scene.at("cx_latency")
    scene.play(Indicate(st.seg_ctx.rect, color=BAD, scale_factor=1.08),
               FadeOut(VGroup(grid, glab, cold), shift=DOWN * 0.15), run_time=0.6)
    st.seg_app1 = st.cpu.band("YOUR APP", px=150, color=USER, sub="finally")
    scene.play(*CPUColumn.anim(st.seg_app1), run_time=0.4)


# ===========================================================================
# ACT 5 -- THE BOTTLENECK   (72.3 - 87.1 s)
#   "Now imagine this happening not once, but millions of times every second."
#   "Interrupts, memory copies, context switches."
#   "Individually, they seem small."
#   "Together, they become the biggest bottleneck in high-performance networking."
# ===========================================================================
def act_bottleneck(scene, st, kb, cap):
    over = [st.seg_irq, st.seg_stack, st.seg_copy, st.seg_ctx]
    top_y = st.seg_irq.rect.get_top()[1]
    bot_y = st.seg_ctx.rect.get_bottom()[1]

    # 72.31  "NOW imagine this happening..."  -- the left lane has made its case.
    # Everything from here is about the column, so the camera goes and lives there.
    scene.at("mn_now")
    cap.clear(run_time=0.4, extra=[cam(scene, (CPU_X - 40, 820, 0.86))] +
              dim([st.nic, st.krn, st.app, st.bound, st.dma, st.dmat, st.skb,
                   st.copy_group, st.pkt, st.dup, st.a2, st.irq], 0.16))

    # 73.95  "...not ONCE..."  Bracket the four bands that are pure overhead:
    # 2,200 cycles of them, against a budget of twenty.
    x0, x1 = X(634), X(652)
    br = VGroup(Line([x1, top_y, 0], [x0, top_y, 0], color=BAD, stroke_width=4),
                Line([x0, top_y, 0], [x0, bot_y, 0], color=BAD, stroke_width=4),
                Line([x0, bot_y, 0], [x1, bot_y, 0], color=BAD, stroke_width=4)) \
        .set_z_index(Z_CARD)
    brl = tag("~2 200 cycles", BAD, TAG_T - 2, mono=True) \
        .move_to([X(524), (top_y + bot_y) / 2, 0])
    scene.at("mn_once")
    scene.play(Create(br), FadeIn(brl, shift=LEFT * 0.1), run_time=0.6)

    # 74.94  "...but MILLIONS OF TIMES every SECOND."  The pattern tiles down the
    # column until there is nothing else in the frame. No new idea -- just the rate.
    pat = VGroup(*[s.rect for s in over])
    span = top_y - bot_y
    n_tiles = 4
    th = span / n_tiles
    tiles = VGroup()
    for i in range(n_tiles):
        c = pat.copy().stretch_to_fit_height(th)
        c.move_to([pat.get_center()[0], top_y - th / 2 - i * th, 0])
        tiles.add(c)
    scene.at("mn_millions")
    scene.play(FadeOut(br), FadeOut(brl),
               *[s.rect.animate.set_opacity(0.0) for s in over],
               *[s.lab.animate.set_opacity(0.25) for s in over],
               LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.12), run_time=1.1)
    scene.at("mn_second")
    scene.play(tiles.animate.set_color(BAD),
               Flash(P(BAR_X, 890), color=BAD, line_length=0.3, num_lines=16,
                     flash_radius=1.4), run_time=0.6)

    # 77.62  "INTERRUPTS, MEMORY COPIES, CONTEXT SWITCHES."  Named, one per word,
    # each pointing at the band the viewer has already watched being built.
    scene.play(FadeOut(tiles),
               *[s.rect.animate.set_opacity(0.80) for s in over],
               *[s.lab.animate.set_opacity(1.0) for s in over], run_time=0.3)
    st.chips = VGroup()
    for label, seg, col, key in (("interrupts", st.seg_irq, BAD, "th_interrupts"),
                                 ("memory copies", st.seg_copy, MEM, "th_copies"),
                                 ("context switches", st.seg_ctx, BAD, "th_switches")):
        c = tag(label, col, TAG_T - 2)
        c.move_to([X(498), seg.rect.get_center()[1], 0])
        st.chips.add(c)
        scene.at(key)
        scene.play(FadeIn(c, shift=RIGHT * 0.12),
                   Indicate(seg.rect, color=col, scale_factor=1.08), run_time=0.45)

    # 80.97  "INDIVIDUALLY, they seem SMALL."  So look at one, close up, where a
    # few hundred cycles genuinely does look like nothing.
    scene.at("iv_indiv")
    kb.hide(run_time=0.8, extra=[cam(scene, (CPU_X - 90, 800, 0.44))])
    scene.at("iv_small")
    cap.show("a few hundred cycles. nothing.", SUBTLE)

    # 82.81  "TOGETHER..."  Pull back hard, and stack them: one bar, all of it red.
    tall = Rectangle(width=U(BAR_W), height=abs(top_y - bot_y), stroke_width=0,
                     fill_color=BAD, fill_opacity=0.9) \
        .move_to([X(BAR_X), (top_y + bot_y) / 2, 0]).set_z_index(Z_NODE)
    scene.at("tg_together")
    scene.play(cam(scene, FULL_FRAME), FadeOut(st.chips), run_time=0.7)
    scene.play(FadeIn(tall), *[s.rect.animate.set_opacity(0.0) for s in over], run_time=0.5)

    # 84.47  "...the biggest BOTTLENECK in high-performance networking."
    # And the throat from the very first ten seconds comes back, by name.
    throat = throat_shape()
    scene.at("tg_biggest")
    kb.to("THE BOTTLENECK", BAD, run_time=0.4)
    scene.at("tg_bottleneck")
    scene.play(ReplacementTransform(st.krn, throat),
               *undim([st.nic, st.app, st.bound]), run_time=0.6)
    scene.at("tg_networking")
    cap.show("not one big cost — three small ones, every packet", BAD)
    st.throat2, st.tall = throat, tall


# ===========================================================================
# ACT 6 -- DPDK   (87.1 - 110.8 s)
#   "This is where DPDK changes everything."
#   "Instead of waiting for interrupts, DPDK continuously polls the network card."
#   "It maps packet buffers directly into user space memory using huge pages,
#    allowing the application to access packets without the traditional kernel
#    networking stack."
#   "The result?  No per-packet interrupts, no unnecessary memory copies, almost
#    no context switches."
# ===========================================================================
def act_dpdk(scene, st, kb, cap):
    # 87.06  the one title card in the film, and it earns it: everything before
    # it was the problem, everything after it is the answer.
    # the constriction turns back into the stack it always was -- the machine is
    # whole again, and this time something is going to route around it.
    st.krn.restore()
    title_card(scene, kb, "DPDK", DPDK_C,
               t_in=CUE["dp_this"], t_out=CUE["dp_changes"] - 0.30,
               sub="data plane development kit",
               extra_out=[ReplacementTransform(st.throat2, st.krn), FadeOut(st.tall),
                          FadeOut(st.skb), FadeOut(st.copy_group),
                          *undim([st.a2, st.pkt, st.dup, st.dma, st.dmat, st.irq])])
    cap.clear(run_time=0.3)

    # 90.58  "Instead of waiting for INTERRUPTS..."  The wire is cut first,
    # because everything else follows from not being interrupted.
    scene.at("pl_interrupts")
    irq_x = strike(st.irq, DPDK_C, 6)
    scene.play(Create(irq_x), st.irq.animate.set_opacity(0.3), run_time=0.45)
    scene.play(FadeOut(st.irq), FadeOut(irq_x), run_time=0.25)

    # 91.27  "...DPDK continuously POLLS the network card."  [HIGH]
    # The application becomes the driver. That is the whole trick: a poll mode
    # driver in user space, spinning on the rx ring, never waiting to be told.
    pmd = node("DPDK APP", "poll mode driver", SPINE_W, APP_H, DPDK_C, SPINE_X, APP_Y)
    scene.at("pl_dpdk")
    scene.play(ReplacementTransform(st.app, pmd), run_time=0.6)
    st.app = pmd

    # 92.63  the loop itself: reach up, take what is there, come back. Three
    # times, so it reads as a loop and not as a one-off.
    scene.at("pl_polls")
    for _ in range(3):
        up = Arrow(P(268, APP_Y - 96), P(268, NIC_Y + 110), buff=0.0, color=DPDK_C,
                   stroke_width=5, max_tip_length_to_length_ratio=0.10).set_z_index(Z_LINE)
        scene.play(GrowArrow(up), run_time=0.18)
        scene.play(FadeOut(up), run_time=0.10)
    scene.at("pl_card")
    burst = VGroup(*[packet(INK, 20).move_to(P(SPINE_X + 108 + (i % 4) * 26, NIC_Y + 44))
                     for i in range(8)])
    scene.play(LaggedStart(*[b.animate.move_to(P(430 + (i % 4) * 26, APP_Y - 30))
                             for i, b in enumerate(burst)], lag_ratio=0.05),
               run_time=0.7, rate_func=rush_into)

    # 94.49  "It MAPS packet buffers DIRECTLY into user space memory..."
    # The kernel is not bypassed by being ignored -- it is bypassed because the
    # NIC writes straight into memory the process already owns. So the stack
    # physically steps out of the middle of the frame, and the user/kernel line
    # moves up with it: from here down, this is all your address space.
    small = node("kernel stack", "bypassed", 250, 84, IDLE, 175, 594,
                 glowing=False, tsize=ROW_T - 2)
    small.set_opacity(0.55)
    scene.at("mp_maps")
    scene.play(FadeOut(st.dma), FadeOut(st.dmat), FadeOut(st.a2), FadeOut(st.dup),
               FadeOut(burst), ReplacementTransform(st.krn, small),
               st.bound.animate.shift(UP * U(448)), run_time=0.65)
    st.krn_small = small

    # 95.19  the lane: NIC to process, one hop, nothing in between.
    lane = Arrow(P(SPINE_X, NIC_Y + NIC_H / 2 + 10), P(SPINE_X, APP_Y - APP_H / 2 - 10),
                 buff=0.0, color=DPDK_C, stroke_width=9,
                 max_tip_length_to_length_ratio=0.07).set_z_index(Z_LINE)
    scene.at("mp_buffers")
    scene.play(GrowArrow(lane), run_time=0.4)
    scene.at("mp_directly")
    scene.play(st.pkt.animate.move_to(P(SPINE_X, 880)), run_time=0.5, rate_func=rush_into)
    st.lane = lane

    # 96.28  the mbuf pool: packet buffers, in user space, addressed by the
    # process directly. Purple is memory; the cyan lane says whose memory it is.
    pool = box(340, 200, MEM, fill=MEM_BG, fill_op=0.55, r=0.10, sw=2.4) \
        .move_to(P(412, 880)).set_z_index(Z_ZONE)
    pl = T("mbuf pool", MONO_S, MEM, font=MN, bold=False) \
        .move_to(P(412, 754)).set_z_index(Z_LABEL)
    pages = VGroup(*[box(50, 40, MEM, fill=SURFACE, r=0.04, sw=1.4)
                     .move_to(P(412 + (i % 6 - 2.5) * 58, 852 + (i // 6) * 52))
                     for i in range(12)]).set_z_index(Z_NODE)
    scene.at("mp_user")
    scene.play(FadeIn(pool, scale=1.1), FadeIn(pl), FadeIn(pages), run_time=0.6)
    st.pool = VGroup(pool, pl)

    # 97.68  "...using HUGE PAGES."  Twelve 4 KB pages become two 2 MB pages, and
    # the reason is not tidiness: it is the TLB. Fewer entries, fewer misses,
    # fewer stalls the core has no way to hide.
    huge = VGroup(*[box(150, 92, MEM, fill=SURFACE, r=0.06, sw=2.0)
                    .move_to(P(412 + (i - 0.5) * 168, 878)) for i in range(2)]) \
        .set_z_index(Z_NODE)
    hlab = VGroup(*[T("2 MB", MONO_S, MEM, font=MN, bold=False)
                    .move_to(P(412 + (i - 0.5) * 168, 878)).set_z_index(Z_LABEL)
                    for i in range(2)])
    scene.at("mp_huge")
    scene.play(Indicate(pages, color=MEM, scale_factor=1.05), run_time=0.35)
    scene.at("mp_pages")
    scene.play(ReplacementTransform(pages, huge), FadeIn(hlab),
               st.pkt.animate.move_to(P(496, 878)), run_time=0.7)
    st.pool.add(huge, hlab)

    # 99.02  "...ALLOWING the application to ACCESS packets..."  No copy: a
    # pointer. The bytes the NIC wrote are the bytes the app reads.
    ptr = Arrow(P(412, APP_Y - 100), P(412, 1000), buff=0.0, color=DPDK_C,
                stroke_width=5, max_tip_length_to_length_ratio=0.18).set_z_index(Z_LINE)
    zc = tag("zero copy", DPDK_C, TAG_T).move_to(P(232, 1080))
    scene.at("mp_allowing")
    scene.play(GrowArrow(ptr), run_time=0.45)
    scene.at("mp_access")
    scene.play(FadeIn(zc, shift=UP * 0.1), run_time=0.45)
    cap.show("the packet is a pointer — nothing is copied", DPDK_C)
    st.zc = VGroup(ptr, zc)

    # 101.12  "...WITHOUT the traditional kernel networking stack."
    scene.at("mp_without")
    scene.play(Indicate(small, color=IDLE, scale_factor=1.05), run_time=0.45)
    scene.at("mp_stack")
    cap.show("the stack is still there — it is just not in the path", IDLE)

    # 103.97  "The RESULT?"  Back to the column. This is what it was built for.
    # The dashed outline records what the kernel path cost, and it does not move
    # again: every band removed from now on is measured against it.
    ghost = DashedVMobject(
        Rectangle(width=U(BAR_W + 20), height=U(st.cpu.y - TL_TOP + 12),
                  stroke_color=BAD, stroke_width=3),
        num_dashes=48).move_to(P(BAR_X, (TL_TOP + st.cpu.y) / 2)).set_z_index(Z_CARD)
    gtag = tag("kernel path", BAD, TAG_T - 4).move_to(P(BAR_X, 1296))
    scene.at("rs_result")
    scene.play(cam(scene, (CPU_X - 60, 820, 0.80)), FadeIn(ghost), FadeIn(gtag),
               *[s.rect.animate.set_fill(s.color, 0.80).set_stroke(s.color, 1.4)
                 for s in (st.seg_irq, st.seg_stack, st.seg_copy, st.seg_ctx)],
               run_time=0.8)
    st.ghost = VGroup(ghost, gtag)

    # 104.97 / 106.57 / 109.14  "NO per-packet interrupts, NO unnecessary memory
    # copies, ALMOST NO context switches."  Three words, three bands, and the
    # column physically shortens by exactly the cycles each one used to cost.
    for key_a, key_b, seg in (("no_irq", "no_irq_w", st.seg_irq),
                              ("no_copy", "no_copy_w", st.seg_copy),
                              ("no_almost", "no_switch", st.seg_ctx)):
        scene.at(key_a)
        sx = strike(seg.rect, DPDK_C, 6)
        scene.play(Create(sx), run_time=0.35)
        scene.at(key_b)
        st.cpu.collapse(seg, run_time=0.6, extra=[FadeOut(sx, shift=RIGHT * 0.2)])
    scene.at("no_switch_w")
    cap.show("no syscall on the fast path at all", DPDK_C)


# ===========================================================================
# ACT 7 -- WHAT THE CORE DOES INSTEAD   (110.8 - 124.9 s)
#   "The CPU spends its time processing packets instead of managing operating
#    system overhead."
#   "That's why technologies like DPDK power high-performance firewalls, load
#    balancers, telecom systems, and modern cloud networking."
# ===========================================================================
def act_payoff(scene, st, kb, cap):
    # 111.02  "The CPU spends its time PROCESSING PACKETS..."  [HIGH]
    # The reclaimed space does not stay empty. The kernel-stack band grows into
    # all of it and changes what it is: this is your code, running, at last -- and
    # it fills the dashed outline exactly, because it is exactly the same time.
    scene.at("cy_cpu")
    kb.to("WHERE THE TIME GOES", DPDK_C, run_time=0.45)
    seg = st.seg_stack
    reclaimed = (500 + 400 + 600) * CYC_PX
    below = st.cpu.below(seg)
    new_h = seg.h + reclaimed
    tgt = seg.rect.copy().stretch_to_fit_height(U(new_h)) \
        .move_to([seg.rect.get_center()[0], seg.rect.get_top()[1] - U(new_h) / 2, 0]) \
        .set_fill(DPDK_C, 0.85).set_stroke(DPDK_C, 1.4)
    nlab = VGroup(T("PROCESS", TAG_T, DPDK_C),
                  T("your packet work", MONO_S - 2, DPDK_C, font=MN, bold=False)) \
        .arrange(DOWN, buff=0.06, aligned_edge=LEFT)
    nlab.move_to([X(LBL_X), seg.rect.get_top()[1] - U(new_h) / 2, 0], aligned_edge=LEFT) \
        .set_z_index(Z_LABEL)
    scene.at("cy_processing")
    scene.play(Transform(seg.rect, tgt), FadeTransform(seg.lab, nlab),
               *[b.animate.shift(DOWN * U(reclaimed)) for b in below], run_time=0.9)

    # 113.39  "...INSTEAD of managing OPERATING SYSTEM OVERHEAD."  The dashed
    # outline is still standing around it: same core, same time, different work.
    scene.at("cy_instead")
    scene.play(Indicate(st.ghost, color=BAD, scale_factor=1.0), run_time=0.5)
    scene.at("cy_overhead")
    cap.show("same core, same packet — the OS work is gone", DPDK_C)

    # 117.70  "That's why technologies like DPDK POWER..."  [HIGH]
    # The machine has done its job; hand the frame to what gets built on it.
    scene.at("ap_dpdk", lead=0.6)
    gone = [m for m in scene.mobjects
            if isinstance(m, VMobject) and m is not scene.camera.frame
            and m is not kb.mob and m is not cap.mob]
    cap.clear(run_time=0.8, extra=[cam(scene, FULL_FRAME)] + [FadeOut(m) for m in gone])
    kb.to("WHY IT MATTERS", DPDK_C, run_time=0.4)

    core = pill("DPDK", DPDK_C, DPDK_BG, TITLE_SIZE - 22, h=110, glowing=True) \
        .move_to(P(CXP, 560))
    scene.play(FadeIn(core, scale=1.1), run_time=0.5)

    # firewalls / load balancers / telecom / cloud -- one per spoken word, each
    # with a glyph, because four boxes of text is a slide and this is not one.
    def g_firewall(c):
        g = VGroup()
        for r in range(3):
            for k in range(3):
                g.add(box(40, 22, c, fill=SURF2, r=0.03, sw=1.6)
                      .move_to(P(-46 + k * 46 + (0 if r % 2 == 0 else 23), r * 26)))
        return g

    def g_lb(c):
        g = VGroup(Line(P(0, -34), P(0, 0), color=c, stroke_width=4))
        for dx in (-52, 0, 52):
            g.add(Arrow(P(0, 0), P(dx, 34), buff=0.0, color=c, stroke_width=3.4,
                        max_tip_length_to_length_ratio=0.3))
        return g

    def g_telecom(c):
        g = VGroup(Line(P(-26, 36), P(0, -24), color=c, stroke_width=3.4),
                   Line(P(26, 36), P(0, -24), color=c, stroke_width=3.4),
                   Line(P(-16, 14), P(16, 14), color=c, stroke_width=3.0))
        for r in (0.24, 0.40):
            g.add(Arc(radius=r, start_angle=PI / 5, angle=PI * 0.6, color=c,
                      stroke_width=3.0).move_arc_center_to(P(0, -28)))
        return g

    def g_cloud(c):
        return VGroup(Circle(radius=0.22, color=c, stroke_width=3.2).move_to(P(-28, 8)),
                      Circle(radius=0.32, color=c, stroke_width=3.2).move_to(P(4, -2)),
                      Circle(radius=0.20, color=c, stroke_width=3.2).move_to(P(36, 10)))

    for name, gl, key, px, py in (("FIREWALLS", g_firewall, "ap_firewalls", 280, 950),
                                  ("LOAD BALANCERS", g_lb, "ap_balancers", 800, 950),
                                  ("TELECOM / 5G", g_telecom, "ap_telecom", 280, 1310),
                                  ("CLOUD NETWORKING", g_cloud, "ap_cloud", 800, 1310)):
        b = box(430, 270, DPDK_C, fill=SURF2, r=0.14, sw=2.4).move_to(P(px, py))
        icon = gl(DPDK_C).move_to(P(px, py - 44))
        lab = T(name, ROW_T, INK).move_to(P(px, py + 84))
        if lab.width > U(400):
            lab.scale_to_fit_width(U(400))
        link = Line(P(CXP, 640), P(px, py - 138), color=DPDK_C, stroke_width=2.2,
                    stroke_opacity=0.35).set_z_index(Z_GLOW)
        scene.at(key)
        scene.play(FadeIn(VGroup(b, icon, lab), scale=1.06), Create(link), run_time=0.5)
    st.core = core


# ===========================================================================
# ACT 8 -- THE CLOSE   (124.9 - 135.6 s)
#   "Where processing millions of packets per second isn't just an optimization,
#    it's a requirement."
#   "Once you understand where the time is actually spent, the performance
#    difference becomes obvious."
# ===========================================================================
def act_close(scene, st, kb, cap):
    # 125.61  "...MILLIONS of packets PER SECOND..."
    sc = make_scrim(0.94)
    scene.at("rq_millions", lead=0.45)
    cap.clear(run_time=0.5, extra=[FadeIn(sc)])
    big = T("148 800 000", TITLE_SIZE + 6, DPDK_C, font=MN).move_to(P(CXP, 640)) \
        .set_z_index(Z_TITLE)
    if big.width > 9.4:
        big.scale_to_fit_width(9.4)
    unit = T("packets per second · 100 GbE, 64-byte frames", CAP_SIZE - 2, SUBTLE,
             bold=False).move_to(P(CXP, 740)).set_z_index(Z_TITLE)
    if unit.width > 9.4:
        unit.scale_to_fit_width(9.4)
    scene.play(FadeIn(big, scale=1.08), run_time=0.5)
    scene.at("rq_second")
    scene.play(FadeIn(unit, shift=UP * 0.1), run_time=0.4)

    # 127.88  "...isn't just an OPTIMIZATION, it's a REQUIREMENT."
    o = T("AN OPTIMIZATION", TITLE_SIZE - 18, IDLE).move_to(P(CXP, 880)).set_z_index(Z_TITLE)
    scene.at("rq_optimization")
    ox = strike(o, BAD, 5)
    scene.play(FadeIn(o), run_time=0.3)
    scene.play(Create(ox), o.animate.set_opacity(0.45), run_time=0.4)
    r = T("A REQUIREMENT", TITLE_SIZE - 12, DPDK_C).move_to(P(CXP, 1030)).set_z_index(Z_TITLE)
    scene.at("rq_requirement")
    scene.play(Write(r), Flash(P(CXP, 1030), color=DPDK_C, line_length=0.34,
                               num_lines=18, flash_radius=1.5), run_time=0.7)

    # 130.72  "ONCE you understand WHERE THE TIME IS ACTUALLY SPENT..."
    # The last thing on screen is the first thing the film taught: two columns,
    # same core, same packet, drawn to the same scale.
    scene.at("cl_once")
    scene.play(FadeOut(VGroup(big, unit, o, ox, r)), run_time=0.5)

    def column(px, label, bands, color):
        g, y = VGroup(), 780
        for name, h, c in bands:
            rect = Rectangle(width=U(280), height=U(h), stroke_width=0, fill_color=c,
                             fill_opacity=0.88).move_to(P(px, y + h / 2)).set_z_index(Z_TITLE)
            nm = T(name, MONO_S, BG, font=MN, bold=False).move_to(P(px, y + h / 2)) \
                .set_z_index(Z_TITLE + 1)
            if nm.width > U(256) or h < 44:
                nm.set_opacity(0.0)
            g.add(rect, nm)
            y += h
        g.add(T(label, ROW_T + 2, color).move_to(P(px, 722)).set_z_index(Z_TITLE))
        return g, y

    kern_col, ky = column(300, "KERNEL PATH",
                          [("IRQ", 100, BAD), ("stack", 140, KERN), ("copy", 80, MEM),
                           ("switch", 120, BAD)], BAD)
    dpdk_col, dy = column(780, "DPDK", [("process", 100, DPDK_C)], DPDK_C)
    scene.play(FadeIn(kern_col, shift=UP * 0.15), run_time=0.6)
    scene.at("cl_spent")
    scene.play(FadeIn(dpdk_col, shift=UP * 0.15), run_time=0.5)
    t1 = tag("~2 200 cyc / packet", BAD, TAG_T - 2, mono=True).move_to(P(300, ky + 58)) \
        .set_z_index(Z_TITLE)
    t2 = tag("~100 cyc / packet", DPDK_C, TAG_T - 2, mono=True).move_to(P(780, dy + 58)) \
        .set_z_index(Z_TITLE)
    scene.play(FadeIn(t1), FadeIn(t2), run_time=0.4)

    # 134.03  "...the PERFORMANCE DIFFERENCE becomes OBVIOUS."
    scene.at("cl_difference")
    res = VGroup(pill("~0.5 Mpps / core", BAD, BAD_BG, TAG_T + 2, h=64, glowing=True),
                 T("→", TITLE_SIZE - 24, INK),
                 pill("15–30 Mpps / core", DPDK_C, DPDK_BG, TAG_T + 2, h=64, glowing=True)) \
        .arrange(RIGHT, buff=0.26).move_to(P(CXP, 1400)).set_z_index(Z_TITLE)
    if res.width > 9.6:
        res.scale_to_fit_width(9.6)
    scene.play(FadeIn(res, scale=1.06), run_time=0.6)
    scene.at("cl_obvious")
    scene.play(Flash(P(CXP, 1400), color=DPDK_C, line_length=0.4, num_lines=20,
                     flash_radius=2.0), run_time=0.7)

    # the narration is over. Ride it out to the exact end of the audio, then clear.
    remaining = (VOICEOVER_SECONDS - scene.epoch) - scene.now()
    if remaining > 1e-3:
        scene.wait(remaining)
    for bar in (kb, cap):
        if bar.mob is not None:
            bar.mob.clear_updaters()
    scene.play(*[FadeOut(m) for m in scene.mobjects if m is not scene.camera.frame],
               run_time=0.7)


# ===========================================================================
# TAIL -- the AxioByte end card (house style, played past the narration)
# ===========================================================================
def act_outro(scene):
    set_cam(scene, FULL_FRAME)
    row = VGroup(T("Axio", TITLE_SIZE + 10, DPDK_C),
                 T("Byte", TITLE_SIZE + 10, KERN)).arrange(RIGHT, buff=0.03)
    sysx = T("SYSTEMS", ROW_T + 8, IDLE, font=MN).next_to(row, DOWN, buff=0.14)
    brand = VGroup(row, sysx).move_to(P(CXP, 580))

    head = T("High-Performance Data Plane", NODE_T + 4, INK).move_to(P(CXP, 850))
    if head.width > 9.2:
        head.scale_to_fit_width(9.2)
    sub = T("systems, from first principles", CAP_SIZE, IDLE, bold=False).move_to(P(CXP, 930))
    dl = Line(LEFT * 1.6, ORIGIN, color=DPDK_C, stroke_width=4).move_to(P(CXP - 80, 1005))
    dr = Line(ORIGIN, RIGHT * 1.6, color=KERN, stroke_width=4).move_to(P(CXP + 80, 1005))

    cta = pill("Follow  @axiobyte.systems", DPDK_C, DPDK_BG, NODE_T, h=110, glowing=True) \
        .move_to(P(CXP, 1180))
    nxt = VGroup(T("next ↓", CAP_SIZE + 2, KERN),
                 T("zero-copy: a packet is just a pointer", CAP_SIZE, INK, bold=False)) \
        .arrange(RIGHT, buff=0.25).move_to(P(CXP, 1370))
    if nxt.width > 9.4:
        nxt.scale_to_fit_width(9.4)

    scene.play(FadeIn(brand, shift=DOWN * 0.2), run_time=0.65)
    scene.play(FadeIn(head, shift=UP * 0.1), FadeIn(sub, shift=UP * 0.1), run_time=0.55)
    scene.play(Create(dl), Create(dr), run_time=0.4)
    scene.play(FadeIn(cta, scale=1.06), run_time=0.55)
    scene.play(FadeIn(nxt, shift=UP * 0.1), run_time=0.45)
    scene.wait(1.8)


# ===========================================================================
# SCENES
# ===========================================================================
class FullVideo(VOScene):
    """The full voiceover-synced cut. Every beat is cued to timeline.json."""

    epoch = 0.0

    def construct(self):
        self.camera.background_color = BG
        _add_voiceover(self)
        st = Stage()
        kb, cap = KeywordBar(self), CaptionBar(self)

        act_hook(self, st, kb, cap)          #   0.0 -  9.6
        act_path(self, st, kb, cap)          #   9.6 - 16.5
        act_arrival(self, st, kb, cap)       #  16.5 - 34.7
        act_stack(self, st, kb, cap)         #  34.7 - 59.0
        act_switch(self, st, kb, cap)        #  59.0 - 72.3
        act_bottleneck(self, st, kb, cap)    #  72.3 - 87.1
        act_dpdk(self, st, kb, cap)          #  87.1 -110.8
        act_payoff(self, st, kb, cap)        # 110.8 -124.9
        act_close(self, st, kb, cap)         # 124.9 -135.6
        act_outro(self)                      # past the audio


# ---------------------------------------------------------------------------
# ACT PREVIEWS
#
# Each preview rebuilds -- instantly, without animating -- the state its act
# inherits, then shifts `epoch` so the act starts near t=0. That is the only way
# to iterate on the context switch at 63 s without sitting through the minute in
# front of it, and it is why every act writes what it created into `st`.
# ---------------------------------------------------------------------------
ACTS = ["arrival", "stack", "switch", "dpdk"]


def _ghost():
    """A placeholder for something an earlier act would have created and a later
    act will fade out. Invisible, and safe to animate."""
    return VGroup(Dot(radius=0.001).set_opacity(0.0))


def _seed(scene, st, upto):
    need = ACTS.index(upto)
    set_cam(scene, LEFT_FRAME if need == 0 else FULL_FRAME)

    st.nic, st.krn = build_nic(), build_kernel()
    st.app, st.bound = build_app(), build_boundary()
    st.a1 = vlink(NIC_Y + NIC_H / 2 + 8, KRN_Y - KRN_H / 2 - 8)
    st.a2 = vlink(KRN_Y + KRN_H / 2 + 8, APP_Y - APP_H / 2 - 8)
    st.pkt = packet(INK, 30, glowing=True).move_to(P(920, 250))
    st.pkts = VGroup()
    st.krn.rows.set_opacity(0.35)
    scene.add(st.nic, st.krn, st.app, st.bound, st.a2)
    if need == 0:
        scene.add(st.a1, st.pkt)

    if need >= 1:                                   # arrival + the IRQ are done
        st.krn.rows.set_opacity(1.0)
        st.dma = vlink(NIC_Y + NIC_H / 2 + 8, KRN_Y - KRN_H / 2 - 8, color=HW, sw=6)
        st.dmat = tag("DMA", HW, TAG_T).move_to(P(SPINE_X + 118, 572))
        st.irq = bolt(P(600, NIC_Y), P(CPU_X - CPU_W / 2 - 6, 470))
        st.pkt.move_to(P(SPINE_X, 600))
        st.cpu = CPUColumn(scene)
        st.cpu_chrome = st.cpu.chrome()
        st.cpu_chrome.box.set_stroke(KERN, 3.4)
        st.budget = st.cpu.budget_mark()
        scene.add(st.dma, st.dmat, st.irq, st.pkt, st.cpu_chrome, st.budget)
        st.seg_app0 = st.cpu.band("YOUR APP", px=190, color=USER, sub="running")
        st.seg_app0.rect.set_fill(USER, 0.32)
        st.seg_irq = st.cpu.band("IRQ", 500, color=BAD, sub="save state")
        scene.add(st.seg_app0, st.seg_irq)

    if need >= 2:                                   # the stack + the copies are done
        st.seg_stack = st.cpu.band("STACK", 700, color=KERN, sub="sk_buff + TCP/IP")
        st.seg_copy = st.cpu.band("COPY", 400, color=MEM, sub="to user space")
        scene.add(st.seg_stack, st.seg_copy)
        st.skb = VGroup(box(320, 132, KERN, fill=KERN_BG, fill_op=0.55, r=0.10, sw=2.6)
                        .move_to(P(SPINE_X, 900)).set_z_index(Z_ZONE + 1))
        st.copy_group = VGroup(box(200, 96, MEM, fill=MEM_BG, fill_op=0.7, r=0.08, sw=2.4)
                               .move_to(P(SPINE_X + 8, 1108)).set_z_index(Z_ZONE + 1))
        st.dup = packet(INK, 26).move_to(P(SPINE_X, APP_Y))
        st.bw = _ghost()
        scene.add(st.skb, st.copy_group, st.dup, st.bw)

    if need >= 3:                                   # the context switch is done
        st.seg_ctx = st.cpu.band("SWITCH", 600, color=BAD, sub="ring 0 → ring 3")
        st.seg_app1 = st.cpu.band("YOUR APP", px=150, color=USER, sub="finally")
        scene.add(st.seg_ctx, st.seg_app1)
        st.throat2, st.tall = throat_shape(), _ghost()
        st.krn.save_state()
        scene.remove(st.krn)
        scene.add(st.throat2, st.tall)


class _Preview(VOScene):
    act = None
    start = 0.0

    def construct(self):
        self.camera.background_color = BG
        self.epoch = self.start
        st = Stage()
        kb, cap = KeywordBar(self), CaptionBar(self)
        _seed(self, st, self.act)
        label, col = {"arrival": ("THE PACKET PATH", NIC_C),
                      "stack": ("THE INTERRUPT", BAD),
                      "switch": ("MEMORY COPIES", MEM),
                      "dpdk": ("THE BOTTLENECK", BAD)}[self.act]
        kb._pin(kb._build(label, col))
        self.add(kb.mob)
        self.run_act(st, kb, cap)

    def run_act(self, st, kb, cap):
        raise NotImplementedError


class ActArrival(_Preview):
    act, start = "arrival", CUE["ls_see"] - 1.0

    def run_act(self, st, kb, cap):
        act_arrival(self, st, kb, cap)


class ActStack(_Preview):
    act, start = "stack", CUE["st_next"] - 1.2

    def run_act(self, st, kb, cap):
        act_stack(self, st, kb, cap)


class ActSwitch(_Preview):
    act, start = "switch", CUE["wk_finally"] - 1.2

    def run_act(self, st, kb, cap):
        act_switch(self, st, kb, cap)
        act_bottleneck(self, st, kb, cap)


class ActDPDK(_Preview):
    act, start = "dpdk", CUE["dp_this"] - 1.2

    def run_act(self, st, kb, cap):
        act_dpdk(self, st, kb, cap)
        act_payoff(self, st, kb, cap)
        act_close(self, st, kb, cap)
        act_outro(self)


class StillStage(Scene):
    """The machine at rest -- the layout check.  manim -sqh ep01_video.py StillStage"""

    def construct(self):
        self.camera.background_color = BG
        self.add(build_nic(), build_kernel(), build_app(), build_boundary(),
                 vlink(NIC_Y + NIC_H / 2 + 8, KRN_Y - KRN_H / 2 - 8),
                 vlink(KRN_Y + KRN_H / 2 + 8, APP_Y - APP_H / 2 - 8),
                 T("THE PACKET PATH", KEY_SIZE, NIC_C).move_to(P(CXP, 118)))


class StillCost(Scene):
    """The cost column, fully built -- the other layout check."""

    def construct(self):
        self.camera.background_color = BG
        col = CPUColumn(self)
        self.add(col.chrome(), col.budget_mark())
        for args in (dict(name="YOUR APP", px=190, color=USER, sub="running"),
                     dict(name="IRQ", cyc=500, color=BAD, sub="save state"),
                     dict(name="STACK", cyc=700, color=KERN, sub="sk_buff + TCP/IP"),
                     dict(name="COPY", cyc=400, color=MEM, sub="to user space"),
                     dict(name="SWITCH", cyc=600, color=BAD, sub="ring 0 → ring 3"),
                     dict(name="YOUR APP", px=150, color=USER, sub="finally")):
            self.add(col.band(**args))
        self.add(build_nic(), build_kernel(), build_app(), build_boundary())
