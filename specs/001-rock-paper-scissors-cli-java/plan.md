# Implementation Plan: Rock-Paper-Scissors CLI (Java)

**Branch**: `001-rock-paper-scissors-cli-java` | **Date**: 2026-08-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-rock-paper-scissors-cli-java/spec.md`

## Summary

Build an interactive Rock-Paper-Scissors terminal game in Java: the player types a move
(`rock`/`paper`/`scissors`, case-insensitive), the computer picks randomly, the program prints the
computer's move and the round outcome, shows a running score, and loops until the player quits
(`quit`/`q`) or input ends (EOF). Technical approach: a single self-contained Java class using only
the standard library (`java.util.Scanner`, `java.util.Random`), compiled and run with the JDK's
native `javac`/`java` tools — no build system, no dependencies.

## Technical Context

**Language/Version**: Java (JDK 25 available in environment: `openjdk 25.0.3`, `javac 25.0.3`).
Source targets standard Java with no version-specific features, so any modern JDK (11+) works.

**Primary Dependencies**: None. Java standard library only (`java.util.Scanner`,
`java.util.Random`).

**Storage**: N/A — score is in-memory for the session only; nothing is persisted.

**Testing**: Manual happy-path smoke test via piped stdin (team policy: single smoke test, no
automated test framework).

**Target Platform**: Any OS with a JDK installed; interactive terminal (stdin/stdout).

**Project Type**: Single-project command-line application (single source file).

**Performance Goals**: N/A — interactive human-speed input; no throughput or latency targets.

**Constraints**: No external dependencies; no build tool (plain `javac`/`java`); single file;
graceful handling of invalid input and EOF.

**Scale/Scope**: One source file (~1 class), one interactive game loop. No multiplayer, no
networking, no persistence.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Checked against Squad POC Constitution v1.0.0:

- **I. POC Speed First**: PASS — single file, native toolchain, no scaffolding overhead.
- **II. Spec-First & Phase-Gated**: PASS — this plan derives from an approved spec; tasks follow.
  `clarify` skipped (spec unambiguous), `analyze` skipped (team policy).
- **III. Happy-Path Definition of Done**: PASS — done = app runs and a full play→score→quit loop
  works; validation is one smoke test.
- **IV. No Gold-Plating**: PASS — no persistence, networking, difficulty levels, best-of-N, or build
  tooling. Standard library only.

No violations. Complexity Tracking section left empty (nothing to justify).

## Project Structure

### Documentation (this feature)

```text
specs/001-rock-paper-scissors-cli-java/
├── plan.md              # This file (/speckit-plan output)
├── spec.md              # Feature specification (/speckit-specify output)
├── research.md          # Phase 0 output (/speckit-plan)
├── data-model.md        # Phase 1 output (/speckit-plan)
├── quickstart.md        # Phase 1 output (/speckit-plan)
├── contracts/
│   └── cli.md           # Phase 1 output (/speckit-plan) — CLI I/O contract
└── tasks.md             # Phase 2 output (/speckit-tasks — NOT created here)
```

### Source Code (repository root)

```text
Rps.java                 # Single self-contained CLI class (public class Rps, main method)
```

**Structure Decision**: Single-file layout at the repository root. The app is a lone Java class
`Rps` with `public static void main(String[] args)`. No `src/` tree, packages, modules, or build
files — this is the leanest runnable form and satisfies the constitution's Delivery Constraints.
The file MUST be named `Rps.java` so it compiles to `Rps.class` and runs as `java Rps`.

## How to Build & Run

```bash
# Compile (produces Rps.class in the current directory)
javac Rps.java

# Run interactively
java Rps

# Happy-path smoke test (non-interactive, piped input)
printf 'rock\npaper\nquit\n' | java Rps
```

Modern JDKs (21+) also allow single-file source-launch without a separate compile step:
`java Rps.java`. The canonical, environment-agnostic path is `javac Rps.java && java Rps`.

## Complexity Tracking

> No constitution violations. No entries required.
