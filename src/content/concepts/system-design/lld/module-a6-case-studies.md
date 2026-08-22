---
title: "Module A6 — LLD Case Studies | LLD Track"
description: "SYSTEM DESIGN MASTERY COURSE TRACK A · LLD · MODULE A6 · WEEKS 9–10 FINAL LLD MODULE Low-Level Design · Case Studies · All Patterns Applied LLD CASE STUDIES Chess · Elevator ·…"
domain: system-design
track: system-design-lld
order: 12
url: /learning/system-design/lld/module-a6-case-studies/
---

<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400;500&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<!-- MASTHEAD -->
<header>
  <div class="mast-top">
    <span>SYSTEM DESIGN MASTERY COURSE</span>
    <span>TRACK A · LLD · MODULE A6 · WEEKS 9–10</span>
    <span>FINAL LLD MODULE</span>
  </div>
  <div class="mast-title">
    <div class="mast-kicker">Low-Level Design · Case Studies · All Patterns Applied</div>
    <div class="mast-h1">LLD <span>CASE</span><br>STUDIES</div>
    <div class="mast-sub">Chess · Elevator · Library · Food Ordering · ATM · Hotel Booking</div>
  </div>
  <div class="mast-cols">
    <div class="mast-col"><div class="mast-col-val">6</div>Case Studies</div>
    <div class="mast-col"><div class="mast-col-val">15+</div>Patterns Used</div>
    <div class="mast-col"><div class="mast-col-val">4</div>Tasks</div>
    <div class="mast-col"><div class="mast-col-val">1</div>Capstone</div>
    <div class="mast-col"><div class="mast-col-val">A6</div>Module</div>
    <div class="mast-col"><div class="mast-col-val">✓</div>Track A End</div>
  </div>
</header>

<nav class="nav">
  <div class="nav-tab active" onclick="show('overview',this)">Overview</div>
  <div class="nav-tab" onclick="show('cases',this)">Case Studies</div>
  <div class="nav-tab" onclick="show('framework',this)">Interview Framework</div>
  <div class="nav-tab" onclick="show('anti',this)">Anti-Patterns</div>
  <div class="nav-tab" onclick="show('tasks',this)">Tasks</div>
  <div class="nav-tab" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- ===== OVERVIEW ===== -->
<div class="view active" id="view-overview">
  <div class="rule-hd"><span>Six systems · all Track A patterns applied</span><span>CLICK CARD TO DEEP DIVE</span></div>

  <div class="front-grid">
    <div class="front-card" onclick="goCase(0)">
      <div class="fc-num" style="color:var(--c1)">01</div>
      <div class="fc-title">Chess Game</div>
      <div class="fc-patterns">State · Command · Observer · Factory</div>
      <div class="fc-challenge">Move validation without revealing Board internals. Undo last N moves. Check/checkmate detection by simulation.</div>
    </div>
    <div class="front-card" onclick="goCase(1)">
      <div class="fc-num" style="color:var(--c2)">02</div>
      <div class="fc-title">Elevator System</div>
      <div class="fc-patterns">State · Strategy · Observer · Concurrent</div>
      <div class="fc-challenge">LOOK algorithm. Multiple elevators sharing floor requests. Concurrent calls from many floors simultaneously.</div>
    </div>
    <div class="front-card" onclick="goCase(2)">
      <div class="fc-num" style="color:var(--c3)">03</div>
      <div class="fc-title">Library Management</div>
      <div class="fc-patterns">Builder · Observer · Iterator · Concurrent</div>
      <div class="fc-challenge">Reservation queue per book. Fine calculation. Thread-safe borrowBook() when one copy remains.</div>
    </div>
    <div class="front-card" onclick="goCase(3)">
      <div class="fc-num" style="color:var(--c4)">04</div>
      <div class="fc-title">Food Ordering</div>
      <div class="fc-patterns">Facade · Strategy · Observer · CoR · State</div>
      <div class="fc-challenge">Order lifecycle state machine. Surge pricing. CoR pipeline: validate→price→pay→dispatch→notify.</div>
    </div>
    <div class="front-card" onclick="goCase(4)">
      <div class="fc-num" style="color:var(--c5)">05</div>
      <div class="fc-title">ATM Machine</div>
      <div class="fc-patterns">State · Chain of Resp. · Command · Observer</div>
      <div class="fc-challenge">PIN retry lock. Transaction atomicity. Cash dispensing chain. What if network fails mid-dispense?</div>
    </div>
    <div class="front-card" onclick="goCase(5)">
      <div class="fc-num" style="color:var(--c6)">06</div>
      <div class="fc-title">Hotel Booking</div>
      <div class="fc-patterns">Builder · Strategy · Observer · Concurrent</div>
      <div class="fc-challenge">Concurrent room booking with date-range contention. Dynamic pricing. Reservation waitlist.</div>
    </div>
  </div>

  <div class="rule-hd"><span>Pattern → Problem mapping</span></div>
  <table class="int-table">
    <thead><tr><th>SYSTEM</th><th>KEY PATTERN</th><th>CONCURRENCY CONCERN</th><th>KILLER INTERVIEW QUESTION</th></tr></thead>
    <tbody>
      <tr><td>Chess</td><td>Command (move+undo), State (game phase)</td><td>Single-player — no concurrency</td><td>"How do you detect checkmate efficiently?"</td></tr>
      <tr><td>Elevator</td><td>State (per elevator), Strategy (LOOK algo)</td><td>Concurrent floor requests → ReentrantLock per elevator</td><td>"How do you handle 1000 floors and 20 elevators?"</td></tr>
      <tr><td>Library</td><td>Builder (Book), Observer (availability)</td><td>synchronized(book) for last-copy race</td><td>"Thread safety of borrowBook() when one copy remains?"</td></tr>
      <tr><td>Food Ordering</td><td>CoR (pipeline), State (order lifecycle)</td><td>Idempotent payment retry, order status updates</td><td>"How to add a new payment method without touching OrderService?"</td></tr>
      <tr><td>ATM</td><td>State (transaction), CoR (dispensing)</td><td>ReentrantLock on account debit+dispense atomicity</td><td>"What happens if network fails after debit but before dispense?"</td></tr>
      <tr><td>Hotel</td><td>Builder (SearchCriteria), Strategy (pricing)</td><td>ReentrantLock per room for date-range booking</td><td>"10,000 users try to book the last room simultaneously?"</td></tr>
    </tbody>
  </table>
