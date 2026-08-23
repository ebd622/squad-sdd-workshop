# Feature Specification: Rock-Paper-Scissors CLI (Java)

**Feature Branch**: `001-rock-paper-scissors-cli-java`

**Created**: 2026-08-23

**Status**: Draft

**Input**: User description: "Interactive Rock-Paper-Scissors CLI app written in Java"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Play a round against the computer (Priority: P1)

A player runs the program in their terminal, is prompted to enter a move, types `rock`, `paper`, or
`scissors`, and immediately sees what the computer chose and who won that round. This is the core of
the game and the MVP.

**Why this priority**: Without the ability to play a single round and see the result, there is no
game. This story alone delivers a demonstrable, playable proof-of-concept.

**Independent Test**: Run the program, enter `rock` (in any casing), and confirm it prints the
computer's move and the round outcome (win/lose/tie).

**Acceptance Scenarios**:

1. **Given** the program is running and prompting for a move, **When** the player enters `rock`,
   **Then** the program shows the computer's move and states whether the player won, lost, or tied.
2. **Given** the program is running, **When** the player enters `PAPER` (mixed/upper case),
   **Then** the input is accepted case-insensitively and a round result is shown.
3. **Given** the player picked a move that beats the computer's move, **When** the round resolves,
   **Then** the outcome is reported as a player win.

---

### User Story 2 - See a running score and keep playing (Priority: P2)

After each round the player sees a running tally (player wins, computer wins, ties) and is prompted
again, so they can play multiple rounds in one session.

**Why this priority**: Turns a one-shot interaction into an actual game session. Small addition on
top of P1, high demo value.

**Independent Test**: Play two rounds in one session and confirm the displayed score reflects both
rounds and the prompt reappears after each round.

**Acceptance Scenarios**:

1. **Given** a round has just resolved, **When** the result is displayed, **Then** the current
   running score (player / computer / ties) is shown.
2. **Given** a round has resolved, **When** the score is shown, **Then** the player is prompted for
   another move so the session continues.

---

### User Story 3 - Quit the game gracefully (Priority: P3)

The player ends the session on demand by typing `quit` or `q`, and the program prints a final score
and exits cleanly.

**Why this priority**: Needed for a clean demo loop, but the game is already playable without it.

**Independent Test**: While being prompted, enter `quit` and confirm the program prints a final
score summary and exits without error.

**Acceptance Scenarios**:

1. **Given** the program is prompting for a move, **When** the player enters `quit` or `q`
   (case-insensitive), **Then** the program prints the final score and exits cleanly.

---

### Edge Cases

- **Invalid input**: When the player enters something that is not a valid move or quit command, the
  program prints a short "invalid input" message and re-prompts (it does not crash or exit).
- **End of input (EOF / Ctrl-D)**: When input stream closes, the program treats it like quitting —
  prints the final score and exits cleanly.
- **Empty line**: An empty entry is treated as invalid input and triggers a re-prompt.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST run as an interactive command-line program that reads player moves from
  standard input and writes prompts and results to standard output.
- **FR-002**: System MUST accept the moves `rock`, `paper`, and `scissors`, matched
  case-insensitively.
- **FR-003**: System MUST select the computer's move randomly among rock, paper, and scissors each
  round.
- **FR-004**: System MUST determine and display the round outcome (player win, computer win, or tie)
  using standard rules: rock beats scissors, scissors beats paper, paper beats rock.
- **FR-005**: System MUST display the computer's chosen move each round.
- **FR-006**: System MUST maintain and display a running score of player wins, computer wins, and
  ties after each round.
- **FR-007**: System MUST loop, prompting for a new move after each round, until the player quits.
- **FR-008**: Users MUST be able to quit by entering `quit` or `q` (case-insensitive); on quit the
  system MUST print a final score and exit cleanly.
- **FR-009**: System MUST handle invalid/empty input by showing a brief message and re-prompting,
  without crashing.
- **FR-010**: System MUST handle end-of-input (EOF / Ctrl-D) by exiting cleanly with a final score.

### Key Entities

- **Move**: One of rock, paper, scissors — the choice made by the player or the computer each round.
- **Round Outcome**: The result of comparing player and computer moves — player win, computer win,
  or tie.
- **Score**: Running counters for player wins, computer wins, and ties across the session.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A player can start the program and complete a full round (enter a move, see the
  computer's move and the outcome) with no additional setup beyond running the program.
- **SC-002**: Move entry is case-insensitive: the same move typed in any casing produces the same
  behavior.
- **SC-003**: After each round the running score is visible and reflects all rounds played so far.
- **SC-004**: The player can play multiple rounds in a single session and then quit, receiving a
  final score and a clean exit (no stack trace, non-error termination).
- **SC-005**: Invalid or empty input re-prompts rather than ending the game.

## Assumptions

- Single human player versus a random-choice computer; no networking or multiplayer.
- Interactive terminal session over standard input/output; no GUI.
- No persistence — score exists only for the current session and is not saved between runs.
- No scoring modes beyond a running tally (no best-of-N, rounds limit, or difficulty levels).
- English-language prompts and messages are sufficient for the demo.
