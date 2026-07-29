"""
AXIOBYTE SYSTEMS -- Episode 02
"Zero-copy: a packet is just a pointer"   (217.8 s, 9:16 portrait)

Render (video):   manim -qh --fps 60 ep02_video.py FullVideo
Render (draft):   manim -ql --fps 30 ep02_video.py FullVideo

Layout checks (one still frame each -- no timing, just geometry):
    manim -sqh ep02_video.py StillCopyChain    # NIC -> A -> B -> C, the copies
    manim -sqh ep02_video.py StillMbuf          # the mbuf, and what it points at
    manim -sqh ep02_video.py StillMempool       # the pool of preallocated buffers
    manim -sqh ep02_video.py StillPipeline      # four stages, one buffer

Act previews (each seeds the state it inherits and starts near its own t=0):
    manim -pql ep02_video.py PrevTrad       # 14 - 42   the copy tax
    manim -pql ep02_video.py PrevMbuf       # 42 - 68   zero-copy, and the mbuf
    manim -pql ep02_video.py PrevPool       # 68 -104   mempool + DMA
    manim -pql ep02_video.py PrevPipe       # 104-143   passing the handle
    manim -pql ep02_video.py PrevCheap      # 143-184   why a pointer wins
    manim -pql ep02_video.py PrevClose      # 184-end   transmit, recycle, recap

---------------------------------------------------------------------------
THE ONE RULE (inherited from Episode 01)
---------------------------------------------------------------------------
Nothing here is eyeballed. Every beat is a WORD START looked up in timeline.json
by W(word, sentence). The whole cue table is resolved at IMPORT, so a typo -- or
a re-cut voiceover that no longer contains the word -- fails immediately instead
of drifting silently out of sync.

---------------------------------------------------------------------------
THE ONE PICTURE
---------------------------------------------------------------------------
The whole episode is an argument about MOVEMENT, made by refusing to move one
object. The packet's bytes are drawn once, as a block of blue cells inside a
purple buffer, and after DMA writes them they do not move again -- not through
the parser, not through the firewall, not even when a router rewrites a header,
not at transmit. What moves instead is a yellow arrow: the pointer. The mbuf is
the small cyan card that carries that arrow from stage to stage. So the closing
line -- "a packet is best thought of not as bytes, but as a pointer to those
bytes" -- is not a caption. It is the literal state of the screen: the bytes
have sat still for two minutes while a yellow arrow did all the travelling.

The film's first forty seconds build the OPPOSITE picture on purpose -- the
traditional path, where the same bytes are copied buffer to buffer in red -- so
that the moment the copies stop, the stillness reads as the point.

---------------------------------------------------------------------------
COLOUR IS MEANING -- one hue per idea, and nothing borrows a hue it does not own
---------------------------------------------------------------------------
    blue    packet bytes / payload     purple  memory: a buffer, the mempool
    yellow  a pointer / the handle     cyan    the mbuf (and the AxioByte mark)
    green   the NIC / the wire         orange  the CPU
    red     a COPY -- bytes moving      grey    idle / empty / unused
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
FH = DH / 100.0                         # full frame height in manim units (19.2)


def P(px, py):
    """Design-space pixel (top-left origin) -> Manim coords."""
    return np.array([(px - CXP) / 100.0, (CYP - py) / 100.0, 0.0])


def U(px):
    """Design-space length -> Manim units."""
    return px / 100.0


def X(px):
    return (px - CXP) / 100.0


def Y(py):
    return (CYP - py) / 100.0


# ---------------------------------------------------------------------------
# FONTS -- DejaVu if present (what the reference episodes render with), else the
# macOS pair the project's setup guide names as the sanctioned substitute.
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

    W("mBuff", s=13) -> the START of the word "mBuff" in sentence 13. Raises if
    it is not there, which is the whole point: a cue can never silently point at
    nothing.
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
VOICEOVER_SECONDS = TL.duration        # 217.809


# ---------------------------------------------------------------------------
# THE CUE TABLE -- every beat in the film, resolved from the timeline at IMPORT.
# Read it top to bottom and you have read the video.
# ---------------------------------------------------------------------------
CUE = {
    # -- HOOK  "Imagine you're moving an entire library every time someone wants
    #           to read a single book."
    "hk_imagine":     W("Imagine", 0),        #   0.03  one shelf of books
    "hk_library":     W("library", 0),        #   1.55  a whole library
    "hk_book":        W("book", 0),           #   4.21  one book is requested

    # -- "You pack all the books into a truck, drive them to a new building,
    #     unload them, and repeat the same process again and again."
    "hk_pack":        W("pack", 1),           #   5.18  every book onto a truck
    "hk_truck":       W("truck", 1),          #   6.36
    "hk_drive":       W("drive", 1),          #   6.86  the truck rolls
    "hk_building":    W("building", 1),       #   7.72  a second building
    "hk_repeat":      W("repeat", 1),         #   9.34  ...and again
    "hk_again":       W("again", 1),          #  10.42

    # -- "Sounds ridiculously inefficient, right?"
    "hk_inefficient": W("inefficient", 2),    #  12.90  the absurd cost stamps
    "hk_right":       W("right", 2),          #  13.38

    # -- "That's exactly what traditional packet processing does."
    "tr_thats":       W("That's", 3),         #  14.64  the library becomes a packet
    "tr_traditional": W("traditional", 3),    #  15.65
    "tr_packet":      W("packet", 3),         #  16.11

    # -- "In traditional networking, when a packet travels from the hardware
    #     through the operating system kernel and up to an application, the actual
    #     bytes are copied across system boundaries."
    "tr_networking":  W("networking", 4),     #  18.37  the three-tier column
    "tr_travels":     W("travels", 4),        #  19.59  the packet enters
    "tr_hardware":    W("hardware", 4),       #  20.25
    "tr_kernel":      W("kernel", 4),         #  21.91
    "tr_application": W("application", 4),     #  23.05
    "tr_bytes":       W("bytes", 4),          #  24.66  [the actual bytes]
    "tr_copied":      W("copied", 4),         #  25.36  COPIED
    "tr_boundaries":  W("boundaries", 4),     #  26.32  across every boundary

    # -- "The network interface card, or NIC, receives the packet into one buffer."
    "nc_nic":         W("NIC", 5),            #  28.88  the NIC, in green
    "nc_receives":    W("receives", 5),       #  29.72
    "nc_buffer":      W("buffer", 5),         #  31.08  buffer A fills

    # -- "Then those bytes are copied into another buffer for processing."
    "c1_copied":      W("copied", 6),         #  32.81  A -> B, in red
    "c1_buffer":      W("buffer", 6),         #  33.79  buffer B

    # -- "They may be copied again before transmission."
    "c2_copied":      W("copied", 7),         #  35.95  B -> C, in red
    "c2_trans":       W("transmission", 7),   #  36.93  buffer C

    # -- "Every copy consumes CPU cycles, memory bandwidth, and cache."
    "ev_every":       W("Every", 8),          #  38.10  the meters appear
    "ev_cpu":         W("CPU", 8),            #  39.24  CPU cycles fill red
    "ev_bandwidth":   W("bandwidth", 8),      #  40.60  memory bandwidth fills
    "ev_cache":       W("cache", 8),          #  41.36  cache fills

    # -- "High performance networking takes a completely different approach."
    "hp_high":        W("High", 9),           #  42.42  title: A DIFFERENT APPROACH
    "hp_different":   W("different", 9),      #  44.89

    # -- "Instead of copying the packet, it simply passes a reference to it."
    "in_instead":     W("Instead", 10),       #  46.27  the red copies are struck out
    "in_reference":   W("reference", 10),     #  48.71  a yellow arrow, not a copy

    # -- "This technique is called zero copy."
    "zc_zero":        W("zero", 11),          #  50.85  ZERO COPY stamps on
    "zc_copy":        W("copy", 11),          #  51.17

    # -- "But what exactly is being passed?"  /  "The answer is an mBuff."
    "q_passed":       W("passed", 12),        #  53.26  a question mark
    "an_mbuf":        W("mBuff", 13),         #  55.18  the mbuf appears

    # -- "Think of an mBuff as a small metadata structure attached to the packet."
    "mb_think":       W("Think", 14),         #  56.24
    "mb_metadata":    W("metadata", 14),      #  57.82  the card, titled
    "mb_attached":    W("attached", 14),      #  58.74  tethered to the bytes

    # -- "It contains information like the packet length, protocol details, and
    #     most importantly, the exact memory address where the packet's payload
    #     begins."
    "mb_contains":    W("contains", 15),      #  60.40  fields fill in
    "mb_length":      W("length", 15),        #  62.01  pkt_len
    "mb_protocol":    W("protocol", 15),      #  62.45  l3/l4 proto
    "mb_exact":       W("exact", 15),         #  65.23  [most importantly]
    "mb_address":     W("address", 15),       #  66.11  buf_addr, in yellow
    "mb_payload":     W("payload", 15),       #  67.11  arrow -> first byte

    # -- "Now let's look at where those bytes live."
    "ml_now":         W("Now", 16),           #  68.39  push toward memory
    "ml_live":        W("live", 16),          #  69.97

    # -- "Before any packet even arrives, DPDK allocates a large collection of
    #     fixed-size packet buffers."
    "ml_before":      W("Before", 17),        #  70.66  before anything arrives
    "ml_dpdk":        W("DPDK", 17),          #  72.74  [HIGH]
    "ml_allocates":   W("allocates", 17),     #  73.52  the grid is preallocated
    "ml_fixed":       W("fixed-size", 17),    #  75.12  identical cells
    "ml_buffers":     W("buffers", 17),       #  76.06

    # -- "This collection is called a mempool."
    "mp_mempool":     W("mempool", 18),       #  78.33  MEMPOOL, named

    # -- "You can think of it as a warehouse filled with thousands of empty packet
    #     containers all ready to be used."
    "wh_warehouse":   W("warehouse", 19),     #  80.43
    "wh_thousands":   W("thousands", 19),     #  81.53  the grid multiplies
    "wh_containers":  W("containers", 19),    #  82.89  all empty, all ready

    # -- "When the NIC receives a packet, it doesn't allocate new memory."
    "dm_when":        W("When", 20),          #  85.24
    "dm_nic":         W("NIC", 20),           #  85.62  the NIC, back in green
    "dm_new":         W("new", 20),           #  87.82  NO malloc -- struck out

    # -- "Instead, the NIC uses Direct Memory Access or DMA to stream the incoming
    #     bytes straight from the wire directly into a free buffer in the mempool."
    "dm_instead":     W("Instead", 21),       #  88.76
    "dm_dma":         W("DMA", 21),           #  92.09  [HIGH] the yellow engine
    "dm_stream":      W("stream", 21),        #  93.05  bytes flow off the wire
    "dm_wire":        W("wire", 21),          #  95.31
    "dm_free":        W("free", 21),          #  96.66  into ONE free slot
    "dm_buffer":      W("buffer", 21),        #  96.90

    # -- "no CPU involvement, no dynamic memory allocation, no unnecessary copies."
    "no_cpu":         W("no", 22, 0),         #  98.18  no CPU
    "no_dynamic":     W("no", 22, 1),         #  99.88  no malloc
    "no_copies":      W("no", 22, 2),         # 101.83  no copy
    "no_copies_w":    W("copies", 22),        # 102.77

    # -- "From this moment onward, every stage of packet processing works with the
    #     same packet buffer."
    "pl_from":        W("From", 23),          # 103.95  build the pipeline
    "pl_stage":       W("stage", 23),         # 105.81
    "pl_same":        W("same", 23),          # 107.76  the SAME buffer
    "pl_buffer":      W("buffer", 23),        # 108.42

    # -- "The passer receives the mBuff."  (the parser stage)
    "s_parser":       W("passer", 24),        # 109.64  handle -> parser
    # -- "The classifier receives the same mBuff."
    "s_classifier":   W("classifier", 25),    # 111.46  ...same handle -> classifier
    # -- "The firewall receives the same mBuff."
    "s_firewall":     W("firewall", 26),      # 114.03  ...-> firewall
    # -- "The routing logic receives the same mBuff."
    "s_routing":      W("routing", 27),       # 116.51  ...-> routing

    # -- "Each component only receives a handle that points to the original packet
    #     buffer."
    "pl_each":        W("Each", 28),          # 119.24
    "pl_handle":      W("handle", 28),        # 121.24  it's only a handle
    "pl_points":      W("points", 28),        # 122.04  every arrow -> one buffer
    "pl_original":    W("original", 28),      # 122.71

    # -- "The packet buffer never moves."
    "nm_never":       W("never", 29),         # 125.19  the buffer is pinned
    "nm_moves":       W("moves", 29),         # 125.47

    # -- "Even if a router needs to modify a header or change an address, it
    #     modifies the bytes right there in place."
    "ip_router":      W("router", 30),        # 127.01
    "ip_modify":      W("modify", 30),        # 127.67
    "ip_header":      W("header", 30),        # 128.22  the header cells...
    "ip_address":     W("address", 30),       # 129.26
    "ip_place":       W("place", 30),         # 132.16  ...change, right here

    # -- "They're still sitting exactly where the NIC originally placed them."
    "ip_exactly":     W("exactly", 31),       # 133.83  same address as ever
    "ip_nic":         W("NIC", 31),           # 134.95

    # -- "This is the key idea behind zero copy."
    "ky_key":         W("key", 32),           # 137.61  THE KEY IDEA
    "ky_idea":        W("idea", 32),          # 138.00

    # -- "The packet isn't travelling through the system."  /  "Only the pointer is."
    "ky_travelling":  W("travelling", 33),    # 140.64  the bytes stay
    "ky_only":        W("Only", 34),          # 142.08  a lone yellow arrow flies
    "ky_pointer":     W("pointer", 34),       # 142.52

    # -- "Passing a pointer is incredibly cheap."
    "ch_passing":     W("Passing", 35),       # 143.70
    "ch_cheap":       W("cheap", 35),         # 145.47

    # -- "It's typically just an 8-byte memory address on a 64-bit system compared
    #     to copying hundreds or even thousands of bytes across system boundaries
    #     for every packet."
    "ch_8byte":       W("8-byte", 36),        # 147.01  8 bytes...
    "ch_64bit":       W("64-bit", 36),        # 148.65
    "ch_copying":     W("copying", 36),       # 150.77  ...versus
    "ch_hundreds":    W("hundreds", 36),      # 151.16
    "ch_thousands":   W("thousands", 36),     # 152.12  ...1500 bytes

    # -- "Now imagine processing millions of packets every second."
    "mi_now":         W("Now", 37),           # 155.94
    "mi_millions":    W("millions", 37),      # 157.32  a counter spins
    "mi_second":      W("second", 37),        # 158.50

    # -- "If every packet required multiple memory copies, the CPU would spend most
    #     of its time moving bytes instead of making forwarding decisions."
    "if_cpu":         W("CPU", 38),           # 162.63  the core's time...
    "if_moving":      W("moving", 38),        # 164.65  ...eaten by copies (red)
    "if_forwarding":  W("forwarding", 38),    # 166.50  a sliver left for the work

    # -- "By eliminating those copies, zero copy dramatically reduces CPU overhead,
    #     lowers memory bandwidth usage, improves cache efficiency, and enables
    #     applications like DPDK to achieve tens or even hundreds of gigabits per
    #     second on modern hardware."
    "po_by":          W("By", 39),            # 168.06  the copies vanish
    "po_reduces":     W("reduces", 39),       # 171.44  down CPU overhead
    "po_lowers":      W("lowers", 39),        # 173.08  down mem bandwidth
    "po_improves":    W("improves", 39),      # 175.13  up cache efficiency
    "po_dpdk":        W("DPDK", 39),          # 178.31  [HIGH]
    "po_tens":        W("tens", 39),          # 179.69
    "po_gigabits":    W("gigabits", 39),      # 181.59  the gauge slams to 100+
    "po_hardware":    W("hardware", 39),      # 183.22

    # -- "Finally, when packet processing is complete, the NIC transmits the packet
    #     using the exact same memory buffer."
    "tx_finally":     W("Finally", 40),       # 183.94
    "tx_complete":    W("complete", 40),      # 185.78
    "tx_nic":         W("NIC", 40),           # 186.80  back to green
    "tx_transmits":   W("transmits", 40),     # 187.28  the buffer -> the wire
    "tx_same":        W("same", 40),          # 189.47  the exact same bytes
    "tx_buffer":      W("buffer", 40),        # 190.09

    # -- "After transmission, that buffer is returned to the mempool, ready to be
    #     reused for the next incoming packet."
    "rc_after":       W("After", 41),         # 191.15
    "rc_returned":    W("returned", 41),      # 193.18  the buffer flies home
    "rc_mempool":     W("mempool", 41),       # 193.76
    "rc_reused":      W("reused", 41),        # 195.00  the slot is free again
    "rc_next":        W("next", 41),          # 195.82

    # -- "The packet buffer was allocated only once."  /  "It was never copied."
    "rp_allocated":   W("allocated", 42),     # 198.36  once
    "rp_once":        W("once", 42),          # 199.41
    "rp_never":       W("never", 43),         # 200.43  never copied
    "rp_copied":      W("copied", 43),        # 200.81

    # -- "Only the mBuff, the handle to that data, was passed from one component to
    #     another."
    "rp_only":        W("Only", 44),          # 201.69
    "rp_mbuf":        W("mBuff", 44),          # 202.31  only the handle moved
    "rp_handle":      W("handle", 44),        # 203.05
    "rp_passed":      W("passed", 44),        # 204.72

    # -- "That's why, in high-performance networking, a packet is often best
    #     thought of not as a collection of bytes, but as a pointer to those bytes."
    "fn_thats":       W("That's", 45),        # 207.04  the thesis
    "fn_packet":      W("packet", 45),        # 209.71
    "fn_not":         W("not", 45),           # 211.46  NOT a pile of bytes...
    "fn_bytes1":      W("bytes", 45, 0),      # 212.41
    "fn_pointer":     W("pointer", 45),       # 213.66  ...but a pointer to them
    "fn_bytes2":      W("bytes", 45, 1),      # 214.52

    # -- "And that's the essence of zero copy."
    "es_and":         W("And", 46),           # 215.81
    "es_essence":     W("essence", 46),       # 216.51  ZERO COPY, one last time
    "es_zero":        W("zero", 46),          # 216.99
}


# ---------------------------------------------------------------------------
# VOICEOVER  (this episode's robust master is ep02-robust.mp3)
# ---------------------------------------------------------------------------
AUDIO_CANDIDATES = [os.path.join(HERE, n) for n in
                    ("ep02-robust.mp3", "voiceover.mp3", "voiceover.mpeg",
                     "voiceover.wav")]


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
    """

    epoch = 0.0
    LEAD = 0.20        # begin each beat ~0.20 s before its spoken word

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

