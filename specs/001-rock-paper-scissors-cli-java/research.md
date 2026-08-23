# Research: Rock-Paper-Scissors CLI (Java)

**Feature**: 001-rock-paper-scissors-cli-java
**Phase**: 0 (Outline & Research)

The spec is unambiguous and the scope is a single-file POC, so there were no open
`NEEDS CLARIFICATION` items. The decisions below record the small set of technical choices needed to
implement the plan, each checked against the constitution's "POC speed / no gold-plating" principles.

## Decision: Language & runtime

- **Decision**: Plain Java compiled and run with the JDK's native `javac`/`java`.
- **Rationale**: JDK 25 is present (`javac 25.0.3`). Java's standard library already provides
  everything needed (console I/O, randomness), so a single `.java` file is the fastest runnable form.
- **Alternatives considered**: Maven/Gradle project — rejected as gold-plating; a POC single-file
  game needs no build tool, dependency management, or module layout.

## Decision: Input handling

- **Decision**: Read lines from `System.in` using `java.util.Scanner`; normalize with
  `trim()` + `toLowerCase()` before matching.
- **Rationale**: `Scanner.hasNextLine()` / `nextLine()` gives simple line-oriented reads and a clean
  EOF signal (`hasNextLine()` returns false on Ctrl-D / closed stream), satisfying FR-010. Case
  normalization satisfies FR-002/SC-002.
- **Alternatives considered**: `BufferedReader` — equally viable but `Scanner` is marginally simpler
  for this loop. `System.console()` — rejected: returns null under piped input, which would break the
  smoke test.

## Decision: Computer move selection

- **Decision**: `java.util.Random.nextInt(3)` indexing into an array of the three moves.
- **Rationale**: Standard-library randomness, trivial and sufficient for a demo (FR-003).
- **Alternatives considered**: `Math.random()` — equivalent; `SecureRandom` — unnecessary for a game.

## Decision: Win/lose/tie logic

- **Decision**: Direct comparison using the fixed rules — rock beats scissors, scissors beats paper,
  paper beats rock; equal moves tie.
- **Rationale**: Three moves make explicit comparison the simplest correct approach (FR-004).
- **Alternatives considered**: Modular-arithmetic trick on move indices — clever but less readable;
  readability wins for a POC handoff.

## Decision: Quit & invalid input

- **Decision**: Treat `quit`/`q` (case-insensitive) as the quit command; any other non-move entry
  (including empty) prints a brief message and re-prompts; EOF behaves like quit.
- **Rationale**: Matches FR-007/008/009/010 with minimal branching and no crashes.
- **Alternatives considered**: Exit on any invalid input — rejected; re-prompting is the specified,
  friendlier happy-path behavior.

## Decision: Testing approach

- **Decision**: One manual happy-path smoke test via piped stdin
  (`printf 'rock\npaper\nquit\n' | java Rps`).
- **Rationale**: Team testing policy — a single happy-path smoke test, no edge-case matrix or
  automated framework (Constitution III).
- **Alternatives considered**: JUnit — rejected as gold-plating for a POC.

**Output**: All technical unknowns resolved; no `NEEDS CLARIFICATION` remain.