</div>

<!-- ===== CASE STUDIES ===== -->
<div class="view" id="view-cases">
  <div class="case-tabs">
    <div class="ct-btn active" id="cb0" onclick="selCase(0)"><span class="cnum" style="color:var(--c1)">01</span>Chess</div>
    <div class="ct-btn" id="cb1" onclick="selCase(1)"><span class="cnum" style="color:var(--c2)">02</span>Elevator</div>
    <div class="ct-btn" id="cb2" onclick="selCase(2)"><span class="cnum" style="color:var(--c3)">03</span>Library</div>
    <div class="ct-btn" id="cb3" onclick="selCase(3)"><span class="cnum" style="color:var(--c4)">04</span>Food</div>
    <div class="ct-btn" id="cb4" onclick="selCase(4)"><span class="cnum" style="color:var(--c5)">05</span>ATM</div>
    <div class="ct-btn" id="cb5" onclick="selCase(5)"><span class="cnum" style="color:var(--c6)">06</span>Hotel</div>
  </div>

  <!-- CHESS -->
  <div class="case-panel active" id="cp0">
    <div class="case-mast" style="border-top:4px solid var(--c1)">
      <div class="cm-number">01</div>
      <div class="cm-title">Chess Game</div>
      <div class="cm-sub">STATE · COMMAND · OBSERVER · FACTORY METHOD</div>
      <div class="cm-desc" style="border-left-color:var(--c1)">2 players, 8×8 board, 6 piece types. Move validation per piece. Check/checkmate detection by simulation. Undo last N moves. Game state serialization.</div>
    </div>
    <div class="state-flow">
      <div class="sf-state">WAITING</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">start</span></div>
      <div class="sf-state">WHITE_TURN</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">valid move</span></div>
      <div class="sf-state">BLACK_TURN</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">check</span></div>
      <div class="sf-state" style="border-color:var(--amber);color:var(--amber)">CHECK</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">no escape</span></div>
      <div class="sf-state" style="border-color:var(--red);color:var(--red)">CHECKMATE</div>
    </div>
    <div class="pat-grid">
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c1)">Command — Move</div>
        <div class="pat-why">Each Move is a Command with execute() + undo(). Stores captured piece + firstMove state for perfect undo. History stack enables N-move rollback.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c1)">Factory Method — Piece</div>
        <div class="pat-why">PieceFactory.create(type, color, pos) returns correct subclass. Client code never does new King() — decoupled from piece hierarchy.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c1)">Observer — Game Events</div>
        <div class="pat-why">ChessGame notifies GameObserver on: moveMade, check, checkmate, gameOver. UI and sound engine are observers — completely decoupled.</div>
      </div>
    </div>
    <div class="code-block">
      <div class="code-hdr">Move.java — Command pattern with undo<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">Move</span> <span class="kw">implements</span> <span class="cls">Command</span> {
    <span class="kw">private final</span> <span class="cls">Piece</span>    piece;
    <span class="kw">private final</span> <span class="cls">Position</span> from, to;
    <span class="kw">private</span>       <span class="cls">Piece</span>    capturedPiece;  <span class="cm">// Saved for undo</span>
    <span class="kw">private</span>       <span class="kw">boolean</span>  wasFirstMove;   <span class="cm">// Pawn/king special rules</span>

    <span class="kw">public void</span> <span class="fn">execute</span>(<span class="cls">Board</span> board) {
        capturedPiece = board.<span class="fn">getPiece</span>(to);
        wasFirstMove  = piece.<span class="fn">isFirstMove</span>();
        board.<span class="fn">setPiece</span>(to, piece);  board.<span class="fn">setPiece</span>(from, <span class="kw">null</span>);
        piece.<span class="fn">setPosition</span>(to);     piece.<span class="fn">setFirstMove</span>(<span class="kw">false</span>);
    }

    <span class="kw">public void</span> <span class="fn">undo</span>(<span class="cls">Board</span> board) {
        board.<span class="fn">setPiece</span>(from, piece);          <span class="cm">// Restore moving piece</span>
        board.<span class="fn">setPiece</span>(to, capturedPiece);     <span class="cm">// Restore captured piece (null if none)</span>
        piece.<span class="fn">setPosition</span>(from);
        piece.<span class="fn">setFirstMove</span>(wasFirstMove);
    }
}

