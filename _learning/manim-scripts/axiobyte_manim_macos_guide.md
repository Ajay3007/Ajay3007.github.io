# Running the AxioByte Manim scripts on macOS

This guide covers how to render the LeetCode animation scripts (e.g. `lc88_video.py` and `cover88_9x16.py`) on a Mac. There are two paths: just downloading the finished files, or setting up Manim to render and edit them yourself.

---

## Path 1 — Just get the finished video and cover (no install)

The `.mp4` video and `.png` cover are already rendered. Download them directly from the chat (each file card has a download button) and upload them to Instagram / YouTube as-is. You do not need Manim for this.

Use Path 2 only if you want to re-render, tweak colors/timing, or build new episodes.

---

## Path 2 — Set up Manim and render on your Mac

### Prerequisites

- macOS (Intel or Apple Silicon)
- Homebrew — the package manager. If you don't have it, install it from https://brew.sh
- These scripts use Manim's `Text` (not LaTeX), so **you do not need MacTeX** — you can skip the 4 GB LaTeX install that some Manim guides mention.

### Step 1 — Install the system dependencies

Run this first (it can take several minutes):

```bash
brew install py3cairo ffmpeg
```

Then, **only if you have an Apple Silicon Mac** (M1/M2/M3/M4), also run:

```bash
brew install pango pkg-config scipy
```

To check your chip:  → About This Mac → look at "Chip". If it says Intel, skip the second command.

### Step 2 — Install Manim in a virtual environment

On recent macOS, running `pip3 install manim` directly fails with an "externally-managed-environment" error because Homebrew's Python is locked down. The clean fix is a virtual environment. The version is pinned to match what the scripts were built and tested against:

```bash
python3 -m venv ~/manim-env
source ~/manim-env/bin/activate
pip install manim==0.20.1
```

You must run `source ~/manim-env/bin/activate` once in each new terminal session before rendering. When the venv is active you'll see `(manim-env)` at the start of your prompt.

### Step 3 — Fonts (do this for a pixel-perfect match)

The scripts specify `DejaVu Sans` and `DejaVu Sans Mono`, which macOS does not ship by default. If they're missing, Manim silently substitutes a system font and the spacing/sizing will drift. Two options:

**Option A — match the original output exactly (recommended).** Install the DejaVu fonts:

```bash
brew install --cask font-dejavu
```

If that cask name doesn't resolve, download the fonts from https://dejavu-fonts.github.io and double-click the `.ttf` files to install them via Font Book.

**Option B — no install.** Open each `.py` file and change the two font lines to macOS built-ins:

```python
FN = "Helvetica Neue"
MN = "Menlo"
```

Layout still works (text widths recompute automatically); it just won't be pixel-identical to the originals.

### Step 4 — Render

From the folder containing the scripts, with the venv active:

```bash
# The 33-second vertical video (1080x1920, 60fps)
manim -qh --fps 60 lc88_video.py LC88

# The 9:16 cover as a still image (-s renders only the last frame)
manim -s -qh cover88_9x16.py Cover88V
```

The two arguments are the file name and the Scene class name inside it.

### Where the files are saved

Manim creates a `media/` folder next to the scripts:

- Video → `media/videos/lc88_video/1920p60/LC88.mp4`
- Cover → `media/images/cover88_9x16/Cover88V_ManimCE_v0.20.1.png`

### Handy flags

- `-p` — auto-open the file when rendering finishes (e.g. `manim -qh -p --fps 60 lc88_video.py LC88`)
- `-o my_name` — set the output filename
- `-ql` — low quality, renders fast; use it for quick drafts while editing, then switch back to `-qh` for the final export
- `-qk` — 4K, if you ever want an ultra-high-res export

---

## Rendering future episodes

Every episode follows the same pattern — a `.py` file with one Scene class:

```bash
manim -qh --fps 60 <script_file>.py <SceneClassName>
```

For a still cover, add `-s`:

```bash
manim -s -qh <cover_file>.py <SceneClassName>
```

---

## Troubleshooting

- **`error: externally-managed-environment` when installing** — you skipped the virtual environment. Run the Step 2 commands. (Quick alternative if you don't want a venv: `pip install manim==0.20.1 --break-system-packages`.)
- **`command not found: manim`** — the virtual environment isn't active. Run `source ~/manim-env/bin/activate` in the current terminal.
- **`Unknown encoder 'libx264'`** — an ffmpeg issue. Reinstall it: `brew reinstall ffmpeg`.
- **Text looks wrong / spacing is off** — the DejaVu fonts aren't installed. Do Step 3 Option A, or switch the fonts per Option B.
- **Rendering feels slow** — use `-ql` while iterating; only render `-qh` for the final version.

---

## One-shot setup (copy-paste)

For an Apple Silicon Mac with Homebrew already installed:

```bash
brew install py3cairo ffmpeg pango pkg-config scipy
brew install --cask font-dejavu
python3 -m venv ~/manim-env
source ~/manim-env/bin/activate
pip install manim==0.20.1
# then, from the folder with the scripts:
manim -qh -p --fps 60 lc88_video.py LC88
manim -s -qh -p cover88_9x16.py Cover88V
```

On an Intel Mac, drop `pango pkg-config scipy` from the first line.
