---
title: "Module A6 — LLD Case Studies (Notes)"
description: "System Design Roadmap › LLD Hub › Module A6 › Full Notes Module A6 — LLD Case Studies Complete reference notes · Track A: LLD · Weeks 9–10 · FINAL LLD MODULE Chess Game…"
domain: system-design
track: system-design-lld
order: 13
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a6-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero" style="--ch-1:#7c6fff;--ch-2:#ff6b9d;">
  <div class="breadcrumb">
    <a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
    <span class="separator">›</span>
    <a href="/learning/system-design/lld/">LLD Hub</a>
    <span class="separator">›</span>
    <a href="/learning/system-design/lld/module-a6-case-studies/">Module A6</a>
    <span class="separator">›</span>
    <span class="current">Full Notes</span>
  </div>
  <h1>Module A6 — LLD Case Studies</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Weeks 9–10 · FINAL LLD MODULE</p>
  <div class="hero-stats">
    <span class="stat-badge">Chess Game</span>
    <span class="stat-badge">Elevator System</span>
    <span class="stat-badge">Library Management</span>
    <span class="stat-badge">Food Ordering</span>
    <span class="stat-badge">ATM Machine</span>
    <span class="stat-badge">Hotel Booking</span>
  </div>
</div>
<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a6-case-studies/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(124,111,255,0.1);border:1px solid rgba(124,111,255,0.3);color:#7c6fff;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>

# Module A6 — LLD Case Studies
## System Design Mastery Course | Track A: LLD | Weeks 9–10

---

## 🎯 Module Overview

**Duration:** 2 Weeks  
**Track:** A — Low-Level Design (LLD) — FINAL MODULE  
**Prerequisites:** A1–A5 (All SOLID, Patterns, Concurrency)  
**Goal:** Apply everything from Track A to complete, production-grade LLD designs. Each case study uses multiple patterns and concurrency correctly. This is the module interviewers test at FAANG.

### The 6 Case Studies

| # | System | Patterns Used | Key Challenge |
|---|--------|--------------|---------------|
| 1 | Chess Game | State, Command, Observer, Factory | Move validation, undo, game state |
| 2 | Elevator System | State, Strategy, Observer, Composite | Scheduling algorithm, multi-elevator |
| 3 | Library Management | Builder, Factory, Observer, Iterator | Reservation queue, fine calculation |
| 4 | Online Food Ordering | Facade, Strategy, Observer, CoR, State | Order lifecycle, restaurant matching |
| 5 | ATM Machine | State, Chain of Responsibility, Command | Transaction atomicity, security |
| 6 | Hotel Booking System | Builder, Observer, Strategy, Concurrency | Room contention, pricing |

---

## Case Study 1 — Chess Game

### Requirement Analysis
- 2 players, 8×8 board, 6 piece types
- Move validation per piece type
- Check and checkmate detection
- Undo last move (Memento/Command)
- Game state persistence (Memento)
- Timer per player

### Class Design