<span class="cm">// Checkmate detection — simulate all moves, check none escape check</span>
<span class="kw">public boolean</span> <span class="fn">isCheckmate</span>(<span class="cls">Board</span> board, <span class="cls">PieceColor</span> color) {
    <span class="kw">if</span> (!<span class="fn">isCheck</span>(board, color)) <span class="kw">return false</span>;
    <span class="kw">return</span> <span class="fn">getAllPieces</span>(board, color).stream()
        .<span class="fn">flatMap</span>(p -> p.<span class="fn">validMoves</span>(board).stream()
            .<span class="fn">map</span>(to -> <span class="kw">new</span> <span class="cls">Move</span>(p, p.<span class="fn">getPosition</span>(), to)))
        .<span class="fn">noneMatch</span>(m -> !<span class="fn">wouldLeaveKingInCheck</span>(m, board, color));
}</pre>
    </div>
  </div>

  <!-- ELEVATOR -->
  <div class="case-panel" id="cp1">
    <div class="case-mast" style="border-top:4px solid var(--c2)">
      <div class="cm-number">02</div>
      <div class="cm-title">Elevator System</div>
      <div class="cm-sub">STATE · STRATEGY (LOOK) · OBSERVER · CONCURRENT</div>
      <div class="cm-desc" style="border-left-color:var(--c2)">N elevators, M floors. LOOK algorithm (sweep up then down). Concurrent floor requests. Pluggable selection strategy for different scheduling algorithms.</div>
    </div>
    <div class="state-flow">
      <div class="sf-state">IDLE</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">request</span></div>
      <div class="sf-state" style="border-color:var(--blue);color:var(--blue)">MOVING_UP</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">floor reached</span></div>
      <div class="sf-state" style="border-color:var(--green);color:var(--green)">STOPPED_OPEN</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">no more up</span></div>
      <div class="sf-state" style="border-color:var(--red);color:var(--red)">MOVING_DOWN</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">done</span></div>
      <div class="sf-state">IDLE</div>
    </div>
    <div class="pat-grid">
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c2)">State — per Elevator</div>
        <div class="pat-why">Each elevator holds a state (IDLE/MOVING_UP/MOVING_DOWN/STOPPED). step() transitions automatically. No giant switch statement.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c2)">Strategy — Scheduling</div>
        <div class="pat-why">ElevatorSelectionStrategy is injected into ElevatorController. Swap LOOK for FCFS or zone-based strategy without changing controller.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c2)">Concurrency — ReentrantLock</div>
        <div class="pat-why">Each Elevator has its own ReentrantLock. addRequest() and step() are both synchronized per elevator — no contention between elevators.</div>
      </div>
    </div>
    <div class="code-block">
      <div class="code-hdr">Elevator.java — LOOK algorithm + concurrent requests<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">Elevator</span> {
    <span class="kw">private final</span> <span class="cls">TreeSet</span>&lt;<span class="cls">Integer</span>&gt; upRequests   = <span class="kw">new</span> <span class="cls">TreeSet</span>&lt;&gt;();
    <span class="kw">private final</span> <span class="cls">TreeSet</span>&lt;<span class="cls">Integer</span>&gt; downRequests = <span class="kw">new</span> <span class="cls">TreeSet</span>&lt;&gt;(<span class="cls">Comparator</span>.<span class="fn">reverseOrder</span>());
    <span class="kw">private final</span> <span class="cls">ReentrantLock</span>  lock = <span class="kw">new</span> <span class="cls">ReentrantLock</span>();
    <span class="kw">private</span>       <span class="cls">ElevatorState</span>  state = <span class="cls">ElevatorState</span>.IDLE;
    <span class="kw">private int</span>                   currentFloor = <span class="num">1</span>;

    <span class="cm">// LOOK: service all requests in current direction, then reverse</span>
    <span class="kw">public void</span> <span class="fn">step</span>() {
        lock.<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="kw">switch</span> (state) {
                <span class="kw">case</span> MOVING_UP -> {
                    <span class="kw">if</span> (!upRequests.<span class="fn">isEmpty</span>()) {
                        currentFloor = upRequests.<span class="fn">first</span>();  <span class="cm">// next floor up</span>
                        upRequests.<span class="fn">remove</span>(currentFloor);
                        state = <span class="cls">ElevatorState</span>.STOPPED_OPEN;
                    } <span class="kw">else if</span> (!downRequests.<span class="fn">isEmpty</span>()) {
                        state = <span class="cls">ElevatorState</span>.MOVING_DOWN;  <span class="cm">// reverse</span>
                    } <span class="kw">else</span> { state = <span class="cls">ElevatorState</span>.IDLE; }
                }
                <span class="cm">/* ... MOVING_DOWN, STOPPED_OPEN, IDLE cases ... */</span>
            }
        } <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
    }
}</pre>
    </div>
  </div>

  <!-- LIBRARY -->
  <div class="case-panel" id="cp2">
    <div class="case-mast" style="border-top:4px solid var(--c3)">
      <div class="cm-number">03</div>
      <div class="cm-title">Library Management</div>
      <div class="cm-sub">BUILDER · OBSERVER · ITERATOR · CONCURRENCY</div>
      <div class="cm-desc" style="border-left-color:var(--c3)">Book catalog, member management, borrowing/returning with fine calculation. Reservation queue notifies next member when book becomes available.</div>
    </div>
    <div class="pat-grid">
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c3)">Builder — Book</div>
        <div class="pat-why">Book has many optional attributes (genre, publisher, year). Builder prevents telescoping constructors and makes required fields explicit.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c3)">Observer — Availability</div>
        <div class="pat-why">returnBook() triggers notification to next member in reservation queue. LibraryObserver decouples notification mechanism from core borrow logic.</div>
      </div>
      <div class="pat-chip">
        <div class="pat-name" style="color:var(--c3)">Concurrency</div>
        <div class="pat-why">synchronized(book) for last-copy race condition. ConcurrentLinkedQueue for reservation queue — safe concurrent enqueue/dequeue.</div>
      </div>
    </div>
    <div class="code-block">
      <div class="code-hdr">LibrarySystem.java — thread-safe last copy borrowing<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">public boolean</span> <span class="fn">borrowBook</span>(<span class="cls">String</span> isbn, <span class="cls">Member</span> member) {
    <span class="cls">Book</span> book = catalog.<span class="fn">get</span>(isbn);
    <span class="kw">if</span> (book == <span class="kw">null</span>) <span class="kw">throw new</span> <span class="cls">BookNotFoundException</span>(isbn);

    <span class="kw">if</span> (book.<span class="fn">getAvailable</span>() == <span class="num">0</span>) {
        reservations.<span class="fn">reserve</span>(book, member);  <span class="cm">// Join waitlist</span>
        <span class="kw">return false</span>;
    }

    <span class="cm">// Synchronize on book object — prevents two threads taking last copy</span>
    <span class="kw">synchronized</span> (book) {
        <span class="kw">if</span> (book.<span class="fn">getAvailable</span>() == <span class="num">0</span>) {  <span class="cm">// Double-check after sync</span>
            reservations.<span class="fn">reserve</span>(book, member);
            <span class="kw">return false</span>;
        }
        book.<span class="fn">decrementAvailable</span>();
    }
    activeBorrow.<span class="fn">put</span>(member.id+<span class="str">":"</span>+isbn, <span class="kw">new</span> <span class="cls">Borrowing</span>(book, member));
    <span class="kw">return true</span>;
}

