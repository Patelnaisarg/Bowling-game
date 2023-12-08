import unittest
from BowlingGame  import BowlingGame  # Assuming the code is in a file named bowling_game.py


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_multiple_times(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_multiple_times(0, 20)  # Roll 20 gutter balls
        self.assertEqual(self.game.score(), [0] * 10)  # Expecting a score of 0 for each frame

    def test_all_ones_game(self):
        self.roll_multiple_times(1, 20)  # Roll 20 ones
        self.assertEqual(self.game.score(), [20] * 10)  # Expecting a score of 20 for each frame

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)  # Spare in the first frame
        self.game.roll(3)
        self.roll_multiple_times(0, 17)  # Roll 17 gutter balls
        self.assertEqual(self.game.score(), [13, 0] + [0] * 8)  # Expecting a score of 13 for the first frame

    def test_one_strike(self):
        self.game.roll(10)  # Strike in the first frame
        self.game.roll(3)
        self.game.roll(4)
        self.roll_multiple_times(0, 16)  # Roll 16 gutter balls
        self.assertEqual(self.game.score(), [17, 7] + [0] * 8)  # Expecting a score of 17 for the first frame

    def test_perfect_game(self):
        self.roll_multiple_times(10, 12)  # 12 strikes
        self.assertEqual(self.game.score(), [30] * 10)  # Expecting a score of 30 for each frame

    def test_invalid_rolls(self):
        with self.assertRaises(ValueError):
            self.game.roll(-1)  # Test negative roll value
        with self.assertRaises(ValueError):
            self.game.roll(11)  # Test roll value greater than 10

   

if __name__ == '__main__':
    unittest.main()