```java
// ENUM — piece types and colors
enum PieceType  { KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN }
enum PieceColor { WHITE, BLACK }

// Piece hierarchy — Factory Method
abstract class Piece {
    protected PieceColor color;
    protected Position   position;

    public abstract List<Position> validMoves(Board board);
    public abstract PieceType getType();
    public abstract boolean   canAttack(Position target, Board board);
}

class King   extends Piece { /* moves 1 in any direction */ }
class Queen  extends Piece { /* moves any distance in 8 directions */ }
class Rook   extends Piece { /* moves horizontally/vertically */ }
class Bishop extends Piece { /* moves diagonally */ }
class Knight extends Piece { /* L-shape, jumps over pieces */ }
class Pawn   extends Piece { /* moves forward, attacks diagonally */ }

// FACTORY METHOD — create pieces by type
class PieceFactory {
    public static Piece create(PieceType type, PieceColor color, Position pos) {
        return switch (type) {
            case KING   -> new King(color, pos);
            case QUEEN  -> new Queen(color, pos);
            case ROOK   -> new Rook(color, pos);
            case BISHOP -> new Bishop(color, pos);
            case KNIGHT -> new Knight(color, pos);
            case PAWN   -> new Pawn(color, pos);
        };
    }
}

// Board — 8x8 grid
class Board {
    private final Piece[][] grid = new Piece[8][8];

    public Piece getPiece(Position pos)           { return grid[pos.row()][pos.col()]; }
    public void  setPiece(Position pos, Piece p)  { grid[pos.row()][pos.col()] = p; }
    public boolean isEmpty(Position pos)          { return getPiece(pos) == null; }
    public boolean isInBounds(int row, int col)   { return row>=0 && row<8 && col>=0 && col<8; }
    public boolean isUnderAttack(Position pos, PieceColor by) {
        // Check if any piece of color 'by' can attack 'pos'
        for (int r=0; r<8; r++)
            for (int c=0; c<8; c++) {
                Piece p = grid[r][c];
                if (p != null && p.getColor() == by && p.canAttack(pos, this))
                    return true;
            }
        return false;
    }
}

// COMMAND — Move encapsulates a chess move + undo
class Move implements Command {
    private final Piece  piece;
    private final Position from, to;
    private Piece         capturedPiece;  // Saved for undo
    private boolean       wasFirstMove;   // For pawn/king/rook special rules

    public void execute(Board board) {
        capturedPiece = board.getPiece(to);
        wasFirstMove  = piece.isFirstMove();
        board.setPiece(to, piece);
        board.setPiece(from, null);
        piece.setPosition(to);
        piece.setFirstMove(false);
    }

    public void undo(Board board) {
        board.setPiece(from, piece);
        board.setPiece(to, capturedPiece);  // Restore captured piece
        piece.setPosition(from);
        piece.setFirstMove(wasFirstMove);
    }
}

// STATE — Game progresses through states
enum GameState { WAITING, WHITE_TURN, BLACK_TURN, CHECK, CHECKMATE, STALEMATE, PAUSED }

// OBSERVER — notify UI and players of game events
interface GameObserver {
    void onMoveMade(Move move);
    void onCheck(PieceColor kingInCheck);
    void onCheckmate(PieceColor winner);
    void onGameOver(GameResult result);
}

// Main game class — FACADE over board/players/rules
class ChessGame {
    private final Board               board;
    private final Player              whitePlayer, blackPlayer;
    private       PieceColor          currentTurn = PieceColor.WHITE;
    private       GameState           state       = GameState.WAITING;
    private final Deque<Move>         moveHistory = new ArrayDeque<>();
    private final List<GameObserver>  observers   = new ArrayList<>();
    private final MoveValidator       validator   = new MoveValidator();

    public boolean makeMove(Position from, Position to) {
        if (!isCurrentPlayersTurn(from)) return false;

        Move move = new Move(board.getPiece(from), from, to);

        if (!validator.isLegal(move, board, currentTurn)) return false;

        move.execute(board);
        moveHistory.push(move);
        notifyObservers(obs -> obs.onMoveMade(move));

        // Check for check/checkmate
        PieceColor opponent = currentTurn.opposite();
        if (validator.isCheckmate(board, opponent)) {
            state = GameState.CHECKMATE;
            notifyObservers(obs -> obs.onCheckmate(currentTurn));
        } else if (validator.isCheck(board, opponent)) {
            state = GameState.CHECK;
            notifyObservers(obs -> obs.onCheck(opponent));
        }

        currentTurn = opponent;
        return true;
    }

    public void undoLastMove() {
        if (!moveHistory.isEmpty()) {
            moveHistory.pop().undo(board);
            currentTurn = currentTurn.opposite();
        }
    }
}

// MoveValidator — pure logic, no side effects
class MoveValidator {
    public boolean isLegal(Move move, Board board, PieceColor turn) {
        // 1. Piece belongs to current player
        // 2. Target square is in valid moves for piece
        // 3. Move does not leave own king in check (simulate move then check)
        Piece piece = move.getPiece();
        if (piece.getColor() != turn) return false;
        if (!piece.validMoves(board).contains(move.getTo())) return false;
        return !wouldLeaveKingInCheck(move, board, turn);
    }

    private boolean wouldLeaveKingInCheck(Move move, Board board, PieceColor color) {
        move.execute(board);
        boolean inCheck = isCheck(board, color);
        move.undo(board);
        return inCheck;
    }

    public boolean isCheck(Board board, PieceColor color) {
        Position kingPos = findKing(board, color);
        return board.isUnderAttack(kingPos, color.opposite());
    }

    public boolean isCheckmate(Board board, PieceColor color) {
        if (!isCheck(board, color)) return false;
        // No legal move exists that gets out of check
        return getAllPieces(board, color).stream()
            .flatMap(p -> p.validMoves(board).stream()
                .map(to -> new Move(p, p.getPosition(), to)))
            .noneMatch(m -> !wouldLeaveKingInCheck(m, board, color));
    }
}
```

