# Quickstart: Rock-Paper-Scissors CLI (Java)

**Feature**: 001-rock-paper-scissors-cli-java

## Prerequisites

- A JDK on your PATH. Verified in this environment: `openjdk 25.0.3`, `javac 25.0.3`
  (any JDK 11+ works). Check with:

```bash
java -version
javac -version
```

## Build

From the repository root, where `Rps.java` lives:

```bash
javac Rps.java
```

This produces `Rps.class` in the same directory.

## Run (interactive)

```bash
java Rps
```

Then type `rock`, `paper`, or `scissors` at the prompt (case-insensitive). After each round you'll
see the computer's move, the outcome, and the running score. Type `quit` or `q` to stop.

## Happy-path smoke test (non-interactive)

Pipe moves in and confirm it plays rounds, shows scores, and exits cleanly:

```bash
printf 'rock\npaper\nquit\n' | java Rps
```

Expected: two rounds are played (each showing computer move, outcome, and running score), then a
final score line and a clean exit (exit code 0). Verify with:

```bash
printf 'rock\npaper\nquit\n' | java Rps; echo "exit=$?"
```

## Optional: single-file launch (JDK 21+)

```bash
java Rps.java
```

Runs directly from source without producing a `.class` file.
