# Voice Timeline

Audio: `voiceover.mpeg`
Duration: **135.63s** · Words: **342** · Sentences: **28** · Speaking speed: **151 WPM** · Language: **en**

## Word timestamps

Format: `start  word` (seconds). Emphasized words are marked in **bold** with their importance.

`0.03`  Have
`0.29`  you
`0.39`  ever
`0.57`  wondered
`0.99`  why
`1.21`  modern
`1.55`  servers
`1.91`  can
`2.09`  have
`2.29`  a
`2.33`  **100**  (emphasis: high)
`2.83`  gigabit
`3.21`  network
`3.56`  card,
`4.08`  but
`4.26`  still
`4.54`  struggle
`4.88`  to
`5.00`  process
`5.38`  every
`5.84`  packet
`6.20`  at
`6.30`  line
`6.52`  rate?
`7.46`  **The**  (emphasis: medium)
`7.66`  answer
`7.98`  isn't
`8.16`  that
`8.34`  Linux
`8.68`  is
`8.76`  slow.
`9.60`  It's
`9.74`  that
`9.92`  the
`10.04`  traditional
`10.54`  networking
`11.00`  path
`11.38`  does
`11.60`  a
`11.68`  lot
`11.98`  of
`12.10`  work
`12.40`  for
`12.56`  **every**  (emphasis: medium)
`13.13`  single
`13.47`  packet.
`14.57`  Let's
`14.75`  see
`14.87`  what
`15.03`  actually
`15.37`  happens.
`16.47`  A
`16.55`  packet
`16.87`  arrives
`17.15`  at
`17.23`  the
`17.33`  network
`17.67`  card.
`18.49`  Instead
`18.81`  of
`18.91`  your
`19.03`  application
`19.55`  receiving
`19.97`  it
`20.09`  immediately,
`21.15`  the
`21.30`  network
`21.68`  card
`21.95`  first
`22.26`  raises
`22.60`  **an**  (emphasis: medium)
`22.88`  interrupt
`23.30`  to
`23.44`  tell
`23.62`  the
`23.74`  **CPU,**  (emphasis: high)
`24.76`  a
`24.84`  packet
`25.14`  has
`25.26`  arrived.
`26.14`  The
`26.38`  **CPU**  (emphasis: medium)
`26.82`  stops
`27.18`  whatever
`27.58`  it
`27.68`  was
`27.82`  doing,
`28.30`  switches
`28.68`  into
`28.88`  kernel
`29.20`  mode,
`29.58`  and
`29.72`  starts
`30.09`  running
`30.34`  the
`30.46`  network
`30.85`  driver.
`32.03`  **That**  (emphasis: medium)
`32.37`  interruption
`32.87`  alone
`33.23`  has
`33.43`  a
`33.49`  **cost.**  (emphasis: medium)
`34.69`  **Next,**  (emphasis: medium)
`35.17`  the
`35.31`  packet
`35.65`  travels
`35.97`  through
`36.21`  multiple
`36.69`  layers
`36.97`  of
`37.05`  the
`37.17`  Linux
`37.51`  networking
`37.99`  stack.
`39.08`  **During**  (emphasis: medium)
`39.35`  this
`39.56`  journey,
`40.04`  the
`40.18`  packet
`40.54`  is
`40.68`  wrapped
`40.98`  in
`41.12`  kernel
`41.46`  data
`41.72`  structures,
`42.44`  **inspected,**  (emphasis: medium)
`43.50`  and
`43.68`  often
`43.98`  copied
`44.36`  into
`44.60`  different
`44.98`  memory
`45.32`  buffers
`45.80`  before
`46.12`  it
`46.24`  finally
`46.72`  reaches
`47.04`  your
`47.19`  application.
`48.47`  And
`48.59`  that's
`48.97`  another
`49.35`  source
`49.61`  of
`49.77`  overhead
`50.13`  **–**  (emphasis: high)
`50.51`  memory
`50.85`  copies.
`51.79`  Copying
`52.29`  thousands
`53.03`  or
`53.17`  even
`53.35`  millions
`53.85`  of
`53.97`  packets
`54.53`  every
`54.80`  second
`55.26`  consumes
`55.72`  valuable
`56.26`  **CPU**  (emphasis: medium)
`56.68`  cycles
`57.28`  and
`57.44`  memory
`57.80`  bandwidth.
`59.02`  **Finally,**  (emphasis: medium)
`59.69`  your
`59.89`  application
`60.39`  has
`60.57`  to
`60.73`  wake
`61.05`  up
`61.17`  to
`61.29`  process
`61.67`  the
`61.77`  packet.
`62.73`  That
`62.93`  means
`63.15`  another
`63.53`  context
`63.95`  switch,
`64.50`  from
`64.66`  the
`64.78`  kernel
`65.30`  back
`65.52`  to
`65.72`  user
`65.96`  space.
`66.88`  **Context**  (emphasis: medium)
`67.36`  switches
`67.78`  **save**  (emphasis: medium)
`68.10`  and
`68.24`  restore
`68.66`  **CPU**  (emphasis: medium)
`69.08`  state,
`69.64`  flush
`69.94`  caches,
`70.63`  and
`70.87`  add
`71.09`  more
`71.33`  latency.
`72.31`  **Now**  (emphasis: medium)
`72.81`  imagine
`73.15`  this
`73.37`  happening
`73.75`  not
`73.95`  **once,**  (emphasis: medium)
`74.65`  but
`74.94`  millions
`75.42`  of
`75.56`  times
`76.10`  every
`76.40`  **second.**  (emphasis: medium)
`77.62`  Interrupts,
`78.40`  **memory**  (emphasis: medium)
`78.76`  copies,
`79.38`  context
`79.84`  switches.
`80.97`  **Individually,**  (emphasis: medium)
`81.57`  they
`81.75`  seem
`82.05`  small.
`82.81`  Together,
`83.21`  they
`83.57`  become
`83.81`  the
`84.01`  biggest
`84.47`  bottleneck
`84.99`  in
`85.11`  high-performance
`85.83`  networking.
`87.06`  This
`87.26`  is
`87.36`  where
`87.56`  **DPDK**  (emphasis: medium)
`88.12`  changes
`88.50`  everything.
`89.52`  Instead
`89.98`  of
`90.08`  waiting
`90.40`  for
`90.58`  interrupts,
`91.27`  **DPDK**  (emphasis: high)
`91.89`  continuously
`92.63`  polls
`92.97`  the
`93.09`  network
`93.47`  card.
`94.35`  It
`94.49`  maps
`94.85`  packet
`95.19`  buffers
`95.59`  directly
`95.99`  into
`96.28`  user
`96.53`  space
`96.84`  memory
`97.40`  using
`97.68`  huge
`98.04`  **pages,**  (emphasis: medium)
`99.02`  **allowing**  (emphasis: medium)
`99.38`  the
`99.54`  application
`100.06`  to
`100.24`  access
`100.60`  packets
`101.12`  without
`101.46`  the
`101.62`  traditional
`102.21`  kernel
`102.51`  networking
`103.01`  stack.
`103.85`  The
`103.97`  result?
`104.97`  **No**  (emphasis: high)
`105.23`  per-packet
`105.81`  interrupts,
`106.57`  **no**  (emphasis: high)
`106.89`  unnecessary
`107.46`  memory
`107.78`  copies,
`108.64`  **almost**  (emphasis: medium)
`109.14`  **no**  (emphasis: medium)
`109.42`  context
`109.86`  switches.
`110.80`  The
`111.02`  **CPU**  (emphasis: high)
`111.46`  spends
`111.78`  its
`111.97`  time
`112.25`  processing
`112.79`  packets
`113.39`  instead
`113.71`  of
`113.83`  managing
`114.25`  operating
`114.77`  system
`115.17`  overhead.
`116.35`  That's
`116.63`  why
`116.83`  technologies
`117.50`  like
`117.70`  **DPDK**  (emphasis: high)
`118.46`  power
`118.82`  high-performance
`119.56`  firewalls,
`120.40`  load
`120.66`  balancers,
`121.64`  **telecom**  (emphasis: medium)
`122.09`  systems,
`122.73`  and
`122.91`  modern
`123.39`  cloud
`123.73`  networking.
`124.87`  Where
`125.05`  processing
`125.61`  millions
`126.06`  of
`126.16`  packets
`126.54`  per
`126.74`  second
`127.30`  isn't
`127.52`  just
`127.76`  an
`127.88`  optimization,
`128.94`  it's
`129.06`  a
`129.18`  requirement.
`130.72`  Once
`130.91`  you
`131.06`  understand
`131.59`  where
`131.81`  the
`131.93`  time
`132.15`  is
`132.29`  actually
`132.67`  spent,
`133.33`  the
`133.45`  performance
`134.03`  difference
`134.49`  becomes
`134.81`  obvious.

