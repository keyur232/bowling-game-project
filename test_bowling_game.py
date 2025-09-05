import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.g = BowlingGame()

    # Helpers
    def roll_many(self, n, pins):
        for _ in range(n):
            self.g.roll(pins)

    def roll_sequence(self, seq):
        for p in seq:
            self.g.roll(p)

    # Core scoring scenarios
    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.g.score(), 20)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.g.score(), 300)

    def test_all_spares(self):
        self.roll_many(21, 5)
        self.assertEqual(self.g.score(), 150)

    def test_regular_game(self):
        seq = [3,4, 2,5, 1,6, 4,2, 8,1, 7,1, 5,3, 2,3, 4,3, 2,6]
        self.roll_sequence(seq)
        self.assertEqual(self.g.score(), 72)

    def test_example_mixed(self):
        seq = [10, 3,6, 5,5, 8,1, 10, 10, 10, 9,0, 7,3, 10,10,8]
        self.roll_sequence(seq)
        self.assertEqual(self.g.score(), 190)

    # 10th-frame edge cases
    def test_tenth_frame_spare_bonus(self):
        self.roll_many(18, 0)
        self.roll_sequence([9,1, 5])  # spare + bonus 5
        self.assertEqual(self.g.score(), 15)

    def test_tenth_frame_open(self):
        self.roll_many(18, 0)
        self.roll_sequence([4,5])  # open 10th
        self.assertEqual(self.g.score(), 9)

    # Special strike cases
    def test_consecutive_strikes(self):
        # Frames: X, X, 4,2 → 24 + 16 + 6 = 46
        self.roll_sequence([10, 10, 4, 2])
        self.roll_many(14, 0)
        self.assertEqual(self.g.score(), 46)

    # Validation tests (minor changes implemented)
    def test_invalid_pin_count_raises(self):
        with self.assertRaises(ValueError):
            self.g.roll(-1)
        with self.assertRaises(ValueError):
            self.g.roll(11)

    def test_frame_total_exceeds_ten_raises(self):
        self.g.roll(3)
        with self.assertRaises(ValueError):
            self.g.roll(8)  # would make 11 in a frame

    def test_no_rolls_after_game_complete(self):
        self.roll_many(12, 10)  # perfect game
        with self.assertRaises(ValueError):
            self.g.roll(0)

if __name__ == "__main__":
    unittest.main()