INK     = "#EAF0F6"    # near-white  -- headline type, neutral labels
SUBTLE  = "#9AA6BC"
IDLE    = "#65728A"    # GREY    -- idle / empty / unused
PKT     = "#4AA8FF"    # BLUE    -- packet bytes / payload
KERN    = "#F0A431"    # ORANGE  -- the CPU (and the kernel, in the traditional half)
NIC_C   = "#4DE6A0"    # GREEN   -- the NIC / the wire
PTR     = "#F5D14F"    # YELLOW  -- a pointer / the handle
MEM     = "#B79CF0"    # PURPLE  -- memory: a buffer, the mempool
BAD     = "#FF5C55"    # RED     -- a COPY: bytes actually moving
MBUF_C  = "#34D8E8"    # CYAN    -- the mbuf (and the AxioByte mark)

KERN_BG = "#33240F"
BAD_BG  = "#331617"
MBUF_BG = "#10303A"
NIC_BG  = "#0F2A20"
MEM_BG  = "#221B38"
PTR_BG  = "#332B10"

Z_GLOW, Z_ZONE, Z_NODE, Z_LINE, Z_LABEL, Z_PKT, Z_CARD = 0, 1, 2, 3, 5, 7, 9
Z_SCRIM, Z_TITLE, Z_KEY = 20, 21, 25

# type ladder (font_size ~= on-screen pixel height at this canvas)
KEY_SIZE, TITLE_SIZE, CAP_SIZE = 38, 66, 30
NODE_T, NODE_S, ROW_T, TAG_T, MONO_S = 33, 21, 24, 22, 18

# the address the mbuf points at -- one literal value, reused everywhere, so the
# pointer and the buffer are visibly the SAME address.
ADDR = "0x7f3a4c00"

FULL_FRAME = (CXP, CYP, 1.00)


# ===========================================================================
# DRAWING TOOLKIT
# ===========================================================================
def glow(shape, color=None, layers=5, spread=0.24, max_op=0.13):
    """A soft halo: nested translucent copies. Survives a camera push far better
    than a fat stroke does."""
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


def M(txt, size=MONO_S, color=SUBTLE):
    return Text(txt, font=MN, weight=NORMAL, color=color, font_size=size)


def box(w, h, color, fill=SURF2, fill_op=1.0, r=0.16, sw=3.0):
    return RoundedRectangle(width=U(w), height=U(h), corner_radius=r,
                            stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=fill_op)


def node(title, sub=None, w=360, h=150, color=NIC_C, px=None, py=None,
         glowing=True, tsize=NODE_T):
    """A labelled component of the machine."""
    b = box(w, h, color).set_z_index(Z_NODE)
    t = T(title, tsize, INK)
    inner = t
    if sub:
        inner = VGroup(t, M(sub, NODE_S, IDLE)).arrange(DOWN, buff=0.09)
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
    g.box, g.text = b, t
    return g


def tag(txt, color, size=TAG_T, mono=False):
    """A small plated label -- readable over anything it is dropped on."""
    t = T(txt, size, color, font=(MN if mono else FN))
    plate = SurroundingRectangle(t, buff=0.13, corner_radius=0.09, stroke_width=0,
                                 fill_color=BG, fill_opacity=0.88)
    return VGroup(plate, t).set_z_index(Z_LABEL)


def ptr_arrow(a, b, color=PTR, sw=6):
    """THE pointer: a yellow arrow. The one thing in the film that is allowed to
    move once the bytes have landed."""
    return Arrow(a, b, buff=0.06, color=color, stroke_width=sw,
                 max_tip_length_to_length_ratio=0.16,
                 max_stroke_width_to_length_ratio=999).set_z_index(Z_LINE + 1)


def vlink(p0, p1, color=IDLE, sw=5):
    return Arrow(p0, p1, buff=0.04, color=color, stroke_width=sw,
                 max_tip_length_to_length_ratio=0.22,
                 max_stroke_width_to_length_ratio=999).set_z_index(Z_LINE)


def strike(mob, color=BAD, sw=6, pad=0.10):
    return Line(mob.get_left() + LEFT * pad, mob.get_right() + RIGHT * pad,
                color=color, stroke_width=sw).set_z_index(Z_CARD + 2)


def cross(center, s=70, color=BAD, sw=7):
    h = U(s) / 2
    c = np.array(center)
    return VGroup(Line(c + [-h, -h, 0], c + [h, h, 0], color=color, stroke_width=sw),
                  Line(c + [-h, h, 0], c + [h, -h, 0], color=color, stroke_width=sw)) \
        .set_z_index(Z_CARD + 2)


def check(center, s=64, color=NIC_C, sw=7):
    c = np.array(center)
    return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners(
        [c + [-U(s) * 0.42, 0, 0], c + [-U(s) * 0.08, -U(s) * 0.34, 0],
         c + [U(s) * 0.5, U(s) * 0.4, 0]]).set_z_index(Z_CARD + 2)


def _dimmed(m, f):
    """A copy of `m` with every fill and stroke opacity SCALED by f (not SET to f
    -- glow halos live at 1-13% and would brighten if assigned)."""
    c = m.copy()
    for sm in c.family_members_with_points():
        sm.set_fill(opacity=sm.get_fill_opacity() * f)
        sm.set_stroke(opacity=sm.get_stroke_opacity() * f)
    return c


