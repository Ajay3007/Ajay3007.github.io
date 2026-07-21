"""
BLOCKS -- Internal Liquidity / Order Block / Breaker Block / Rejection Block.
9:16 portrait, voiceover-synced.

Render (video): manim -pqh blocks.py FullVideo
Render (still): manim -sqh blocks.py StillFrame

Preview a single section (cues are shifted so each starts near t=0):
    manim -pqh blocks.py HookScene        # "why does the market respect THIS candle?"
    manim -pqh blocks.py RoadmapScene     # the four concepts
    manim -pqh blocks.py LiquidityScene   # internal liquidity -> the sweep
    manim -pqh blocks.py OrderBlockScene  # bearish OB, then the bullish mirror
    manim -pqh blocks.py BreakerScene     # the break -> the role change
    manim -pqh blocks.py RejectionScene   # the spike, the rejection, the return
    manim -pqh blocks.py RecapScene       # the four zones, side by side

--------------------------------------------------------------------------
THE ONE RULE  (inherited from ema_full / double_ema_rsi / ema_macd / liquidity)
--------------------------------------------------------------------------
In the sibling videos the indicators are COMPUTED FROM THE CANDLE CLOSES, never
hand-drawn, so a line cannot drift away from the price it describes. This film
has no indicator -- its subject IS the raw structure -- so the rule is enforced
one level down: every zone is DERIVED FROM THE OHLC TABLE and asserted at import
by _verify_structure().

  * the internal highs are equal     -- high[4]  == high[7] == 88.0 exactly
  * the internal lows are equal      -- low[5]   == low[8]  == 80.0 exactly
  * nothing pierces them early       -- max(high[:11]) == 88.0
  * the sweep really sweeps          -- high[11] == 92.4, and it CLOSES above
  * the order block really is the
    last bullish candle before the
    drop                             -- close[12] > open[12], bars 13..17 all red
  * the breaker really breaks        -- close[23] (95.0) > high[12] (94.0)
  * the old resistance really holds  -- low[25] re-enters the zone, low[26] holds
                                        above it, close[27] rallies away
  * the rejection really rejects     -- bar 29's upper wick is 6.6x its body
  * it really explodes away          -- close[30] < low[29]
  * price really returns to it       -- high[36] lands INSIDE the rejection zone
                                        and closes back below it
  * the rejection high is never
    exceeded                         -- max(high) == high[29] == 114.0

If you edit BARS, every zone, ring and label follows automatically -- and the
import fails loudly if the edit breaks the story.

--------------------------------------------------------------------------
ONE CHART, FOUR CONCEPTS
--------------------------------------------------------------------------
The four topics are not four slides. They are one price series, read left to
right, and each concept is the CAUSE of the next:

  equal internal highs/lows hold retail stops -> those stops ARE the internal
  liquidity -> price sweeps them -> the last bullish candle of that sweep is
  where institutions sold: the ORDER BLOCK -> price collapses, and the last
  bearish candle at the low is the bullish order block -> the rally back up
  BREAKS the bearish order block, so the same rectangle changes role: the
  BREAKER -> price retests it from above and it holds as support -> price runs
  up into a zone, is rejected instantly and explodes away: the REJECTION BLOCK
  -> and when price returns there, it reacts again.

So the closing line -- "start reading the story behind every candle" -- is not
an assertion laid over the chart. It is the chart.

--------------------------------------------------------------------------
TIMELINE
--------------------------------------------------------------------------
Nothing here is eyeballed. Every beat below is a WORD START looked up in
timeline.json by W(word, sentence). The whole cue table is resolved at import,
so a typo -- or a re-cut voiceover that no longer contains the word -- fails
immediately instead of drifting silently out of sync.
"""

from manim import *
import numpy as np
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# CANVAS -- 1080 x 1920 design space, 1 unit == 100 px  (matches the project)
# ---------------------------------------------------------------------------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 10.8
config.frame_height = 19.2

DW, DH = 1080, 1920
CX, CY = DW / 2, DH / 2
FH = DH / 100.0                       # full frame height in manim units (19.2)

# FONT: match ema_full / ema_macd / liquidity -- they do NOT override the font,
# so neither do we. Same family, same weights, same size ladder.


