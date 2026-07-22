# Voice Timeline

Audio: `voiceover.mpeg`
Duration: **217.81s** · Words: **579** · Sentences: **47** · Speaking speed: **159 WPM** · Language: **en**

## Word timestamps

Format: `start  word` (seconds). Emphasized words are marked in **bold** with their importance.

`0.03`  Imagine
`0.53`  you're
`0.71`  moving
`0.97`  an
`1.05`  entire
`1.55`  library
`2.03`  every
`2.65`  time
`2.89`  someone
`3.21`  wants
`3.41`  to
`3.51`  read
`3.75`  a
`3.83`  single
`4.21`  book.
`5.04`  You
`5.18`  pack
`5.60`  all
`5.74`  the
`5.86`  books
`6.06`  into
`6.32`  a
`6.36`  truck,
`6.86`  drive
`7.14`  them
`7.30`  to
`7.46`  a
`7.54`  new
`7.72`  building,
`8.30`  unload
`8.70`  them,
`9.20`  and
`9.34`  repeat
`9.66`  the
`9.76`  same
`9.98`  process
`10.42`  again
`10.76`  and
`10.96`  again.
`11.82`  **Sounds**  (emphasis: medium)
`12.16`  ridiculously
`12.90`  inefficient,
`13.38`  **right?**  (emphasis: medium)
`14.64`  That's
`14.90`  exactly
`15.43`  what
`15.65`  traditional
`16.11`  packet
`16.39`  processing
`16.83`  **does.**  (emphasis: high)
`17.85`  In
`17.93`  traditional
`18.37`  networking,
`18.99`  when
`19.17`  a
`19.23`  packet
`19.59`  travels
`19.95`  from
`20.11`  the
`20.25`  hardware
`20.83`  through
`21.09`  the
`21.23`  operating
`21.61`  system
`21.91`  kernel
`22.39`  and
`22.65`  up
`22.75`  to
`22.91`  an
`23.05`  application,
`24.07`  the
`24.27`  actual
`24.66`  bytes
`25.18`  are
`25.36`  copied
`25.76`  across
`26.06`  system
`26.32`  boundaries.
`27.24`  The
`27.48`  network
`27.84`  interface
`28.26`  card,
`28.68`  or
`28.88`  **NIC,**  (emphasis: high)
`29.72`  receives
`30.12`  the
`30.22`  packet
`30.60`  into
`30.82`  one
`31.08`  buffer.
`31.86`  Then
`32.09`  those
`32.35`  bytes
`32.67`  are
`32.81`  copied
`33.23`  into
`33.47`  another
`33.79`  buffer
`34.11`  for
`34.29`  **processing.**  (emphasis: medium)
`35.55`  **They**  (emphasis: medium)
`35.69`  may
`35.83`  be
`35.95`  copied
`36.33`  again
`36.61`  before
`36.93`  transmission.
`38.10`  **Every**  (emphasis: medium)
`38.48`  copy
`38.84`  consumes
`39.24`  **CPU**  (emphasis: medium)
`39.62`  cycles,
`40.26`  memory
`40.60`  bandwidth,
`41.20`  and
`41.36`  **cache.**  (emphasis: medium)
`42.42`  High
`42.78`  performance
`43.24`  networking
`43.73`  takes
`43.99`  a
`44.09`  completely
`44.89`  different
`45.21`  approach.
`46.27`  **Instead**  (emphasis: medium)
`46.59`  of
`46.71`  copying
`47.07`  the
`47.17`  packet,
`47.73`  it
`47.85`  simply
`48.25`  passes
`48.63`  a
`48.71`  reference
`49.11`  to
`49.27`  it.
`49.77`  This
`49.99`  technique
`50.43`  is
`50.53`  called
`50.85`  zero
`51.17`  copy.
`51.94`  But
`52.26`  what
`52.48`  exactly
`52.94`  is
`53.04`  being
`53.26`  passed?
`54.12`  The
`54.32`  answer
`54.88`  is
`55.00`  an
`55.18`  **mBuff.**  (emphasis: medium)
`56.24`  Think
`56.50`  of
`56.62`  an
`56.78`  mBuff
`57.18`  as
`57.28`  a
`57.42`  small
`57.82`  metadata
`58.34`  structure
`58.74`  attached
`59.12`  to
`59.22`  the
`59.32`  packet.
`60.28`  It
`60.40`  contains
`60.84`  information
`61.39`  like
`61.55`  the
`61.67`  packet
`62.01`  length,
`62.45`  protocol
`62.93`  details,
`63.69`  and
`63.89`  most
`64.21`  importantly,
`64.97`  the
`65.23`  **exact**  (emphasis: medium)
`65.77`  memory
`66.11`  address
`66.45`  where
`66.61`  the
`66.73`  packet's
`67.11`  payload
`67.47`  begins.
`68.39`  **Now**  (emphasis: medium)
`68.53`  let's
`68.75`  look
`68.97`  at
`69.15`  where
`69.39`  those
`69.66`  bytes
`69.97`  live.
`70.66`  Before
`71.16`  any
`71.38`  packet
`71.72`  even
`71.94`  arrives,
`72.74`  **DPDK**  (emphasis: high)
`73.52`  allocates
`74.02`  a
`74.12`  large
`74.52`  collection
`74.96`  of
`75.12`  fixed-size
`75.76`  packet
`76.06`  buffers.
`77.15`  This
`77.35`  collection
`77.85`  is
`77.97`  called
`78.25`  a
`78.33`  **mempool.**  (emphasis: medium)
`79.49`  You
`79.63`  can
`79.77`  think
`79.99`  of
`80.11`  it
`80.25`  as
`80.37`  a
`80.43`  warehouse
`81.03`  filled
`81.33`  with
`81.53`  thousands
`82.09`  of
`82.19`  empty
`82.58`  packet
`82.89`  containers
`83.72`  all
`83.92`  ready
`84.16`  to
`84.28`  be
`84.48`  used.
`85.24`  When
`85.40`  the
`85.62`  **NIC**  (emphasis: medium)
`85.96`  receives
`86.34`  a
`86.40`  packet,
`87.02`  it
`87.12`  doesn't
`87.42`  allocate
`87.82`  new
`88.00`  memory.
`88.76`  **Instead,**  (emphasis: medium)
`89.50`  the
`89.77`  **NIC**  (emphasis: medium)
`90.25`  uses
`90.55`  Direct
`91.07`  Memory
`91.45`  Access
`91.93`  or
`92.09`  **DMA**  (emphasis: high)
`92.87`  to
`93.05`  stream
`93.47`  the
`93.61`  incoming
`94.05`  bytes
`94.59`  straight
`95.03`  from
`95.21`  the
`95.31`  wire
`95.75`  directly
`96.26`  into
`96.52`  a
`96.66`  free
`96.90`  buffer
`97.24`  in
`97.32`  the
`97.42`  mempool.
`98.18`  **no**  (emphasis: high)
`98.58`  **CPU**  (emphasis: medium)
`98.96`  involvement,
`99.88`  **no**  (emphasis: medium)
`100.12`  dynamic
`100.54`  memory
`100.82`  allocation,
`101.83`  **no**  (emphasis: high)
`102.19`  unnecessary
`102.77`  **copies.**  (emphasis: medium)
`103.95`  **From**  (emphasis: medium)
`104.13`  this
`104.43`  moment
`104.81`  onward,
`105.45`  every
`105.81`  stage
`106.13`  of
`106.25`  packet
`106.56`  processing
`107.12`  works
`107.44`  with
`107.60`  the
`107.76`  same
`108.10`  packet
`108.42`  buffer.
`109.50`  The
`109.64`  passer
`110.06`  receives
`110.42`  the
`110.60`  mBuff.
`111.34`  The
`111.46`  classifier
`112.13`  receives
`112.51`  the
`112.65`  same
`112.97`  mBuff.
`113.87`  The
`114.03`  firewall
`114.73`  receives
`115.09`  the
`115.21`  same
`115.53`  mBuff.
`116.39`  The
`116.51`  routing
`116.88`  logic
`117.42`  receives
`117.78`  the
`117.96`  same
`118.30`  mBuff.
`119.24`  Each
`119.66`  component
`120.36`  **only**  (emphasis: medium)
`120.64`  receives
`121.14`  a
`121.24`  handle
`121.58`  that
`122.04`  points
`122.36`  to
`122.50`  the
`122.71`  original
`123.13`  packet
`123.43`  buffer.
`124.23`  The
`124.35`  packet
`124.67`  buffer
`125.19`  never
`125.47`  **moves.**  (emphasis: medium)
`126.63`  Even
`126.83`  if
`126.95`  a
`127.01`  router
`127.31`  needs
`127.53`  to
`127.67`  modify
`128.14`  a
`128.22`  header
`128.56`  **or**  (emphasis: medium)
`128.88`  change
`129.14`  an
`129.26`  address,
`130.10`  it
`130.26`  modifies
`130.76`  the
`130.90`  bytes
`131.44`  right
`131.78`  there
`132.02`  in
`132.16`  place.
`133.01`  They're
`133.23`  still
`133.51`  sitting
`133.83`  **exactly**  (emphasis: medium)
`134.55`  where
`134.79`  the
`134.95`  **NIC**  (emphasis: medium)
`135.43`  originally
`135.87`  placed
`136.15`  them.
`136.87`  This
`137.27`  is
`137.37`  the
`137.61`  **key**  (emphasis: medium)
`138.00`  idea
`138.35`  behind
`138.70`  zero
`138.98`  **copy.**  (emphasis: medium)
`139.92`  The
`140.06`  packet
`140.44`  isn't
`140.64`  travelling
`141.00`  through
`141.20`  the
`141.30`  system.
`142.08`  **Only**  (emphasis: medium)
`142.34`  the
`142.52`  pointer
`143.00`  is.
`143.70`  Passing
`144.08`  a
`144.16`  pointer
`144.69`  is
`144.81`  incredibly
`145.47`  cheap.
`146.05`  It's
`146.19`  typically
`146.61`  just
`146.91`  an
`147.01`  **8-byte**  (emphasis: medium)
`147.69`  memory
`148.03`  address
`148.49`  on
`148.61`  a
`148.65`  **64-bit**  (emphasis: medium)
`149.43`  system
`150.19`  compared
`150.63`  to
`150.77`  copying
`151.16`  hundreds
`151.80`  or
`151.94`  even
`152.12`  thousands
`152.80`  of
`152.94`  bytes
`153.32`  across
`153.62`  system
`153.96`  boundaries
`154.48`  for
`154.82`  every
`155.10`  packet.
`155.94`  Now
`156.30`  imagine
`156.70`  processing
`157.32`  millions
`157.78`  of
`157.91`  packets
`158.28`  every
`158.50`  second.
`159.53`  If
`159.77`  every
`160.07`  packet
`160.43`  required
`160.93`  multiple
`161.37`  memory
`161.71`  copies,
`162.47`  the
`162.63`  **CPU**  (emphasis: high)
`163.13`  would
`163.33`  spend
`163.75`  most
`164.09`  of
`164.23`  its
`164.39`  time
`164.65`  **moving**  (emphasis: medium)
`165.17`  bytes
`165.69`  instead
`166.01`  of
`166.16`  making
`166.50`  forwarding
`166.92`  decisions.
`168.06`  **By**  (emphasis: medium)
`168.30`  eliminating
`168.86`  those
`169.10`  copies,
`169.90`  **zero**  (emphasis: medium)
`170.26`  copy
`170.62`  dramatically
`171.44`  reduces
`171.90`  **CPU**  (emphasis: medium)
`172.34`  overhead,
`173.08`  **lowers**  (emphasis: medium)
`173.50`  memory
`173.84`  bandwidth
`174.33`  usage,
`175.13`  improves
`175.61`  cache
`175.89`  efficiency,
`176.81`  and
`176.97`  enables
`177.43`  applications
`178.09`  like
`178.31`  **DPDK**  (emphasis: high)
`179.09`  to
`179.27`  achieve
`179.69`  **tens**  (emphasis: medium)
`180.39`  or
`180.49`  even
`180.83`  hundreds
`181.47`  of
`181.59`  gigabits
`182.06`  per
`182.26`  second
`182.72`  on
`182.86`  modern
`183.22`  hardware.
`183.94`  Finally,
`184.62`  when
`184.84`  packet
`185.18`  processing
`185.66`  is
`185.78`  complete,
`186.58`  the
`186.80`  **NIC**  (emphasis: medium)
`187.28`  transmits
`187.91`  the
`188.03`  packet
`188.51`  using
`188.77`  the
`188.97`  exact
`189.47`  same
`189.73`  memory
`190.09`  buffer.
`191.15`  After
`191.41`  transmission,
`192.31`  that
`192.59`  buffer
`192.91`  is
`193.18`  returned
`193.53`  to
`193.64`  the
`193.76`  mempool,
`194.46`  ready
`194.74`  to
`194.86`  be
`195.00`  reused
`195.52`  for
`195.66`  the
`195.82`  next
`196.14`  incoming
`196.56`  packet.
`197.42`  The
`197.56`  packet
`197.88`  buffer
`198.20`  was
`198.36`  allocated
`198.97`  **only**  (emphasis: medium)
`199.41`  once.
`200.15`  It
`200.27`  was
`200.43`  never
`200.81`  copied.
`201.69`  **Only**  (emphasis: medium)
`201.97`  the
`202.31`  mBuff,
`202.87`  the
`203.05`  handle
`203.41`  to
`203.53`  that
`203.73`  **data,**  (emphasis: medium)
`204.44`  was
`204.72`  passed
`205.08`  from
`205.28`  **one**  (emphasis: medium)
`205.60`  component
`206.12`  to
`206.26`  another.
`207.04`  That's
`207.44`  why,
`207.68`  **in**  (emphasis: medium)
`207.99`  high-performance
`208.69`  networking,
`209.63`  a
`209.71`  packet
`210.12`  is
`210.30`  often
`210.64`  best
`210.92`  thought
`211.22`  of
`211.46`  not
`211.69`  as
`211.81`  a
`211.87`  collection
`212.27`  of
`212.41`  **bytes,**  (emphasis: medium)
`213.15`  but
`213.37`  as
`213.51`  a
`213.66`  pointer
`214.14`  to
`214.28`  those
`214.52`  **bytes.**  (emphasis: medium)
`215.81`  **And**  (emphasis: medium)
`216.01`  that's
`216.35`  the
`216.51`  essence
`216.89`  of
`216.99`  zero
`217.40`  copy.