### Key Design Decisions
- **Command** for moves enables undo history without complex state copying
- **State enum** tracks game phase — drives UI transitions
- **Observer** decouples game logic from UI rendering and sound
- **MoveValidator** as a pure service — no state, all inputs via parameters (easy to test)

---

## Case Study 2 — Elevator System

### Requirement Analysis
- N elevators in a building with M floors
- Requests: floor + direction (UP/DOWN)
- Scheduling: LOOK algorithm (sweep up then down)
- State per elevator: IDLE, MOVING_UP, MOVING_DOWN, STOPPED
- Concurrent requests from multiple floors

### Class Design

```java
// STATE per elevator
enum ElevatorState { IDLE, MOVING_UP, MOVING_DOWN, STOPPED_OPEN }

class Elevator {
    private final int              id;
    private       int              currentFloor = 1;
    private       ElevatorState   state        = ElevatorState.IDLE;
    private final TreeSet<Integer> upRequests   = new TreeSet<>();   // Sorted
    private final TreeSet<Integer> downRequests = new TreeSet<>(Comparator.reverseOrder());
    private final ReentrantLock    lock         = new ReentrantLock();

    public void addRequest(int floor) {
        lock.lock();
        try {
            if (floor > currentFloor) upRequests.add(floor);
            else                      downRequests.add(floor);
        } finally { lock.unlock(); }
    }

    // LOOK algorithm: service all requests in current direction, then reverse
    public void step() {
        lock.lock();
        try {
            switch (state) {
                case MOVING_UP -> {
                    if (!upRequests.isEmpty()) {
                        currentFloor = upRequests.first();  // Next floor up
                        upRequests.remove(currentFloor);
                        state = ElevatorState.STOPPED_OPEN;
                    } else if (!downRequests.isEmpty()) {
                        state = ElevatorState.MOVING_DOWN;  // Reverse
                    } else {
                        state = ElevatorState.IDLE;
                    }
                }
                case MOVING_DOWN -> {
                    if (!downRequests.isEmpty()) {
                        currentFloor = downRequests.first();
                        downRequests.remove(currentFloor);
                        state = ElevatorState.STOPPED_OPEN;
                    } else if (!upRequests.isEmpty()) {
                        state = ElevatorState.MOVING_UP;
                    } else {
                        state = ElevatorState.IDLE;
                    }
                }
                case STOPPED_OPEN -> state = upRequests.isEmpty() && downRequests.isEmpty()
                    ? ElevatorState.IDLE
                    : (upRequests.isEmpty() ? ElevatorState.MOVING_DOWN : ElevatorState.MOVING_UP);
                case IDLE -> {
                    if (!upRequests.isEmpty())   state = ElevatorState.MOVING_UP;
                    else if (!downRequests.isEmpty()) state = ElevatorState.MOVING_DOWN;
                }
            }
        } finally { lock.unlock(); }
    }

    public int distanceTo(int floor) { return Math.abs(currentFloor - floor); }
    public ElevatorState getState()  { return state; }
    public int getCurrentFloor()     { return currentFloor; }
}

// STRATEGY — elevator selection algorithm (pluggable)
interface ElevatorSelectionStrategy {
    Elevator selectElevator(List<Elevator> elevators, int requestedFloor, Direction dir);
}

class NearestIdleStrategy implements ElevatorSelectionStrategy {
    public Elevator selectElevator(List<Elevator> elevators, int floor, Direction dir) {
        return elevators.stream()
            .filter(e -> e.getState() == ElevatorState.IDLE)
            .min(Comparator.comparingInt(e -> e.distanceTo(floor)))
            .or(() -> elevators.stream()  // Fallback: nearest elevator moving same direction
                .filter(e -> isSameDirection(e, dir, floor))
                .min(Comparator.comparingInt(e -> e.distanceTo(floor))))
            .orElse(elevators.get(0));    // Last resort: any elevator
    }

    private boolean isSameDirection(Elevator e, Direction dir, int floor) {
        return (dir == Direction.UP   && e.getState() == ElevatorState.MOVING_UP   && e.getCurrentFloor() < floor)
            || (dir == Direction.DOWN && e.getState() == ElevatorState.MOVING_DOWN && e.getCurrentFloor() > floor);
    }
}

// FACADE — ElevatorController coordinates all elevators
class ElevatorController {
    private final List<Elevator>              elevators;
    private final ElevatorSelectionStrategy   strategy;
    private final List<ElevatorObserver>      observers = new ArrayList<>();
    private final ScheduledExecutorService    scheduler;

    public ElevatorController(int numElevators, int numFloors,
                               ElevatorSelectionStrategy strategy) {
        this.elevators = IntStream.range(0, numElevators)
            .mapToObj(Elevator::new).collect(toList());
        this.strategy  = strategy;
        this.scheduler = Executors.newScheduledThreadPool(1);
        // Step all elevators every 500ms
        scheduler.scheduleAtFixedRate(this::stepAll, 0, 500, TimeUnit.MILLISECONDS);
    }

    public void requestElevator(int floor, Direction direction) {
        Elevator chosen = strategy.selectElevator(elevators, floor, direction);
        chosen.addRequest(floor);
        observers.forEach(o -> o.onRequested(floor, direction, chosen));
    }

    private void stepAll() {
        elevators.forEach(e -> {
            int prevFloor = e.getCurrentFloor();
            e.step();
            if (prevFloor != e.getCurrentFloor()) {
                observers.forEach(o -> o.onFloorChanged(e));
            }
        });
    }
}
```