<span class="kw">public void</span> <span class="fn">returnBook</span>(<span class="cls">String</span> isbn, <span class="cls">Member</span> member) {
    <span class="cls">Borrowing</span> b = activeBorrow.<span class="fn">remove</span>(member.id+<span class="str">":"</span>+isbn);
    b.<span class="fn">markReturned</span>();
    <span class="kw">synchronized</span> (b.<span class="fn">getBook</span>()) { b.<span class="fn">getBook</span>().<span class="fn">incrementAvailable</span>(); }
    <span class="cm">// Notify next in queue</span>
    reservations.<span class="fn">nextInQueue</span>(book).<span class="fn">ifPresent</span>(next ->
        observers.<span class="fn">forEach</span>(o -> o.<span class="fn">onBookAvailable</span>(book, next)));
}</pre>
    </div>
  </div>

  <!-- FOOD -->
  <div class="case-panel" id="cp3">
    <div class="case-mast" style="border-top:4px solid var(--c4)">
      <div class="cm-number">04</div>
      <div class="cm-title">Online Food Ordering</div>
      <div class="cm-sub">FACADE · STRATEGY · OBSERVER · CHAIN OF RESPONSIBILITY · STATE</div>
      <div class="cm-desc" style="border-left-color:var(--c4)">Complete order lifecycle state machine. Surge pricing strategy. CoR processing pipeline: validate → price → payment → delivery assignment → notification.</div>
    </div>
    <div class="state-flow">
      <div class="sf-state">PLACED</div>
      <div class="sf-arrow"><span>→</span></div>
      <div class="sf-state">ACCEPTED</div>
      <div class="sf-arrow"><span>→</span></div>
      <div class="sf-state">PREPARING</div>
      <div class="sf-arrow"><span>→</span></div>
      <div class="sf-state">READY</div>
      <div class="sf-arrow"><span>→</span></div>
      <div class="sf-state">PICKED_UP</div>
      <div class="sf-arrow"><span>→</span></div>
      <div class="sf-state" style="border-color:var(--green);color:var(--green)">DELIVERED</div>
    </div>
    <div class="code-block">
      <div class="code-hdr">OrderService.java — CoR pipeline + Strategy<span class="clang">JAVA</span></div>
<pre class="code"><span class="cm">// Chain: Validation → Payment → Delivery → Notification</span>
<span class="cls">OrderHandler</span> chain = <span class="kw">new</span> <span class="cls">ValidationHandler</span>();
chain.<span class="fn">setNext</span>(<span class="kw">new</span> <span class="cls">PaymentHandler</span>(paymentService))
     .<span class="fn">setNext</span>(<span class="kw">new</span> <span class="cls">DeliveryAssignmentHandler</span>(deliveryService))
     .<span class="fn">setNext</span>(<span class="kw">new</span> <span class="cls">NotificationHandler</span>(notifier));

<span class="cm">// STRATEGY: surge pricing (pluggable at runtime)</span>
<span class="kw">class</span> <span class="cls">SurgePricingStrategy</span> <span class="kw">implements</span> <span class="cls">PricingStrategy</span> {
    <span class="kw">public double</span> <span class="fn">calculateTotal</span>(<span class="cls">Order</span> order) {
        <span class="kw">double</span> base  = order.<span class="fn">getItems</span>().<span class="fn">stream</span>().<span class="fn">mapToDouble</span>(<span class="cls">Item</span>::<span class="fn">getPrice</span>).<span class="fn">sum</span>();
        <span class="kw">double</span> surge = <span class="fn">isPeakHour</span>(order.<span class="fn">getTime</span>()) ? <span class="num">1.3</span> : <span class="num">1.0</span>;
        <span class="kw">return</span> base * surge + DELIVERY_FEE;
    }
}

