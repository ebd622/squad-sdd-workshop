# Implementation Plan: Rock-Paper-Scissors CLI

**Branch**: `001-rock-paper-scissors-cli` | **Date**: 2026-08-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-rock-paper-scissors-cli/spec.md`

## Summary

Build an interactive human-vs-computer Rock-Paper-Scissors CLI in a single Python file.
A loop prompts for a move, the computer picks randomly, the outcome is judged by standard
rules, a running score is shown, and the player quits with `quit`/`q`. Standard library
only; happy path is the deliverable.

## Technical Context

**Language/Version**: Python 3 (3.8+)

**Primary Dependencies**: None — standard library only (`random`, `sys`)

**Storage**: N/A (score kept in memory for the session)

**Testing**: Manual/piped-input smoke test (`printf 'rock\nquit\n' | python rps.py`)

**Target Platform**: Any OS with Python 3 (terminal)

**Project Type**: single-file CLI

**Performance Goals**: N/A — interactive, instant per round

**Constraints**: No external dependencies; runnable via `python rps.py`

**Scale/Scope**: Single user, one process, ~1 file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- I. Speed Over Polish — PASS: single file, no abstractions beyond helper functions.
- II. Happy Path Is Done — PASS: scope is play-loop + quit; edge cases limited to reprompt
  and graceful EOF/interrupt.
- III. Standard Library Only — PASS: only `random` and `sys`; runnable via `python rps.py`.
- IV. SDD Gate — PASS: constitution → spec → plan (this) → tasks → implement, in order.

No violations. Complexity Tracking omitted.

## Project Structure

### Documentation (this feature)

```text
specs/001-rock-paper-scissors-cli/
├── plan.md              # This file
├── spec.md              # Feature spec
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── cli.md           # CLI interaction contract
├── checklists/
│   └── requirements.md
└── tasks.md             # /speckit-tasks output (not created here)
```

### Source Code (repository root)

```text
rps.py                   # Single-file interactive CLI (entry point)
```

**Structure Decision**: A single file `rps.py` at the repo root. No package, modules, or
tests directory — the POC happy path needs nothing more. `python rps.py` is the entry point.
