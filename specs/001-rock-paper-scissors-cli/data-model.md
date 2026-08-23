# Data Model: Rock-Paper-Scissors CLI

All state is in-memory for the session; nothing is persisted.

## Move
- Domain: one of `rock`, `paper`, `scissors`.
- Input forms accepted: full name or shorthand `r`/`p`/`s`, case-insensitive.

## Round
- Fields: `player_move` (Move), `computer_move` (Move), `outcome` (win | lose | tie).
- Outcome rule: `rock` beats `scissors`, `scissors` beats `paper`, `paper` beats `rock`;
  equal moves are a tie; otherwise the player loses.

## Score
- Fields: `wins` (int), `losses` (int), `ties` (int), all starting at 0.
- Transition: after each judged round, increment exactly one counter based on the outcome.
- Display: shown after every round and once more as the final score on quit.