<span class="cm">// Add new payment method: new class implementing PaymentHandler</span>
<span class="cm">// No changes to ValidationHandler, DeliveryHandler, NotificationHandler (OCP)</span></pre>
    </div>
  </div>

  <!-- ATM -->
  <div class="case-panel" id="cp4">
    <div class="case-mast" style="border-top:4px solid var(--c5)">
      <div class="cm-number">05</div>
      <div class="cm-title">ATM Machine</div>
      <div class="cm-sub">STATE · CHAIN OF RESPONSIBILITY · COMMAND · OBSERVER</div>
      <div class="cm-desc" style="border-left-color:var(--c5)">PIN retry lockout, transaction atomicity, cash dispensing via CoR. Command enables transaction reversal if dispense fails after debit.</div>
    </div>
    <div class="state-flow">
      <div class="sf-state">IDLE</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">insert card</span></div>
      <div class="sf-state">CARD_IN</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">correct PIN</span></div>
      <div class="sf-state">AUTH</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">select txn</span></div>
      <div class="sf-state">TXN_SELECTED</div>
      <div class="sf-arrow"><span>→</span><span class="sf-label">dispense</span></div>
      <div class="sf-state" style="border-color:var(--green);color:var(--green)">COMPLETE</div>
    </div>
    <div class="code-block">
      <div class="code-hdr">ATM — PIN retry + transaction atomicity<span class="clang">JAVA</span></div>
<pre class="code"><span class="cm">// PIN retry: 3 attempts then card retained</span>
<span class="kw">class</span> <span class="cls">CardInsertedState</span> <span class="kw">implements</span> <span class="cls">ATMState</span> {
    <span class="kw">private int</span> attempts = <span class="num">0</span>;

    <span class="kw">public void</span> <span class="fn">enterPin</span>(<span class="cls">ATM</span> atm, <span class="cls">String</span> pin) {
        <span class="kw">if</span> (atm.<span class="fn">getBank</span>().<span class="fn">verifyPin</span>(atm.<span class="fn">getCurrentCard</span>(), pin)) {
            atm.<span class="fn">setState</span>(<span class="kw">new</span> <span class="cls">AuthenticatedState</span>());
        } <span class="kw">else if</span> (++attempts >= <span class="num">3</span>) {
            atm.<span class="fn">getCardReader</span>().<span class="fn">retainCard</span>();  <span class="cm">// Swallow card</span>
            atm.<span class="fn">setState</span>(<span class="kw">new</span> <span class="cls">IdleState</span>());
            atm.<span class="fn">display</span>(<span class="str">"Card retained — 3 failed attempts"</span>);
        }
    }
}

<span class="cm">// Transaction atomicity: debit then dispense</span>
<span class="cm">// If dispense fails → undo() credits account back</span>
<span class="kw">class</span> <span class="cls">WithdrawalCommand</span> <span class="kw">implements</span> <span class="cls">Command</span> {
    <span class="kw">public void</span> <span class="fn">execute</span>() {
        account.<span class="fn">debit</span>(amount);   <span class="cm">// 1. Debit</span>
        dispenser.<span class="fn">dispense</span>(amount); <span class="cm">// 2. Dispense (may fail)</span>
    }
    <span class="kw">public void</span> <span class="fn">undo</span>() {
        account.<span class="fn">credit</span>(amount);  <span class="cm">// Reversal if dispense failed</span>
        <span class="fn">logReversal</span>(transactionId);
    }
}</pre>
    </div>
  </div>

  <!-- HOTEL -->
  <div class="case-panel" id="cp5">
    <div class="case-mast" style="border-top:4px solid var(--c6)">
      <div class="cm-number">06</div>
      <div class="cm-title">Hotel Booking System</div>
      <div class="cm-sub">BUILDER · STRATEGY · OBSERVER · CONCURRENCY</div>
      <div class="cm-desc" style="border-left-color:var(--c6)">Concurrent room booking with date-range contention. Dynamic pricing (weekend/occupancy surge). Reservation waitlist with Observer notification.</div>
    </div>
    <div class="code-block">
      <div class="code-hdr">Room.java — thread-safe date-range booking<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">Room</span> {
    <span class="kw">private final</span> <span class="cls">ReentrantLock</span> lock       = <span class="kw">new</span> <span class="cls">ReentrantLock</span>();
    <span class="kw">private final</span> <span class="cls">Set</span>&lt;<span class="cls">LocalDate</span>&gt; booked    = <span class="kw">new</span> <span class="cls">HashSet</span>&lt;&gt;();

    <span class="kw">public boolean</span> <span class="fn">tryBook</span>(<span class="cls">LocalDate</span> in, <span class="cls">LocalDate</span> out) {
        lock.<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="cls">List</span>&lt;<span class="cls">LocalDate</span>&gt; dates = in.<span class="fn">datesUntil</span>(out).<span class="fn">collect</span>(<span class="fn">toList</span>());
            <span class="kw">if</span> (dates.<span class="fn">stream</span>().<span class="fn">anyMatch</span>(booked::<span class="fn">contains</span>)) <span class="kw">return false</span>;
            booked.<span class="fn">addAll</span>(dates);  <span class="kw">return true</span>;
        } <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
    }
}

