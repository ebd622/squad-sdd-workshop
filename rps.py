#!/usr/bin/env python3
"""Interactive Rock-Paper-Scissors CLI (human vs. computer).

Run with: python rps.py
"""

import random
import sys

MOVES = ["rock", "paper", "scissors"]
SHORTHAND = {"r": "rock", "p": "paper", "s": "scissors"}
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

PROMPT = "Your move (rock/paper/scissors or r/p/s, q to quit): "


def normalize_move(text):
    """Return the canonical move for user input, or None if unrecognized."""
    value = text.strip().lower()
    if value in MOVES:
        return value
    return SHORTHAND.get(value)


def judge(player, computer):
    """Return 'tie', 'win', or 'lose' from the player's perspective."""
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "win"
    return "lose"


def score_line(score):
    return (
        "Score - You: {wins}  Computer: {losses}  Ties: {ties}".format(**score)
    )


def main():
    score = {"wins": 0, "losses": 0, "ties": 0}
    print("Rock-Paper-Scissors! Type 'quit' or 'q' to stop.")
    while True:
        try:
            raw = input(PROMPT)
        except (EOFError, KeyboardInterrupt):
            print()
            break

        command = raw.strip().lower()
        if command in ("quit", "q"):
            break

        player = normalize_move(raw)
        if player is None:
            print("Not recognized. Please enter rock, paper, scissors (or r/p/s).")
            continue

        computer = random.choice(MOVES)
        outcome = judge(player, computer)
        print("You chose {}, computer chose {}.".format(player, computer))
        if outcome == "win":
            score["wins"] += 1
            print("You win!")
        elif outcome == "lose":
            score["losses"] += 1
            print("You lose!")
        else:
            score["ties"] += 1
            print("Tie!")
        print(score_line(score))

    print("Final " + score_line(score))
    print("Thanks for playing!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