## Sentences

- `[0.03 – 4.39]` Imagine you're moving an entire library every time someone wants to read a single book.
- `[5.04 – 11.20]` You pack all the books into a truck, drive them to a new building, unload them, and repeat the same process again and again.
- `[11.82 – 13.60]` Sounds ridiculously inefficient, right?
- `[14.64 – 17.83]` That's exactly what traditional packet processing does.
- `[17.85 – 27.24]` In traditional networking, when a packet travels from the hardware through the operating system kernel and up to an application, the actual bytes are copied across system boundaries.
- `[27.24 – 31.36]` The network interface card, or NIC, receives the packet into one buffer.
- `[31.86 – 34.77]` Then those bytes are copied into another buffer for processing.
- `[35.55 – 37.45]` They may be copied again before transmission.
- `[38.10 – 42.42]` Every copy consumes CPU cycles, memory bandwidth, and cache.
- `[42.42 – 45.53]` High performance networking takes a completely different approach.
- `[46.27 – 49.33]` Instead of copying the packet, it simply passes a reference to it.
- `[49.77 – 51.47]` This technique is called zero copy.
- `[51.94 – 53.60]` But what exactly is being passed?
- `[54.12 – 56.22]` The answer is an mBuff.
- `[56.24 – 59.62]` Think of an mBuff as a small metadata structure attached to the packet.
- `[60.28 – 67.77]` It contains information like the packet length, protocol details, and most importantly, the exact memory address where the packet's payload begins.
- `[68.39 – 70.66]` Now let's look at where those bytes live.
- `[70.66 – 76.41]` Before any packet even arrives, DPDK allocates a large collection of fixed-size packet buffers.
- `[77.15 – 78.83]` This collection is called a mempool.
- `[79.49 – 85.22]` You can think of it as a warehouse filled with thousands of empty packet containers all ready to be used.
- `[85.24 – 88.30]` When the NIC receives a packet, it doesn't allocate new memory.
- `[88.76 – 98.18]` Instead, the NIC uses Direct Memory Access or DMA to stream the incoming bytes straight from the wire directly into a free buffer in the mempool.
- `[98.18 – 103.13]` no CPU involvement, no dynamic memory allocation, no unnecessary copies.
- `[103.95 – 108.72]` From this moment onward, every stage of packet processing works with the same packet buffer.
- `[109.50 – 111.32]` The passer receives the mBuff.
- `[111.34 – 113.25]` The classifier receives the same mBuff.
- `[113.87 – 115.81]` The firewall receives the same mBuff.
- `[116.39 – 119.24]` The routing logic receives the same mBuff.
- `[119.24 – 123.71]` Each component only receives a handle that points to the original packet buffer.
- `[124.23 – 126.61]` The packet buffer never moves.
- `[126.63 – 132.42]` Even if a router needs to modify a header or change an address, it modifies the bytes right there in place.
- `[133.01 – 136.87]` They're still sitting exactly where the NIC originally placed them.
- `[136.87 – 139.26]` This is the key idea behind zero copy.
- `[139.92 – 141.58]` The packet isn't travelling through the system.
- `[142.08 – 143.10]` Only the pointer is.
- `[143.70 – 146.03]` Passing a pointer is incredibly cheap.
- `[146.05 – 155.94]` It's typically just an 8-byte memory address on a 64-bit system compared to copying hundreds or even thousands of bytes across system boundaries for every packet.
- `[155.94 – 158.79]` Now imagine processing millions of packets every second.
- `[159.53 – 167.34]` If every packet required multiple memory copies, the CPU would spend most of its time moving bytes instead of making forwarding decisions.
- `[168.06 – 183.94]` By eliminating those copies, zero copy dramatically reduces CPU overhead, lowers memory bandwidth usage, improves cache efficiency, and enables applications like DPDK to achieve tens or even hundreds of gigabits per second on modern hardware.
- `[183.94 – 190.37]` Finally, when packet processing is complete, the NIC transmits the packet using the exact same memory buffer.
- `[191.15 – 196.88]` After transmission, that buffer is returned to the mempool, ready to be reused for the next incoming packet.
- `[197.42 – 199.69]` The packet buffer was allocated only once.
- `[200.15 – 201.13]` It was never copied.
- `[201.69 – 207.04]` Only the mBuff, the handle to that data, was passed from one component to another.
- `[207.04 – 214.80]` That's why, in high-performance networking, a packet is often best thought of not as a collection of bytes, but as a pointer to those bytes.
- `[215.81 – 217.86]` And that's the essence of zero copy.