def dim(mobs, f=0.20):
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
# THE PINNED CHROME -- chapter keyword (top) and caption (bottom).
# Both ride the CAMERA FRAME, so a push-in neither crops nor doubles them.
# ===========================================================================
class _Pinned:
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
    MAXW = 6.6

    def _build(self, label, color):
        t = T(label, KEY_SIZE, color).set_z_index(Z_KEY)
        if t.width > self.MAXW:
            t.scale_to_fit_width(self.MAXW)
        return self._place(t)

    def to(self, label, color, run_time=0.6, extra=None):
        new = self._build(label, color)
        if self.mob is None:
            self.scene.play(FadeIn(new, shift=DOWN * 0.14), *(extra or []), run_time=run_time)
        else:
            self.mob.clear_updaters()
            self.scene.play(FadeTransform(self.mob, new), *(extra or []), run_time=run_time)
        self._pin(new)

    def hide(self, run_time=0.5, extra=None):
        if self.mob is None:
            if extra:
                self.scene.play(*extra, run_time=run_time)
            return
        self.mob.clear_updaters()
        self.scene.play(FadeOut(self.mob, shift=UP * 0.16), *(extra or []), run_time=run_time)
        self.mob = None

    def morph_from(self, title, label, color, run_time=0.85, extra=None):
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
    MAXW = 8.8

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


def make_scrim(op=0.90):
    return Rectangle(width=config.frame_width * 1.5, height=config.frame_height * 1.5,
                     fill_color=BG, fill_opacity=op, stroke_width=0) \
        .move_to(ORIGIN).set_z_index(Z_SCRIM)


def title_card(scene, kb, label, color, t_in, t_out, sub=None, extra_out=None):
    """The film's one title grammar: a full-screen card SHRINKS into the top of
    the frame and BECOMES the chapter keyword it just opened."""
    sc = make_scrim()
    f = scene.camera.frame
    ttl = T(label, TITLE_SIZE, color).move_to(f.get_center() + UP * 0.6).set_z_index(Z_TITLE)
    if ttl.width > FH * 0.44:
        ttl.scale_to_fit_width(config.frame_width - 1.0)
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
# THE PARTS OF THE MACHINE
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


def byte_cells(n=6, cw=42, ch=70, gap=7, color=PKT, filled=True):
    """The packet's payload, drawn as individual bytes so a copy has something to
    move and an in-place edit has something to recolour."""
    cells = VGroup(*[
        RoundedRectangle(width=U(cw), height=U(ch), corner_radius=U(6),
                         stroke_color=color, stroke_width=1.4,
                         fill_color=(color if filled else SURF2),
                         fill_opacity=(0.85 if filled else 1.0))
        for _ in range(n)])
    cells.arrange(RIGHT, buff=U(gap))
    return cells.set_z_index(Z_PKT)


def packet_buffer(px, py, addr=ADDR, n=6, w=350, h=170, filled=True,
                  title="packet buffer", glowing=True):
    """One buffer allocated from the mempool: a purple frame (the memory) holding
    a blue payload (the bytes). This exact object, once filled by DMA, does not
    move again for the rest of the film."""
    b = box(w, h, MEM, fill=MEM_BG, fill_op=0.45, r=0.12, sw=2.6).set_z_index(Z_NODE)
    cells = byte_cells(n=n, filled=filled).move_to(b.get_center() + DOWN * U(8))
    ttl = M(title, MONO_S, MEM).next_to(b, UP, buff=U(12)) if title else VGroup()
    ad = M(addr, MONO_S, PTR).move_to(b.get_center() + UP * U(h / 2 - 20))
    g = VGroup(b, cells, ad, ttl).move_to(P(px, py))
    if glowing:
        g.add_to_back(glow(b, MEM, layers=5, spread=0.12, max_op=0.08))
    g.box, g.cells, g.addr, g.title = b, cells, ad, ttl
    return g


def mbuf_card(px, py, w=330, h=280):
    """The mbuf: metadata plus, crucially, buf_addr -- the address of the bytes.
    Everything above buf_addr is bookkeeping; buf_addr is the pointer itself."""
    b = box(w, h, MBUF_C, fill=MBUF_BG, fill_op=0.9, r=0.12, sw=2.8).set_z_index(Z_NODE)
    ttl = T("mbuf", NODE_T - 3, MBUF_C, font=MN).move_to(b.get_center() + UP * U(h / 2 - 40))
    rule = Line(b.get_left() + RIGHT * 0.2, b.get_right() + LEFT * 0.2,
                color=MBUF_C, stroke_width=1.4).set_opacity(0.5) \
        .move_to(b.get_center() + UP * U(h / 2 - 78))
    rows = VGroup()
    fields = [("pkt_len", "64", SUBTLE), ("l3/l4", "IPv4/TCP", SUBTLE),
              ("buf_addr", ADDR, PTR)]
    for i, (k, v, col) in enumerate(fields):
        kk = M(k, MONO_S, IDLE)
        vv = M(v, MONO_S, col)
        r = VGroup(kk, vv)
        kk.move_to(b.get_left() + RIGHT * U(24) + UP * U(h / 2 - 130 - i * 56),
                   aligned_edge=LEFT)
        vv.move_to(b.get_right() + LEFT * U(24) + UP * U(h / 2 - 130 - i * 56),
                   aligned_edge=RIGHT)
        r.key, r.val = kk, vv
        rows.add(r)
    g = VGroup(b, ttl, rule, rows).move_to(P(px, py)).set_z_index(Z_NODE)
    g.add_to_back(glow(b, MBUF_C, layers=5, spread=0.14, max_op=0.09))
    g.box, g.title, g.rows = b, ttl, rows
    g.addr_row = rows[2]
    return g


def mempool(px, py, cols=8, rows=1, slot=88, gap=12, hot=None):
    """A row (or grid) of preallocated, fixed-size buffer slots. Empty slots are
    grey; the one DMA fills is blue."""
    slots = VGroup()
    for r in range(rows):
        for c in range(cols):
            col = PKT if (hot is not None and r * cols + c == hot) else IDLE
            fill = PKT if (hot is not None and r * cols + c == hot) else SURF2
            fop = 0.7 if (hot is not None and r * cols + c == hot) else 1.0
            s = RoundedRectangle(width=U(slot), height=U(slot * 0.62), corner_radius=U(6),
                                 stroke_color=col, stroke_width=1.8,
                                 fill_color=fill, fill_opacity=fop)
            slots.add(s)
    slots.arrange_in_grid(rows=rows, cols=cols, buff=U(gap))
    ttl = M("mempool", MONO_S, MEM).next_to(slots, UP, buff=U(12))
    g = VGroup(slots, ttl).move_to(P(px, py))
    g.slots, g.title = slots, ttl
    return g


def cost_meter(label, px, py, w=300, h=44, color=BAD):
    """A little gauge that fills red -- the price of one copy."""
    frame = box(w, h, IDLE, fill=SURF2, r=0.08, sw=1.8)
    fill = RoundedRectangle(width=0.001, height=U(h) - 0.08, corner_radius=U(6),
                            stroke_width=0, fill_color=color, fill_opacity=0.85)
    fill.align_to(frame, LEFT).shift(RIGHT * 0.04)
    lab = M(label, MONO_S, SUBTLE).next_to(frame, UP, buff=U(6), aligned_edge=LEFT)
    g = VGroup(frame, fill, lab).move_to(P(px, py))
    g.frame, g.fill, g.w = frame, fill, w
    return g


def meter_fill(meter, frac=0.85):
    target = meter.frame.copy().stretch_to_fit_width((U(meter.w) - 0.08) * frac) \
        .align_to(meter.frame, LEFT).shift(RIGHT * 0.04) \
        .set_stroke(width=0).set_fill(meter.fill.get_fill_color(), 0.85)
    return Transform(meter.fill, target)


# ===========================================================================
# ACT 0 -- THE HOOK   (0.0 - 14.6 s)
#   "Imagine you're moving an entire library every time someone wants to read a
#    single book."
#   "You pack all the books into a truck, drive them to a new building, unload
#    them, and repeat the same process again and again."
#   "Sounds ridiculously inefficient, right?"
#
# The whole film in metaphor: to read ONE book you haul the ENTIRE library. The
# books are bytes; the truck is a copy. It should feel absurd, because it is.
# ===========================================================================
def act_hook(scene, st, kb, cap):
    set_cam(scene, FULL_FRAME)

    # 0.03  a library: shelves of books.
    def shelf(px, py, nb=7, color=PKT):
        frame = box(300, 78, IDLE, fill=SURF2, r=0.04, sw=2.0)
        books = VGroup(*[
            RoundedRectangle(width=U(30), height=U(56), corner_radius=U(3),
                             stroke_color=color, stroke_width=1.2,
                             fill_color=color, fill_opacity=0.8)
            for _ in range(nb)]).arrange(RIGHT, buff=U(6))
        books.move_to(frame.get_center())
        g = VGroup(frame, books).move_to(P(px, py))
        g.books = books
        return g

    lib = VGroup(*[shelf(CXP, 560 + i * 108) for i in range(4)]).set_z_index(Z_NODE)
    scene.at("hk_imagine", lead=0.0)
    scene.play(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in lib],
                           lag_ratio=0.18), run_time=1.0)

    # 1.55  "an entire LIBRARY"
    libtag = tag("the library  =  your packet's bytes", MEM, TAG_T - 2).move_to(P(CXP, 430))
    scene.at("hk_library")
    scene.play(FadeIn(libtag, shift=DOWN * 0.1),
               lib.animate.set_stroke(opacity=1.0), run_time=0.5)

    # 4.21  "...to read a single BOOK."  One book is wanted -- just one.
    want = lib[1].books[3]
    halo = SurroundingRectangle(want, color=NIC_C, buff=0.06, corner_radius=0.04,
                                stroke_width=4).set_z_index(Z_CARD)
    booktag = tag("wanted: 1 book", NIC_C, TAG_T - 3).next_to(lib[1], RIGHT, buff=0.2)
    scene.at("hk_book")
    scene.play(Create(halo), FadeIn(booktag, shift=RIGHT * 0.1),
               Flash(want.get_center(), color=NIC_C, line_length=0.12,
                     num_lines=10, flash_radius=0.28), run_time=0.6)

    # 5.18  "You PACK all the books into a TRUCK"  -- the absurd part: to move one
    # book, the whole library is boxed up.
    truck = VGroup(
        box(240, 150, KERN, fill=KERN_BG, fill_op=0.5, r=0.08, sw=2.6),
        box(120, 90, KERN, fill=SURF2, r=0.06, sw=2.0).shift(RIGHT * U(150)),
    )
    wheels = VGroup(*[Circle(radius=U(26), color=IDLE, fill_color=SURF2, fill_opacity=1,
                             stroke_width=3).move_to(truck.get_bottom() + RIGHT * dx + DOWN * U(4))
                      for dx in (U(-70), U(60), U(150))])
    truck = VGroup(truck, wheels).move_to(P(280, 1080)).set_z_index(Z_NODE)
    truck.set_opacity(0.0)
    scene.at("hk_pack")
    scene.play(FadeOut(halo), FadeOut(booktag), FadeOut(libtag),
               lib.animate.scale(0.42).move_to(P(280, 1080)), run_time=0.7)
    scene.at("hk_truck")
    scene.play(truck.animate.set_opacity(1.0), lib.animate.set_opacity(0.0), run_time=0.4)
    scene.remove(lib)

    # 6.86  "DRIVE them to a NEW BUILDING, unload"  -- across the frame it goes,
    # and everything it carried is set down again, untouched, for one read.
    dest = box(300, 360, IDLE, fill=SURF2, r=0.06, sw=2.4).move_to(P(840, 980))
    destt = M("new building", MONO_S, IDLE).next_to(dest, UP, buff=U(10))
    scene.at("hk_drive")
    scene.play(FadeIn(dest), FadeIn(destt), run_time=0.35)
    scene.play(truck.animate.move_to(P(760, 1080)), run_time=0.8, rate_func=rush_from)
    lib2 = VGroup(*[box(240, 60, PKT, fill=SURF2, r=0.03, sw=1.6).move_to(P(840, 900 + i * 74))
                    for i in range(4)]).set_z_index(Z_NODE)
    lib2.set_opacity(0.0)
    scene.at("hk_building")
    scene.play(lib2.animate.set_opacity(1.0), run_time=0.5)

    # 9.34  "and REPEAT the same process AGAIN and AGAIN."
    scene.at("hk_repeat")
    loop = CurvedArrow(P(760, 820), P(360, 820), angle=-TAU / 3, color=BAD, stroke_width=5) \
        .set_z_index(Z_LINE)
    scene.play(Create(loop), run_time=0.5)
    scene.at("hk_again")
    scene.play(Indicate(truck, color=KERN, scale_factor=1.06),
               Indicate(loop, color=BAD, scale_factor=1.04), run_time=0.7)

    # 12.90  "Sounds ridiculously INEFFICIENT, right?"
    stamp = pill("ridiculously inefficient", BAD, BAD_BG, TAG_T, h=64, glowing=True) \
        .move_to(P(CXP, 1440)).rotate(-6 * DEGREES)
    scene.at("hk_inefficient")
    scene.play(FadeIn(stamp, scale=1.25), run_time=0.45)
    scene.at("hk_right")
    scene.play(Indicate(stamp, color=BAD, scale_factor=1.06), run_time=0.5)
    st.hook = VGroup(truck, dest, destt, lib2, loop, stamp)