<span class="cm">// Dynamic pricing strategy</span>
<span class="kw">class</span> <span class="cls">DynamicPricingStrategy</span> <span class="kw">implements</span> <span class="cls">PricingStrategy</span> {
    <span class="kw">public double</span> <span class="fn">getPrice</span>(<span class="cls">Room</span> room, <span class="cls">LocalDate</span> date, <span class="kw">int</span> occupancy) {
        <span class="kw">double</span> base = room.<span class="fn">getBasePrice</span>();
        <span class="kw">if</span> (date.<span class="fn">getDayOfWeek</span>() == <span class="cls">DayOfWeek</span>.FRIDAY
                || date.<span class="fn">getDayOfWeek</span>() == <span class="cls">DayOfWeek</span>.SATURDAY) base *= <span class="num">1.2</span>;
        <span class="kw">if</span>      (occupancy > <span class="num">80</span>) base *= <span class="num">1.5</span>;
        <span class="kw">else if</span> (occupancy > <span class="num">60</span>) base *= <span class="num">1.2</span>;
        <span class="kw">return</span> base;
    }
}</pre>
    </div>
  </div>
</div>

<!-- ===== FRAMEWORK ===== -->
<div class="view" id="view-framework">
  <div class="rule-hd"><span>5-step LLD interview framework</span></div>

  <div class="framework">
    <div class="fw-hdr">THE 5-STEP LLD FRAMEWORK — USE FOR EVERY INTERVIEW</div>
    <div class="fw-steps">
      <div class="fw-step">
        <div class="fw-n" style="color:var(--red)">01</div>
        <div class="fw-title">CLARIFY (3 min)</div>
        <div class="fw-body">Who are users? What are core use cases? Single machine or distributed? Any specific NFRs (concurrency, scale)? Don't assume — ask.</div>
      </div>
      <div class="fw-step">
        <div class="fw-n" style="color:var(--red)">02</div>
        <div class="fw-title">ENTITIES (5 min)</div>
        <div class="fw-body">List 5–8 core nouns from requirements. Define key attributes and relationships. Draw a simple entity diagram. Avoid over-modelling at this stage.</div>
      </div>
      <div class="fw-step">
        <div class="fw-n" style="color:var(--red)">03</div>
        <div class="fw-title">DESIGN (15 min)</div>
        <div class="fw-body">Interface first, implementation second. Identify patterns and justify WHY. Don't use a pattern unless it solves a real problem. Explain trade-offs aloud.</div>
      </div>
      <div class="fw-step">
        <div class="fw-n" style="color:var(--red)">04</div>
        <div class="fw-title">EDGE CASES (5 min)</div>
        <div class="fw-body">Concurrency: which operations need thread safety? Error states: failure recovery? Validation: where is input validated? What are the invariants?</div>
      </div>
      <div class="fw-step">
        <div class="fw-n" style="color:var(--red)">05</div>
        <div class="fw-title">CODE (15 min)</div>
        <div class="fw-body">Focus on the most interesting class. Show you understand the pattern — don't just write boilerplate. Verbalize trade-offs. Time-box ruthlessly.</div>
      </div>
    </div>
  </div>

  <div class="rule-hd" style="margin-top:24px"><span>Killer questions + strong answers</span></div>
  <table class="int-table">
    <thead><tr><th>SYSTEM</th><th>KILLER QUESTION</th><th>STRONG ANSWER</th></tr></thead>
    <tbody>
      <tr><td>Chess</td><td>"How do you detect checkmate?"</td><td>Simulate every legal move for the player in check. If none escape check → checkmate. Key: simulate-check-undo via Command pattern.</td></tr>
      <tr><td>Elevator</td><td>"Handle 1000 floors efficiently?"</td><td>TreeSet for requests (O(log n) insert/min). LOOK direction reversal. Per-elevator locking prevents cross-elevator contention.</td></tr>
      <tr><td>Library</td><td>"Thread safety of last copy?"</td><td>synchronized(book) with double-check. ConcurrentLinkedQueue for reservation. Synchronized block is on the specific book — not the entire catalog.</td></tr>
      <tr><td>Food Ordering</td><td>"Add new payment method?"</td><td>New class implementing PaymentHandler. Set it in the chain. Zero changes to ValidationHandler, DeliveryHandler. OCP via CoR.</td></tr>
      <tr><td>ATM</td><td>"Network fails after debit, before dispense?"</td><td>WithdrawalCommand.undo() credits account back. Transaction ID logged for idempotent replay. Same-transaction retry is safe.</td></tr>
      <tr><td>Hotel</td><td>"10,000 concurrent bookings for last room?"</td><td>ReentrantLock per room. tryBook() is atomic. Losers get waitlisted via reservation queue. Observer notifies when room cancels.</td></tr>
    </tbody>
  </table>
</div>