---

## Case Study 3 — Library Management System

### Core Classes

```java
// Builder — Book has many optional attributes
class Book {
    private final String  isbn;         // required
    private final String  title;        // required
    private final String  author;       // required
    private final String  genre;        // optional
    private final int     year;         // optional
    private final String  publisher;    // optional
    private final int     totalCopies;  // required
    private int           availableCopies;

    private Book(Builder b) { /* from builder */ }

    public static class Builder {
        private final String isbn, title, author;
        private String genre, publisher;
        private int    year = 0, totalCopies = 1;

        public Builder(String isbn, String title, String author) {
            this.isbn = isbn; this.title = title; this.author = author;
        }
        public Builder genre(String g)     { this.genre = g;       return this; }
        public Builder year(int y)         { this.year = y;        return this; }
        public Builder publisher(String p) { this.publisher = p;   return this; }
        public Builder copies(int c)       { this.totalCopies = c; return this; }
        public Book build()                { return new Book(this); }
    }
}

// Observer — notify members of book availability
interface LibraryObserver {
    void onBookAvailable(Book book, Member member);
    void onOverdue(Borrowing borrowing, int daysOverdue);
}

// State — borrowing lifecycle
enum BorrowingState { BORROWED, RETURNED, OVERDUE, LOST }

class Borrowing {
    private final Book         book;
    private final Member       member;
    private final LocalDate    borrowDate;
    private       LocalDate    returnDate;
    private       BorrowingState state = BorrowingState.BORROWED;

    public double calculateFine() {
        if (state == BorrowingState.RETURNED) return 0;
        long daysOverdue = ChronoUnit.DAYS.between(
            borrowDate.plusDays(14), LocalDate.now());  // 14-day lending period
        return Math.max(0, daysOverdue * 5.0);           // ₹5/day fine
    }
}

// Reservation queue — FIFO per book
class ReservationQueue {
    private final Map<String, Queue<Member>> queues = new ConcurrentHashMap<>();

    public void reserve(Book book, Member member) {
        queues.computeIfAbsent(book.getIsbn(), k -> new ConcurrentLinkedQueue<>())
              .offer(member);
    }

    public Optional<Member> nextInQueue(Book book) {
        Queue<Member> q = queues.get(book.getIsbn());
        return q == null ? Optional.empty() : Optional.ofNullable(q.poll());
    }
}

// LibrarySystem — FACADE
class LibrarySystem {
    private final Map<String, Book>        catalog      = new ConcurrentHashMap<>();
    private final Map<String, Borrowing>   activeBorrow = new ConcurrentHashMap<>();
    private final ReservationQueue         reservations = new ReservationQueue();
    private final List<LibraryObserver>    observers    = new CopyOnWriteArrayList<>();
    private final ReadWriteLock            catalogLock  = new ReentrantReadWriteLock();

    public boolean borrowBook(String isbn, Member member) {
        Book book = catalog.get(isbn);
        if (book == null || book.getAvailable() == 0) {
            reservations.reserve(book, member);
            return false;
        }
        synchronized (book) {  // Synchronize on the specific book
            if (book.getAvailable() == 0) { reservations.reserve(book, member); return false; }
            book.decrementAvailable();
        }
        activeBorrow.put(member.getId() + ":" + isbn,
                         new Borrowing(book, member, LocalDate.now()));
        return true;
    }

    public void returnBook(String isbn, Member member) {
        String key = member.getId() + ":" + isbn;
        Borrowing b = activeBorrow.remove(key);
        if (b == null) throw new IllegalStateException("No active borrowing");
        b.markReturned();

        Book book = catalog.get(isbn);
        synchronized (book) { book.incrementAvailable(); }

        // Notify next in reservation queue
        reservations.nextInQueue(book).ifPresent(nextMember -> {
            observers.forEach(o -> o.onBookAvailable(book, nextMember));
        });
    }
}
```