# ===========================================================================
# ACT 1 -- THE COPY TAX   (14.6 - 42.4 s)
#   "That's exactly what traditional packet processing does."
#   "In traditional networking, when a packet travels from the hardware through
#    the operating system kernel and up to an application, the actual bytes are
#    copied across system boundaries."
#   "The NIC receives the packet into one buffer."
#   "Then those bytes are copied into another buffer for processing."
#   "They may be copied again before transmission."
#   "Every copy consumes CPU cycles, memory bandwidth, and cache."
# ===========================================================================
def act_traditional(scene, st, kb, cap):
    # 14.64  the metaphor collapses into the real thing: one packet.
    scene.at("tr_thats")
    pkt0 = packet_buffer(CXP, 900, n=6, w=300, h=150, title="", glowing=True)
    pkt0.title.set_opacity(0.0)
    scene.play(FadeOut(st.hook, scale=0.7), run_time=0.5)
    kb.to("TRADITIONAL PATH", BAD)
    scene.at("tr_traditional")
    scene.play(FadeIn(pkt0, scale=1.1), run_time=0.5)
    scene.at("tr_packet")
    scene.play(Indicate(pkt0.cells, color=PKT, scale_factor=1.08), run_time=0.4)

    # 18.37  the three-tier column the packet must climb: hardware -> kernel ->
    # app. Each boundary between them is where a copy will happen.
    hw = node("HARDWARE", "NIC", 360, 130, NIC_C, CXP, 470, tsize=NODE_T - 3)
    krn = node("OS KERNEL", "network stack", 360, 130, KERN, CXP, 900, tsize=NODE_T - 3)
    app = node("APPLICATION", "your process", 360, 130, PKT, CXP, 1330, tsize=NODE_T - 3)
    scene.at("tr_networking")
    scene.play(FadeOut(pkt0, shift=UP * 0.3),
               LaggedStart(FadeIn(hw, shift=DOWN * 0.1), FadeIn(krn), FadeIn(app, shift=UP * 0.1),
                           lag_ratio=0.25), run_time=0.9)
    st.hw, st.krn, st.app = hw, krn, app

    # 19.59  "when a packet TRAVELS from the HARDWARE ... KERNEL ... APPLICATION"
    trav = packet_buffer(CXP, 470, n=4, w=150, h=90, title="", glowing=True)
    trav.title.set_opacity(0.0)
    scene.at("tr_travels")
    scene.add(trav)
    scene.play(Indicate(hw, color=NIC_C, scale_factor=1.05), run_time=0.4)
    scene.at("tr_hardware")
    scene.play(trav.animate.move_to(P(CXP, 620)), run_time=0.4)
    scene.at("tr_kernel")
    scene.play(trav.animate.move_to(P(CXP, 900)),
               Indicate(krn, color=KERN, scale_factor=1.04), run_time=0.5)
    scene.at("tr_application")
    scene.play(trav.animate.move_to(P(CXP, 1330)),
               Indicate(app, color=PKT, scale_factor=1.04), run_time=0.5)

    # 24.66  "the actual BYTES are COPIED across system BOUNDARIES." The two
    # boundaries light red, and a red duplicate is torn off at each -- the packet
    # is not passed, it is re-created.
    scene.at("tr_bytes")
    scene.play(FadeOut(trav), run_time=0.25)
    b1 = DashedLine(P(360, 685), P(720, 685), color=BAD, stroke_width=3, dash_length=0.14) \
        .set_z_index(Z_LINE)
    b2 = DashedLine(P(360, 1115), P(720, 1115), color=BAD, stroke_width=3, dash_length=0.14) \
        .set_z_index(Z_LINE)
    scene.at("tr_copied")
    scene.play(Create(b1), Create(b2), run_time=0.5)
    scene.at("tr_boundaries")
    ghost1 = byte_cells(4, color=BAD).scale(0.5).move_to(P(CXP, 620))
    ghost2 = byte_cells(4, color=BAD).scale(0.5).move_to(P(CXP, 1050))
    scene.play(FadeIn(ghost1, target_position=P(CXP, 550)),
               FadeIn(ghost2, target_position=P(CXP, 980)), run_time=0.5)
    scene.play(FadeOut(ghost1), FadeOut(ghost2), run_time=0.3)
    st.bounds = VGroup(b1, b2)

    # 27.24  Now the real chain, close up. The camera drops the abstract column and
    # walks the buffers: NIC -> A -> B -> C. This is the sequence the whole film
    # exists to demolish, so it is drawn honestly.
    kb.to("THREE BUFFERS, THREE COPIES", BAD, run_time=0.5,
          extra=[FadeOut(hw, shift=UP * 0.2), FadeOut(krn), FadeOut(app, shift=DOWN * 0.2),
                 FadeOut(st.bounds)])
    nic = node("NIC", "off the wire", 300, 120, NIC_C, 300, 430, tsize=NODE_T)
    bufA = packet_buffer(300, 720, n=6, w=330, h=150, title="buffer A", glowing=True)
    scene.at("nc_nic")
    scene.play(FadeIn(nic, shift=DOWN * 0.15), run_time=0.45)
    scene.at("nc_receives")
    nicarr = vlink(P(300, 490), P(300, 645), color=NIC_C)
    scene.play(GrowArrow(nicarr), run_time=0.4)
    scene.at("nc_buffer")
    scene.play(FadeIn(bufA, scale=1.08), run_time=0.5)
    st.nic, st.bufA, st.nicarr = nic, bufA, nicarr

    # 31.86  "copied into ANOTHER BUFFER for processing"  A -> B. A red copy of
    # every byte physically slides down into a new buffer. The bytes MOVED.
    bufB = packet_buffer(300, 1060, addr="0x9c14e880", n=6, w=330, h=150,
                         title="buffer B", glowing=True)
    bufB.cells.set_opacity(0.0)
    arrAB = vlink(P(300, 800), P(300, 980), color=BAD, sw=6)
    scene.at("c1_copied")
    scene.play(GrowArrow(arrAB), FadeIn(bufB.box), FadeIn(bufB.addr), FadeIn(bufB.title),
               run_time=0.4)
    copyAB = bufA.cells.copy().set_color(BAD).set_z_index(Z_PKT + 1)
    scene.add(copyAB)
    scene.play(copyAB.animate.move_to(bufB.cells.get_center()), run_time=0.55,
               rate_func=rush_from)
    scene.play(bufB.cells.animate.set_opacity(0.85), FadeOut(copyAB), run_time=0.25)
    scene.at("c1_buffer")
    scene.play(Indicate(bufB.box, color=MEM, scale_factor=1.04), run_time=0.35)
    st.bufB, st.arrAB = bufB, arrAB

    # 35.55  "COPIED AGAIN before TRANSMISSION"  B -> C. Same crime, third time.
    bufC = packet_buffer(300, 1400, addr="0xab02f100", n=6, w=330, h=150,
                         title="buffer C  (tx)", glowing=True)
    bufC.cells.set_opacity(0.0)
    arrBC = vlink(P(300, 1140), P(300, 1320), color=BAD, sw=6)
    scene.at("c2_copied")
    scene.play(GrowArrow(arrBC), FadeIn(bufC.box), FadeIn(bufC.addr), FadeIn(bufC.title),
               run_time=0.4)
    copyBC = bufB.cells.copy().set_color(BAD).set_z_index(Z_PKT + 1)
    scene.add(copyBC)
    scene.play(copyBC.animate.move_to(bufC.cells.get_center()), run_time=0.5,
               rate_func=rush_from)
    scene.play(bufC.cells.animate.set_opacity(0.85), FadeOut(copyBC), run_time=0.25)
    scene.at("c2_trans")
    scene.play(Indicate(bufC.box, color=MEM, scale_factor=1.04), run_time=0.35)
    st.bufC, st.arrBC = bufC, arrBC

    # 38.10  "EVERY COPY consumes CPU CYCLES, memory BANDWIDTH, and CACHE."
    # Three meters on the right, filling red as each cost is named. The bill.
    mCPU = cost_meter("CPU cycles", 820, 720, color=BAD)
    mBW = cost_meter("memory bandwidth", 820, 880, color=BAD)
    mCA = cost_meter("cache", 820, 1040, color=BAD)
    scene.at("ev_every")
    scene.play(cam(scene, (600, 950, 1.0)),
               LaggedStart(FadeIn(mCPU), FadeIn(mBW), FadeIn(mCA), lag_ratio=0.2),
               run_time=0.7)
    scene.at("ev_cpu")
    scene.play(meter_fill(mCPU, 0.88), run_time=0.5)
    scene.at("ev_bandwidth")
    scene.play(meter_fill(mBW, 0.82), run_time=0.5)
    scene.at("ev_cache")
    scene.play(meter_fill(mCA, 0.9), run_time=0.5)
    cap.show("paid per packet · millions of times a second", BAD)
    st.meters = VGroup(mCPU, mBW, mCA)
    st.copychain = VGroup(st.nic, st.nicarr, st.bufA, st.bufB, st.bufC, st.arrAB, st.arrBC)