## Pauses

- `[4.39 – 5.04]` 0.64s (long)
- `[6.60 – 6.86]` 0.26s (short)
- `[8.04 – 8.30]` 0.26s (short)
- `[8.86 – 9.20]` 0.34s (short)
- `[11.20 – 11.82]` 0.62s (long)
- `[13.60 – 14.64]` 1.04s (long)
- `[23.55 – 24.07]` 0.52s (short)
- `[29.30 – 29.72]` 0.42s (short)
- `[31.36 – 31.86]` 0.50s (short)
- `[34.77 – 35.55]` 0.78s (long)
- `[37.45 – 38.10]` 0.64s (long)
- `[40.00 – 40.26]` 0.26s (short)
- `[45.53 – 46.27]` 0.74s (long)
- `[49.33 – 49.77]` 0.44s (short)
- `[51.47 – 51.94]` 0.46s (short)
- `[53.60 – 54.12]` 0.52s (short)
- `[59.62 – 60.28]` 0.66s (long)
- `[63.29 – 63.69]` 0.40s (short)
- `[67.77 – 68.39]` 0.62s (long)
- `[72.32 – 72.74]` 0.42s (short)
- `[76.41 – 77.15]` 0.74s (long)
- `[78.83 – 79.49]` 0.66s (long)
- `[83.38 – 83.72]` 0.34s (short)
- `[88.30 – 88.76]` 0.46s (short)
- `[89.12 – 89.50]` 0.38s (short)
- `[92.51 – 92.87]` 0.36s (short)
- `[94.31 – 94.59]` 0.28s (short)
- `[99.44 – 99.88]` 0.44s (short)
- `[101.28 – 101.83]` 0.54s (short)
- `[103.13 – 103.95]` 0.82s (long)
- `[105.15 – 105.45]` 0.30s (short)
- `[108.72 – 109.50]` 0.78s (long)
- `[113.25 – 113.87]` 0.62s (long)
- `[115.81 – 116.39]` 0.58s (short)
- `[117.16 – 117.42]` 0.26s (short)
- `[123.71 – 124.23]` 0.52s (short)
- `[129.60 – 130.10]` 0.50s (short)
- `[131.18 – 131.44]` 0.26s (short)
- `[132.42 – 133.01]` 0.58s (short)
- `[139.26 – 139.92]` 0.66s (long)
- `[141.58 – 142.08]` 0.50s (short)
- `[143.10 – 143.70]` 0.60s (short)
- `[149.73 – 150.19]` 0.46s (short)
- `[158.79 – 159.53]` 0.74s (long)
- `[162.05 – 162.47]` 0.42s (short)
- `[165.43 – 165.69]` 0.26s (short)
- `[167.34 – 168.06]` 0.72s (long)
- `[169.44 – 169.90]` 0.46s (short)
- `[172.70 – 173.08]` 0.38s (short)
- `[174.61 – 175.13]` 0.52s (short)
- `[176.45 – 176.81]` 0.36s (short)
- `[180.01 – 180.39]` 0.38s (short)
- `[186.18 – 186.58]` 0.40s (short)
- `[190.37 – 191.15]` 0.78s (long)
- `[191.93 – 192.31]` 0.38s (short)
- `[194.20 – 194.46]` 0.26s (short)
- `[196.88 – 197.42]` 0.54s (short)
- `[199.69 – 200.15]` 0.46s (short)
- `[201.13 – 201.69]` 0.56s (short)
- `[204.06 – 204.44]` 0.38s (short)
- `[209.19 – 209.63]` 0.44s (short)
- `[212.75 – 213.15]` 0.40s (short)
- `[214.80 – 215.81]` 1.01s (long)

## Instructions for Claude

Synchronize every Manim animation with these timestamps.

- Visuals should begin slightly before the spoken keyword (start each animation about 0.15–0.30 s early).
- Finish each animation before the next important keyword begins.
- Use pauses for scene transitions — a long pause is a natural cut point.
- Use sentence boundaries for camera changes and section headers.
- Words marked **high** importance deserve the strongest visual moment (highlight, zoom, color flash); **medium** importance words deserve a secondary accent.
- Keep total scene durations aligned to the sentence spans above so audio and video never drift.