<!-- ===== ANTI-PATTERNS ===== -->
<div class="view" id="view-anti">
  <div class="rule-hd"><span>Common LLD anti-patterns — avoid these in interviews</span></div>

  <div class="anti-grid">
    <div class="anti-card">
      <div class="anti-icon">🧱</div>
      <div class="anti-name">God Class</div>
      <div class="anti-desc">One class does everything — BookingService has 2000 lines handling payment, notifications, seat locking, pricing, emails. Violates SRP. Fix: split into focused services behind a Facade.</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">🏚️</div>
      <div class="anti-name">Anemic Domain Model</div>
      <div class="anti-desc">Entities are pure data bags (only getters/setters). All logic lives in service classes. Result: procedural code disguised as OOP. Fix: move behaviour to entities — Order.cancel(), Seat.lock(), Booking.getFee().</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">🔧</div>
      <div class="anti-name">Over-Engineering</div>
      <div class="anti-desc">Using every design pattern you know regardless of need. A simple CRUD system with Factory + Builder + Strategy + Observer + Decorator is a red flag. Fix: use a pattern only when it solves a concrete problem.</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">🔗</div>
      <div class="anti-name">No Interfaces</div>
      <div class="anti-desc">Every class references concrete types: PaymentService uses new StripeGateway() directly. Kills OCP, testability, and swappability. Fix: all dependencies injected via interfaces.</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">⚡</div>
      <div class="anti-name">Ignoring Concurrency</div>
      <div class="anti-desc">"I'll add thread safety later." In interviews, the concurrency question IS the design question. Fix: identify shared mutable state upfront, choose the right primitive (atomic vs lock vs semaphore).</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">🔓</div>
      <div class="anti-name">Exposing Internals</div>
      <div class="anti-desc">getBoard()[row][col] = piece — letting clients mutate internal structures. Breaks encapsulation, makes validation impossible. Fix: expose behaviour methods (makeMove, isValidMove) not raw data.</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">🗺️</div>
      <div class="anti-name">Validation Scattered Everywhere</div>
      <div class="anti-desc">if (seat != null && !seat.isBooked() && user != null && ...) in 12 different places. Fix: single Validator class per domain object. Or CoR where ValidationHandler is one step.</div>
    </div>
    <div class="anti-card">
      <div class="anti-icon">📋</div>
      <div class="anti-name">Missing Invariants</div>
      <div class="anti-desc">No thought given to what must always be true: "available + occupied == total", "seat has at most one booking", "balance never goes negative". Fix: state invariants explicitly; enforce in synchronized/locked sections.</div>
    </div>
  </div>

  <div style="margin-top:20px;background:var(--cream);border:2px solid var(--ink);padding:20px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--grey2);margin-bottom:12px;">// PATTERN SELECTION CHEAT SHEET</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;font-family:'IBM Plex Mono',monospace;font-size:11px;line-height:1.9;">
      <div><span style="color:var(--ink);font-weight:500">if/else on algorithm type</span><span style="color:var(--grey2)"> → Strategy</span></div>
      <div><span style="color:var(--ink);font-weight:500">Need undo/redo</span><span style="color:var(--grey2)"> → Command</span></div>
      <div><span style="color:var(--ink);font-weight:500">Object behaves differently per mode</span><span style="color:var(--grey2)"> → State</span></div>
      <div><span style="color:var(--ink);font-weight:500">One change → many notifications</span><span style="color:var(--grey2)"> → Observer</span></div>
      <div><span style="color:var(--ink);font-weight:500">Multiple handlers, unknown upfront</span><span style="color:var(--grey2)"> → CoR</span></div>
      <div><span style="color:var(--ink);font-weight:500">Simplify complex subsystem</span><span style="color:var(--grey2)"> → Facade</span></div>
      <div><span style="color:var(--ink);font-weight:500">Many optional constructor params</span><span style="color:var(--grey2)"> → Builder</span></div>
      <div><span style="color:var(--ink);font-weight:500">Limit concurrent access (N slots)</span><span style="color:var(--grey2)"> → Semaphore</span></div>
      <div><span style="color:var(--ink);font-weight:500">Incompatible interface</span><span style="color:var(--grey2)"> → Adapter</span></div>
      <div><span style="color:var(--ink);font-weight:500">Add behaviour without subclassing</span><span style="color:var(--grey2)"> → Decorator</span></div>
      <div><span style="color:var(--ink);font-weight:500">Tree structure, uniform ops</span><span style="color:var(--grey2)"> → Composite</span></div>
      <div><span style="color:var(--ink);font-weight:500">Read-heavy shared data</span><span style="color:var(--grey2)"> → ReadWriteLock</span></div>
    </div>
  </div>
</div>

<!-- ===== TASKS ===== -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-label">Snake and Ladder Game</div><div class="t-meta">~3 hrs · full LLD</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <pre>Design Snake and Ladder:
  - N players, 100-cell board, configurable snakes/ladders
  - Dice rolling: pluggable strategy (single die, two dice, biased die)
  - Special cells: snake head slides down, ladder bottom climbs up
  - Win condition: exactly 100 (overshoot = no move)
  - Multiplayer: track current player
  - Save/load game state (Memento)

Required patterns:
  Factory:   Dice creation
  Strategy:  Dice rolling algorithm
  Observer:  onPlayerMoved, onSnakeBite, onLadderClimb, onWin
  Command:   Move (with undo for "take back" variant)
  Memento:   Save game state to resume later

Deliver: Full Java + UML + test for 4 players, 10-round game</pre>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-label">Parking Lot V2 — Extensions</div><div class="t-meta">~2.5 hrs · extend A5</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <pre>Extend the A5 Parking Lot with:
  - Monthly pass holders: reserved spots, no time-based fee
  - EV charging spots: AVAILABLE → CHARGING → CHARGED → AVAILABLE
  - VIP spots: premium pricing, observer notification on availability
  - Smart fee:
      < 30 min:  flat ₹20
      < 2 hours: flat ₹50
      > 2 hours: ₹80/hour after first 2h
  - Multiple entry/exit gates (separate rate limiters per gate)
  - Daily revenue report: thread-safe aggregation