# ===========================================================================
# ACT 2 -- A DIFFERENT APPROACH, AND THE mbuf   (42.4 - 68.4 s)
#   "High performance networking takes a completely different approach."
#   "Instead of copying the packet, it simply passes a reference to it."
#   "This technique is called zero copy."
#   "But what exactly is being passed?"  /  "The answer is an mBuff."
#   "Think of an mBuff as a small metadata structure attached to the packet."
#   "It contains ... the packet length, protocol details, and most importantly,
#    the exact memory address where the packet's payload begins."
# ===========================================================================
def act_zerocopy_intro(scene, st, kb, cap):
    # 42.42  clear the copy machine and title the turn.
    cap.clear(run_time=0.4)
    title_card(scene, kb, "A DIFFERENT WAY", MBUF_C,
               CUE["hp_high"], CUE["hp_different"],
               sub="stop moving the bytes",
               extra_out=[FadeOut(st.copychain, scale=0.85), FadeOut(st.meters, scale=0.85)])

    # 46.27  "INSTEAD of copying" -- one buffer, and the red copies are gone.
    set_cam(scene, FULL_FRAME)
    buf = packet_buffer(360, 980, n=6, w=360, h=180, glowing=True)
    scene.at("in_instead")
    scene.play(FadeIn(buf, scale=1.08), run_time=0.55)
    nocopy = cross(P(360, 640), s=90)
    nocopy_t = tag("no copy", BAD, TAG_T - 2).move_to(P(360, 740))
    scene.play(Create(nocopy), FadeIn(nocopy_t), run_time=0.4)

    # 48.71  "it simply passes a REFERENCE to it."  A single yellow arrow -- the
    # first pointer of the film -- reaches for the buffer instead of copying it.
    ref = ptr_arrow(P(820, 980), P(560, 980))
    ref_t = tag("a reference", PTR, TAG_T - 2).move_to(P(880, 890))
    scene.at("in_reference")
    scene.play(FadeOut(nocopy), FadeOut(nocopy_t),
               GrowArrow(ref), FadeIn(ref_t, shift=LEFT * 0.1), run_time=0.6)

    # 50.85  "This technique is called ZERO COPY."
    zc = pill("ZERO COPY", MBUF_C, MBUF_BG, NODE_T, h=96, glowing=True).move_to(P(CXP, 470))
    scene.at("zc_zero")
    scene.play(FadeIn(zc, scale=1.15), run_time=0.45)
    scene.at("zc_copy")
    scene.play(Indicate(zc, color=MBUF_C, scale_factor=1.06), run_time=0.4)
    st.zc = zc

    # 53.26  "But what exactly is being PASSED?"  -- interrogate the arrow.
    q = T("?", TITLE_SIZE, PTR).move_to(ref.get_center() + UP * 0.5)
    scene.at("q_passed")
    scene.play(FadeIn(q, scale=1.3), FadeOut(ref_t), run_time=0.5)

    # 55.18  "The answer is an mBuff." The arrow's tail resolves into the mbuf.
    kb.to("THE mbuf", MBUF_C, run_time=0.5)
    mb = mbuf_card(840, 980)
    scene.at("an_mbuf")
    scene.play(FadeOut(q), FadeOut(zc, shift=UP * 0.2),
               ReplacementTransform(VGroup(ref.copy()), mb), FadeOut(ref), run_time=0.7)
    # re-anchor the pointer: it now leaves buf_addr and lands on the first byte.
    ptr = ptr_arrow(mb.addr_row.val.get_left() + LEFT * 0.08, buf.cells[0].get_right() + RIGHT * 0.05)
    scene.play(GrowArrow(ptr), run_time=0.5)
    st.buf, st.mbuf, st.ptr = buf, mb, ptr

    # 56.24  "a small METADATA structure ATTACHED to the packet."
    scene.at("mb_metadata")
    scene.play(Indicate(mb.title, color=MBUF_C, scale_factor=1.1), run_time=0.4)
    scene.at("mb_attached")
    scene.play(Indicate(ptr, color=PTR, scale_factor=1.05),
               Flash(buf.cells[0].get_center(), color=PTR, line_length=0.12,
                     num_lines=8, flash_radius=0.24), run_time=0.5)
    cap.show("metadata + a pointer — not the bytes", MBUF_C)

    # 60.40  "it CONTAINS ... LENGTH, PROTOCOL ... and the exact ADDRESS where the
    # PAYLOAD begins." Each field lights as it is named; buf_addr is the payoff.
    scene.at("mb_contains")
    scene.play(Indicate(mb.box, color=MBUF_C, scale_factor=1.03), run_time=0.4)
    scene.at("mb_length")
    scene.play(Indicate(mb.rows[0], color=MBUF_C, scale_factor=1.12), run_time=0.4)
    scene.at("mb_protocol")
    scene.play(Indicate(mb.rows[1], color=MBUF_C, scale_factor=1.12), run_time=0.4)
    scene.at("mb_exact")
    cap.clear(run_time=0.25)
    scene.at("mb_address")
    box_addr = SurroundingRectangle(mb.addr_row, color=PTR, buff=0.08, corner_radius=0.05,
                                    stroke_width=3.5).set_z_index(Z_CARD)
    scene.play(Create(box_addr),
               mb.addr_row.val.animate.scale(1.12).set_color(PTR), run_time=0.5)
    scene.at("mb_payload")
    scene.play(Indicate(ptr, color=PTR, scale_factor=1.06),
               Flash(buf.cells[0].get_center(), color=PTR, line_length=0.14,
                     num_lines=10, flash_radius=0.3), run_time=0.6)
    cap.show(f"buf_addr = {ADDR}  →  the first byte", PTR)
    st.addr_hi = box_addr


# ===========================================================================
# ACT 3 -- WHERE THE BYTES LIVE: THE MEMPOOL, AND DMA   (68.4 - 103.9 s)
#   "Now let's look at where those bytes live."
#   "Before any packet even arrives, DPDK allocates a large collection of
#    fixed-size packet buffers."  /  "This collection is called a mempool."
#   "...a warehouse filled with thousands of empty packet containers..."
#   "When the NIC receives a packet, it doesn't allocate new memory."
#   "Instead, the NIC uses DMA to stream the incoming bytes straight from the
#    wire directly into a free buffer in the mempool."
#   "no CPU involvement, no dynamic memory allocation, no unnecessary copies."
# ===========================================================================
def act_mempool(scene, st, kb, cap):
    # 68.39  "Now let's look at WHERE those bytes LIVE." Fold the mbuf/buffer away
    # and go to the memory it all comes from.
    cap.clear(run_time=0.4)
    scene.at("ml_now")
    scene.play(FadeOut(st.buf, scale=0.7), FadeOut(st.mbuf, scale=0.7),
               FadeOut(st.ptr), FadeOut(st.addr_hi),
               kb_hide(kb), run_time=0.6)

    # 70.66  "BEFORE any packet even arrives, DPDK ALLOCATES ... FIXED-SIZE packet
    # BUFFERS." The pool exists first -- that is the whole trick. It is preallocated.
    scene.at("ml_before")
    kb.to("THE MEMPOOL", MEM, run_time=0.45)
    pool = mempool(CXP, 900, cols=6, rows=4, slot=120, gap=18)
    pool.title.set_opacity(0.0)
    scene.at("ml_dpdk")
    dpdk = tag("DPDK · at startup", MBUF_C, TAG_T - 2).move_to(P(CXP, 560))
    scene.play(FadeIn(dpdk, shift=DOWN * 0.1), run_time=0.4)
    scene.at("ml_allocates")
    scene.play(LaggedStart(*[FadeIn(s, scale=0.6) for s in pool.slots],
                           lag_ratio=0.03), run_time=1.1)
    scene.at("ml_fixed")
    scene.play(LaggedStart(*[Indicate(s, color=MEM, scale_factor=1.1)
                             for s in pool.slots[:6]], lag_ratio=0.06), run_time=0.7)
    scene.at("ml_buffers")
    cap.show("every buffer identical · same fixed size", MEM)
    st.pool, st.dpdk = pool, dpdk

    # 78.33  "This collection is called a MEMPOOL."
    scene.at("mp_mempool")
    pool.title.set_opacity(1.0)
    ml = pill("mempool", MEM, MEM_BG, NODE_T - 2, h=76, glowing=True).move_to(P(CXP, 560))
    scene.play(FadeOut(dpdk), FadeIn(ml, scale=1.12), run_time=0.5)
    st.ml = ml

    # 80.43  "...a WAREHOUSE filled with THOUSANDS of empty CONTAINERS, all ready."
    scene.at("wh_warehouse")
    scene.play(Indicate(pool.slots, color=MEM, scale_factor=1.03), run_time=0.5)
    scene.at("wh_thousands")
    cap.clear(run_time=0.25)
    cap.show("thousands of empty buffers, waiting", MEM)
    scene.at("wh_containers")
    scene.play(Indicate(pool.slots, color=IDLE, scale_factor=1.02), run_time=0.5)

    # 85.24  "When the NIC RECEIVES a packet, it DOESN'T allocate NEW memory."
    # The NIC returns (green), and the naive move -- malloc a fresh buffer -- is
    # shown and immediately crossed out.
    cap.clear(run_time=0.3)
    scene.at("dm_when")
    kb.to("DMA — STRAIGHT TO MEMORY", NIC_C, run_time=0.5,
          extra=[FadeOut(ml, shift=UP * 0.2),
                 cam(scene, (CXP, 1000, 1.0)),
                 pool.animate.scale(0.62).move_to(P(CXP, 1180))])
    nic = node("NIC", "100 GbE", 320, 120, NIC_C, CXP, 470, tsize=NODE_T)
    scene.at("dm_nic")
    scene.play(FadeIn(nic, shift=DOWN * 0.15), run_time=0.45)
    scene.at("dm_new")
    malloc = tag("malloc() a new buffer?", KERN, TAG_T - 3).move_to(P(CXP, 700))
    malloc_x = cross(malloc.get_center(), s=120)
    scene.play(FadeIn(malloc), run_time=0.3)
    scene.play(Create(malloc_x), malloc.animate.set_opacity(0.4), run_time=0.45)

    # 88.76  "INSTEAD, the NIC uses DMA to STREAM the incoming bytes straight from
    # the WIRE directly into a FREE BUFFER." Yellow bytes fly off the wire and
    # land in exactly one slot -- which lights blue. The CPU never touched them.
    scene.at("dm_instead")
    scene.play(FadeOut(malloc), FadeOut(malloc_x), run_time=0.3)
    hot = 14
    target = pool.slots[hot]
    scene.at("dm_dma")
    dma_t = pill("DMA engine", PTR, PTR_BG, TAG_T, h=64, glowing=True).move_to(P(CXP, 690))
    scene.play(FadeIn(dma_t, scale=1.1), Indicate(nic, color=NIC_C, scale_factor=1.04),
               run_time=0.5)
    scene.at("dm_stream")
    stream = byte_cells(6, color=PTR).scale(0.8).move_to(P(CXP, 560))
    scene.play(FadeIn(stream, target_position=nic.get_bottom()), run_time=0.4)
    scene.at("dm_wire")
    path = ptr_arrow(P(CXP, 760), target.get_top() + UP * 0.05, sw=6)
    scene.play(GrowArrow(path), run_time=0.4)
    scene.at("dm_free")
    scene.play(stream.animate.scale(0.4).move_to(target.get_center()),
               run_time=0.5, rate_func=rush_from)
    scene.at("dm_buffer")
    scene.play(target.animate.set_stroke(PKT, 2.4).set_fill(PKT, 0.7),
               FadeOut(stream), FadeOut(path),
               Flash(target.get_center(), color=PKT, line_length=0.14, num_lines=12,
                     flash_radius=0.34), run_time=0.45)
    st.nic2, st.dma_t, st.hot = nic, dma_t, hot

    # 98.18  "NO CPU involvement, NO dynamic allocation, NO unnecessary copies."
    # Three denials, each struck through as it is spoken. This is the payoff of
    # the whole section, and every clause negates a cost the traditional path paid.
    denies = VGroup(
        M("CPU involvement", ROW_T, SUBTLE),
        M("dynamic allocation", ROW_T, SUBTLE),
        M("unnecessary copies", ROW_T, SUBTLE),
    ).arrange(DOWN, buff=U(28), aligned_edge=LEFT).move_to(P(CXP, 900))
    nos = VGroup(*[T("no", ROW_T, BAD).next_to(d, LEFT, buff=0.2) for d in denies])
    scene.play(FadeOut(st.dma_t), FadeOut(nic, shift=UP * 0.2),
               cam(scene, (CXP, 980, 1.0)), run_time=0.5)
    strikes = VGroup()
    for key, d, n in zip(("no_cpu", "no_dynamic", "no_copies"), denies, nos):
        scene.at(key)
        scene.play(FadeIn(n, scale=1.2), FadeIn(d, shift=RIGHT * 0.1), run_time=0.35)
        s = strike(VGroup(n, d), color=BAD)
        scene.play(Create(s), run_time=0.3)
        strikes.add(s)
    scene.at("no_copies_w")
    cap.show("the bytes are written exactly once", NIC_C)
    st.denies = VGroup(denies, nos, strikes)


def kb_hide(kb):
    """A no-op animation slot that also clears the keyword bar (so it can ride in
    a single play() call alongside other fades)."""
    if kb.mob is None:
        return Wait(0.01)
    m = kb.mob
    m.clear_updaters()
    kb.mob = None
    return FadeOut(m, shift=UP * 0.16)