# ===========================================================================
# TIMELINE CONTROLLER  --  the film is driven by timeline.json, never by guesses
# ===========================================================================
class Timeline:
    """word_timeline.json, indexed for lookup.

    W("breaker", s=19) -> the START of the word "breaker" in sentence 19.
    Raises if the word is not there, which is the whole point: a cue can never
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
        return w.strip().strip(".,?!;:—\"'").lower()

    def word(self, text, s=None, occ=0):
        """Start time of a spoken word. `s` scopes it to one sentence,
        `occ` picks among repeats inside that scope."""
        key = self._norm(text)
        hits = [w for w in self.words
                if self._norm(w["word"]) == key
                and (s is None or w["sentence_index"] == s)]
        if len(hits) <= occ:
            where = "" if s is None else f" in sentence {s}"
            raise KeyError(f"timeline.json has no word {text!r}{where} (occurrence {occ})")
        return hits[occ]["start"]


TL = Timeline(os.path.join(HERE, "timeline.json"))
W = TL.word                        # wait_until_word() / animate_at_timestamp()
VOICEOVER_SECONDS = TL.duration    # 111.647


# ---------------------------------------------------------------------------
# THE CUE TABLE -- every beat in the film, resolved from the timeline at IMPORT.
# This is the script. Read it top to bottom and you have read the video.
# ---------------------------------------------------------------------------
CUE = {
    # --- HOOK  "Why does the market respect this candle but completely ignore
    #            every other one?  Is it random?  Not at all.  Institutions
    #            leave footprints on the chart.  And if you know how to read
    #            them, price starts making a lot more sense."
    "hk_open":        W("Why", 0),               # 0.03  chart starts printing
    "hk_candle":      W("candle", 0),            # 2.05  THE candle is named
    "hk_but":         W("but", 0),               # 2.83  price comes back to it
    "hk_every":       W("every", 0),             # 4.08  it TAGS the candle
    "hk_other":       W("other", 0),             # 4.64  and reverses off it
    "hk_random":      W("random", 1),            # 5.82  everything else dims
    "hk_not":         W("Not", 2),               # 7.00
    "hk_footprints":  W("footprints", 3),        # 9.26  the footprint is drawn
    "hk_read":        W("read", 4),              # 11.59 the chart lights back up
    "hk_sense":       W("sense", 4),             # 14.49 clear the hook

    # --- ROADMAP  "There are four concepts you need to understand.  Internal
    #               Liquidity, Order Blocks, Breaker Blocks, and Rejection Blocks."
    "rd_four":        W("four", 5),              # 16.07
    "rd_il":          W("Internal", 6),          # 18.20
    "rd_ob":          W("Order", 6),             # 19.62
    "rd_bb":          W("Breaker", 6),           # 20.72
    "rd_rb":          W("Rejection", 6),         # 22.40

    # --- INTERNAL LIQUIDITY  "Let's start with Internal Liquidity.  Every small
    #      high and every small low contains stop losses.  Those stop losses
    #      become liquidity.  Before making a big move, the market often sweeps
    #      that liquidity first."
    "il_start":       W("Let's", 7),             # 24.11 the roadmap row becomes the title
    "il_title":       W("Internal", 7),          # 24.81
    "il_chart":       W("Every", 8),             # 26.46 title -> keyword, chart prints
    "il_high":        W("high", 8),              # 27.34 the equal internal highs
    "il_low":         W("low", 8),               # 29.02 the equal internal lows
    "il_stops":       W("stop", 8),              # 30.36 stop losses appear
    "il_become":      W("become", 9),            # 32.95
    "il_liquidity":   W("liquidity", 9),         # 33.37 the stops BECOME the pools
    "il_before":      W("Before", 10),           # 34.63 price approaches
    "il_sweeps":      W("sweeps", 10),           # 37.09 THE SWEEP
    "il_first":       W("first", 10),            # 38.29

    # --- ORDER BLOCK  "Now comes the order block.  Imagine price falling
    #      aggressively.  The last bullish candle before that drop is often where
    #      institutions entered their sell positions.  That candle becomes a
    #      bearish order block.  In an uptrend, the opposite creates a bullish
    #      order block."
    "ob_now":         W("Now", 11),              # 39.61 pull back
    "ob_title":       W("order", 11),            # 40.48 ORDER BLOCK title card
    "ob_imagine":     W("Imagine", 12),          # 41.80 title -> keyword
    "ob_falling":     W("falling", 12),          # 42.52 THE DROP
    "ob_last":        W("last", 13),             # 44.32 isolate the candle
    "ob_bullish":     W("bullish", 13),          # 44.72
    "ob_candle":      W("candle", 13),           # 45.06
    "ob_institutions": W("institutions", 13),    # 47.34
    "ob_sell":        W("sell", 13),             # 48.70 the sell orders
    "ob_becomes":     W("becomes", 14),          # 51.01
    "ob_bearish":     W("bearish", 14),          # 51.73 the rectangle draws L->R
    "ob_block":       W("block", 14),            # 52.51 the label fades in
    "ob_uptrend":     W("uptrend", 15),          # 53.91 the mirror: the low
    "ob_opposite":    W("opposite", 15),         # 54.81 the rally starts
    "ob_bull2":       W("bullish", 15),          # 55.88 the bullish OB draws
    "ob_block2":      W("block", 15),            # 56.62

    # --- BREAKER BLOCK  "But what if price later breaks that order block?  It
    #      doesn't simply disappear.  Its role changes.  That's called a breaker
    #      block.  Old resistance becomes support or old support becomes
    #      resistance."
    "bb_but":         W("But", 16),              # 57.84 price runs at the zone
    "bb_breaks":      W("breaks", 16),           # 59.16 THE BREAK
    "bb_disappear":   W("disappear", 17),        # 61.41 the rectangle stays put
    "bb_role":        W("role", 18),             # 62.85 pull back
    "bb_changes":     W("changes", 18),          # 63.17
    "bb_thats":       W("That's", 19),           # 64.27 BREAKER BLOCK title card
    "bb_title":       W("breaker", 19),          # 65.23
    "bb_oldres":      W("Old", 20),              # 66.71 title -> keyword, zone morphs
    "bb_support1":    W("support", 20, 0),       # 67.92 price pulls back INTO it
    "bb_or":          W("or", 20),               # 68.92 it holds
    "bb_support2":    W("support", 20, 1),       # 69.44 RESISTANCE -> SUPPORT
    "bb_res2":        W("resistance", 20, 1),    # 70.44 and price rallies away

    # --- REJECTION BLOCK  "Finally, rejection blocks.  Sometimes price enters a
    #      zone, gets rejected instantly, and explodes in the opposite direction.
    #      That rejection leaves behind a very important candle.  Whenever price
    #      returns there, reactions often happen again."
    "rb_finally":     W("Finally", 21),          # 72.22 REJECTION BLOCK title card
    "rb_title":       W("rejection", 21),        # 72.70
    "rb_sometimes":   W("Sometimes", 22),        # 74.56 title -> keyword
    "rb_enters":      W("enters", 22),           # 75.57 the wick SPIKES up
    "rb_rejected":    W("rejected", 22),         # 76.89 and snaps back
    "rb_explodes":    W("explodes", 22),         # 78.57 it explodes away
    "rb_leaves":      W("leaves", 23),           # 81.78 isolate the candle
    "rb_important":   W("important", 23),        # 83.12 the rectangle draws
    "rb_candle":      W("candle", 23),           # 83.56 the label fades in
    "rb_returns":     W("returns", 24),          # 85.40 price comes back
    "rb_reactions":   W("reactions", 24),        # 86.54 and reacts again
    "rb_again":       W("again", 24),            # 87.68

    # --- RECAP  "So remember, internal liquidity tells you where the market
    #      wants to go.  Order blocks tell you where institutions entered.
    #      Breaker blocks tell you when those zones changed their role.  And
    #      rejection blocks tell you where the market refused to trade."
    "rc_so":          W("So", 25),               # 88.76 pull all the way back
    "rc_il":          W("internal", 25),         # 89.85
    "rc_ob":          W("Order", 26),            # 93.33
    "rc_bb":          W("Breaker", 27),          # 96.37
    "rc_rb":          W("rejection", 28),        # 100.26

    # --- CLOSE  "Once you understand these four concepts, you'll stop memorizing
    #      patterns and start reading the story behind every candle."
    "cl_once":        W("Once", 29),             # 103.61
    "cl_stop":        W("stop", 29),             # 106.91
    "cl_memorizing":  W("memorizing", 29),       # 107.17
    "cl_start":       W("start", 29),            # 108.81
    "cl_story":       W("story", 29),            # 109.56
    "cl_candle":      W("candle", 29),           # 111.10
}


# ---------------------------------------------------------------------------
# VOICEOVER
# ---------------------------------------------------------------------------
AUDIO_CANDIDATES = [
    os.path.join(HERE, "voiceover.mpeg"),
    os.path.join(HERE, "input", "voiceover.mpeg"),
    os.path.join(HERE, "voice-sync", "output", "voiceover.mpeg"),
]


def _add_voiceover(scene):
    """Mux the narration if the file is present; render silent otherwise."""
    for p in AUDIO_CANDIDATES:
        if os.path.exists(p):
            scene.add_sound(p)
            return
    print("[VO] narration audio not found -- rendering silent. Keep voiceover.mpeg "
          "next to this file to bake the audio in.")


class VOScene(MovingCameraScene):
    """Scene whose cue(t) anchors beats to voiceover timestamps.

    Identical contract to the sibling files: the authoritative clock is manim's
    own self.renderer.time, and cue(t) inserts exactly enough dead time to reach
    absolute time t (minus a small lead, so motion is already underway when the
    word is heard). `epoch` shifts the whole timeline so a single section can be
    previewed starting near t=0.

    Do NOT override play()/wait() to keep a private clock -- manim's wait() is
    implemented on top of play(), so a naive play() override double-counts every
    wait. renderer.time already tracks both correctly.
    """

    epoch = 0.0
    LEAD = 0.20        # begin each beat ~0.2 s before its spoken word

    def now(self):
        return self.renderer.time

    def cue(self, t, lead=None):
        """pause_until(): insert dead time so the NEXT play() begins at abs time t."""
        lead = self.LEAD if lead is None else lead
        target = (t - self.epoch) - lead
        gap = target - self.now()
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"[SYNC] behind by {-gap:5.2f}s at t={t:6.2f} "
                  f"(clock={self.now():6.2f}, epoch={self.epoch})")

    def at(self, key, lead=None):
        """cue() by cue-table name -- animate_at_timestamp(CUE[key])."""
        self.cue(CUE[key], lead=lead)


def P(px, py):
    """Design-space pixel (top-left origin) -> Manim coords."""
    return np.array([(px - CX) / 100.0, (CY - py) / 100.0, 0.0])


# ---------------------------------------------------------------------------
# PALETTE  (DARK theme -- the project's black background + the ink set)
#
# COLOUR IS MEANING HERE, and each concept owns exactly one hue for the whole
# film: its title, its top keyword, its zone, its rings and its recap row all
# carry the same colour, so a viewer who pauses on any frame knows which of the
# four they are looking at. Nothing else is allowed to borrow these four.
# ---------------------------------------------------------------------------
BG        = "#000000"
INK       = "#F4F3EF"   # light ink for text / rings / arrows on black
SUBTLE    = "#A2A2AA"   # muted captions
CARD_BG   = "#0C0E14"   # solid dark callout card fill
GRID_C    = "#6E6E78"

G_BODY    = "#2FB257"   # green candle
R_BODY    = "#E64B44"   # red candle

LIQ_C     = "#22D3EE"   # CYAN      -- internal liquidity (the resting stops)
LIQ_T     = "#7DE7F7"   # ...lighter twin for TEXT on black
OB_C      = "#F2A81C"   # GOLD      -- order block (where institutions entered)
BRK_C     = "#FF6B3D"   # ORANGE    -- breaker block (the zone that changed role)
REJ_C     = "#2DD4A7"   # EMERALD   -- rejection block (where price refused to trade)

STOP_C    = "#F0574F"   # retail stop losses
SELL_C    = "#F0574F"   # institutional sell orders
BUY_C     = "#3FC061"


# ---------------------------------------------------------------------------
# LAYOUT LANES  (design px) -- every element lives in exactly one lane.
#   keyword      :  pinned 0.95 units below the CAMERA FRAME top (see KeywordBar)
#   title card   :  y  800          (slightly ABOVE centre, per the brief)
#   chart        :  y  430 ..1450   (candles, zones, levels, tags)
#   caption      :  pinned 0.95 units above the CAMERA FRAME bottom
#   recap card   :  y 1510 ..1880
#
# The keyword and the caption are pinned to the CAMERA FRAME, not to the world:
# this film pushes the camera deep into single candles, and a world-anchored
# header would be cropped the instant it did. Pinning keeps the chapter
# indicator exactly one (scaled) unit below the top edge at every zoom, which is
# what the brief asks for and what a static header cannot deliver.
#
# Z-ORDER, and it matters: every price ZONE sits BEHIND the candles. A zone drawn
# on top -- even at 13% opacity -- visibly mutes the bars inside it, and the bars
# inside a breaker are exactly the ones the viewer is being asked to watch.
# ---------------------------------------------------------------------------
TITLE_Y = 800
Z_GLOW, Z_ZONE, Z_CANDLE, Z_LEVEL, Z_MARK, Z_LABEL, Z_CARD = 0, 1, 2, 4, 5, 6, 8
Z_SCRIM, Z_TITLE, Z_KEY = 20, 21, 25


# ---------------------------------------------------------------------------
# PRICE DATA  --  explicit OHLC. The sibling files derive OHLC from closes with
# random wicks; this film cannot: THE WICKS ARE THE SUBJECT. The sweep is a wick
# through the internal highs, and a rejection block IS a wick. So every bar is
# stated exactly, and _verify_structure() proves the story is really in there.
# ---------------------------------------------------------------------------
BARS = [
    # (open,   high,   low,  close)
    ( 70.0,  73.2,  69.4,  72.6),   #  0
    ( 72.6,  76.6,  72.0,  76.0),   #  1
    ( 76.0,  80.4,  75.6,  79.8),   #  2
    ( 79.8,  84.6,  79.2,  84.0),   #  3
    ( 84.0,  88.0,  83.4,  86.6),   #  4  INTERNAL HIGH #1   (high == 88.0 exactly)
    ( 86.6,  87.2,  80.0,  80.8),   #  5  INTERNAL LOW  #1   (low  == 80.0 exactly)
    ( 80.8,  84.2,  80.4,  83.8),   #  6
    ( 83.8,  88.0,  83.2,  86.4),   #  7  INTERNAL HIGH #2   (equal to #1)
    ( 86.4,  86.9,  80.0,  81.2),   #  8  INTERNAL LOW  #2   (equal to #1)
    ( 81.2,  85.0,  80.8,  84.6),   #  9
    ( 84.6,  87.4,  84.0,  86.8),   # 10  coils UNDER the highs -- never touches them
    ( 86.8,  92.4,  86.2,  91.6),   # 11  THE SWEEP -- takes the stops above 88.0
    ( 91.6,  94.0,  91.0,  93.4),   # 12  LAST BULLISH CANDLE  ->  BEARISH ORDER BLOCK
    ( 93.4,  93.6,  86.0,  86.6),   # 13  the drop begins, and it engulfs
    ( 86.6,  87.0,  79.0,  79.6),   # 14
    ( 79.6,  80.0,  72.4,  73.0),   # 15
    ( 73.0,  73.4,  66.6,  67.2),   # 16
    ( 67.2,  68.0,  63.0,  64.2),   # 17
    ( 64.2,  65.0,  61.0,  61.8),   # 18  LAST BEARISH CANDLE ->  BULLISH ORDER BLOCK
    ( 61.8,  68.4,  61.4,  67.8),   # 19  the rally, and it is impulsive
    ( 67.8,  74.6,  67.2,  74.0),   # 20
    ( 74.0,  81.0,  73.4,  80.4),   # 21
    ( 80.4,  87.6,  79.8,  87.0),   # 22
    ( 87.0,  95.6,  86.4,  95.0),   # 23  THE BREAK -- closes ABOVE the bearish OB
    ( 95.0,  97.6,  94.4,  96.8),   # 24  continuation (never re-enters the zone)
    ( 96.8,  97.2,  93.4,  93.8),   # 25  the retest -- price drops back INTO it
    ( 93.8,  94.4,  92.2,  94.0),   # 26  and it HOLDS: old resistance is now support
    ( 94.0,  99.4,  93.6,  98.8),   # 27  away from the breaker
    ( 98.8, 103.6,  98.4, 103.4),   # 28
    (103.4, 114.0, 101.4, 101.8),   # 29  THE REJECTION -- wick 6.6x the body
    (101.8, 102.6,  95.6,  96.2),   # 30  and it explodes in the opposite direction
    ( 96.2,  96.8,  90.0,  90.6),   # 31
    ( 90.6,  91.2,  85.4,  86.0),   # 32
    ( 86.0,  91.0,  85.6,  90.6),   # 33  price returns...
    ( 90.6,  97.2,  90.2,  96.8),   # 34
    ( 96.8, 103.4,  96.2, 103.0),   # 35  ...back to the zone
    (103.0, 108.6, 102.4, 102.6),   # 36  and it reacts AGAIN
    (102.6, 103.0,  96.4,  97.0),   # 37
    ( 97.0,  97.6,  92.0,  92.6),   # 38
]
N = len(BARS)

OPEN  = [b[0] for b in BARS]
HIGH  = [b[1] for b in BARS]
LOW   = [b[2] for b in BARS]
CLOSE = [b[3] for b in BARS]

# --- narrative anchors (indices into BARS -- do NOT drift) ------------------
IH_BARS = (4, 7)        # the equal internal highs
IL_BARS = (5, 8)        # the equal internal lows
SWEEP_I = 11            # the candle that takes the internal liquidity
OB_I    = 12            # the last bullish candle -> bearish order block -> breaker
DROP    = (13, 18)      # the aggressive drop  [13, 18)
BULL_I  = 18            # the last bearish candle -> bullish order block
RALLY   = (19, 25)      # the impulsive rally  [19, 25)
BREAK_I = 23            # the candle that closes above the order block
REJ_I   = 29            # the rejection candle
BLAST   = (30, 33)      # the move away from it
RETURN  = (33, 36)      # price coming back

# --- levels, all DERIVED from the table above -------------------------------
IH      = HIGH[IH_BARS[0]]                      # 88.0  internal high
IL      = LOW[IL_BARS[0]]                       # 80.0  internal low
BSL_HI, BSL_LO = IH + 2.0, IH - 0.6             # buy-side pool: stops ABOVE the highs
SSL_HI, SSL_LO = IL + 0.5, IL - 2.4             # sell-side pool: stops BELOW the lows
OB_HI, OB_LO   = HIGH[OB_I],  LOW[OB_I]         # 94.0 / 91.0  -- the order block zone
BO_HI, BO_LO   = HIGH[BULL_I], LOW[BULL_I]      # 65.0 / 61.0  -- the bullish order block
RB_HI          = HIGH[REJ_I]                    # 114.0 -- top of the rejection wick
RB_LO          = max(OPEN[REJ_I], CLOSE[REJ_I])  # 103.4 -- the body it snapped back to


def _verify_structure():
    """The story, asserted. If an edit to BARS breaks a beat, the import dies
    here rather than shipping a video whose narration no longer matches."""
    assert HIGH[4] == HIGH[7] == 88.0,  "the internal highs must be EQUAL"
    assert LOW[5] == LOW[8] == 80.0,    "the internal lows must be EQUAL"
    assert max(HIGH[:SWEEP_I]) == IH,   "nothing may pierce the internal highs early"
    assert HIGH[SWEEP_I] > IH and CLOSE[SWEEP_I] > IH, "the sweep must sweep, and close through"

    assert CLOSE[OB_I] > OPEN[OB_I],    "the order block must be a BULLISH candle"
    assert all(CLOSE[i] < OPEN[i] for i in range(*DROP)), "the drop must be all bearish"
    assert CLOSE[DROP[1] - 1] < IL,     "the drop must be aggressive"

    assert CLOSE[BULL_I] < OPEN[BULL_I], "the bullish order block must be a BEARISH candle"
    assert all(CLOSE[i] > OPEN[i] for i in range(*RALLY)), "the rally must be all bullish"

    assert CLOSE[BREAK_I] > OB_HI,      "the breaker must CLOSE above the order block"
    assert LOW[24] > OB_HI,             "the break must not immediately fall back in"
    assert OB_LO <= LOW[25] <= OB_HI,   "the retest must re-enter the zone"
    assert LOW[26] >= OB_LO,            "and the zone must HOLD (old resistance -> support)"
    assert CLOSE[27] > OB_HI,           "and price must rally away from it"

    body = abs(CLOSE[REJ_I] - OPEN[REJ_I])
    wick = HIGH[REJ_I] - max(OPEN[REJ_I], CLOSE[REJ_I])
    assert wick > 5 * body,             "the rejection candle must be mostly WICK"
    assert CLOSE[30] < LOW[REJ_I],      "and price must explode away from it"

    assert RB_LO <= HIGH[36] <= RB_HI,  "price must RETURN into the rejection zone"
    assert CLOSE[36] < RB_LO,           "and be rejected out of it again"
    assert CLOSE[37] < CLOSE[36],       "and follow through"

    assert max(HIGH) == HIGH[REJ_I] == 114.0, "the rejection high is the high of the film"
    assert min(LOW) == LOW[BULL_I] == 61.0,   "the bullish OB low is the low of the film"


_verify_structure()


# ---------------------------------------------------------------------------
# CHART GEOMETRY  (design px)
# ---------------------------------------------------------------------------
PLOT_L, PLOT_R = 80, 1000          # first / last candle centre x
CHART_TOP, CHART_BOT = 430, 1450   # price plot band
PRICE_HI, PRICE_LO = 118.0, 57.0   # price -> py mapping (headroom above the wick)
BODY_W = 0.135                     # candle body width, manim units


def IX(i):
    """Bar index -> centre x (px)."""
    return PLOT_L + i * (PLOT_R - PLOT_L) / (N - 1)


def PY(v):
    """Price -> py (px). Higher price -> smaller py."""
    return CHART_TOP + (PRICE_HI - v) / (PRICE_HI - PRICE_LO) * (CHART_BOT - CHART_TOP)


# Camera windows. Each is chosen so the action fills the frame WITHOUT the
# keyword or the caption ever leaving it -- they are pinned to the frame, so
# that part is free, but the CHART still has to fit.
ZOOM_IL   = (240, 975, 0.44)       # the internal range and its two pools
ZOOM_OB   = (500, 1050, 0.56)      # the last bullish candle and the drop
ZOOM_BULL = (565, 1185, 0.52)      # the low, and the bullish order block
ZOOM_BRK  = (600, 950, 0.58)       # the break, and the retest that holds
ZOOM_REJ  = (800, 760, 0.54)       # the spike, and the explosion away
ZOOM_RET  = (885, 810, 0.56)       # price coming back to the rejection block


# ===========================================================================
# CANDLESTICK BUILDER
# ===========================================================================
def candle_at(o, h, l, c, cx, pyf, bw, wick_from=None):
    """The one candle constructor. Geometry is injected (`cx`, `pyf`, `bw`) so the
    same builder serves the main chart AND the hook's separate little chart --
    they differ only in their coordinate frame, never in how a candle is made.

    `grow_edge` records which edge the OPEN sits on, so the body can later grow
    OUT OF ITS OPEN rather than fade in. `wick_from` overrides how the wick is
    animated: the sweep and the rejection candle grow their wick from the BOTTOM,
    so the spike visibly SHOOTS upward instead of blooming out of a midpoint.
    """
    up = c >= o
    col = G_BODY if up else R_BODY
    wick = Line(np.array([cx, pyf(h), 0]), np.array([cx, pyf(l), 0]),
                color=col, stroke_width=2.4)
    ytop, ybot = pyf(max(o, c)), pyf(min(o, c))
    body = Rectangle(width=bw, height=max(ytop - ybot, 0.035),
                     fill_color=col, fill_opacity=1.0,
                     stroke_color=col, stroke_width=1.0)
    body.move_to([cx, (ytop + ybot) / 2, 0])
    g = VGroup(wick, body)
    g.grow_edge = DOWN if up else UP     # bullish opens at the bottom, bearish at the top
    g.wick_from = wick_from
    g.up = up
    # Set here, not at the call sites: a candle left at the default z=0 renders
    # UNDERNEATH the zones (z=1), and the bars breaking a breaker come out muted
    # -- which is precisely the moment the viewer is meant to be watching.
    return g.set_z_index(Z_CANDLE)


def make_candle(i, wick_from=None):
    """Bar i of the main chart."""
    o, h, l, c = BARS[i]
    return candle_at(o, h, l, c,
                     cx=P(IX(i), 0)[0], pyf=lambda v: P(0, PY(v))[1],
                     bw=BODY_W, wick_from=wick_from)


def form(candle, lag=0.34):
    """A candle FORMING, never fading in: the wick explores first, then the body
    expands out of the open. That order is the grammar of this whole film -- it
    is what makes a sweep look like a sweep and a rejection look like a rejection
    (price GOES there, then it refuses to STAY there)."""
    wick_anim = (GrowFromEdge(candle[0], candle.wick_from) if candle.wick_from is not None
                 else GrowFromCenter(candle[0]))
    return AnimationGroup(wick_anim,
                          GrowFromEdge(candle[1], candle.grow_edge),
                          lag_ratio=lag)


def grow(scene, ctx, i0, i1, run_time=1.2, lag_ratio=0.10, extra=None, rate=smooth):
    """Print bars [i0, i1) as a wave. Candles are built ONCE by _new_ctx() and
    reused -- nothing is rebuilt per beat. Bearish runs accelerate INTO the move
    (rush_into) and bullish runs burst OUT of it (rush_from), which is what makes
    a drop feel aggressive and a rally feel impulsive with no extra effects."""
    cs = ctx["candles"]
    anims = [form(cs[i]) for i in range(i0, i1)]
    scene.play(LaggedStart(*anims, lag_ratio=lag_ratio), *(extra or []),
               run_time=run_time, rate_func=rate)
    ctx["printed"].update(range(i0, i1))


def dim_to(ctx, level, keep=()):
    """Isolate candles: everything printed EXCEPT `keep` drops to `level`."""
    cs = ctx["candles"]
    keep = set(keep)
    return [cs[i].animate.set_opacity(level)
            for i in sorted(ctx["printed"]) if i not in keep]


def undim(ctx):
    cs = ctx["candles"]
    return [cs[i].animate.set_opacity(1.0) for i in sorted(ctx["printed"])]


# ===========================================================================
# TYPOGRAPHY -- the chapter indicator, the title cards, the captions
# ===========================================================================
KEY_SIZE, TITLE_SIZE, CAP_SIZE = 34, 62, 27


class KeywordBar:
    """The top chapter indicator: ONE keyword at a time, pinned to the camera
    frame, never popped on.

    The brief asks for a keyword held ~1 unit below the top edge, always centred,
    always replaced by a transform rather than a cut. Both halves are handled here:

      * PINNING -- an updater re-solves the position AND the on-screen size from
        the live camera frame every frame, so a push-in from 1.0x to 0.44x neither
        crops the keyword nor blows it up to twice its size.
      * REPLACEMENT -- to() cross-fades the outgoing keyword into the incoming one,
        and morph_from() lets a full-screen concept title SHRINK into the slot,
        which is what ties a title card to the section it opens.

    The updater is detached before a transform and re-attached after: an updater
    that keeps snapping a mobject to its final home fights the interpolation that
    is trying to carry it there.
    """

    def __init__(self, scene, pad=0.95):
        self.scene, self.pad, self.mob = scene, pad, None

    def _apply(self, m):
        f = self.scene.camera.frame
        k = f.height / FH
        want = m._base_w * k
        if abs(m.width - want) > 1e-4:
            m.scale_to_fit_width(want)
        m.move_to([f.get_center()[0], f.get_top()[1] - k * self.pad - m.height / 2, 0])

    def _place(self, m):
        m._base_w = m.width
        self._apply(m)
        return m

    def _pin(self, m):
        m.add_updater(self._apply)
        self.mob = m

    def _build(self, label, color):
        return self._place(Text(label, font_size=KEY_SIZE, color=color,
                                weight=BOLD).set_z_index(Z_KEY))

    def to(self, label, color, run_time=0.75, extra=None):
        """Replace the keyword. Never a remove-and-recreate."""
        new = self._build(label, color)
        if self.mob is None:
            self.scene.play(FadeIn(new, shift=DOWN * 0.14), *(extra or []), run_time=run_time)
        else:
            self.mob.clear_updaters()
            self.scene.play(FadeTransform(self.mob, new), *(extra or []), run_time=run_time)
        self._pin(new)

    def morph_from(self, title, label, color, run_time=1.0, extra=None):
        """The concept title itself BECOMES the chapter keyword."""
        new = self._build(label, color)
        anims = [ReplacementTransform(title, new)]
        if self.mob is not None:
            self.mob.clear_updaters()
            anims.append(FadeOut(self.mob, shift=UP * 0.18))
        self.scene.play(*anims, *(extra or []), run_time=run_time)
        self._pin(new)


class CaptionBar:
    """One caption at a time, pinned above the camera frame's bottom edge, on a
    soft dark plate so it stays legible over candles at any zoom."""

    def __init__(self, scene, pad=0.95):
        self.scene, self.pad, self.mob = scene, pad, None

    def _apply(self, m):
        f = self.scene.camera.frame
        k = f.height / FH
        want = m._base_w * k
        if abs(m.width - want) > 1e-4:
            m.scale_to_fit_width(want)
        m.move_to([f.get_center()[0], f.get_bottom()[1] + k * self.pad + m.height / 2, 0])

    def _build(self, txt, color):
        t = Text(txt, font_size=CAP_SIZE, color=color, weight=BOLD)
        plate = SurroundingRectangle(t, buff=0.22, corner_radius=0.14, stroke_width=0,
                                     fill_color=CARD_BG, fill_opacity=0.90)
        g = VGroup(plate, t).set_z_index(Z_CARD)
        g._base_w = g.width
        self._apply(g)
        return g

    def show(self, txt, color=SUBTLE, run_time=0.5, extra=None):
        new = self._build(txt, color)
        if self.mob is None:
            self.scene.play(FadeIn(new, shift=UP * 0.10), *(extra or []), run_time=run_time)
        else:
            self.mob.clear_updaters()
            self.scene.play(FadeTransform(self.mob, new), *(extra or []), run_time=run_time)
        new.add_updater(self._apply)
        self.mob = new

    def clear(self, run_time=0.4, extra=None):
        if self.mob is None:
            if extra:
                self.scene.play(*extra, run_time=run_time)
            return
        self.mob.clear_updaters()
        self.scene.play(FadeOut(self.mob, shift=DOWN * 0.10), *(extra or []), run_time=run_time)
        self.mob = None


def make_scrim(opacity=0.87):
    """The dim behind a concept title card. Title cards are always played at full
    frame (the camera is pulled back first), so an origin-centred plate covers."""
    return Rectangle(width=config.frame_width * 1.25, height=config.frame_height * 1.25,
                     fill_color=BG, fill_opacity=opacity, stroke_width=0) \
        .move_to(ORIGIN).set_z_index(Z_SCRIM)


def concept_title(scene, kb, label, color, t_in, t_out,
                  src=None, extra_in=None, extra_out=None):
    """The film's one title grammar, used four times.

    Large type, set slightly ABOVE centre so it reads as a title card and not as
    a caption; revealed letter by letter (or grown out of `src`, the roadmap row
    that promised it); ruled underneath; held; and then -- this is the part that
    matters -- it does not simply leave. It shrinks into the top of the frame and
    BECOMES the chapter keyword for the section it just opened, so the viewer
    never loses track of which of the four is on screen.
    """
    sc = make_scrim()
    ttl = Text(label, font_size=TITLE_SIZE, color=color, weight=BOLD) \
        .move_to(P(CX, TITLE_Y)).set_z_index(Z_TITLE)
    rule = Line(ttl.get_left(), ttl.get_right(), color=color, stroke_width=3) \
        .next_to(ttl, DOWN, buff=0.24).set_opacity(0.6).set_z_index(Z_TITLE)

    # The rule draws WITH the title, not after it. The narration gives a concept
    # its name and starts explaining it about a second and a half later, and a
    # title card that spends a second of that admiring its own underline is late
    # to its own section -- so the reveal is one gesture, not two.
    reveal = ReplacementTransform(src, ttl) if src is not None else Write(ttl)
    scene.cue(t_in)
    scene.play(FadeIn(sc), reveal, Create(rule), *(extra_in or []), run_time=0.95)

    # `t_out` is when the morph STARTS; it runs 0.85 s, so callers pass it early
    # enough that the keyword has landed by the time the chart beat is spoken.
    # The keyword pins itself to the camera frame, so its landing spot is solved
    # from wherever the frame is RIGHT NOW -- which is why no camera move may ride
    # along in this play. Push in on the next beat instead; the pin will track it.
    scene.cue(t_out)
    kb.morph_from(ttl, label, color, run_time=0.85,
                  extra=[FadeOut(sc), FadeOut(rule, scale=0.6)] + list(extra_out or []))


# ===========================================================================
# CHART FURNITURE
# ===========================================================================
def zone(px0, px1, p_hi, p_lo, color, fill=0.13, sw=2.6):
    """A price zone: the order block, the breaker, the rejection block.
    Always revealed with GrowFromEdge(LEFT), so it is DRAWN left to right out of
    the candle that created it -- never switched on."""
    tl, br = P(px0, PY(p_hi)), P(px1, PY(p_lo))
    r = Rectangle(width=br[0] - tl[0], height=tl[1] - br[1],
                  stroke_color=color, stroke_width=sw,
                  fill_color=color, fill_opacity=fill)
    return r.move_to([(tl[0] + br[0]) / 2, (tl[1] + br[1]) / 2, 0]).set_z_index(Z_ZONE)


def glow(rect, color, layers=3):
    """A soft halo behind a zone. Three nested translucent copies -- cheap, and it
    survives a camera push far better than a stroke does."""
    g = VGroup()
    for k in range(layers, 0, -1):
        c = rect.copy().scale(1 + 0.030 * k)
        c.set_fill(color=color, opacity=0.05)
        c.set_stroke(color=color, width=1.5, opacity=0.16 / k)
        g.add(c)
    return g.set_z_index(Z_GLOW)


def tag(txt, color, px, py, size=30):
    """A label WELDED to a chart coordinate: it stays with the zone it names while
    the camera moves around it, but holds a constant size on screen.

    Manim measures type in world units, so a label authored to read at the full
    frame comes out more than twice as large the moment the camera pushes to
    0.44x -- which is how "BUY-SIDE LIQUIDITY" ended up wider than the pool it was
    labelling. Sizing each tag for the one window it is born in would fix that and
    then break the recap, where every zone is seen at once from the full frame.

    So the tag stores the width it wants at 1.0x, and weld() re-solves its world
    width from the LIVE frame height every frame. `size` therefore means what it
    should mean: how big this reads to the viewer, at any zoom, always.
    """
    t = Text(txt, font_size=size, color=color, weight=BOLD)
    plate = SurroundingRectangle(t, buff=0.16, corner_radius=0.10, stroke_width=0,
                                 fill_color=BG, fill_opacity=0.82)
    g = VGroup(plate, t).set_z_index(Z_LABEL)
    g._base_w, g._anchor = g.width, (px, py)
    return g.move_to(P(px, py))


def _fit(scene, m, k=None):
    """Solve a welded tag's world size + position for a frame scale of `k`
    (default: the live frame). Pass k explicitly when a tag is transformed IN THE
    SAME PLAY as a camera move -- it must land at the size the frame is arriving
    at, not the one it is leaving."""
    k = (scene.camera.frame.height / FH) if k is None else k
    want = m._base_w * k
    if abs(m.width - want) > 1e-4:
        m.scale_to_fit_width(want)
    return m.move_to(P(*m._anchor))


def weld(scene, m, k=None):
    """Fix `m` to its chart anchor at constant on-screen size, for good."""
    _fit(scene, m, k)
    m.add_updater(lambda mo: _fit(scene, mo))
    return m


def level_line(price, px0, px1, color=LIQ_C, sw=2.6, dash=0.13):
    return DashedLine(P(px0, PY(price)), P(px1, PY(price)),
                      color=color, stroke_width=sw, dash_length=dash).set_z_index(Z_LEVEL)


def ring(px, py, r=0.17, color=INK, sw=3.0):
    return Circle(radius=r, color=color, stroke_width=sw).move_to(P(px, py)).set_z_index(Z_MARK)


def xmark(px, py, s=6.5, color=STOP_C, sw=3.0):
    """A retail stop loss, sitting where retail leaves it: just past the level."""
    return VGroup(
        Line(P(px - s, py - s), P(px + s, py + s), color=color, stroke_width=sw),
        Line(P(px - s, py + s), P(px + s, py - s), color=color, stroke_width=sw),
    ).set_z_index(Z_MARK)


def stop_cluster(x0, x1, p_lo, p_hi, n, seed):
    """n stop losses scattered through a band. Seeded, so the render is
    reproducible frame for frame."""
    rng = np.random.default_rng(seed)
    xs = np.linspace(x0, x1, n) + rng.uniform(-8, 8, n)
    ps = rng.uniform(p_lo, p_hi, n)
    return VGroup(*[xmark(float(x), PY(float(p))) for x, p in zip(xs, ps)]).set_z_index(Z_MARK)


def AR(px0, py0, px1, py1, color=INK, sw=4.0):
    return Arrow(P(px0, py0), P(px1, py1), color=color, stroke_width=sw, buff=0.03,
                 tip_length=0.20, max_tip_length_to_length_ratio=0.4,
                 max_stroke_width_to_length_ratio=999).set_z_index(Z_MARK)


def gridlines():
    """The Bloomberg floor: a few faint rules, so the chart sits in a room rather
    than floating in a void. Faint enough to read as furniture, never as data."""
    g = VGroup()
    for p in (70, 80, 90, 100, 110):
        g.add(Line(P(56, PY(p)), P(1024, PY(p)), color=GRID_C,
                   stroke_width=1.1, stroke_opacity=0.13))
    g.add(Line(P(56, CHART_BOT + 14), P(1024, CHART_BOT + 14), color=GRID_C,
               stroke_width=1.6, stroke_opacity=0.22))
    return g.set_z_index(Z_GLOW)


# ---- camera ---------------------------------------------------------------
# A push-in narrows the frame in BOTH axes (scale_to_fit_height keeps 9:16), so
# at 0.44x only ~475 px of the 1080-wide design survives. The keyword and the
# caption are pinned to the frame and ride along; the CHART is what has to be
# aimed, which is what the ZOOM_* windows do.
# These RETURN an animation rather than playing one, and that is the whole point: a
# push-in played on its own is a cutaway, while the brief asks the camera to FOLLOW
# price. Handed to grow(extra=[...]) instead, the move happens WHILE the candles are
# printing -- so the frame is chasing the market, not inspecting it afterwards.
def cam(scene, window):
    px, py, factor = window
    return scene.camera.frame.animate.scale_to_fit_height(FH * factor).move_to(P(px, py))


def cam_full(scene):
    return scene.camera.frame.animate.scale_to_fit_height(FH).move_to(ORIGIN)


# ===========================================================================
# PHASE 0 -- THE HOOK   (0.0 - 15.0 s)
#   "Why does the market respect this candle but completely ignore every other
#    one?"  "Is it random?"  "Not at all."  "Institutions leave footprints on
#    the chart."  "And if you know how to read them, price starts making a lot
#    more sense."
#
# The hook gets its OWN little chart, cleared before the film's real chart is
# ever seen. It has one job: pose the question as a fact. Price falls away from
# one candle, comes all the way back to it, and reverses there -- and the viewer
# has watched that happen before anyone has told them what an order block is.
# ===========================================================================
HBARS = [
    (100.0, 101.5,  99.0, 101.0),   # 0
    (101.0, 103.0, 100.5, 102.6),   # 1  <- THE candle
    (102.6, 102.8,  96.0,  96.6),   # 2  price falls away from it
    ( 96.6,  97.0,  91.5,  92.0),   # 3
    ( 92.0,  92.4,  87.0,  87.6),   # 4
    ( 87.6,  90.0,  87.0,  89.6),   # 5  and comes back...
    ( 89.6,  93.5,  89.2,  93.0),   # 6
    ( 93.0,  97.0,  92.6,  96.6),   # 7
    ( 96.6, 101.0,  96.2, 100.6),   # 8
    (100.6, 102.8, 100.2, 101.0),   # 9  ...taps the candle, and closes back off it
    (101.0, 101.2,  95.0,  95.6),   # 10 THE RESPECT: it reverses, hard
    ( 95.6,  96.0,  89.5,  90.0),   # 11
]
HN = len(HBARS)
H_CANDLE = 1                        # the candle the market respects
HPL, HPR = 190, 890
HTOP, HBOT = 640, 1400
HPHI, HPLO = 106.0, 86.0
H_BODY_W = 0.40

# the zone the hook is really about: the body of the candle price came back to
HZ_HI = max(HBARS[H_CANDLE][0], HBARS[H_CANDLE][3])
HZ_LO = min(HBARS[H_CANDLE][0], HBARS[H_CANDLE][3])
assert HBARS[9][1] > HZ_LO and HBARS[9][3] <= HZ_LO + 0.1, \
    "the hook's return must actually TAG the candle's body and close back off it"
assert HBARS[10][3] < HBARS[9][2], "and it must reverse away from it"


def _hx(i):
    return P(HPL + i * (HPR - HPL) / (HN - 1), 0)[0]


def _hpy(v):
    return P(0, HTOP + (HPHI - v) / (HPHI - HPLO) * (HBOT - HTOP))[1]


def hook_candle(i):
    o, h, l, c = HBARS[i]
    return candle_at(o, h, l, c, cx=_hx(i), pyf=_hpy, bw=H_BODY_W)


def phase_hook(scene):
    """The hook: a single candle the market respects, and the footprint that
    explains why -- twelve seconds before the concept has a name."""
    hs = [hook_candle(i) for i in range(HN)]

    def hgrow(i0, i1, rt, rate=smooth, extra=None):
        scene.play(LaggedStart(*[form(hs[i]) for i in range(i0, i1)], lag_ratio=0.12),
                   *(extra or []), run_time=rt, rate_func=rate)

    # 0.03  "Why does the market..."  -- the market is already printing as the
    # narration starts. No title, no caption: just the chart, answering a question
    # that has not been asked out loud yet.
    scene.at("hk_open", lead=0.0)
    hgrow(0, 2, 0.85)
    hgrow(2, 5, 0.90, rate=rush_into)               # it falls away, and it means it

    # 2.05  "...this candle..."  -- name it, without a word. A single pulse.
    scene.at("hk_candle")
    scene.play(Indicate(hs[H_CANDLE], color=OB_C, scale_factor=1.16), run_time=0.6)

    # 2.83  "...but completely ignore every other one?"  -- price comes all the
    # way back. 4.08 it TAGS the candle. 4.64 it reverses off it, hard.
    scene.at("hk_but")
    hgrow(5, 8, 1.20, rate=rush_from)
    scene.at("hk_every")
    hgrow(8, 10, 0.50)
    scene.at("hk_other")
    hgrow(10, 12, 0.95, rate=rush_into)

    # 5.82  "Is it random?"  -- the answer is already on the screen; all that is
    # needed is to take everything else away. Every other candle drops to 18%,
    # and the eye lands where it should have been looking the whole time.
    others = [hs[i] for i in range(HN) if i != H_CANDLE]
    scene.at("hk_random")
    scene.play(*[m.animate.set_opacity(0.18) for m in others],
               scene.camera.frame.animate.scale_to_fit_height(FH * 0.72)
               .move_to([_hx(6), _hpy(96.5), 0]),
               run_time=1.1)

    # 7.00  "Not at all."
    hglow = Circle(radius=0.44, color=OB_C, stroke_width=3.5) \
        .move_to(hs[H_CANDLE].get_center()).set_z_index(Z_MARK)
    scene.at("hk_not")
    scene.play(Create(hglow), hs[H_CANDLE].animate.set_stroke(OB_C, width=2.6), run_time=0.7)

    # 8.28  "Institutions leave footprints on the chart."   9.26 "footprints"
    # The footprint is the zone. It is drawn OUT OF the candle, left to right,
    # and it lands exactly where price turned -- which is the entire film in one
    # rectangle, twelve seconds before it has a name.
    hz = Rectangle(width=_hx(11) + 0.2 - (_hx(H_CANDLE) - 0.2),
                   height=_hpy(HZ_HI) - _hpy(HZ_LO),
                   stroke_color=OB_C, stroke_width=2.6,
                   fill_color=OB_C, fill_opacity=0.13).set_z_index(Z_ZONE)
    hz.move_to([(_hx(H_CANDLE) - 0.2 + _hx(11) + 0.2) / 2,
                (_hpy(HZ_HI) + _hpy(HZ_LO)) / 2, 0])
    hz_g = glow(hz, OB_C)
    scene.at("hk_footprints")
    scene.play(GrowFromEdge(hz, LEFT), FadeIn(hz_g),
               FadeOut(hglow, scale=1.5), run_time=1.10)

    # 11.59  "...if you know how to read them..."  -- the chart comes back up, and
    # now the reversal is not a coincidence, it is a consequence. The arrow is the
    # only thing in the hook that editorialises, and it says one word: here.
    arr = Arrow(np.array([_hx(9), _hpy(101.2), 0]), np.array([_hx(10.6), _hpy(93.0), 0]),
                color=REJ_C, stroke_width=6, buff=0.06, tip_length=0.28,
                max_tip_length_to_length_ratio=0.3).set_z_index(Z_MARK)
    scene.at("hk_read")
    scene.play(*[m.animate.set_opacity(1.0) for m in others], run_time=0.8)
    scene.play(GrowArrow(arr), run_time=0.7)
    scene.play(scene.camera.frame.animate.shift(RIGHT * 0.18 + UP * 0.10),
               run_time=1.4, rate_func=linear)

    # 14.49  "...a lot more sense."  -- clear the hook. The real chart is next and
    # it must arrive on an empty stage.
    scene.at("hk_sense")
    scene.play(FadeOut(VGroup(*hs, hz, hz_g, arr)), cam_full(scene), run_time=1.0)


# ===========================================================================
# PHASE 1 -- THE ROADMAP   (15.8 - 24.1 s)
#   "There are four concepts you need to understand.  Internal Liquidity, Order
#    Blocks, Breaker Blocks, and Rejection Blocks."
#
# Four rows, four colours, and those four colours are then never used for
# anything else for the rest of the film. This is where the viewer is taught the
# legend -- so that later, a cyan glow or an orange rectangle needs no caption.
# ===========================================================================
CONCEPTS = [
    ("INTERNAL LIQUIDITY", LIQ_C),
    ("ORDER BLOCK",        OB_C),
    ("BREAKER BLOCK",      BRK_C),
    ("REJECTION BLOCK",    REJ_C),
]
ROAD_KEYS = ["rd_il", "rd_ob", "rd_bb", "rd_rb"]


def phase_roadmap(scene):
    """Returns (heading, dots, names). The names are added to the scene as
    TOP-LEVEL mobjects, not as children of a layout group: the Internal Liquidity
    name is handed to the next phase, which ReplacementTransforms it into that
    section's title card -- and a transform cannot cleanly remove a source that
    is nested inside some other group still on stage."""
    head = Text("FOUR CONCEPTS", font_size=34, color=SUBTLE, weight=BOLD) \
        .move_to(P(CX, 640)).set_z_index(Z_TITLE)
    rule = Line(head.get_left(), head.get_right(), color=SUBTLE, stroke_width=2) \
        .next_to(head, DOWN, buff=0.16).set_opacity(0.35).set_z_index(Z_TITLE)
    heading = VGroup(head, rule)

    names = [Text(label, font_size=44, color=col, weight=BOLD)
             for label, col in CONCEPTS]
    dots = [Dot(radius=0.11, color=col) for _, col in CONCEPTS]
    # laid out as a group, then let go of: only the leaves reach the stage
    VGroup(*[VGroup(d, n).arrange(RIGHT, buff=0.34) for d, n in zip(dots, names)]) \
        .arrange(DOWN, aligned_edge=LEFT, buff=0.52).move_to(P(CX, 1010))
    for m in names + dots:
        m.set_z_index(Z_TITLE)

    # 16.07  "...four concepts..."
    scene.at("rd_four")
    scene.play(Write(head), Create(rule), run_time=0.9)

    # 18.20 / 19.62 / 20.72 / 22.40 -- each row lands on its own spoken name, in
    # the colour it will keep for the rest of the film. They slide in from the
    # left rather than appear: nothing in this film pops onto the screen.
    for key, d, n in zip(ROAD_KEYS, dots, names):
        scene.at(key)
        scene.play(FadeIn(d, shift=RIGHT * 0.45), FadeIn(n, shift=RIGHT * 0.45),
                   run_time=0.55)

    return heading, dots, names


# ===========================================================================
# PHASE 2 -- INTERNAL LIQUIDITY   (24.1 - 39.0 s)   [CYAN]
#   "Let's start with Internal Liquidity."
#   "Every small high and every small low contains stop losses."
#   "Those stop losses become liquidity."
#   "Before making a big move, the market often sweeps that liquidity first."
# ===========================================================================
def phase_liquidity(scene, ctx, kb, cap, heading, dots, names):
    cs = ctx["candles"]

    # 24.11  "Let's start with Internal Liquidity."  -- the row the roadmap just
    # promised is the row that BECOMES the title. The other three step aside, and
    # the chart's floor fades up underneath. Nothing is thrown away and rebuilt.
    stand_down = VGroup(*names[1:], *dots)
    grid = gridlines()
    concept_title(
        scene, kb, "INTERNAL LIQUIDITY", LIQ_C,
        t_in=CUE["il_start"], t_out=CUE["il_chart"] - 0.65,
        src=names[0],
        extra_in=[FadeOut(stand_down, shift=DOWN * 0.3), FadeOut(heading)],
    )

    # 26.46  "Every small high and every small low..."  -- and the camera pushes
    # into the range WHILE it prints, so the market is never once seen standing
    # still. The keyword is pinned to the frame and rides the push in.
    scene.at("il_chart", lead=0.0)
    grow(scene, ctx, 0, 10, run_time=0.65, lag_ratio=0.09,
         extra=[FadeIn(grid), cam(scene, ZOOM_IL)])

    # 27.34  "...high..."   The two highs are IDENTICAL in the data (88.0 == 88.0),
    # so the line through them is a fact about the chart, not a drawing on top of
    # it. Same for the lows at 29.02.
    hi_line = level_line(IH, IX(3) - 10, IX(12) + 12, LIQ_C)
    hi_rings = VGroup(*[ring(IX(i), PY(IH), 0.13, LIQ_C, 2.8) for i in IH_BARS])
    scene.at("il_high")
    scene.play(Create(hi_line),
               LaggedStart(*[Create(r) for r in hi_rings], lag_ratio=0.3), run_time=0.85)

    lo_line = level_line(IL, IX(3) - 10, IX(12) + 12, LIQ_C)
    lo_rings = VGroup(*[ring(IX(i), PY(IL), 0.13, LIQ_C, 2.8) for i in IL_BARS])
    scene.at("il_low")
    scene.play(Create(lo_line),
               LaggedStart(*[Create(r) for r in lo_rings], lag_ratio=0.3), run_time=0.85)

    # 30.36  "...contains stop losses."  Retail leaves its stop just PAST the
    # level -- above the highs, below the lows. That placement is the whole reason
    # the sweep works, so the crosses land exactly there and nowhere else.
    stops_hi = stop_cluster(IX(3), IX(10), IH + 0.5, BSL_HI, 8, seed=11)
    stops_lo = stop_cluster(IX(3), IX(10), SSL_LO, IL - 0.4, 7, seed=29)
    scene.at("il_stops")
    scene.play(LaggedStart(*[FadeIn(m, scale=1.7) for m in stops_hi], lag_ratio=0.07),
               LaggedStart(*[FadeIn(m, scale=1.7) for m in stops_lo], lag_ratio=0.07),
               run_time=1.05)
    cap.show("everyone leaves their stop in the same place", SUBTLE, run_time=0.5)

    # 33.37  "Those stop losses BECOME liquidity."  -- one is the other, which is
    # the entire idea. So this is a Transform, not a fade-in of a second object:
    # the crosses ARE the pools, and the viewer watches them turn into them.
    bsl = zone(IX(3) - 10, IX(12) + 12, BSL_HI, BSL_LO, LIQ_C, fill=0.20)
    ssl = zone(IX(3) - 10, IX(12) + 12, SSL_HI, SSL_LO, LIQ_C, fill=0.20)
    bsl_g, ssl_g = glow(bsl, LIQ_C), glow(ssl, LIQ_C)
    bsl_t = weld(scene, tag("BUY-SIDE", LIQ_T, 215, 862, 26))
    ssl_t = weld(scene, tag("SELL-SIDE", LIQ_T, 255, 1140, 26))

    scene.at("il_liquidity")
    scene.play(ReplacementTransform(stops_hi.copy(), bsl),
               ReplacementTransform(stops_lo.copy(), ssl),
               FadeIn(bsl_g), FadeIn(ssl_g),
               FadeIn(bsl_t, shift=UP * 0.08), FadeIn(ssl_t, shift=DOWN * 0.08),
               stops_hi.animate.set_opacity(0.5), stops_lo.animate.set_opacity(0.5),
               run_time=1.20)

    # 34.63  "Before making a big move..."  -- price coils UNDER the highs. Bar 10
    # never touches them (max(high[:11]) == 88.0 is asserted), which is what makes
    # the next candle a sweep instead of just a rally.
    scene.at("il_before")
    grow(scene, ctx, 10, 11, run_time=0.6)
    cap.show("price coils beneath the highs", SUBTLE, run_time=0.45)

    # 37.09  "...the market often SWEEPS that liquidity first."
    # Bar 11's wick is built to grow from the BOTTOM (wick_from=DOWN), so it
    # visibly shoots up through the pool rather than materialising past it. The
    # stops it just took are extinguished in the same breath.
    scene.at("il_sweeps")
    grow(scene, ctx, 11, 12, run_time=0.85, rate=rush_from,
         extra=[bsl.animate.set_fill(opacity=0.05).set_stroke(opacity=0.35)])
    scene.play(FadeOut(stops_hi, scale=1.5), Flash(P(IX(11), PY(IH)), color=LIQ_C,
                                                   line_length=0.16, num_lines=10,
                                                   flash_radius=0.34),
               run_time=0.35)

    # 38.29  "...first."
    scene.at("il_first")
    cap.show("the stops above the highs are gone", LIQ_T, run_time=0.5)

    ctx.update(dict(hi_line=hi_line, lo_line=lo_line, hi_rings=hi_rings, lo_rings=lo_rings,
                    bsl=bsl, ssl=ssl, bsl_g=bsl_g, ssl_g=ssl_g, bsl_t=bsl_t, ssl_t=ssl_t,
                    stops_lo=stops_lo, grid=grid))


# ===========================================================================
# PHASE 3 -- ORDER BLOCK   (39.0 - 57.5 s)   [GOLD]
#   "Now comes the order block."
#   "Imagine price falling aggressively."
#   "The last bullish candle before that drop is often where institutions
#    entered their sell positions."
#   "That candle becomes a bearish order block."
#   "In an uptrend, the opposite creates a bullish order block."
#
# The brief's sequence, in order, and nothing skipped:
#   price moves -> the last opposite candle becomes important -> brief highlight
#   -> rectangle drawn left to right -> label fades in.
# The rectangle is never simply switched on. By the time it appears the viewer
# has already been told, in pictures, WHY that candle and not another one.
# ===========================================================================
OB_ZX0, OB_ZX1 = IX(OB_I) - 14, IX(28) + 6      # the zone, projected forward


def phase_orderblock(scene, ctx, kb, cap):
    cs = ctx["candles"]

    # 38.9 -- the pull-back rides the PAUSE between "first." and "Now comes the
    # order block", so the title card gets the whole of its own sentence rather
    # than sharing the first second of it with a camera move.
    # The two pool labels have been read; they are carried out on the pull-back.
    # The POOLS stay -- the recap needs them -- but left on the chart their names
    # would spend the next fifty seconds sliding through the order block, cropped
    # mid-word, saying nothing.
    scene.cue(CUE["il_first"] + 0.55, lead=0.0)
    cap.clear(run_time=0.65, extra=[FadeOut(ctx["bsl_t"]), FadeOut(ctx["ssl_t"]),
                                    cam_full(scene)])

    # 39.76 -> the title lands exactly on the spoken words "order block" (40.48).
    concept_title(scene, kb, "ORDER BLOCK", OB_C,
                  t_in=CUE["ob_now"] + 0.15, t_out=CUE["ob_imagine"] - 0.65)

    # 41.80  "Imagine price falling aggressively."  -- one more bullish candle
    # prints (the last one, though nobody knows that yet), and then the floor goes.
    scene.at("ob_imagine", lead=0.0)
    grow(scene, ctx, OB_I, OB_I + 1, run_time=0.55, extra=[cam(scene, ZOOM_OB)])

    # 42.52  "...FALLING AGGRESSIVELY."  rush_into: the move accelerates as it
    # goes, the way a real liquidation does. Five red bars, no easing out.
    scene.at("ob_falling")
    grow(scene, ctx, *DROP, run_time=1.45, lag_ratio=0.16, rate=rush_into)

    # 44.32  "The LAST BULLISH CANDLE before that drop..."  -- everything else on
    # the chart steps back to 20%. This is the beat the whole section turns on:
    # the candle is not important because a rectangle was drawn on it, the
    # rectangle is drawn on it because it was important.
    scene.at("ob_last")
    scene.play(*dim_to(ctx, 0.20, keep=[OB_I]), run_time=0.7)
    scene.at("ob_candle")
    scene.play(Indicate(cs[OB_I], color=OB_C, scale_factor=1.22), run_time=0.7)

    # 47.34  "...is often where INSTITUTIONS entered their SELL positions."
    # Three sell orders, landing on the candle they were filled at.
    sells = VGroup(*[AR(IX(OB_I) + 24 * (k - 1), PY(97.6),
                        IX(OB_I) + 24 * (k - 1), PY(94.6), SELL_C, 3.6)
                     for k in range(3)]).set_z_index(Z_MARK)
    sell_t = weld(scene, tag("INSTITUTIONAL SELLS", SELL_C, 520, PY(98.8), 22))
    scene.at("ob_institutions")
    cap.show("this is where they sold", SUBTLE, run_time=0.5)
    scene.at("ob_sell")
    scene.play(LaggedStart(*[GrowArrow(a) for a in sells], lag_ratio=0.22),
               FadeIn(sell_t, shift=LEFT * 0.12), run_time=0.9)

    # 51.73  "That candle BECOMES a bearish ORDER BLOCK."
    # The rectangle is DRAWN, left to right, out of the candle that made it -- the
    # sell orders dissolving into it as it goes, so the zone reads as a record of
    # those orders rather than as a shape that appeared next to them. The label
    # comes last, on the word "block", never before the thing it names exists.
    obz = zone(OB_ZX0, OB_ZX1, OB_HI, OB_LO, OB_C, fill=0.15)
    obz_g = glow(obz, OB_C)
    obz_t = weld(scene, tag("BEARISH OB", OB_C, 500, 745, 26))

    scene.at("ob_bearish")
    scene.play(GrowFromEdge(obz, LEFT), FadeIn(obz_g),
               FadeOut(sells, scale=0.4), FadeOut(sell_t, shift=RIGHT * 0.15),
               run_time=0.75)
    scene.at("ob_block")
    scene.play(FadeIn(obz_t, shift=UP * 0.10), *undim(ctx), run_time=0.7)
    cap.clear(run_time=0.4)

    # 53.91  "In an UPTREND, the OPPOSITE creates a BULLISH order block."
    # The mirror is not a second diagram. It is the same chart, ten bars later:
    # the drop ends on a bearish candle, price rips away from it, and that candle
    # is a bullish order block by exactly the same logic, read upside down.
    scene.at("ob_uptrend", lead=0.0)
    grow(scene, ctx, BULL_I, BULL_I + 1, run_time=0.6, extra=[cam(scene, ZOOM_BULL)])

    scene.at("ob_opposite")
    grow(scene, ctx, 19, 22, run_time=1.05, lag_ratio=0.14, rate=rush_from)

    boz = zone(IX(BULL_I) - 14, IX(24) + 10, BO_HI, BO_LO, OB_C, fill=0.15)
    boz_g = glow(boz, OB_C)
    boz_t = weld(scene, tag("BULLISH OB", OB_C, 600, 1418, 26))
    scene.at("ob_bull2")
    scene.play(Indicate(cs[BULL_I], color=OB_C, scale_factor=1.22), run_time=0.35)
    scene.play(GrowFromEdge(boz, LEFT), FadeIn(boz_g), run_time=0.45)
    scene.at("ob_block2")
    scene.play(FadeIn(boz_t, shift=DOWN * 0.10), run_time=0.6)

    ctx.update(dict(obz=obz, obz_g=obz_g, obz_t=obz_t, boz=boz, boz_g=boz_g, boz_t=boz_t))


# ===========================================================================
# PHASE 4 -- BREAKER BLOCK   (57.5 - 72.0 s)   [ORANGE]
#   "But what if price later breaks that order block?"
#   "It doesn't simply disappear."   "Its role changes."
#   "That's called a breaker block."
#   "Old resistance becomes support or old support becomes resistance."
#
# The brief is explicit and it is right: do NOT delete the rectangle. MORPH it.
# So there is exactly one rectangle in this section, and it is the same object
# that was created in phase 3. It never moves and it is never redrawn. Only its
# COLOUR and its NAME change -- because in the market, only its role changed.
# ===========================================================================
def phase_breaker(scene, ctx, kb, cap):
    cs, obz, obz_t = ctx["candles"], ctx["obz"], ctx["obz_t"]

    # 57.84  "But what if price later BREAKS that order block?"  -- the rally that
    # started as the bullish order block's impulse is the very thing that comes
    # back for the bearish one. One move, two lessons.
    scene.at("bb_but", lead=0.0)
    grow(scene, ctx, 22, BREAK_I, run_time=0.7, extra=[cam(scene, ZOOM_BRK)])

    # 59.16  "...BREAKS..."  close[23] (95.0) > high[12] (94.0), asserted at import.
    # The candle does not stop at the zone. It goes through it and closes above it,
    # and the zone flashes as it is pierced.
    scene.at("bb_breaks")
    grow(scene, ctx, BREAK_I, BREAK_I + 1, run_time=0.85, rate=rush_from,
         extra=[obz.animate.set_stroke(width=4.0)])
    scene.play(Flash(P(IX(BREAK_I), PY(OB_HI)), color=BRK_C, line_length=0.18,
                     num_lines=12, flash_radius=0.4),
               obz.animate.set_stroke(width=2.6), run_time=0.5)
    grow(scene, ctx, 24, 25, run_time=0.55)

    # 61.41  "It doesn't simply disappear."  -- and so it doesn't. The rectangle
    # is still there, and the film says so by pulsing it rather than by saying it.
    scene.at("bb_disappear")
    scene.play(Indicate(obz, color=OB_C, scale_factor=1.03), run_time=0.8)

    # 62.85  "Its role changes."  -- pull back for the title card.
    scene.at("bb_role", lead=0.0)
    cap.clear(run_time=0.6, extra=[cam_full(scene)])

    concept_title(scene, kb, "BREAKER BLOCK", BRK_C,
                  t_in=CUE["bb_thats"], t_out=CUE["bb_oldres"] - 0.85)

    # 66.71  "OLD RESISTANCE becomes support..."  -- the morph. Same rectangle,
    # same coordinates, new colour and new name. Gold -> orange, "BEARISH ORDER
    # BLOCK" -> "BULLISH BREAKER BLOCK", by Transform, never by delete-and-redraw.
    brk_t = _fit(scene, tag("BULLISH BREAKER", BRK_C, 500, 745, 26), k=ZOOM_BRK[2])
    role = _fit(scene, tag("OLD RESISTANCE", BRK_C, 740, 900, 24), k=ZOOM_BRK[2])
    scene.at("bb_oldres", lead=0.0)
    obz_t.clear_updaters()
    scene.play(cam(scene, ZOOM_BRK),
               obz.animate.set_stroke(BRK_C).set_fill(BRK_C, opacity=0.15),
               ctx["obz_g"].animate.set_color(BRK_C),
               ReplacementTransform(obz_t, brk_t),
               FadeIn(role, shift=RIGHT * 0.12),
               run_time=0.90)
    ctx["obz_t"] = weld(scene, brk_t)
    weld(scene, role)

    # 67.92  "...becomes SUPPORT..."  -- price falls back INTO the zone (low[25] is
    # inside it, asserted), and 68.92 it HOLDS (low[26] >= the zone floor, asserted).
    scene.at("bb_support1")
    grow(scene, ctx, 25, 26, run_time=0.7, rate=rush_into)
    scene.at("bb_or")
    grow(scene, ctx, 26, 27, run_time=0.7, rate=rush_from)

    # 69.44  "...or old SUPPORT becomes resistance."  -- the label the zone was
    # wearing when price broke it is replaced by the label it wears now. The
    # rectangle sat still; only what it MEANS moved.
    role2 = _fit(scene, tag("NEW SUPPORT", REJ_C, 740, 900, 24))
    scene.at("bb_support2")
    role.clear_updaters()
    scene.play(ReplacementTransform(role, role2),
               Flash(P(IX(26), PY(OB_LO)), color=REJ_C, line_length=0.16,
                     num_lines=10, flash_radius=0.32),
               run_time=0.75)

    # 70.44  "...becomes RESISTANCE."  -- and price leaves, off the level it once
    # got rejected at. The zone held. That is the proof, and it needs no caption.
    hold = AR(IX(26) + 14, PY(92.6), IX(27) + 34, PY(99.4), BUY_C, 5.0)
    scene.at("bb_res2")
    grow(scene, ctx, 27, 28, run_time=0.75, rate=rush_from)
    scene.play(GrowArrow(hold), run_time=0.55)
    weld(scene, role2)
    cap.show("the zone flipped -- and it held", BRK_C, run_time=0.40)

    ctx.update(dict(brk_t=brk_t, role2=role2, hold=hold))


# ===========================================================================
# PHASE 5 -- REJECTION BLOCK   (72.0 - 88.5 s)   [EMERALD]
#   "Finally, rejection blocks."
#   "Sometimes price enters a zone, gets rejected instantly, and explodes in the
#    opposite direction."
#   "That rejection leaves behind a very important candle."
#   "Whenever price returns there, reactions often happen again."
#
# The brief asks that the rejection be obvious with the sound off. It is, because
# the candle is animated in the order the market actually made it: the WICK
# shoots up first (wick_from=DOWN), alone, into empty space -- and then the body
# closes back at the bottom, so the spike is visibly REFUSED rather than simply
# drawn. The rectangle covers the wick, because the wick IS the rejection block.
# ===========================================================================
RB_ZX0, RB_ZX1 = IX(REJ_I) - 16, PLOT_R + 12


def phase_rejection(scene, ctx, kb, cap):
    cs = ctx["candles"]

    # 72.22  "Finally, rejection blocks."  -- pull back for the last title card.
    # The role annotation is transient -- it made its point, and bars 28-38 are
    # about to print straight through where it sits.
    scene.at("rb_finally", lead=0.0)
    ctx["role2"].clear_updaters()
    cap.clear(run_time=0.55, extra=[FadeOut(ctx["hold"]), FadeOut(ctx["role2"]),
                                    cam_full(scene)])

    concept_title(scene, kb, "REJECTION BLOCK", REJ_C,
                  t_in=CUE["rb_title"] + 0.20, t_out=CUE["rb_sometimes"] - 0.70)

    # 74.56  "Sometimes price enters a zone..."  -- price runs up into clear air.
    scene.at("rb_sometimes", lead=0.0)
    grow(scene, ctx, 28, REJ_I, run_time=0.65, rate=rush_from,
         extra=[cam(scene, ZOOM_REJ)])

    # 75.57  "...ENTERS a zone..."   76.89  "...gets REJECTED instantly..."
    # The candle is split into its two halves and each is played on its own word.
    # First the wick alone -- price going somewhere. Then the body snapping shut
    # at the bottom of it -- price being thrown out of there. Two beats, one bar.
    rej = cs[REJ_I]
    scene.at("rb_enters")
    scene.play(GrowFromEdge(rej[0], DOWN), run_time=0.85, rate=rush_from)
    scene.at("rb_rejected")
    scene.play(GrowFromEdge(rej[1], rej.grow_edge), run_time=0.45, rate=rush_into)
    scene.play(Flash(P(IX(REJ_I), PY(RB_HI)), color=REJ_C, line_length=0.20,
                     num_lines=12, flash_radius=0.42), run_time=0.5)
    # The two halves were animated individually, so the wick and the body are on
    # stage as separate top-level mobjects while the VGroup that owns them is not.
    # Re-seat them under it, or the later dim/undim -- which animates the GROUP --
    # would add a second copy of both on top of the first.
    scene.remove(rej[0], rej[1])
    scene.add(rej)
    ctx["printed"].add(REJ_I)

    # 78.57  "...and EXPLODES in the opposite direction."  Three bars, accelerating,
    # and the camera falls with them. close[30] < low[29] is asserted at import:
    # the move away is real, not implied.
    scene.at("rb_explodes")
    grow(scene, ctx, *BLAST, run_time=1.25, lag_ratio=0.16, rate=rush_into,
         extra=[scene.camera.frame.animate.shift(DOWN * 1.05)])

    # 81.78  "That rejection LEAVES BEHIND a very important candle."
    # Isolate it, then draw the zone over the WICK -- not the body. That is the
    # distinction between a rejection block and an order block, and it is made
    # here in geometry rather than in words.
    scene.at("rb_leaves")
    scene.play(*dim_to(ctx, 0.20, keep=[REJ_I]), cam(scene, ZOOM_REJ), run_time=0.85)
    scene.play(Indicate(rej, color=REJ_C, scale_factor=1.10), run_time=0.50)

    rbz = zone(RB_ZX0, RB_ZX1, RB_HI, RB_LO, REJ_C, fill=0.14)
    rbz_g = glow(rbz, REJ_C)
    rbz_t = weld(scene, tag("REJECTION BLOCK", REJ_C, 800, 466, 26))
    scene.at("rb_important")
    scene.play(GrowFromEdge(rbz, LEFT), FadeIn(rbz_g), run_time=0.55)
    scene.at("rb_candle")
    scene.play(FadeIn(rbz_t, shift=UP * 0.10), *undim(ctx), run_time=0.65)

    # 85.40  "Whenever price RETURNS there..."   86.54 "...REACTIONS often happen
    # again."  high[36] lands inside the zone and closes back below it -- asserted.
    # The lesson is not that the zone is magic. It is that the same refusal repeats.
    scene.at("rb_returns")
    grow(scene, ctx, *RETURN, run_time=1.05, lag_ratio=0.14, rate=rush_from,
         extra=[cam(scene, ZOOM_RET)])

    scene.at("rb_reactions")
    grow(scene, ctx, 36, 37, run_time=0.7, rate=rush_into,
         extra=[rbz.animate.set_fill(opacity=0.24)])
    scene.play(Flash(P(IX(36), PY(HIGH[36])), color=REJ_C, line_length=0.18,
                     num_lines=10, flash_radius=0.36),
               rbz.animate.set_fill(opacity=0.14), run_time=0.5)

    scene.at("rb_again")
    grow(scene, ctx, 37, 39, run_time=0.95, lag_ratio=0.16, rate=rush_into)

    ctx.update(dict(rbz=rbz, rbz_g=rbz_g, rbz_t=rbz_t))


# ===========================================================================
# PHASE 6 -- RECAP   (88.5 - 103.5 s)
#   "So remember, internal liquidity tells you where the market wants to go."
#   "Order blocks tell you where institutions entered."
#   "Breaker blocks tell you when those zones changed their role."
#   "And rejection blocks tell you where the market refused to trade."
#
# The camera pulls all the way back, and for the first time the whole chart is
# visible at once -- with all four zones still on it, exactly where they were
# drawn. Nothing is re-created for the summary. The summary IS the chart, and
# each concept simply lights back up as it is named.
# ===========================================================================
RECAP = [
    ("INTERNAL LIQUIDITY", "where the market wants to go",   LIQ_C, "rc_il"),
    ("ORDER BLOCK",        "where institutions entered",     OB_C,  "rc_ob"),
    ("BREAKER BLOCK",      "when a zone changed its role",   BRK_C, "rc_bb"),
    ("REJECTION BLOCK",    "where price refused to trade",   REJ_C, "rc_rb"),
]


def _recap_rows():
    """Four rows, colour-keyed to the four zones. The names are set in a fixed
    column so the meanings line up -- a ragged right edge here would read as
    sloppy in a film that has spent ninety seconds being precise."""
    names = [Text(n, font_size=25, color=c, weight=BOLD) for n, _, c, _ in RECAP]
    col_w = max(t.width for t in names)
    rows = VGroup()
    for (nm_txt, meaning, col, _), nm in zip(RECAP, names):
        slot = Rectangle(width=col_w, height=nm.height, stroke_width=0, fill_opacity=0)
        nm.move_to(slot.get_left(), aligned_edge=LEFT)
        mn = Text(meaning, font_size=23, color=SUBTLE)
        rows.add(VGroup(Dot(radius=0.08, color=col), VGroup(slot, nm), mn)
                 .arrange(RIGHT, buff=0.26))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.26)
    card = SurroundingRectangle(rows, buff=0.34, corner_radius=0.16, stroke_width=1.6,
                                stroke_color=GRID_C, fill_color=CARD_BG, fill_opacity=0.94)
    card.set_stroke(opacity=0.35)
    return VGroup(card, rows).move_to(P(CX, 1690)).set_z_index(Z_CARD), rows


def phase_recap(scene, ctx, kb, cap):
    # 88.76  "So remember..."  -- all the way out. Everything the film drew is
    # still there; the viewer sees it assembled for the first time.
    # Only the zone RECTANGLES are driven here. Their glows are left alone: a halo
    # is atmosphere, and re-setting its fill would flatten the very softness it
    # exists to provide.
    zones = {"rc_il": [ctx["bsl"], ctx["ssl"]],
             "rc_ob": [ctx["boz"]],
             "rc_bb": [ctx["obz"]],
             "rc_rb": [ctx["rbz"]]}
    fills = {"rc_il": 0.20, "rc_ob": 0.15, "rc_bb": 0.15, "rc_rb": 0.14}

    scene.at("rc_so", lead=0.0)
    cap.clear(run_time=0.55, extra=[cam_full(scene)])

    card, rows = _recap_rows()
    scene.play(FadeIn(card[0]), run_time=0.35)

    # Each row lands on its own spoken concept, the top keyword changes to match,
    # and -- the point of the whole layout -- the ZONE on the chart above lights
    # up at the same instant. Name, colour and geometry all arrive together.
    # the pool labels were carried out at the order block; the recap is exactly
    # where they belong again -- welded, so they come back at full-frame size
    relabel = {"rc_il": [FadeIn(ctx["bsl_t"]), FadeIn(ctx["ssl_t"])]}

    for (label, _, col, key), row in zip(RECAP, rows):
        z = zones[key]
        scene.at(key)
        kb.to(label, col, run_time=0.6)
        scene.play(FadeIn(row, shift=RIGHT * 0.35),
                   *[m.animate.set_stroke(width=4.2) for m in z],
                   *relabel.get(key, []),
                   run_time=0.55)
        scene.play(*[m.animate.set_stroke(width=2.6) for m in z], run_time=0.45)
        # the other three step back, so at any instant exactly one idea is lit
        scene.play(*[mm.animate.set_fill(opacity=fills[k] * 0.45)
                     for k, zz in zones.items() if k != key for mm in zz],
                   *[mm.animate.set_fill(opacity=fills[key]) for mm in z],
                   run_time=0.4)

    ctx["card"] = card


# ===========================================================================
# PHASE 7 -- THE CLOSE   (103.5 - 111.6 s)
#   "Once you understand these four concepts, you'll stop memorizing patterns
#    and start reading the story behind every candle."
# ===========================================================================
def phase_close(scene, ctx, kb):
    frame = scene.camera.frame

    # 103.61  "Once you understand these four concepts..."  -- the chart, having
    # made its case, gets out of the way.
    sc = make_scrim(0.92)
    scene.at("cl_once", lead=0.0)
    # Everything the film drew, so it can be swept in one gesture at the end. The
    # camera frame lives in self.mobjects too -- it is scenery, not content.
    drawn = [m for m in scene.mobjects if isinstance(m, VMobject) and m is not frame]
    scene.play(FadeIn(sc), run_time=0.9)
    kb.mob.clear_updaters()

    l1 = Text("STOP MEMORIZING PATTERNS", font_size=40, color=SUBTLE, weight=BOLD) \
        .move_to(P(CX, 830)).set_z_index(Z_TITLE)
    strike = Line(l1.get_left(), l1.get_right(), color=STOP_C, stroke_width=3.5) \
        .set_z_index(Z_TITLE)
    l2 = Text("START READING THE STORY", font_size=44, color=INK, weight=BOLD) \
        .move_to(P(CX, 960)).set_z_index(Z_TITLE)

    # 106.91 / 107.17  "...you'll STOP MEMORIZING patterns..."  -- the line
    # arrives on "stop" and is struck through on "memorizing", 0.26 s later.
    scene.at("cl_stop")
    scene.play(FadeOut(kb.mob), FadeIn(l1, shift=UP * 0.12), run_time=0.35)
    scene.at("cl_memorizing")
    scene.play(Create(strike), l1.animate.set_opacity(0.45), run_time=0.55)

    # 108.81  "...and START READING THE STORY..."
    scene.at("cl_start")
    scene.play(Write(l2), run_time=0.70)

    # 109.56 / 111.10  "...behind every CANDLE."  -- and the film ends on the
    # object it began with: one candle, lit, with a zone drawn out of it. Which
    # is, in the end, the only thing it has been teaching.
    fin = candle_at(96.0, 104.0, 94.0, 102.0, cx=0.0,
                    pyf=lambda v: P(0, 1330 - (v - 96.0) * 17.0)[1],
                    bw=0.46)
    halo = Circle(radius=0.72, color=OB_C, stroke_width=3.0).move_to(fin.get_center()) \
        .set_z_index(Z_MARK)
    fin.set_z_index(Z_TITLE)
    halo.set_z_index(Z_TITLE)

    scene.at("cl_story")
    scene.play(form(fin), run_time=0.9)
    scene.at("cl_candle")
    scene.play(Create(halo), Flash(fin.get_center(), color=OB_C, line_length=0.25,
                                   num_lines=14, flash_radius=0.85), run_time=0.9)

    # The narration is over. Ride it out to the exact end of the audio, then clear.
    remaining = (VOICEOVER_SECONDS - scene.epoch) - scene.now()
    if remaining > 1e-3:
        scene.wait(remaining)
    scene.play(FadeOut(VGroup(l1, strike, l2, fin, halo, sc)),
               *[FadeOut(m) for m in drawn if m in scene.mobjects],
               run_time=0.8)


def phase_outro(scene):
    """Branded tail, played past the narration (matches the sibling files)."""
    o = Text("SCARCITY CIRCLE", font_size=48, color=OB_C, weight=BOLD)
    h = Text("@scarcitycircle", font_size=28, color=INK)
    VGroup(o, h).arrange(DOWN, buff=0.30).move_to(ORIGIN)
    scene.play(FadeIn(o, shift=UP * 0.10), run_time=0.7)
    scene.play(FadeIn(h, shift=UP * 0.10), run_time=0.5)
    scene.wait(1.0)
    scene.play(FadeOut(o), FadeOut(h), run_time=0.6)


# ===========================================================================
# SCENES
# ===========================================================================
def _new_ctx():
    """Every candle built ONCE and reused by every phase. The sweep and the
    rejection candle grow their wicks from below -- see candle_at()."""
    return {
        "candles": [make_candle(i, wick_from=(DOWN if i in (SWEEP_I, REJ_I) else None))
                    for i in range(N)],
        "printed": set(),
    }


class FullVideo(VOScene):
    """The full voiceover-synced cut. Every beat is cued to timeline.json."""

    epoch = 0.0

    def construct(self):
        self.camera.background_color = BG
        _add_voiceover(self)

        kb, cap = KeywordBar(self), CaptionBar(self)
        ctx = _new_ctx()

        phase_hook(self)                                    #   0.0 - 15.0
        head, rows, names = phase_roadmap(self)             #  15.8 - 24.1
        phase_liquidity(self, ctx, kb, cap, head, rows, names)   # 24.1 - 39.0  CYAN
        phase_orderblock(self, ctx, kb, cap)                #  39.0 - 57.5  GOLD
        phase_breaker(self, ctx, kb, cap)                   #  57.5 - 72.0  ORANGE
        phase_rejection(self, ctx, kb, cap)                 #  72.0 - 88.5  EMERALD
        phase_recap(self, ctx, kb, cap)                     #  88.5 -103.5
        phase_close(self, ctx, kb)                          # 103.5 -111.6
        phase_outro(self)                                   # past the audio


# ---------------------------------------------------------------------------
# SECTION PREVIEWS
#
# Each preview shifts `epoch` so its section starts near t=0, and _seed() rebuilds
# -- instantly, without animating -- whatever the earlier sections had left on the
# chart. That is the only way to iterate on the breaker at 60 s without sitting
# through the sixty seconds in front of it, and it is why every phase writes what
# it created into `ctx` instead of keeping it in a local.
# ---------------------------------------------------------------------------
SECTIONS = ["liquidity", "orderblock", "breaker", "rejection", "recap"]


def _seed(scene, ctx, upto):
    """Reconstruct the state the section `upto` inherits. Mirrors what the earlier
    phases put in ctx -- if you add a mobject to a phase, add it here too."""
    need = SECTIONS.index(upto)
    add = scene.add
    add(gridlines())

    if need >= 1:                                   # INTERNAL LIQUIDITY is done
        for i in range(0, SWEEP_I + 1):
            add(ctx["candles"][i])
        ctx["printed"].update(range(0, SWEEP_I + 1))
        add(level_line(IH, IX(3) - 10, IX(12) + 12, LIQ_C),
            level_line(IL, IX(3) - 10, IX(12) + 12, LIQ_C))
        for i in IH_BARS:
            add(ring(IX(i), PY(IH), 0.13, LIQ_C, 2.8))
        for i in IL_BARS:
            add(ring(IX(i), PY(IL), 0.13, LIQ_C, 2.8))
        # the buy-side pool has already been swept -- it is spent, and it shows
        bsl = zone(IX(3) - 10, IX(12) + 12, BSL_HI, BSL_LO, LIQ_C, fill=0.05)
        bsl.set_stroke(opacity=0.35)
        ssl = zone(IX(3) - 10, IX(12) + 12, SSL_HI, SSL_LO, LIQ_C, fill=0.20)
        bsl_t = weld(scene, tag("BUY-SIDE", LIQ_T, 215, 862, 26))
        ssl_t = weld(scene, tag("SELL-SIDE", LIQ_T, 255, 1140, 26))
        add(bsl, ssl, glow(bsl, LIQ_C), glow(ssl, LIQ_C),
            stop_cluster(IX(3), IX(10), SSL_LO, IL - 0.4, 7, seed=29).set_opacity(0.5))
        ctx.update(bsl=bsl, ssl=ssl, bsl_t=bsl_t, ssl_t=ssl_t)
        if need >= 2:                               # ...and its labels have gone
            scene.remove(bsl_t, ssl_t)

    if need >= 2:                                   # ORDER BLOCK is done
        for i in range(OB_I, 22):
            add(ctx["candles"][i])
        ctx["printed"].update(range(OB_I, 22))
        obz = zone(OB_ZX0, OB_ZX1, OB_HI, OB_LO, OB_C, fill=0.15)
        boz = zone(IX(BULL_I) - 14, IX(24) + 10, BO_HI, BO_LO, OB_C, fill=0.15)
        obz_t = weld(scene, tag("BEARISH OB", OB_C, 500, 745, 26))
        boz_t = weld(scene, tag("BULLISH OB", OB_C, 600, 1418, 26))
        add(obz, boz, glow(obz, OB_C), glow(boz, OB_C))
        ctx.update(obz=obz, obz_g=glow(obz, OB_C), obz_t=obz_t,
                   boz=boz, boz_g=glow(boz, OB_C), boz_t=boz_t)

    if need >= 3:                                   # BREAKER is done: same zone,
        for i in range(22, 28):                     # new colour, new name
            add(ctx["candles"][i])
        ctx["printed"].update(range(22, 28))
        scene.remove(ctx["obz_t"])
        ctx["obz"].set_stroke(BRK_C).set_fill(BRK_C, opacity=0.15)
        ctx["obz_g"].set_color(BRK_C)
        ctx["obz_t"] = weld(scene, tag("BULLISH BREAKER", BRK_C, 500, 745, 26))
        ctx["role2"] = weld(scene, tag("NEW SUPPORT", REJ_C, 740, 900, 24))
        ctx["hold"] = AR(IX(26) + 14, PY(92.6), IX(27) + 34, PY(99.4), BUY_C, 5.0)
        add(ctx["obz_t"], ctx["role2"], ctx["hold"])

    if need >= 4:                                   # REJECTION is done
        for i in range(28, N):
            add(ctx["candles"][i])
        ctx["printed"].update(range(28, N))
        scene.remove(ctx["role2"], ctx["hold"])
        rbz = zone(RB_ZX0, RB_ZX1, RB_HI, RB_LO, REJ_C, fill=0.14)
        rbz_t = weld(scene, tag("REJECTION BLOCK", REJ_C, 800, 466, 26))
        add(rbz, glow(rbz, REJ_C), rbz_t)
        ctx.update(rbz=rbz, rbz_g=glow(rbz, REJ_C), rbz_t=rbz_t)


class _Preview(VOScene):
    """Base: seed the past, restore the chapter keyword, play one section."""
    section = None
    start = 0.0

    def construct(self):
        self.camera.background_color = BG
        self.epoch = self.start
        kb, cap = KeywordBar(self), CaptionBar(self)
        ctx = _new_ctx()
        _seed(self, ctx, self.section)

        prior = {"orderblock": ("INTERNAL LIQUIDITY", LIQ_C),
                 "breaker": ("ORDER BLOCK", OB_C),
                 "rejection": ("BREAKER BLOCK", BRK_C),
                 "recap": ("REJECTION BLOCK", REJ_C)}
        if self.section in prior:
            label, col = prior[self.section]
            kb._pin(kb._build(label, col))
            self.add(kb.mob)

        self.run_section(ctx, kb, cap)

    def run_section(self, ctx, kb, cap):
        raise NotImplementedError


class HookScene(VOScene):
    def construct(self):
        self.camera.background_color = BG
        phase_hook(self)
        self.wait(0.8)


class RoadmapScene(VOScene):
    epoch = CUE["rd_four"] - 1.0

    def construct(self):
        self.camera.background_color = BG
        phase_roadmap(self)
        self.wait(0.5)


class LiquidityScene(_Preview):
    section, start = "liquidity", CUE["rd_four"] - 1.0

    def run_section(self, ctx, kb, cap):
        # the roadmap has to be on screen: the title card grows out of its first row
        heading, dots, names = phase_roadmap(self)
        phase_liquidity(self, ctx, kb, cap, heading, dots, names)


class OrderBlockScene(_Preview):
    section, start = "orderblock", CUE["il_first"] - 0.6

    def run_section(self, ctx, kb, cap):
        phase_orderblock(self, ctx, kb, cap)


class BreakerScene(_Preview):
    section, start = "breaker", CUE["bb_but"] - 1.2

    def run_section(self, ctx, kb, cap):
        phase_breaker(self, ctx, kb, cap)


class RejectionScene(_Preview):
    section, start = "rejection", CUE["rb_finally"] - 1.2

    def run_section(self, ctx, kb, cap):
        phase_rejection(self, ctx, kb, cap)


class RecapScene(_Preview):
    section, start = "recap", CUE["rc_so"] - 1.2

    def run_section(self, ctx, kb, cap):
        phase_recap(self, ctx, kb, cap)
        phase_close(self, ctx, kb)
        phase_outro(self)


class StillFrame(Scene):
    """The whole chart, every zone, no animation -- the layout check.
    Render: manim -sqh blocks.py StillFrame"""

    def construct(self):
        self.camera.background_color = BG
        self.add(gridlines())
        for i in range(N):
            self.add(make_candle(i))

        for z, c, fill in ((zone(IX(3) - 10, IX(12) + 12, BSL_HI, BSL_LO, LIQ_C, 0.20), LIQ_C, 0),
                           (zone(IX(3) - 10, IX(12) + 12, SSL_HI, SSL_LO, LIQ_C, 0.20), LIQ_C, 0),
                           (zone(OB_ZX0, OB_ZX1, OB_HI, OB_LO, BRK_C, 0.15), BRK_C, 0),
                           (zone(IX(BULL_I) - 14, IX(24) + 10, BO_HI, BO_LO, OB_C, 0.15), OB_C, 0),
                           (zone(RB_ZX0, RB_ZX1, RB_HI, RB_LO, REJ_C, 0.14), REJ_C, 0)):
            self.add(glow(z, c), z)

        for t in (tag("BUY-SIDE", LIQ_T, 215, 862, 26),
                  tag("SELL-SIDE", LIQ_T, 255, 1140, 26),
                  tag("BULLISH BREAKER", BRK_C, 500, 745, 26),
                  tag("BULLISH OB", OB_C, 600, 1418, 26),
                  tag("REJECTION BLOCK", REJ_C, 800, 466, 26)):
            self.add(t)

        self.add(Text("BREAKER BLOCK", font_size=KEY_SIZE, color=BRK_C, weight=BOLD)
                 .move_to(P(CX, 95 + 20)))
        card, _ = _recap_rows()
        self.add(card)