---

## Case Study 4 — Online Food Ordering (Zomato/Swiggy)

### Order Lifecycle (State Machine)
```
PLACED → RESTAURANT_ACCEPTED → PREPARING → READY → PICKED_UP → DELIVERED
      ↘ RESTAURANT_REJECTED
      ↘ CANCELLED (before PREPARING)
```

### Core Design

```java
// FACADE — OrderService is the single entry point
class OrderService {
    private final RestaurantMatcher   matcher;
    private final PricingStrategy     pricing;
    private final PaymentHandler      payment;
    private final DeliveryService     delivery;
    private final NotificationService notifier;
    private final OrderRepository     repo;

    // Chain of Responsibility: validate → price → payment → assign delivery
    private final OrderHandler handlerChain;

    public Order placeOrder(Cart cart, User user, Address deliveryAddress) {
        Order order = Order.builder()
            .id(UUID.randomUUID().toString())
            .user(user)
            .items(cart.getItems())
            .restaurant(matcher.findBestRestaurant(cart, deliveryAddress))
            .state(OrderState.PLACED)
            .build();

        handlerChain.handle(order);  // Runs through validation→pricing→payment→dispatch
        repo.save(order);
        notifier.notify(user, "Order placed! Est. delivery: 30 min");
        return order;
    }
}

// STRATEGY — pricing strategies
interface PricingStrategy {
    double calculateTotal(Order order);
}

class SurgePricingStrategy implements PricingStrategy {
    public double calculateTotal(Order order) {
        double base = order.getItems().stream().mapToDouble(Item::getPrice).sum();
        double surge = calculateSurge(order.getRestaurant(), order.getOrderTime());
        return base * surge + DELIVERY_FEE;
    }

    private double calculateSurge(Restaurant r, LocalTime time) {
        boolean isPeak = time.isAfter(LocalTime.of(12,0)) && time.isBefore(LocalTime.of(14,0))
            || time.isAfter(LocalTime.of(19,0)) && time.isBefore(LocalTime.of(22,0));
        return isPeak ? 1.3 : 1.0;  // 30% surge during peak hours
    }
}

// CHAIN OF RESPONSIBILITY — order processing pipeline
abstract class OrderHandler {
    protected OrderHandler next;
    public OrderHandler setNext(OrderHandler n) { this.next = n; return n; }
    public abstract void handle(Order order);
    protected void passToNext(Order order) { if (next != null) next.handle(order); }
}

class ValidationHandler extends OrderHandler {
    public void handle(Order order) {
        if (order.getItems().isEmpty()) throw new InvalidOrderException("Empty cart");
        if (order.getRestaurant() == null) throw new NoRestaurantException("No restaurant found");
        passToNext(order);
    }
}

class PaymentHandler extends OrderHandler {
    private final PaymentService payment;
    public void handle(Order order) {
        PaymentResult result = payment.charge(order.getUser(), order.getTotalAmount());
        if (!result.isSuccess()) throw new PaymentFailedException(result.getError());
        order.setPaymentId(result.getTransactionId());
        passToNext(order);
    }
}

class DeliveryAssignmentHandler extends OrderHandler {
    private final DeliveryService delivery;
    public void handle(Order order) {
        DeliveryAgent agent = delivery.findNearestAgent(order.getRestaurant().getLocation());
        order.setDeliveryAgent(agent);
        delivery.assignOrder(agent, order);
        passToNext(order);
    }
}
```