Design challenge: adding EV state without breaking existing Spot hierarchy.
Show OCP — new spot type = new class, existing code unchanged.</pre>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-label">Multi-Level Cache System</div><div class="t-meta">~3 hrs · code</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <pre>Design a three-level cache:
  L1: In-process LRU (1,000 items, O(1) get/put)
  L2: Distributed (Redis-like, 100,000 items, TTL-based eviction)
  L3: Database (unlimited, slowest)

On get(key):
  Hit L1 → return immediately
  Miss L1, hit L2 → populate L1, return
  Miss L2, hit L3 → populate L2 + L1, return
  Miss all → return null

Write policies (Strategy, pluggable):
  write-through:  write all levels synchronously
  write-back:     write L1 only; async flush to L2/L3
  write-around:   bypass cache; write directly to L3

Concurrency: ReadWriteLock per level (reads don't block each other)
Invalidation: CacheInvalidationEvent via Observer pattern

Test: cache hit rates, concurrency safety, write policy correctness</pre>
      </div>
    </div>

    <div class="task-card" style="border-top:3px solid var(--red)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--red)">★</div><div class="t-label">Capstone — BookMyShow (Full Track A)</div><div class="t-meta">~8 hrs · complete LLD</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <pre>Entities: Movie, Show, Screen, Seat, Booking, User, Theatre, Payment, Ticket

Features:
  1. Browse movies by city/date
  2. Select show → choose seats → pay → receive ticket
  3. Seat hold expires after 5 minutes if unpaid
  4. Concurrent seat selection — no double booking
  5. Pricing: weekday/weekend × screen type × seat type multipliers
  6. Cancellation: full refund >24h, 50% refund 2–24h, none <2h
  7. Notifications: booking confirmation, 2h-before show reminder

All 9 patterns with justification:
  State:    Seat (AVAILABLE/LOCKED/BOOKED/CANCELLED)
  Observer: Booking events, seat expiry alerts
  Command:  BookSeat + CancelBooking with undo/refund
  Strategy: Pricing engine (multipliers per category)
  CoR:      validate → price → payment → confirm → notify
  Facade:   BookingService.bookSeats(userId, showId, seatIds)
  Builder:  BookingRequest (optional fields: promo code, special needs)
  Factory:  TicketFactory (standard vs IMAX vs 4DX ticket format)
  Concurrency: ReentrantLock per Seat + ScheduledExecutor for 5-min expiry

Deliverables:
  1. Complete Java implementation (every class)
  2. UML class diagram with all 9 patterns annotated
  3. Sequence diagram: "User books 2 IMAX seats" happy path
  4. JUnit test: 20 threads try to book last 3 seats — zero double bookings</pre>
      </div>
    </div>
  </div>
</div>

<!-- ===== CHECKLIST ===== -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 12 completed</span><span>MODULE A6 · TRACK A FINAL</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design Chess Game — move validation, undo, checkmate detection</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design Elevator — LOOK algorithm, concurrent requests, pluggable strategy</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design Library — reservation queue, fine calc, thread-safe last copy</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design Food Ordering — CoR pipeline, surge pricing, order state machine</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design ATM — PIN retry, transaction atomicity, Command undo</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can design Hotel Booking — concurrent date-range locking, dynamic pricing</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know the 5-step LLD interview framework by heart</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can recite pattern selection cheat sheet (12 patterns → triggers)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: Snake & Ladder — all 5 patterns + game state save/load</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: Parking Lot V2 — EV spots, monthly pass, multi-gate</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 3: Multi-Level Cache — 3 levels, 3 write policies, concurrent</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Capstone: BookMyShow — 9 patterns, concurrency proof, UML, sequence diagram</div></div>
  </div>

  <div style="margin-top:32px;background:var(--ink);color:var(--paper);padding:28px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--grey2);margin-bottom:12px;">TRACK A COMPLETE</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:40px;letter-spacing:2px;margin-bottom:10px;">🎉 Ready for Track B</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--grey1);line-height:2;">
      B1 · HLD Fundamentals — CAP theorem, consistency models, availability<br>
      B2 · Databases at Scale — sharding, replication, SQL vs NoSQL<br>
      B3 · Caching — Redis, CDN, cache invalidation strategies<br>
      B4 · Message Queues — Kafka, RabbitMQ, event streaming<br>
      B5 · URL Shortener · Pastebin · TinyURL<br>
      B6–B10 · Twitter · Netflix · Uber · WhatsApp · Google Drive
    </div>
  </div>
</div>

</div><!-- end content -->

<script>
function show(tab, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}

function selCase(i) {
  document.querySelectorAll('.ct-btn').forEach((b,j) => b.classList.toggle('active', i===j));
  document.querySelectorAll('.case-panel').forEach((p,j) => p.classList.toggle('active', i===j));
}

function goCase(i) {
  show('cases', document.querySelectorAll('.nav-tab')[1]);
  selCase(i);
}

function tt(hd) {
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function tick(el) {
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.chk').length;
  const done  = document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done/total)*100}%`;
}
</script>
<div class="m6-bottom-nav" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--border2);padding-top:20px;">
  <a href="/learning/system-design/lld/module-a5-concurrency/" class="m6-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">← PREVIOUS: LLD A5</a>
  <a href="/learning/system-design/lld/module-a6-notes/" class="m6-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--amber);color:var(--amber);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" class="m6-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/hld/module-b1-hld-fundamentals/" class="m6-nav-footer-btn" style="padding:12px 24px;background:var(--amber);color:var(--bg);border-radius:4px;text-decoration:none;font-weight:600;">NEXT: HLD B1 →</a>
</div>