# ===========================================================================
# ACT 4 -- PASSING THE HANDLE   (103.9 - 137.6 s)
#   "From this moment onward, every stage of packet processing works with the
#    same packet buffer."
#   "The parser / classifier / firewall / routing logic receives the same mBuff."
#   "Each component only receives a handle that points to the original buffer."
#   "The packet buffer never moves."
#   "Even if a router needs to modify a header ... it modifies the bytes in place."
#   "They're still sitting exactly where the NIC originally placed them."
# ===========================================================================
def act_pipeline(scene, st, kb, cap):
    # 103.95  "From this moment, every STAGE works with the SAME packet BUFFER."
    # Four stages down the left; the one filled buffer, pinned, on the right.
    cap.clear(run_time=0.3)
    scene.at("pl_from")
    kb.to("ONE BUFFER, MANY STAGES", MEM, run_time=0.5,
          extra=[FadeOut(st.denies, scale=0.85), FadeOut(st.pool, scale=0.6),
                 cam(scene, FULL_FRAME)])

    buf = packet_buffer(800, 980, n=6, w=330, h=170, glowing=True)
    buf.title.become(M("the one buffer", MONO_S, MEM).move_to(buf.title))
    scene.play(FadeIn(buf, scale=1.08), run_time=0.5)
    st.buf = buf

    stages = []
    names = [("PARSER", "s_parser"), ("CLASSIFIER", "s_classifier"),
             ("FIREWALL", "s_firewall"), ("ROUTING", "s_routing")]
    ys = [720, 920, 1120, 1320]
    for (nm, _), y in zip(names, ys):
        stages.append(node(nm, None, 300, 130, MBUF_C, 290, y, tsize=NODE_T - 4,
                           glowing=False))
    stage_grp = VGroup(*stages)
    scene.at("pl_stage")
    scene.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.12) for s in stages],
                           lag_ratio=0.15), run_time=0.9)
    scene.at("pl_same")
    scene.play(Indicate(buf.box, color=MEM, scale_factor=1.05), run_time=0.4)
    scene.at("pl_buffer")
    scene.play(Indicate(buf.cells, color=PKT, scale_factor=1.06), run_time=0.4)
    st.stages = stage_grp

    # 109.64  The mbuf handle visits each stage in turn. The chip moves; the yellow
    # pointer re-anchors its TAIL to the chip while its HEAD stays welded to the
    # buffer. Same buffer, four times. Nothing but the arrow ever moves.
    chip = pill("mbuf", MBUF_C, MBUF_BG, TAG_T, h=54, glowing=True)
    ptr = [None]

    def hand_to(stage, first=False):
        chip.generate_target()
        chip.target.next_to(stage, RIGHT, buff=0.16)
        tail = chip.target.get_right() + RIGHT * 0.05 if not first else chip.get_right()
        new_ptr = ptr_arrow(chip.target.get_right() + RIGHT * 0.05,
                            buf.box.get_left() + LEFT * 0.05)
        if first:
            chip.next_to(stage, RIGHT, buff=0.16)
            scene.add(chip)
            scene.play(FadeIn(chip, scale=1.1), GrowArrow(new_ptr),
                       Indicate(stage, color=MBUF_C, scale_factor=1.06), run_time=0.5)
        else:
            anims = [MoveToTarget(chip), Indicate(stage, color=MBUF_C, scale_factor=1.06)]
            if ptr[0] is not None:
                anims.append(ReplacementTransform(ptr[0], new_ptr))
            else:
                anims.append(GrowArrow(new_ptr))
            scene.play(*anims, run_time=0.5)
        ptr[0] = new_ptr

    scene.at("s_parser")
    hand_to(stages[0], first=True)
    scene.at("s_classifier")
    hand_to(stages[1])
    scene.at("s_firewall")
    hand_to(stages[2])
    scene.at("s_routing")
    hand_to(stages[3])
    st.chip, st.ptr = chip, ptr[0]
    cap.show("the same mbuf, handed down the chain", MBUF_C)

    # 119.24  "EACH component only receives a HANDLE that POINTS to the ORIGINAL
    # buffer." Freeze the truth of it: four faint pointers, from every stage at
    # once, all landing on the one buffer.
    scene.at("pl_each")
    fan = VGroup(*[ptr_arrow(s.get_right() + RIGHT * 0.05, buf.box.get_left() + LEFT * 0.05,
                             sw=3).set_opacity(0.55) for s in stages])
    cap.clear(run_time=0.2)
    scene.at("pl_handle")
    scene.play(FadeOut(st.chip), FadeOut(st.ptr), run_time=0.3)
    scene.play(LaggedStart(*[GrowArrow(a) for a in fan], lag_ratio=0.1), run_time=0.8)
    scene.at("pl_points")
    scene.play(Flash(buf.box.get_left(), color=PTR, line_length=0.16, num_lines=12,
                     flash_radius=0.4), run_time=0.5)
    scene.at("pl_original")
    scene.play(Indicate(buf.addr, color=PTR, scale_factor=1.15), run_time=0.5)
    st.fan = fan

    # 124.23  "The packet buffer NEVER MOVES." A lock, and the buffer refuses a
    # nudge -- it shakes and snaps back. The address label does not so much as flicker.
    scene.at("nm_never")
    lock = tag("pinned · never moves", MEM, TAG_T - 2).next_to(buf, DOWN, buff=0.2)
    scene.play(FadeIn(lock, shift=UP * 0.1), run_time=0.35)
    scene.at("nm_moves")
    scene.play(Wiggle(buf.box, scale_value=1.02, rotation_angle=0.015 * TAU), run_time=0.7)
    st.lock = lock

    # 126.63  "Even if a ROUTER MODIFIES a HEADER or ADDRESS, it modifies the bytes
    # right there IN PLACE." Two byte cells (the header) flip colour where they sit.
    # The router reaches in along the pointer; nothing is copied out.
    scene.at("ip_router")
    scene.play(Indicate(stages[3], color=MBUF_C, scale_factor=1.06),
               FadeOut(st.fan[:3]), st.fan[3].animate.set_opacity(1.0), run_time=0.5)
    scene.at("ip_modify")
    cap.clear(run_time=0.2)
    cap.show("rewrites the bytes where they already are", KERN)
    scene.at("ip_header")
    hdr = VGroup(buf.cells[0], buf.cells[1])
    scene.play(hdr.animate.set_color(KERN).set_fill(KERN, 0.85), run_time=0.4)
    scene.at("ip_address")
    scene.play(Indicate(hdr, color=KERN, scale_factor=1.12), run_time=0.5)
    scene.at("ip_place")
    scene.play(Flash(hdr.get_center(), color=KERN, line_length=0.12, num_lines=10,
                     flash_radius=0.28),
               buf.box.animate.set_stroke(MEM, 2.6), run_time=0.5)

    # 133.83  "still sitting EXACTLY where the NIC originally PLACED them."  The
    # address is the proof: it never changed.
    scene.at("ip_exactly")
    scene.play(Indicate(buf.addr, color=PTR, scale_factor=1.18),
               Circumscribe(buf.addr, color=PTR, buff=0.06, run_time=0.9), run_time=0.9)
    scene.at("ip_nic")
    cap.show(f"same address, start to finish: {ADDR}", PTR)


# ===========================================================================
# ACT 5 -- THE KEY IDEA, AND WHY A POINTER WINS   (137.6 - 168.1 s)
#   "This is the key idea behind zero copy."
#   "The packet isn't travelling through the system."  /  "Only the pointer is."
#   "Passing a pointer is incredibly cheap."
#   "It's typically just an 8-byte memory address on a 64-bit system compared to
#    copying hundreds or even thousands of bytes ... for every packet."
#   "Now imagine processing millions of packets every second."
#   "If every packet required multiple memory copies, the CPU would spend most of
#    its time moving bytes instead of making forwarding decisions."
# ===========================================================================
def act_cheap(scene, st, kb, cap):
    # 137.61  name the idea, and strip back to just buffer + one pointer.
    cap.clear(run_time=0.3)
    scene.at("ky_key")
    kb.to("THE KEY IDEA", MBUF_C, run_time=0.5,
          extra=[FadeOut(st.stages, scale=0.8), FadeOut(st.lock),
                 FadeOut(st.fan[3])])
    scene.at("ky_idea")
    # restore the header colour and settle the buffer at centre
    scene.play(VGroup(st.buf.cells[0], st.buf.cells[1]).animate.set_color(PKT).set_fill(PKT, 0.85),
               st.buf.animate.move_to(P(CXP, 1050)), run_time=0.6)

    # 140.64  "The packet isn't TRAVELLING." The bytes hold dead still while a lone
    # yellow pointer loops around them -- the literal picture of the thesis.
    scene.at("ky_travelling")
    still = tag("bytes: not moving", PKT, TAG_T - 2).next_to(st.buf, DOWN, buff=0.22)
    scene.play(FadeIn(still, shift=UP * 0.08), run_time=0.4)
    scene.at("ky_only")
    p = ptr_arrow(P(CXP - 40, 700), st.buf.box.get_top() + UP * 0.05)
    scene.play(GrowArrow(p), run_time=0.4)
    scene.at("ky_pointer")
    # the pointer orbits the (motionless) buffer -- the literal picture of the thesis
    scene.play(Rotate(p, angle=TAU, about_point=st.buf.box.get_center()),
               run_time=1.1, rate_func=smooth)
    scene.play(FadeOut(still), run_time=0.3)
    st.loop_ptr = p

    # 143.70  "Passing a pointer is incredibly CHEAP." Side by side, honestly to
    # scale in spirit: 8 bytes of address versus a 1500-byte frame.
    scene.at("ch_passing")
    kb.to("8 BYTES vs 1500", PTR, run_time=0.5,
          extra=[FadeOut(st.buf, scale=0.8), FadeOut(st.loop_ptr)])
    scene.at("ch_cheap")
    small = VGroup(byte_cells(8, cw=30, ch=44, color=PTR),
                   M(f"{ADDR}", MONO_S, PTR)).arrange(DOWN, buff=U(14))
    small_lab = T("8 bytes", ROW_T, PTR).next_to(small, UP, buff=0.2)
    smallg = VGroup(small_lab, small).move_to(P(300, 980))
    scene.play(FadeIn(smallg, scale=1.1), run_time=0.5)

    # 147.01  "an 8-BYTE address on a 64-BIT system"
    scene.at("ch_8byte")
    scene.play(Indicate(small[0], color=PTR, scale_factor=1.1), run_time=0.4)
    scene.at("ch_64bit")
    scene.play(Flash(small[1].get_center(), color=PTR, line_length=0.1, num_lines=8,
                     flash_radius=0.24), run_time=0.4)

    # 150.77  "COMPARED to copying HUNDREDS or THOUSANDS of bytes"
    scene.at("ch_copying")
    big_cells = VGroup(*[RoundedRectangle(width=U(22), height=U(30), corner_radius=U(2),
                                          stroke_color=PKT, stroke_width=0.8,
                                          fill_color=PKT, fill_opacity=0.8)
                         for _ in range(60)]).arrange_in_grid(rows=6, cols=10, buff=U(4))
    big_lab = T("1500 bytes", ROW_T, PKT).next_to(big_cells, UP, buff=0.2)
    bigg = VGroup(big_lab, big_cells).move_to(P(800, 980))
    vs = T("vs", NODE_T, IDLE).move_to(P(CXP, 980))
    scene.at("ch_hundreds")
    scene.play(FadeIn(vs), FadeIn(bigg, scale=1.05), run_time=0.5)
    scene.at("ch_thousands")
    scene.play(Indicate(big_cells, color=PKT, scale_factor=1.03),
               Flash(bigg.get_center(), color=PKT, line_length=0.2, num_lines=16,
                     flash_radius=0.6), run_time=0.6)
    cap.show("copy 1500 bytes — or move an 8-byte pointer", PTR)
    st.cheap = VGroup(smallg, bigg, vs)

    # 155.94  "Now imagine MILLIONS of packets every SECOND." A counter, spinning.
    scene.at("mi_now")
    kb.to("MILLIONS PER SECOND", BAD, run_time=0.5,
          extra=[FadeOut(st.cheap, scale=0.85)])
    counter = VGroup(T("148,800,000", TITLE_SIZE - 8, INK, font=MN),
                     M("packets / second", MONO_S + 2, SUBTLE)).arrange(DOWN, buff=0.18) \
        .move_to(P(CXP, 720))
    scene.at("mi_millions")
    scene.play(FadeIn(counter[0], scale=1.1), run_time=0.4)
    scene.at("mi_second")
    scene.play(FadeIn(counter[1]), Flash(counter.get_center(), color=BAD, line_length=0.2,
                                         num_lines=16, flash_radius=0.7), run_time=0.5)
    st.counter = counter

    # 159.53  "If every packet required copies, the CPU would spend most of its
    # TIME MOVING BYTES instead of FORWARDING." A single bar of the core's time:
    # almost all of it red (memcpy), a sliver blue (the actual work).
    core = box(560, 120, KERN, fill=SURF2, r=0.1, sw=2.6).move_to(P(CXP, 1080))
    core_t = M("one CPU core · its time", MONO_S, KERN).next_to(core, UP, buff=U(10))
    scene.at("if_cpu")
    scene.play(FadeIn(core), FadeIn(core_t), FadeOut(st.counter, scale=0.85), run_time=0.45)

    # the core's time as one bar: red = the bytes it is busy copying, blue sliver =
    # the actual forwarding work. Plain rectangles (not rounded) grown from an edge,
    # so a width tween can never fold into an hourglass.
    scene.at("if_moving")
    moving = Rectangle(width=U(560) * 0.80, height=U(104), stroke_width=0,
                       fill_color=BAD, fill_opacity=0.85)
    moving.move_to(core.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.07).set_z_index(Z_NODE)
    mv_tag = tag("moving bytes", BAD, TAG_T - 3).move_to(P(420, 1080))
    scene.play(GrowFromEdge(moving, LEFT), FadeIn(mv_tag), run_time=0.6)
    scene.at("if_forwarding")
    fwd = Rectangle(width=U(560) * 0.16, height=U(104), stroke_width=0,
                    fill_color=PKT, fill_opacity=0.85)
    fwd.move_to(core.get_right(), aligned_edge=RIGHT).shift(LEFT * 0.07).set_z_index(Z_NODE)
    fwd_t = tag("forwarding", PKT, TAG_T - 3).move_to(P(770, 1180))
    scene.play(GrowFromEdge(fwd, RIGHT), FadeIn(fwd_t, shift=LEFT * 0.1), run_time=0.4)
    cap.show("the work drowns under the copies", BAD)
    st.moving, st.fwd = moving, fwd
    st.core = VGroup(core, core_t, moving, fwd, mv_tag, fwd_t)