## Sentences

- `[0.03 – 6.72]` Have you ever wondered why modern servers can have a 100 gigabit network card, but still struggle to process every packet at line rate?
- `[7.46 – 9.04]` The answer isn't that Linux is slow.
- `[9.60 – 13.81]` It's that the traditional networking path does a lot of work for every single packet.
- `[14.57 – 15.67]` Let's see what actually happens.
- `[16.47 – 17.91]` A packet arrives at the network card.
- `[18.49 – 26.14]` Instead of your application receiving it immediately, the network card first raises an interrupt to tell the CPU, a packet has arrived.
- `[26.14 – 31.17]` The CPU stops whatever it was doing, switches into kernel mode, and starts running the network driver.
- `[32.03 – 33.79]` That interruption alone has a cost.
- `[34.69 – 38.29]` Next, the packet travels through multiple layers of the Linux networking stack.
- `[39.08 – 47.70]` During this journey, the packet is wrapped in kernel data structures, inspected, and often copied into different memory buffers before it finally reaches your application.
- `[48.47 – 51.79]` And that's another source of overhead – memory copies.
- `[51.79 – 58.22]` Copying thousands or even millions of packets every second consumes valuable CPU cycles and memory bandwidth.
- `[59.02 – 62.09]` Finally, your application has to wake up to process the packet.
- `[62.73 – 66.24]` That means another context switch, from the kernel back to user space.
- `[66.88 – 72.31]` Context switches save and restore CPU state, flush caches, and add more latency.
- `[72.31 – 77.60]` Now imagine this happening not once, but millions of times every second.
- `[77.62 – 80.20]` Interrupts, memory copies, context switches.
- `[80.97 – 82.35]` Individually, they seem small.
- `[82.81 – 86.34]` Together, they become the biggest bottleneck in high-performance networking.
- `[87.06 – 89.52]` This is where DPDK changes everything.
- `[89.52 – 93.69]` Instead of waiting for interrupts, DPDK continuously polls the network card.
- `[94.35 – 103.29]` It maps packet buffers directly into user space memory using huge pages, allowing the application to access packets without the traditional kernel networking stack.
- `[103.85 – 104.29]` The result?
- `[104.97 – 110.80]` No per-packet interrupts, no unnecessary memory copies, almost no context switches.
- `[110.80 – 115.53]` The CPU spends its time processing packets instead of managing operating system overhead.
- `[116.35 – 124.23]` That's why technologies like DPDK power high-performance firewalls, load balancers, telecom systems, and modern cloud networking.
- `[124.87 – 130.70]` Where processing millions of packets per second isn't just an optimization, it's a requirement.
- `[130.72 – 135.68]` Once you understand where the time is actually spent, the performance difference becomes obvious.

