# Feature Specification: Rock-Paper-Scissors CLI

**Feature Branch**: `001-rock-paper-scissors-cli`

**Created**: 2026-08-23

**Status**: Draft

**Input**: User description: "Interactive Rock-Paper-Scissors CLI app in Python — human vs. computer, play rounds in a loop, show outcome and running score, quit gracefully."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Play a round against the computer (Priority: P1)

A player launches the app, is prompted for a move, types their choice, and immediately
sees whether they won, lost, or tied against the computer's move, plus the updated score.

**Why this priority**: This is the core game loop — without it there is no game. It alone
delivers a demonstrable, valuable app.

**Independent Test**: Run the app, enter `rock` (or `r`), and confirm the app prints the
computer's move, the round outcome (win/lose/tie), and a running score.

**Acceptance Scenarios**:

1. **Given** the app is running and prompting for a move, **When** the player enters a
   valid move (`rock`, `paper`, `scissors` or `r`/`p`/`s`), **Then** the app picks a random
   computer move, prints both moves, prints the outcome, and updates the running score.
2. **Given** a round has completed, **When** the app returns to the prompt, **Then** the
   player can play another round and the score persists across rounds.

---

### User Story 2 - Quit gracefully and see final score (Priority: P2)

At the prompt, the player types a quit command and the app exits cleanly after showing the
final score.

**Why this priority**: A clean exit is needed for a complete happy path and a good demo,
but the game is already valuable without it.

**Independent Test**: Run the app, type `quit` (or `q`) at the prompt, and confirm the app
prints the final score and exits without error.

**Acceptance Scenarios**:

1. **Given** the app is prompting for a move, **When** the player enters `quit` or `q`,
   **Then** the app prints the final score and exits with a success status.

---

### Edge Cases

- When the player enters an unrecognized move, the app reprompts with a short message and
  does not count a round.
- When the player triggers end-of-input (Ctrl-D) or interrupt (Ctrl-C), the app exits
  gracefully showing the final score rather than crashing.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST prompt the player for a move each round.
- **FR-002**: System MUST accept the moves `rock`, `paper`, `scissors` and their shorthand
  `r`, `p`, `s`, case-insensitively.
- **FR-003**: System MUST select the computer's move randomly each round.
- **FR-004**: System MUST determine and display the round outcome (win, lose, or tie) using
  standard rules (rock beats scissors, scissors beats paper, paper beats rock).
- **FR-005**: System MUST maintain and display a running score (player wins, computer wins,
  ties) after each round.
- **FR-006**: Users MUST be able to quit by entering `quit` or `q`, after which the system
  displays the final score and exits.
- **FR-007**: System MUST reject unrecognized input with a brief message and reprompt
  without counting a round.

### Key Entities

- **Move**: one of rock, paper, scissors.
- **Round**: a single play consisting of the player's move, the computer's move, and the
  resulting outcome.
- **Score**: running tally of player wins, computer wins, and ties.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A player can complete a full round (input → outcome + score shown) in a single
  prompt-and-response interaction.
- **SC-002**: 100% of valid inputs (`rock`/`paper`/`scissors` and `r`/`p`/`s`, any case)
  produce a correctly judged outcome.
- **SC-003**: The running score correctly reflects the number of wins, losses, and ties
  across all rounds played in a session.
- **SC-004**: Entering a quit command always exits the app cleanly showing the final score,
  with no error output.

## Assumptions

- Single human player versus a computer opponent that chooses randomly (no AI strategy).
- No persistence between sessions; the score resets each run.
- Text-only CLI, standard input/output; no GUI, network, or configuration.
- Best-of / target-score modes are out of scope; play continues until the player quits.
