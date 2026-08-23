# CLI Contract: Rock-Paper-Scissors

## Entry point
- Command: `python rps.py`
- No arguments or flags.

## Interaction loop
1. Prints a prompt asking for a move (e.g., `Your move (rock/paper/scissors or r/p/s, q to quit):`).
2. Reads one line from stdin.
3. Input handling (case-insensitive, trimmed):
   - `rock`/`r`, `paper`/`p`, `scissors`/`s` → play a round.
   - `quit`/`q` → print final score, exit 0.
   - anything else → print a brief "not recognized" message, reprompt, no round counted.
4. On a played round, prints: player move, computer move, outcome (You win / You lose / Tie),
   then the running score (`Score - You: W  Computer: L  Ties: T`).

## Termination
- `quit`/`q`, EOF (Ctrl-D), or interrupt (Ctrl-C) → print final score line and exit with
  status 0. No stack traces on normal termination.