---

## Case Study 5 — ATM Machine

### State Machine
```
IDLE → CARD_INSERTED → PIN_ENTERED → TRANSACTION_SELECTED
     → AMOUNT_ENTERED → DISPENSING → COMPLETE → IDLE
     ↘ (any state) → ERROR → IDLE
```

### Core Design

```java
// STATE pattern — each state handles only valid operations
interface ATMState {
    void insertCard(ATM atm, Card card);
    void enterPin(ATM atm, String pin);
    void selectTransaction(ATM atm, TransactionType type);
    void enterAmount(ATM atm, double amount);
    void cancel(ATM atm);
}

class IdleState implements ATMState {
    public void insertCard(ATM atm, Card card) {
        if (atm.getCardReader().readCard(card)) {
            atm.setCurrentCard(card);
            atm.setState(new CardInsertedState());
            atm.display("Card accepted. Enter PIN:");
        }
    }
    public void enterPin(ATM atm, String pin)                  { atm.display("Insert card first"); }
    public void selectTransaction(ATM atm, TransactionType t)  { atm.display("Insert card first"); }
    public void enterAmount(ATM atm, double amount)            { atm.display("Insert card first"); }
    public void cancel(ATM atm)                                { /* nothing to cancel */ }
}

class CardInsertedState implements ATMState {
    private int attempts = 0;

    public void enterPin(ATM atm, String pin) {
        if (atm.getBank().verifyPin(atm.getCurrentCard(), pin)) {
            atm.setState(new AuthenticatedState());
            atm.display("Select transaction:");
        } else {
            attempts++;
            if (attempts >= 3) {
                atm.getCardReader().retainCard();
                atm.setState(new IdleState());
                atm.display("Card retained — 3 failed attempts");
            } else {
                atm.display("Wrong PIN. " + (3-attempts) + " attempts left");
            }
        }
    }
    public void insertCard(ATM atm, Card card)                 { atm.display("Card already inserted"); }
    public void selectTransaction(ATM atm, TransactionType t)  { atm.display("Enter PIN first"); }
    public void enterAmount(ATM atm, double amount)            { atm.display("Enter PIN first"); }
    public void cancel(ATM atm) {
        atm.getCardReader().ejectCard();
        atm.setState(new IdleState());
    }
}

// CHAIN OF RESPONSIBILITY — cash dispensing
class TwoThousandDispenser extends CashHandler { /* A3 pattern */ }
class FiveHundredDispenser  extends CashHandler { }
class HundredDispenser      extends CashHandler { }

// COMMAND — transaction with undo capability
class WithdrawalCommand implements Command {
    private final Account account;
    private final double  amount;
    private       String  transactionId;

    public void execute() {
        transactionId = UUID.randomUUID().toString();
        account.debit(amount);
        // Log to audit trail
    }

    public void undo() {
        // Credit back (error reversal)
        account.credit(amount);
        // Log reversal
    }
}

// OBSERVER — log all ATM events
interface ATMObserver {
    void onCardInserted(Card card);
    void onPinAttempt(Card card, boolean success);
    void onTransaction(Transaction tx);
    void onError(String error, Card card);
}
```

---

## Case Study 6 — Hotel Booking System

### Design Highlights

