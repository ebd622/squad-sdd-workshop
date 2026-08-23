---
description: "Task list for Rock-Paper-Scissors CLI"
---

# Tasks: Rock-Paper-Scissors CLI

**Input**: Design documents from `/specs/001-rock-paper-scissors-cli/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli.md, quickstart.md

**Tests**: Not requested. POC — validation is a piped-input smoke test, no test tasks.

**Organization**: Tasks grouped by user story. Single file `rps.py` at repo root.

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: Setup

**Purpose**: Create the entry-point file and its skeleton.

- [X] T001 Create `rps.py` at repo root with a `#!/usr/bin/env python3` shebang, module docstring, `import random`, `import sys`, and a `main()` guarded by `if __name__ == "__main__"`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core move/outcome helpers all stories depend on.

**⚠️ CRITICAL**: Must complete before user stories.

- [X] T002 In `rps.py`, add move constants and normalization: `MOVES = ["rock", "paper", "scissors"]`, a `SHORTHAND = {"r": "rock", "p": "paper", "s": "scissors"}` map, and a `normalize_move(text)` helper that lowercases/strips input and resolves full names and shorthand, returning the move or `None`.
- [X] T003 In `rps.py`, add the outcome engine: `BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}` and a `judge(player, computer)` that returns `"tie"`, `"win"`, or `"lose"` per data-model.md.

**Checkpoint**: Core game logic exists and is callable.

---

## Phase 3: User Story 1 - Play a round against the computer (Priority: P1) 🎯 MVP

**Goal**: Prompt for a move, judge it against a random computer move, show outcome and running score, loop.

**Independent Test**: `printf 'rock\nquit\n' | python rps.py` prints computer move, outcome, and score.

- [X] T004 [US1] In `rps.py`, implement the game loop in `main()`: keep a score dict `{"wins":0,"losses":0,"ties":0}`, print the prompt from contracts/cli.md, read input with `input()`, and on a valid move pick `random.choice(MOVES)` for the computer, call `judge`, update the score, and print player move, computer move, and outcome (You win / You lose / Tie).
- [X] T005 [US1] In `rps.py`, after each round print the running score line `Score - You: W  Computer: L  Ties: T` from the score dict.
- [X] T006 [US1] In `rps.py`, handle unrecognized input (FR-007): when `normalize_move` returns `None` and the input is not a quit command, print a brief "not recognized" message and reprompt without counting a round.

**Checkpoint**: The core game is fully playable in a loop.

---

## Phase 4: User Story 2 - Quit gracefully and see final score (Priority: P2)

**Goal**: Exit cleanly on quit/EOF/interrupt, showing the final score.

**Independent Test**: Typing `quit` (or Ctrl-D) prints the final score and exits with status 0, no traceback.

- [X] T007 [US2] In `rps.py`, treat `quit`/`q` (case-insensitive) as an exit command in the loop: print a final score line and return from `main()` (exit 0).
- [X] T008 [US2] In `rps.py`, wrap the input loop to catch `EOFError` and `KeyboardInterrupt`, printing the final score and exiting cleanly (status 0) without a stack trace.

**Checkpoint**: All exit paths are graceful and show the final score.

---

## Phase 5: Polish & Validation

- [X] T009 Run the quickstart smoke test `printf 'rock\nquit\n' | python rps.py` and confirm the happy path (round outcome, score, clean exit) works.

---

## Dependencies & Execution Order

- **Setup (T001)**: first.
- **Foundational (T002–T003)**: after Setup; blocks all stories.
- **US1 (T004–T006)**: after Foundational. MVP.
- **US2 (T007–T008)**: after Foundational; integrates with the US1 loop.
- **Polish (T009)**: after US1 (and US2 for full happy path).

### Parallel Opportunities

- Single file, so tasks are largely sequential. T002 and T003 are independent logic blocks but edit the same file — keep them ordered to avoid conflicts.

---

## Implementation Strategy

- **MVP**: T001 → T003 → T004–T006 gives a playable game.
- **Full happy path**: add T007–T008 for graceful quit, then T009 to validate.
