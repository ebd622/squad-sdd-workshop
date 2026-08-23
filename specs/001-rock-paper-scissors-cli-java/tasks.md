# Tasks: Rock-Paper-Scissors CLI (Java)

**Input**: Design documents from `/specs/001-rock-paper-scissors-cli-java/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/cli.md, quickstart.md

**Tests**: No automated tests. Per team policy (Constitution III) validation is a single manual
happy-path smoke test — see T009. No JUnit / test framework tasks.

**Organization**: Tasks are grouped by user story (US1–US3 from spec.md). Because this is a single
self-contained file (`Rps.java`), the story slices below are implemented within that one file; each
story is still independently demonstrable at its checkpoint.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single-file project: `Rps.java` at the **repository root**. No `src/` tree, no build files.
- Build/run with the native JDK toolchain: `javac Rps.java && java Rps`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Get a compilable skeleton in place.

- [x] T001 Verify the JDK toolchain is available: run `java -version` and `javac -version`
  (expect a JDK 11+; environment has 25.0.3).
- [x] T002 Create `Rps.java` at the repository root with a `public class Rps` and an empty
  `public static void main(String[] args)`; confirm it compiles with `javac Rps.java`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core building blocks every user story needs.

**⚠️ CRITICAL**: Must be complete before US1–US3 work.

- [x] T003 In `Rps.java`, define the move set (`{"rock","paper","scissors"}`), a
  `java.util.Random` instance, and a helper to pick the computer's random move (FR-003).
- [x] T004 In `Rps.java`, implement the outcome logic: a method that takes player move + computer
  move and returns PLAYER_WIN / COMPUTER_WIN / TIE using standard rules — rock>scissors,
  scissors>paper, paper>rock (FR-004); and add in-memory score counters (playerWins, computerWins,
  ties) per data-model.md (FR-006).

**Checkpoint**: Core game logic exists and compiles; ready for the interactive loop.

---

## Phase 3: User Story 1 - Play a round against the computer (Priority: P1) 🎯 MVP

**Goal**: Player enters a move (case-insensitive) and sees the computer's move and the round outcome.

**Independent Test**: `printf 'rock\n' | java Rps` shows a computer move and a win/lose/tie result.

- [x] T005 [US1] In `Rps.java`, add input reading with `java.util.Scanner` over `System.in`: print a
  prompt, read a line, `trim()` + `toLowerCase()` it, and map valid entries to a move; on a valid
  move, pick the computer move (T003), resolve the outcome (T004), and print the computer's move and
  the round result (FR-001, FR-002, FR-005).

**Checkpoint**: A single round plays end-to-end and prints the result — MVP demoable.

---

## Phase 4: User Story 2 - Running score and keep playing (Priority: P2)

**Goal**: After each round show the running score and prompt again for continuous play.

**Independent Test**: `printf 'rock\npaper\n' | java Rps` plays two rounds, each printing an updated
running score.

- [x] T006 [US2] In `Rps.java`, update the score counters after each resolved round and print the
  running score (You / Computer / Ties) after the round result (FR-006).
- [x] T007 [US2] In `Rps.java`, wrap round handling in a loop so the program re-prompts for a new
  move after each round; also print a short "invalid input" message and re-prompt on empty/unknown
  input instead of crashing (FR-007, FR-009).

**Checkpoint**: Multiple rounds play in one session with a live running score.

---

## Phase 5: User Story 3 - Quit the game gracefully (Priority: P3)

**Goal**: Player quits with `quit`/`q` (or EOF); program prints a final score and exits cleanly.

**Independent Test**: `printf 'rock\nquit\n' | java Rps; echo "exit=$?"` prints a final score and
exits with code 0.

- [x] T008 [US3] In `Rps.java`, handle `quit`/`q` (case-insensitive) and end-of-input
  (`Scanner.hasNextLine()` false / Ctrl-D) by breaking the loop, printing a final score summary, and
  exiting cleanly with no stack trace (FR-008, FR-010).

**Checkpoint**: Full play → score → quit loop works end-to-end.

---

## Phase 6: Validation (Happy-Path Smoke Test)

**Purpose**: Confirm the definition of done — app runs and the happy path works.

- [x] T009 Build and smoke-test per quickstart.md: `javac Rps.java` then
  `printf 'rock\npaper\nquit\n' | java Rps` — verify it plays two rounds (computer move + outcome +
  running score each), prints a final score, and exits cleanly (exit code 0). Hand off to the
  Implementer/Tester once green.

---

## Dependencies & Execution Order

- **Setup (T001–T002)**: no dependencies — do first.
- **Foundational (T003–T004)**: depends on T002 — BLOCKS all user stories.
- **US1 (T005)**: depends on T003, T004.
- **US2 (T006–T007)**: depends on T005.
- **US3 (T008)**: depends on the loop from T007.
- **Validation (T009)**: depends on T005–T008 (needs the full loop).

Because all logic lives in the single `Rps.java` file, the tasks are inherently sequential — there
are no `[P]` parallel opportunities within one file. The natural build order is
T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008 → T009.

## Notes

- Single file `Rps.java` at repo root; compile/run with `javac Rps.java && java Rps`.
- Standard library only (`java.util.Scanner`, `java.util.Random`) — no dependencies, no build tool.
- Stop at the T005 checkpoint for the minimal MVP demo; T006–T008 complete the full session loop.
- Keep it lean: no persistence, no best-of-N, no difficulty levels (Constitution IV).
