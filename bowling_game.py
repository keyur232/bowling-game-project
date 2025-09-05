"""
Bowling Game Implementation 

This module provides a `BowlingGame` class that implements standard
ten-pin bowling scoring rules with correct handling of the 10th frame,
strikes, spares, and open frames.
"""

from __future__ import annotations
from typing import List


class BowlingGame:
    """
    Represents a single ten-pin bowling game.

    Attributes:
        rolls: A flat list of all rolls made in the game.
    """
    def __init__(self):
        self.rolls: List[int] = []

    # ------------------------------- Public API -------------------------------
    def roll(self, pins: int) -> None:
        """Record a roll."""
        if self.is_complete():
            raise ValueError("No more rolls allowed: the game is complete.")

        if not isinstance(pins, int) or pins < 0 or pins > 10:
            raise ValueError("Pins must be an integer between 0 and 10.")

        tentative = self.rolls + [pins]
        self._validate_sequence(tentative)
        self.rolls = tentative

    def score(self) -> int:
        """Calculate the score for the current game."""
        score = 0
        i = 0

        # Frames 1–9
        for _ in range(9):
            if i >= len(self.rolls):
                break
            if self._is_strike(i):
                score += 10 + self._bonus_sum(i + 1, 2)
                i += 1
            elif self._is_spare(i):
                score += 10 + self._bonus_sum(i + 2, 1)
                i += 2
            else:
                frame_sum = self.rolls[i]
                if i + 1 < len(self.rolls):
                    frame_sum += self.rolls[i + 1]
                score += frame_sum
                i += 2

        # 10th frame
        tenth = self._extract_tenth_frame_rolls()
        score += sum(tenth)
        return score

    # ----------------------------- Helper methods ----------------------------
    def _is_strike(self, i: int) -> bool:
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i: int) -> bool:
        return (i + 1 < len(self.rolls)
                and self.rolls[i] != 10
                and self.rolls[i] + self.rolls[i + 1] == 10)

    def _bonus_sum(self, start: int, count: int) -> int:
        return sum(self.rolls[start:start + count])

    def is_complete(self) -> bool:
        return self._extract_tenth_frame_rolls_fullonly() is not None

    def _extract_tenth_frame_rolls(self) -> List[int]:
        i = 0
        frames_done = 0
        while frames_done < 9 and i < len(self.rolls):
            if self._is_strike(i):
                i += 1
            else:
                i += 2
            frames_done += 1
        return self.rolls[i:i + 3]

    def _extract_tenth_frame_rolls_fullonly(self) -> List[int] | None:
        i = 0
        frames_done = 0
        while frames_done < 9:
            if i >= len(self.rolls):
                return None
            if self._is_strike(i):
                i += 1
            else:
                if i + 1 >= len(self.rolls):
                    return None
                i += 2
            frames_done += 1

        r = self.rolls[i:]
        if not r:
            return None

        if r[0] == 10:
            if len(r) < 3:
                return None
            return r[:3]
        if len(r) >= 2 and r[0] + r[1] == 10:
            if len(r) < 3:
                return None
            return r[:3]
        if len(r) >= 2 and r[0] + r[1] < 10:
            return r[:2]
        return None

    def _validate_sequence(self, seq: List[int]) -> None:
        i = 0
        frames_done = 0
        while frames_done < 9 and i < len(seq):
            first = seq[i]
            if first == 10:
                i += 1
            else:
                if i + 1 < len(seq):
                    second = seq[i + 1]
                    if first + second > 10:
                        raise ValueError("Frame total cannot exceed 10 (frames 1–9).")
                    i += 2
                else:
                    i += 1
            frames_done += 1

        tenth = seq[i:]
        if not tenth:
            return
        if len(tenth) > 3:
            raise ValueError("10th frame cannot have more than 3 rolls.")
        a = tenth[0]
        if a == 10:
            return
        if len(tenth) >= 2:
            b = tenth[1]
            if a + b > 10:
                raise ValueError("10th-frame first two rolls cannot exceed 10 unless first was a strike.")
            if a + b < 10 and len(tenth) == 3:
                raise ValueError("No bonus roll allowed for open 10th frame.")
