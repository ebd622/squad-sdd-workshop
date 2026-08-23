# Quickstart: Rock-Paper-Scissors CLI

## Prerequisites
- Python 3 (3.8+). No dependencies to install.

## Run interactively
```bash
python rps.py
```
Type `rock`, `paper`, `scissors` (or `r`/`p`/`s`) at the prompt. Type `quit` or `q` to exit.

## Non-interactive smoke test (happy path)
```bash
printf 'rock\nquit\n' | python rps.py
```
Expected: the app prints the computer's move, the round outcome, the running score, then a
final score line, and exits cleanly (status 0).

## What to verify
- Valid moves and shorthand are judged correctly (see [contracts/cli.md](./contracts/cli.md)).
- Running score updates each round (see [data-model.md](./data-model.md)).
- `quit`/`q` and EOF exit with the final score and no error output.