```java
// BUILDER — Room search criteria
class SearchCriteria {
    private final String    city;
    private final LocalDate checkIn, checkOut;
    private final int       guests;
    private       RoomType  roomType;
    private       double    maxPrice;
    private       List<String> amenities;

    private SearchCriteria(Builder b) { /* from builder */ }

    public static class Builder {
        public Builder(String city, LocalDate in, LocalDate out, int guests) { ... }
        public Builder roomType(RoomType t)    { this.roomType = t;   return this; }
        public Builder maxPrice(double p)      { this.maxPrice = p;   return this; }
        public Builder amenity(String a)       { amenities.add(a);    return this; }
        public SearchCriteria build()          { return new SearchCriteria(this); }
    }
}

// CONCURRENCY — Room booking with optimistic locking
class Room {
    private final String         id;
    private       RoomStatus     status = RoomStatus.AVAILABLE;
    private final ReentrantLock  lock = new ReentrantLock();
    private final Set<LocalDate> bookedDates = new HashSet<>();

    public boolean tryBook(LocalDate checkIn, LocalDate checkOut, String guestId) {
        lock.lock();
        try {
            // Check all dates in range are free
            List<LocalDate> dates = checkIn.datesUntil(checkOut).collect(toList());
            if (dates.stream().anyMatch(bookedDates::contains)) return false;
            bookedDates.addAll(dates);
            return true;
        } finally { lock.unlock(); }
    }

    public void cancelBooking(LocalDate checkIn, LocalDate checkOut) {
        lock.lock();
        try {
            checkIn.datesUntil(checkOut).forEach(bookedDates::remove);
        } finally { lock.unlock(); }
    }
}

// STRATEGY — dynamic pricing
interface HotelPricingStrategy {
    double getPrice(Room room, LocalDate date, int occupancyPercent);
}

class DynamicPricingStrategy implements HotelPricingStrategy {
    public double getPrice(Room room, LocalDate date, int occupancy) {
        double base = room.getBasePrice();
        // Weekend premium
        if (date.getDayOfWeek() == DayOfWeek.SATURDAY
                || date.getDayOfWeek() == DayOfWeek.FRIDAY) base *= 1.2;
        // Occupancy-based surge
        if (occupancy > 80) base *= 1.5;
        else if (occupancy > 60) base *= 1.2;
        return base;
    }
}

// OBSERVER — booking notifications
class BookingObserver implements HotelObserver {
    public void onBookingConfirmed(Booking b) { sendConfirmationEmail(b); }
    public void onBookingCancelled(Booking b) { sendCancellationEmail(b); processRefund(b); }
    public void onRoomAvailable(Room r, Guest g) { sendAvailabilityAlert(g, r); }
}
```

---

## 📝 Tasks

### Task 1 — LLD Interview Question: Snake and Ladder
Design Snake and Ladder game:
- N players, 100-cell board, configurable snakes/ladders
- Dice rolling (pluggable strategy: single die, two dice, biased die)
- Special cells: snake head (slides down), ladder bottom (climbs up)
- Win condition: exactly 100
- Multiplayer: track current player, skip on snake, extra turn on ladder
- Persist game state (save/load)

**Required patterns:** Factory (dice), Strategy (dice rolling), Observer (events), Command (undo move), Memento (game state save/load)

### Task 2 — LLD Interview Question: Parking Lot V2
Extend the A5 Parking Lot with:
- Monthly pass holders (reserved spots, no time-based fee)
- EV charging spots with charging state
- VIP spots with special pricing
- Smart fee: flat ₹20 for <30 min, ₹50 for <2h, ₹80/hour after
- Multiple entry/exit gates (concurrent, separate rate limiters)
- Daily revenue report (read-heavy aggregation)

### Task 3 — LLD Interview Question: Cache System
Design a multi-level cache:
- L1: In-process LRU cache (fast, small, 1000 items)
- L2: Redis-like distributed cache (medium, 100k items)
- L3: Database (slow, unlimited)
- Eviction: LRU for L1, TTL for L2
- Write policies: write-through, write-back, write-around (pluggable Strategy)
- Concurrent access: readers don't block each other (ReadWriteLock)
- Cache invalidation: publish invalidation events via Observer

### ⭐ Capstone — Design BookMyShow (Complete LLD)

Full system design covering all Track A concepts:

**Entities:** Movie, Show, Screen, Seat, Booking, User, Theatre, Payment, Ticket

**Feature requirements:**
1. Browse movies by city/date
2. View shows for a movie → select seats → payment → ticket
3. Seat holds expire after 5 minutes if unpaid
4. Concurrent seat selection by multiple users
5. Different pricing: weekday/weekend, screen type (IMAX, 4DX, regular), seat type (premium/regular)
6. Cancellation: full refund >24h before, 50% refund 2-24h before, no refund <2h
7. Notification: booking confirmation, seat reminder 2h before show