## Pauses

- `[3.79 – 4.08]` 0.28s (short)
- `[6.72 – 7.46]` 0.74s (long)
- `[9.04 – 9.60]` 0.56s (short)
- `[13.81 – 14.57]` 0.76s (long)
- `[15.67 – 16.47]` 0.80s (long)
- `[17.91 – 18.49]` 0.58s (short)
- `[20.61 – 21.15]` 0.54s (short)
- `[24.14 – 24.76]` 0.62s (long)
- `[28.04 – 28.30]` 0.26s (short)
- `[31.17 – 32.03]` 0.86s (long)
- `[33.79 – 34.69]` 0.90s (long)
- `[38.29 – 39.08]` 0.78s (long)
- `[42.18 – 42.44]` 0.26s (short)
- `[43.00 – 43.50]` 0.50s (short)
- `[47.70 – 48.47]` 0.76s (long)
- `[58.22 – 59.02]` 0.80s (long)
- `[62.09 – 62.73]` 0.64s (long)
- `[64.17 – 64.50]` 0.32s (short)
- `[66.24 – 66.88]` 0.64s (long)
- `[69.36 – 69.64]` 0.28s (short)
- `[74.35 – 74.65]` 0.30s (short)
- `[78.06 – 78.40]` 0.34s (short)
- `[80.20 – 80.97]` 0.76s (long)
- `[82.35 – 82.81]` 0.46s (short)
- `[86.34 – 87.06]` 0.72s (long)
- `[90.98 – 91.27]` 0.28s (short)
- `[93.69 – 94.35]` 0.66s (long)
- `[98.36 – 99.02]` 0.66s (long)
- `[103.29 – 103.85]` 0.56s (short)
- `[104.29 – 104.97]` 0.68s (long)
- `[106.19 – 106.57]` 0.38s (short)
- `[108.14 – 108.64]` 0.50s (short)
- `[115.53 – 116.35]` 0.82s (long)
- `[120.10 – 120.40]` 0.30s (short)
- `[121.18 – 121.64]` 0.46s (short)
- `[124.23 – 124.87]` 0.64s (long)
- `[128.56 – 128.94]` 0.38s (short)
- `[132.99 – 133.33]` 0.34s (short)

## Instructions for Claude

Synchronize every Manim animation with these timestamps.

- Visuals should begin slightly before the spoken keyword (start each animation about 0.15–0.30 s early).
- Finish each animation before the next important keyword begins.
- Use pauses for scene transitions — a long pause is a natural cut point.
- Use sentence boundaries for camera changes and section headers.
- Words marked **high** importance deserve the strongest visual moment (highlight, zoom, color flash); **medium** importance words deserve a secondary accent.
- Keep total scene durations aligned to the sentence spans above so audio and video never drift.
