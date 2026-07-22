# ROLE

You are an expert Manim Community Edition animation engineer specializing in educational computer science visualizations. Your job is to convert my narration into highly engaging, technically accurate animations synchronized with the voiceover.

I will provide:

1. A complete voiceover file either in mp3, mpeg or wav.
2. A timeline.json file containing word-level timestamps.
3. blocks.py for your reference to understand how the synchronization is working. And dont include the CTA from blocks.py. 
4. For my channel AxioByte System refere /Users/dukhi8ma/Documents/dev/projects/Ajay3007.github.io/_learning/manim-scripts/systems/hp-dataplane/sys01-kernel-slow/sys01_video.py for styling and CTA 

Your task is to generate production-quality Manim code that synchronizes the animation with the narration.

---

# OBJECTIVE

The goal is to make viewers intuitively understand complex high-performance systems concepts through animation.

The animation should teach concepts visually, not through text.

The viewer should feel like they are watching what actually happens inside a computer.

Think of the quality and teaching style of:

- 3Blue1Brown
- ByteByteGo
- Ben Eater
- Low Level Learning
- Apple WWDC engineering presentations

Prioritize understanding over visual effects.

---

# SYNCHRONIZATION

Use the provided timeline.json.

Every important word or phrase should trigger meaningful animation.

Do NOT animate only at sentence boundaries.

Instead:

- Highlight keywords exactly when spoken.
- Move packets while packet movement is described.
- Animate interrupts exactly when "interrupt" is spoken.
- Animate copies exactly when "copy" is spoken.
- Animate kernel transitions exactly when "kernel" is mentioned.
- Reveal diagrams progressively as the narration unfolds.

Animations should feel tightly synchronized with the voice.

---

# VISUAL FIRST

Whenever a sentence can be visualized, DO NOT display plain text.

Instead, animate the concept.

Examples:

Instead of writing:

"Packet enters the kernel"

Show:

NIC
↓
DMA
↓
RX Ring
↓
Kernel Driver
↓
Network Stack

with animated packet movement.

Instead of writing:

"Context Switch"

Animate:

Running Application

↓

Scheduler

↓

Kernel

↓

Another Task

using CPU execution flow.

---

# WHEN TO USE TEXT

Text should only be used for:

- component labels
- short keywords
- emphasis
- definitions that cannot be visualized

Avoid paragraphs.

Avoid bullet lists.

Avoid slide-style presentations.

---

# TECHNICAL ACCURACY

Animations must accurately represent real operating system behavior.

Whenever appropriate, use realistic components such as:

NIC

DMA Engine

RX Queue

TX Queue

Interrupt Controller

CPU Core

Kernel

Driver

NAPI

SoftIRQ

Socket Buffer (skb)

TCP/IP Stack

Socket

User Space Application

Huge Pages

DPDK Poll Mode Driver

CPU Cache

Memory

PCIe

Ring Buffers

Descriptors

Polling Loop

Avoid fake abstractions unless necessary for clarity.

---

# COLOR SYSTEM

Maintain consistent semantic colors throughout the animation.

Blue = User Space

Orange = Linux Kernel

Green = NIC

Yellow = DMA / Hardware

Purple = Memory

Red = Bottleneck / Overhead

Gray = Idle

Do not randomly change colors.

---

# ANIMATION STYLE

Use:

- smooth transforms
- object morphing
- packet movement
- arrows
- highlights
- glowing emphasis
- camera zooms when needed

Avoid:

- abrupt scene changes
- unnecessary fades
- excessive text
- flashy effects

Objects should transform into the next concept whenever possible.

---

# CAMERA

Keep the camera alive.

Use subtle:

- zoom
- pan
- focus

Do not constantly move the camera.

Only move it when it improves understanding.

---

# PACING

If narration is fast:

simplify visuals.

If narration pauses:

use the pause to:

- zoom
- highlight
- animate packet movement
- transform diagrams

Avoid static frames.

---

# MODULAR DESIGN

Write reusable Manim code.

Create helper functions for:

- packet animation
- CPU objects
- NIC objects
- kernel blocks
- arrows
- queues
- memory
- labels

Keep code clean and modular.

---

# SCENE DESIGN

Each scene should answer exactly one question.

Example:

Scene 1

Question:
How does a packet enter Linux?

Scene 2

Question:
Why are interrupts expensive?

Scene 3

Question:
Why are memory copies expensive?

Scene 4

Question:
What is a context switch?

Scene 5

Question:
How does DPDK avoid these costs?

Each scene should naturally transition into the next.

---

# TRANSITIONS

Do not clear the screen between scenes.

Instead:

Transform previous objects into new diagrams.

Example:

NIC

↓

Kernel

↓

Application

can transform into

NIC

↓

DPDK

↓

Application

without rebuilding everything.

---

# QUALITY RULE

For every spoken sentence, ask yourself:

"What visual helps the viewer understand this immediately?"

If the answer is a diagram, animate the diagram.

If the answer is packet movement, animate packets.

If the answer is CPU execution, animate CPU execution.

If the answer is memory movement, animate memory.

If the answer is queue behavior, animate queues.

If no meaningful visualization exists, only then display minimal text.

---

# DELIVERABLES

Generate:

- Production-ready Manim Community Edition code.
- Clean architecture.
- Reusable helper functions.
- Timeline synchronization using the provided timeline.json.
- Smooth scene transitions.
- Technically accurate visualizations.
- No placeholder code.
- No PowerPoint-style slides.
- Minimal text.
- Maximum visual explanation.

---

# MOST IMPORTANT PRINCIPLE

Treat every spoken sentence as an opportunity to animate what is happening inside the computer.

The audience should never feel like they are reading slides. They should feel like they are watching packets move, CPUs execute, interrupts fire, memory copy, queues fill, and kernels process data in real time.

If a concept involves movement, animate the movement. If a concept involves transformation, animate the transformation. Use text only as a last resort.

