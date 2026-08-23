# Data Model: Rock-Paper-Scissors CLI (Java)

**Feature**: 001-rock-paper-scissors-cli-java
**Phase**: 1 (Design)

This is an in-memory, single-session POC. There is no persistence and no external schema. The
"data model" is the small set of in-process concepts the single `Rps` class works with.

## Entities

### Move

Represents a rock-paper-scissors choice made by the player or the computer.

- **Values**: `rock`, `paper`, `scissors` (a closed set of three).
- **Representation**: a lowercase string, or equivalently an index into a
  `{"rock", "paper", "scissors"}` array.
- **Validation**: player input is trimmed and lowercased, then checked for membership in the valid
  set; anything else is invalid input (not a Move).

### Round Outcome

The result of comparing the player's Move to the computer's Move.

- **Values**: `PLAYER_WIN`, `COMPUTER_WIN`, `TIE`.
- **Derivation rules**:
  - Equal moves → `TIE`.
  - rock vs scissors → rock wins; scissors vs paper → scissors wins; paper vs rock → paper wins.
  - The winning side determines `PLAYER_WIN` vs `COMPUTER_WIN`.

### Score

Running tally for the current session (resets every run; not persisted).

- **Fields**:
  - `playerWins`: integer, starts at 0.
  - `computerWins`: integer, starts at 0.
  - `ties`: integer, starts at 0.
- **Transitions**: after each resolved round, exactly one counter increments based on the Round
  Outcome. Displayed after every round and again as a final summary on quit/EOF.

## State & Lifecycle

```text
start → [prompt for move] → read line
    ├─ quit/q or EOF → print final Score → exit
    ├─ invalid/empty → print message → back to prompt
    └─ valid Move → computer picks random Move
                  → compute Round Outcome
                  → update Score
                  → print computer move, outcome, running Score
                  → back to prompt
```

No relationships beyond the above; no identifiers, no storage, no concurrency.
