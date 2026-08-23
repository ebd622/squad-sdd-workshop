# CLI Contract: Rock-Paper-Scissors (Java)

**Feature**: 001-rock-paper-scissors-cli-java
**Phase**: 1 (Design) — interface contract

This app has no network or library API; its "contract" is the terminal interaction over
stdin/stdout. Wording below is illustrative — exact strings are the implementer's choice as long as
they satisfy the requirements and the smoke test.

## Invocation

```bash
javac Rps.java && java Rps      # compile then run
# or, JDK 21+ single-file launch:
java Rps.java
```

## Input contract (stdin)

- One move per line. Accepted, case-insensitive after trimming whitespace:
  - `rock`, `paper`, `scissors` → play a round.
  - `quit`, `q` → end the session.
- Any other line (including empty) → invalid input.
- End-of-input (EOF / Ctrl-D) → treated as quit.

## Output contract (stdout)

- **Startup**: a brief greeting/instructions and the first prompt.
- **Prompt** (before each move): e.g. `Enter your move (rock/paper/scissors) or 'quit':`
- **After a valid round**, in order:
  1. The computer's move, e.g. `Computer chose: paper`.
  2. The outcome: one of player win / computer win / tie, e.g. `You lose this round!`.
  3. The running score, e.g. `Score — You: 0  Computer: 1  Ties: 0`.
- **Invalid input**: a short message, e.g. `Invalid input. Please type rock, paper, scissors, or quit.`, then re-prompt.
- **On quit / EOF**: a final score summary, e.g. `Final score — You: 2  Computer: 1  Ties: 0`, then exit.

## Behavioral guarantees

- Exit code `0` on normal quit and on EOF (clean exit, no stack trace).
- The program never terminates on invalid input — it always re-prompts.
- The computer's move is chosen uniformly at random each round.
- Outcome follows standard rules: rock > scissors, scissors > paper, paper > rock.

## Reference happy-path transcript

```text
$ printf 'rock\npaper\nquit\n' | java Rps
Welcome to Rock-Paper-Scissors!
Enter your move (rock/paper/scissors) or 'quit': Computer chose: scissors
You win this round!
Score — You: 1  Computer: 0  Ties: 0
Enter your move (rock/paper/scissors) or 'quit': Computer chose: paper
It's a tie!
Score — You: 1  Computer: 0  Ties: 1
Enter your move (rock/paper/scissors) or 'quit': Final score — You: 1  Computer: 0  Ties: 1
Goodbye!
```

(Computer moves above are illustrative; actual moves are random.)