**Patterns required (with justification):**
- State: Seat (AVAILABLE/LOCKED/BOOKED/CANCELLED)
- Observer: booking notifications, seat expiry events
- Command: BookSeat + CancelBooking (with undo/refund)
- Strategy: Pricing (weekday/weekend/IMAX multipliers)
- Chain of Responsibility: booking pipeline (validate→price→payment→confirm→notify)
- Facade: BookingService hides all subsystem complexity
- Builder: BookingRequest with optional fields
- Factory: Ticket creation (regular vs IMAX ticket)
- Concurrency: ReentrantLock per Seat + ScheduledExecutor for 5-min expiry

**Deliverables:**
1. Complete Java implementation (all classes, all patterns)
2. UML class diagram with pattern annotations
3. Sequence diagram: "User books 2 seats" happy path
4. Concurrency test: 20 threads try to book last 3 seats simultaneously

---

## 💡 LLD Interview Playbook

### The 5-Step Framework

```
1. CLARIFY (3 min)
   - Who are the users? What are the core use cases?
   - Scale: single machine or distributed?
   - Any specific non-functional requirements?

2. ENTITIES (5 min)
   - List 5-8 core entities/nouns from requirements
   - Define their key attributes and relationships
   - Draw a simple entity diagram

3. DESIGN CORE CLASSES (15 min)
   - Interface first, implementation second
   - Identify which patterns apply and WHY
   - Don't over-engineer — use pattern only if it solves a real problem

4. HANDLE EDGE CASES (5 min)
   - Concurrency: which operations need to be thread-safe?
   - Error states: what happens when things fail?
   - Validation: where do you validate inputs?

5. CODE KEY CLASSES (15 min)
   - Focus on the most interesting/complex classes
   - Show you understand the pattern — don't just copy boilerplate
   - Explain trade-offs as you go
```

### Common LLD Interview Questions at FAANG

| System | Key Insight | Killer Question |
|--------|-------------|-----------------|
| Chess | Move validation by simulating then checking | "How do you detect checkmate?" |
| Elevator | LOOK algorithm, concurrent requests | "How do you handle 1000 floors?" |
| Library | Reservation queue, fine calculation | "Thread safety of borrowBook()?" |
| Food ordering | Order state machine, pricing strategy | "How to add new payment method?" |
| ATM | PIN retry limit, transaction atomicity | "What if network fails mid-dispense?" |
| Hotel | Concurrent booking, dynamic pricing | "How to handle 10,000 concurrent bookings?" |
| BookMyShow | Seat locking timeout, concurrency | "Seat selected by 2 users simultaneously?" |
| Parking lot | Spot claiming (CAS), entry rate limiting | "Add EV charging — design changes?" |

### Anti-Patterns to Avoid in LLD Interviews

```
❌ God class: One class does everything → violates SRP
❌ Anemic model: Entities are just POJOs with getters/setters; all logic in services
❌ Over-engineering: Using every pattern you know — pick patterns that solve problems
❌ No interfaces: Every class references concrete types → kills OCP and testability
❌ Ignoring concurrency: "I'll add thread safety later" — add it from the start
❌ Getters everywhere: Exposing internals breaks encapsulation → prefer behaviour methods
❌ No validation: Where do you validate? Not in every service method — centralise it
```

---

## ✅ Module A6 + Track A Completion Checklist

- [ ] Can design Chess Game end-to-end with Move validation and undo
- [ ] Can design Elevator system with LOOK algorithm and concurrent requests
- [ ] Can design Library system with reservation queue and fine calculation
- [ ] Can design Food ordering system with order state machine
- [ ] Can design ATM with PIN retry, transaction atomicity, and cash dispensing
- [ ] Know the 5-step LLD interview framework
- [ ] Know which pattern to apply to which LLD problem
- [ ] Can identify anti-patterns in LLD design
- [ ] Completed Task 1 — Snake and Ladder (all 5 patterns)
- [ ] Completed Task 2 — Parking Lot V2 (monthly pass, EV, VIP)
- [ ] Completed Task 3 — Multi-level Cache System
- [ ] Completed Capstone — BookMyShow (all patterns + concurrency)

**🎉 TRACK A COMPLETE — Ready for Track B: High-Level System Design**

### What's Next in Track B
- B1: HLD Fundamentals — CAP theorem, consistency, availability
- B2: Databases at scale — sharding, replication, indexing
- B3: Caching — Redis, CDN, cache invalidation strategies
- B4: Message queues — Kafka, RabbitMQ, event streaming
- B5–B10: Classic HLD problems — URL shortener, Twitter, Netflix, Uber, WhatsApp, Google Drive