# ===========================================================================
# ACT 6 -- THE PAYOFF   (168.1 - 183.9 s)
#   "By eliminating those copies, zero copy dramatically reduces CPU overhead,
#    lowers memory bandwidth usage, improves cache efficiency, and enables
#    applications like DPDK to achieve tens or even hundreds of gigabits per
#    second on modern hardware."
# ===========================================================================
def act_payoff(scene, st, kb, cap):
    # 168.06  "BY ELIMINATING those copies" -- the red time is reclaimed. The bar
    # collapses back to a sliver; the core is free.
    cap.clear(run_time=0.3)
    scene.at("po_by")
    kb.to("THE PAYOFF", NIC_C, run_time=0.5)
    # the red "moving bytes" region collapses and the blue "forwarding" bar grows to
    # fill it -- the core's time flips from copying to real work.
    core_box = st.core[0]
    red_small = Rectangle(width=U(560) * 0.12, height=U(104), stroke_width=0,
                          fill_color=BAD, fill_opacity=0.85)
    red_small.move_to(core_box.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.07) \
        .set_z_index(Z_NODE)
    anims = [Transform(st.moving, red_small)]
    if getattr(st, "fwd", None) is not None:
        blue_big = Rectangle(width=U(560) * 0.82, height=U(104), stroke_width=0,
                             fill_color=PKT, fill_opacity=0.85)
        blue_big.move_to(core_box.get_right(), aligned_edge=RIGHT).shift(LEFT * 0.07) \
            .set_z_index(Z_NODE)
        anims.append(Transform(st.fwd, blue_big))
    scene.play(*anims, run_time=0.6)

    # three benefit chips, one per clause, then the throughput gauge.
    chips = [("↓  CPU overhead", "po_reduces", KERN),
             ("↓  memory bandwidth", "po_lowers", MEM),
             ("↑  cache efficiency", "po_improves", PKT)]
    ys = [720, 850, 980]
    built = []
    for (txt, key, col), y in zip(chips, ys):
        scene.at(key)
        c = pill(txt, col, SURF2, TAG_T, h=68, glowing=True).move_to(P(CXP, y))
        scene.play(FadeIn(c, shift=RIGHT * 0.12), run_time=0.45)
        built.append(c)

    # 178.31  "applications like DPDK ... TENS or HUNDREDS of GIGABITS per second."
    scene.at("po_dpdk")
    dpdk = pill("DPDK", MBUF_C, MBUF_BG, NODE_T - 2, h=76, glowing=True).move_to(P(CXP, 1160))
    scene.play(FadeIn(dpdk, scale=1.12), run_time=0.4)
    gauge_bg = box(560, 60, IDLE, fill=SURF2, r=0.3, sw=2.0).move_to(P(CXP, 1330))
    gfill = Rectangle(width=U(560) * 0.45, height=U(46), stroke_width=0,
                      fill_color=NIC_C, fill_opacity=0.9)
    gfill.move_to(gauge_bg.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.07).set_z_index(Z_NODE)
    scene.at("po_tens")
    scene.play(FadeIn(gauge_bg), run_time=0.35)
    scene.play(GrowFromEdge(gfill, LEFT), run_time=0.5)
    scene.at("po_gigabits")
    gfill_full = Rectangle(width=U(560) * 0.95, height=U(46), stroke_width=0,
                           fill_color=NIC_C, fill_opacity=0.9)
    gfill_full.move_to(gauge_bg.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.07) \
        .set_z_index(Z_NODE)
    num = T("100+ Gb/s", NODE_T, NIC_C).move_to(P(CXP, 1440))
    scene.play(Transform(gfill, gfill_full), FadeIn(num, scale=1.15),
               Flash(P(CXP, 1330), color=NIC_C, line_length=0.2, num_lines=16,
                     flash_radius=0.7), run_time=0.6)
    scene.at("po_hardware")
    cap.show("line rate, on ordinary hardware", NIC_C)
    st.payoff = VGroup(st.core, *built, dpdk, gauge_bg, gfill, num)


# ===========================================================================
# ACT 7 -- TRANSMIT, AND RECYCLE   (183.9 - 197.4 s)
#   "Finally, when packet processing is complete, the NIC transmits the packet
#    using the exact same memory buffer."
#   "After transmission, that buffer is returned to the mempool, ready to be
#    reused for the next incoming packet."
# ===========================================================================
def act_tx(scene, st, kb, cap):
    # 183.94  the same buffer, one more time -- out to the wire.
    cap.clear(run_time=0.3)
    scene.at("tx_finally")
    kb.to("TRANSMIT — SAME BYTES", NIC_C, run_time=0.5,
          extra=[FadeOut(st.payoff, scale=0.85)])
    buf = packet_buffer(CXP, 1050, n=6, w=340, h=170, glowing=True)
    nic = node("NIC", "tx", 300, 120, NIC_C, CXP, 560, tsize=NODE_T)
    scene.at("tx_complete")
    scene.play(FadeIn(nic, shift=DOWN * 0.12), FadeIn(buf, scale=1.05), run_time=0.6)
    st.buf, st.nic = buf, nic

    # 186.80  "the NIC TRANSMITS the packet using the EXACT SAME buffer." The
    # pointer, not the bytes, is what the NIC is handed. The bytes go on the wire
    # straight from where they have sat the whole time.
    scene.at("tx_nic")
    scene.play(Indicate(nic, color=NIC_C, scale_factor=1.05), run_time=0.4)
    scene.at("tx_transmits")
    p = ptr_arrow(buf.box.get_top() + UP * 0.05, nic.get_bottom() + DOWN * 0.05)
    scene.play(GrowArrow(p), run_time=0.45)
    wire = byte_cells(6, color=PKT).scale(0.6).move_to(buf.cells.get_center())
    scene.add(wire)
    scene.at("tx_same")
    scene.play(wire.animate.move_to(P(CXP, 400)).scale(0.7), run_time=0.7, rate_func=rush_from)
    scene.at("tx_buffer")
    scene.play(FadeOut(wire), Indicate(buf.addr, color=PTR, scale_factor=1.12), run_time=0.4)
    st.tx_ptr = p

    # 191.15  "AFTER transmission, that buffer is RETURNED to the MEMPOOL, ready to
    # be REUSED for the NEXT packet." The whole point of a pool: the buffer flies
    # home to its slot, empties, and is available again. No free(), no churn.
    scene.at("rc_after")
    pool = mempool(CXP, 1400, cols=6, rows=2, slot=90, gap=14, hot=8)
    scene.play(FadeOut(p), FadeIn(pool, shift=UP * 0.1),
               cam(scene, (CXP, 1050, 1.05)), run_time=0.6)
    scene.at("rc_returned")
    scene.play(buf.animate.scale(0.28).move_to(pool.slots[8].get_center()),
               FadeOut(nic, shift=UP * 0.2), run_time=0.8, rate_func=rush_from)
    scene.at("rc_mempool")
    scene.play(FadeOut(buf),
               pool.slots[8].animate.set_stroke(NIC_C, 2.4).set_fill(NIC_C, 0.35),
               Flash(pool.slots[8].get_center(), color=NIC_C, line_length=0.12,
                     num_lines=10, flash_radius=0.3), run_time=0.5)
    scene.at("rc_reused")
    scene.play(pool.slots[8].animate.set_stroke(IDLE, 1.8).set_fill(SURF2, 1.0), run_time=0.4)
    scene.at("rc_next")
    scene.play(Indicate(pool.slots, color=MEM, scale_factor=1.03), run_time=0.5)
    cap.show("allocated once · reused forever", MEM)
    st.pool = pool


# ===========================================================================
# ACT 8 -- THE RECAP, AND THE THESIS   (197.4 - end)
#   "The packet buffer was allocated only once."  /  "It was never copied."
#   "Only the mBuff, the handle to that data, was passed from one component to
#    another."
#   "...a packet is best thought of not as a collection of bytes, but as a
#    pointer to those bytes."
#   "And that's the essence of zero copy."
# ===========================================================================
def act_recap(scene, st, kb, cap):
    cap.clear(run_time=0.3)
    scene.at("rp_allocated")
    kb.to("WHAT ACTUALLY HAPPENED", MBUF_C, run_time=0.5,
          extra=[FadeOut(st.pool, scale=0.85), cam(scene, FULL_FRAME)])

    # two one-line receipts, ticked as spoken.  (k_line opens the line, k_tick
    # lands the check-mark.)
    lines = [
        ("rp_allocated", "buffer allocated", "rp_once", NIC_C),
        ("rp_never", "never copied", "rp_copied", NIC_C),
    ]
    ys = [700, 850]
    made = []
    for (k_line, txt, k_tick, col), y in zip(lines, ys):
        scene.at(k_line)
        row = M(txt, ROW_T, INK).move_to(P(CXP, y))
        scene.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.4)
        scene.at(k_tick)
        ck = check(row.get_left() + LEFT * 0.4, s=54, color=col)
        scene.play(Create(ck), run_time=0.35)
        made.append(VGroup(row, ck))

    # 201.69  "ONLY the mBuff, the HANDLE, was PASSED." The mbuf chip slides across
    # a faint stage row -- the only thing that ever moved.
    scene.at("rp_only")
    line3 = M("only the mbuf was passed", ROW_T, INK).move_to(P(CXP, 1000))
    scene.play(FadeIn(line3, shift=RIGHT * 0.1), run_time=0.4)
    chip = pill("mbuf", MBUF_C, MBUF_BG, TAG_T - 2, h=50, glowing=True).move_to(P(260, 1120))
    scene.at("rp_mbuf")
    scene.play(FadeIn(chip, scale=1.1), run_time=0.35)
    scene.at("rp_handle")
    trail = ptr_arrow(P(260, 1180), P(820, 1180), sw=5).set_opacity(0.6)
    scene.play(GrowArrow(trail), run_time=0.4)
    scene.at("rp_passed")
    scene.play(chip.animate.move_to(P(820, 1120)), run_time=0.9, rate_func=rush_from)
    st.recap = VGroup(*made, line3, chip, trail)

    # 207.04  THE THESIS. A blue block of bytes labelled "packet". We strike out
    # "= bytes" and reveal "= a pointer" (yellow). Everything the film built,
    # in one substitution.
    scene.at("fn_thats")
    kb.to("A PACKET IS…", PTR, run_time=0.5, extra=[FadeOut(st.recap, scale=0.85)])
    bytes_block = VGroup(byte_cells(6, cw=44, ch=64, color=PKT),
                         M("the bytes", MONO_S, PKT)).arrange(DOWN, buff=U(12)) \
        .move_to(P(CXP, 800))
    scene.at("fn_packet")
    scene.play(FadeIn(bytes_block, scale=1.08), run_time=0.5)
    eq1 = T("packet  =  a pile of bytes", NODE_T - 4, INK).move_to(P(CXP, 1050))
    scene.at("fn_not")
    scene.play(FadeIn(eq1), run_time=0.4)
    scene.at("fn_bytes1")
    scene.play(Create(strike(eq1[-11:] if len(eq1) > 11 else eq1, color=BAD)),
               run_time=0.45)
    # the substitution: bytes -> pointer
    scene.at("fn_pointer")
    eq2 = T("packet  =  a pointer", NODE_T - 2, PTR).move_to(P(CXP, 1200))
    arrow = ptr_arrow(P(CXP, 1120), bytes_block.get_bottom() + DOWN * 0.05)
    scene.play(FadeIn(eq2, shift=UP * 0.1), GrowArrow(arrow),
               Flash(P(CXP, 1200), color=PTR, line_length=0.16, num_lines=12,
                     flash_radius=0.5), run_time=0.6)
    scene.at("fn_bytes2")
    scene.play(Indicate(bytes_block[0], color=PKT, scale_factor=1.05),
               Indicate(eq2, color=PTR, scale_factor=1.04), run_time=0.6)
    st.thesis = VGroup(bytes_block, eq1, eq2, arrow)

    # 215.81  "And that's the ESSENCE of ZERO COPY."
    scene.at("es_and")
    scene.play(FadeOut(st.thesis, scale=0.85), kb_hide(kb), run_time=0.5)
    scene.at("es_essence")
    zc = pill("ZERO COPY", MBUF_C, MBUF_BG, TITLE_SIZE - 18, h=130, glowing=True) \
        .move_to(P(CXP, 900))
    sub = M("move the pointer, not the bytes", MONO_S + 3, SUBTLE).next_to(zc, DOWN, buff=0.3)
    scene.play(FadeIn(zc, scale=1.15), run_time=0.5)
    scene.at("es_zero")
    scene.play(FadeIn(sub, shift=UP * 0.1),
               Flash(zc.get_center(), color=MBUF_C, line_length=0.24, num_lines=18,
                     flash_radius=0.9), run_time=0.6)
    st.zc_final = VGroup(zc, sub)


