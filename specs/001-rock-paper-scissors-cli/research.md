# Research: Rock-Paper-Scissors CLI

## Decision: Single-file Python script using stdlib only
- **Rationale**: POC speed. `random.choice` gives the computer move; `input()` reads the
  player move; a plain loop drives rounds. No dependencies keeps the demo zero-setup.
- **Alternatives considered**: `argparse`-based subcommands or a package with modules —
  rejected as gold-plating for an interactive loop; a class-based engine — rejected, plain
  functions are enough.

## Decision: Outcome judged with a "beats" map
- **Rationale**: `beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}` makes
  win logic a one-line lookup, clearer and less error-prone than nested conditionals.
- **Alternatives considered**: modular arithmetic on indices — rejected as less readable.

## Decision: Input normalization + shorthand
- **Rationale**: Lowercase and strip input; map `r/p/s` to full names so both forms work.
  Unrecognized input reprompts without counting a round (FR-007).

## Decision: Graceful exit on quit / EOF / interrupt
- **Rationale**: Treat `quit`/`q` plus `EOFError` (Ctrl-D) and `KeyboardInterrupt` (Ctrl-C)
  as "print final score and exit 0", satisfying the clean-exit criteria (SC-004).

## Unknowns
- None. All Technical Context fields resolved; no NEEDS CLARIFICATION remain.