# ===========================================================================
# OUTRO / CTA  (past the audio)
# ===========================================================================
def act_outro(scene, st):
    scene.wait(0.6)
    scene.play(FadeOut(st.zc_final, scale=0.85), run_time=0.6)
    set_cam(scene, FULL_FRAME)

    row = VGroup(T("Axio", TITLE_SIZE + 10, MBUF_C),
                 T("Byte", TITLE_SIZE + 10, KERN)).arrange(RIGHT, buff=0.03)
    sysx = T("SYSTEMS", ROW_T + 8, IDLE, font=MN).next_to(row, DOWN, buff=0.14)
    brand = VGroup(row, sysx).move_to(P(CXP, 640))

    head = T("High-Performance Data Plane", NODE_T + 2, INK).move_to(P(CXP, 900))
    if head.width > 9.2:
        head.scale_to_fit_width(9.2)
    sub = T("systems, from first principles", CAP_SIZE, IDLE, bold=False).move_to(P(CXP, 980))
    dl = Line(LEFT * 1.6, ORIGIN, color=MBUF_C, stroke_width=4).move_to(P(CXP - 80, 1055))
    dr = Line(ORIGIN, RIGHT * 1.6, color=KERN, stroke_width=4).move_to(P(CXP + 80, 1055))

    cta = pill("Follow  @axiobyte.systems", MBUF_C, MBUF_BG, NODE_T, h=110, glowing=True) \
        .move_to(P(CXP, 1230))
    recap = VGroup(T("this episode ↑", CAP_SIZE + 2, PTR),
                   T("a packet is just a pointer", CAP_SIZE, INK, bold=False)) \
        .arrange(RIGHT, buff=0.25).move_to(P(CXP, 1410))
    if recap.width > 9.4:
        recap.scale_to_fit_width(9.4)

    scene.play(FadeIn(brand, shift=DOWN * 0.2), run_time=0.65)
    scene.play(FadeIn(head, shift=UP * 0.1), FadeIn(sub, shift=UP * 0.1), run_time=0.55)
    scene.play(Create(dl), Create(dr), run_time=0.4)
    scene.play(FadeIn(cta, scale=1.06), run_time=0.55)
    scene.play(FadeIn(recap, shift=UP * 0.1), run_time=0.45)
    scene.wait(1.8)


# ===========================================================================
# THE FILM
# ===========================================================================
class FullVideo(VOScene):
    """The full voiceover-synced cut. Every beat is cued to timeline.json."""

    epoch = 0.0

    def construct(self):
        self.camera.background_color = BG
        _add_voiceover(self)
        st = Stage()
        kb, cap = KeywordBar(self), CaptionBar(self)

        act_hook(self, st, kb, cap)             #   0.0 -  14.6
        act_traditional(self, st, kb, cap)      #  14.6 -  42.4
        act_zerocopy_intro(self, st, kb, cap)   #  42.4 -  68.4
        act_mempool(self, st, kb, cap)          #  68.4 - 103.9
        act_pipeline(self, st, kb, cap)         # 103.9 - 137.6
        act_cheap(self, st, kb, cap)            # 137.6 - 168.1
        act_payoff(self, st, kb, cap)           # 168.1 - 183.9
        act_tx(self, st, kb, cap)               # 183.9 - 197.4
        act_recap(self, st, kb, cap)            # 197.4 - end
        act_outro(self, st)                     # past the audio


# ===========================================================================
# ACT PREVIEWS  -- iterate on one act without sitting through the film.
# Each rebuilds (instantly) the minimum state its act inherits, then shifts
# `epoch` so the act starts near t=0.
# ===========================================================================
class _Preview(VOScene):
    start = 0.0

    def construct(self):
        self.camera.background_color = BG
        self.epoch = self.start
        self.st = Stage()
        self.kb, self.cap = KeywordBar(self), CaptionBar(self)
        set_cam(self, FULL_FRAME)
        self.body()

    def body(self):
        raise NotImplementedError


class PrevTrad(_Preview):
    start = CUE["tr_thats"] - 1.0

    def body(self):
        # act_traditional expects st.hook to exist to fade out.
        self.st.hook = VGroup(Dot(radius=0.001).set_opacity(0))
        self.add(self.st.hook)
        act_traditional(self, self.st, self.kb, self.cap)


class PrevMbuf(_Preview):
    start = CUE["hp_high"] - 1.2

    def body(self):
        self.st.copychain = VGroup(Dot(radius=0.001).set_opacity(0))
        self.st.meters = VGroup(Dot(radius=0.001).set_opacity(0))
        self.add(self.st.copychain, self.st.meters)
        act_zerocopy_intro(self, self.st, self.kb, self.cap)


class PrevPool(_Preview):
    start = CUE["ml_now"] - 1.2

    def body(self):
        self.st.buf = packet_buffer(360, 980, glowing=True)
        self.st.mbuf = mbuf_card(840, 980)
        self.st.ptr = ptr_arrow(self.st.mbuf.addr_row.val.get_left() + LEFT * 0.08,
                                self.st.buf.cells[0].get_right() + RIGHT * 0.05)
        self.st.addr_hi = SurroundingRectangle(self.st.mbuf.addr_row, color=PTR,
                                               buff=0.08, stroke_width=3.5)
        self.add(self.st.buf, self.st.mbuf, self.st.ptr, self.st.addr_hi)
        self.kb._pin(self.kb._build("THE mbuf", MBUF_C))
        self.add(self.kb.mob)
        act_mempool(self, self.st, self.kb, self.cap)


class PrevPipe(_Preview):
    start = CUE["pl_from"] - 1.2

    def body(self):
        self.st.denies = VGroup(Dot(radius=0.001).set_opacity(0))
        self.st.pool = mempool(CXP, 1180, cols=6, rows=4, slot=74, gap=12, hot=14).scale(0.62)
        self.add(self.st.denies, self.st.pool)
        act_pipeline(self, self.st, self.kb, self.cap)


class PrevCheap(_Preview):
    start = CUE["ky_key"] - 1.2

    def body(self):
        self.st.buf = packet_buffer(800, 980, glowing=True)
        self.st.stages = VGroup(*[node(n, None, 300, 130, MBUF_C, 290, y, glowing=False)
                                  for n, y in zip(("PARSER", "CLASSIFIER", "FIREWALL", "ROUTING"),
                                                  (720, 920, 1120, 1320))])
        self.st.lock = tag("pinned", MEM).next_to(self.st.buf, DOWN, buff=0.2)
        # act_pipeline leaves only the routing (fan[3]) pointer live entering act_cheap
        self.st.fan = VGroup(*[ptr_arrow(s.get_right(), self.st.buf.box.get_left())
                               for s in self.st.stages])
        self.add(self.st.buf, self.st.stages, self.st.lock, self.st.fan[3])
        act_cheap(self, self.st, self.kb, self.cap)


class PrevClose(_Preview):
    start = CUE["po_by"] - 1.2

    def body(self):
        core = box(560, 120, KERN, fill=SURF2, r=0.1, sw=2.6).move_to(P(CXP, 1080))
        core_t = M("one CPU core · its time", MONO_S, KERN).next_to(core, UP, buff=U(10))
        moving = Rectangle(width=U(560) * 0.80, height=U(104), stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        moving.move_to(core.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.07).set_z_index(Z_NODE)
        fwd = Rectangle(width=U(560) * 0.16, height=U(104), stroke_width=0,
                        fill_color=PKT, fill_opacity=0.85)
        fwd.move_to(core.get_right(), aligned_edge=RIGHT).shift(LEFT * 0.07).set_z_index(Z_NODE)
        self.st.moving, self.st.fwd = moving, fwd
        self.st.core = VGroup(core, core_t, moving, fwd)
        self.st.counter = VGroup(Dot(radius=0.001).set_opacity(0))
        self.add(self.st.core, self.st.counter)
        act_payoff(self, self.st, self.kb, self.cap)
        act_tx(self, self.st, self.kb, self.cap)
        act_recap(self, self.st, self.kb, self.cap)
        act_outro(self, self.st)


# ===========================================================================
# STILL LAYOUT CHECKS -- one frame, no timing.  manim -sqh ep02_video.py <Name>
# ===========================================================================
class StillCopyChain(Scene):
    def construct(self):
        self.camera.background_color = BG
        nic = node("NIC", "off the wire", 300, 120, NIC_C, 300, 430)
        a = packet_buffer(300, 720, title="buffer A")
        b = packet_buffer(300, 1060, title="buffer B")
        c = packet_buffer(300, 1400, title="buffer C  (tx)")
        self.add(nic, a, b, c,
                 vlink(P(300, 800), P(300, 980), color=BAD, sw=6),
                 vlink(P(300, 1140), P(300, 1320), color=BAD, sw=6),
                 cost_meter("CPU cycles", 820, 720), cost_meter("memory bandwidth", 820, 880),
                 cost_meter("cache", 820, 1040),
                 T("TRADITIONAL PATH", KEY_SIZE, BAD).move_to(P(CXP, 150)))


class StillMbuf(Scene):
    def construct(self):
        self.camera.background_color = BG
        buf = packet_buffer(360, 980, glowing=True)
        mb = mbuf_card(840, 980)
        p = ptr_arrow(mb.addr_row.val.get_left() + LEFT * 0.08,
                      buf.cells[0].get_right() + RIGHT * 0.05)
        self.add(buf, mb, p, T("THE mbuf", KEY_SIZE, MBUF_C).move_to(P(CXP, 150)))


class StillMempool(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(mempool(CXP, 950, cols=6, rows=5, slot=120, gap=18, hot=14),
                 T("THE MEMPOOL", KEY_SIZE, MEM).move_to(P(CXP, 200)))


class StillPipeline(Scene):
    def construct(self):
        self.camera.background_color = BG
        buf = packet_buffer(800, 980, glowing=True)
        stages = [node(n, None, 300, 130, MBUF_C, 290, y, glowing=False)
                  for n, y in zip(("PARSER", "CLASSIFIER", "FIREWALL", "ROUTING"),
                                  (720, 920, 1120, 1320))]
        fan = [ptr_arrow(s.get_right() + RIGHT * 0.05, buf.box.get_left() + LEFT * 0.05, sw=3)
               for s in stages]
        self.add(buf, *stages, *fan,
                 T("ONE BUFFER, MANY STAGES", KEY_SIZE, MEM).move_to(P(CXP, 200)))
