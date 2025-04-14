import unittest
import loops

class TestLoops(unittest.TestCase):
    def test_ex21(self):
        self.assertEqual(loops.ex21(),[['X', ' ', ' ', ' ', 'X'], [' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', ' ', ' '], [' ', 'X', ' ', 'X', ' '], ['X', ' ', ' ', ' ', 'X']])
        # self.assertEqual(loops.ex21(),[[' ', ' ', ' ', ' ', ' '], [' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', ' ', ' '], [' ', 'X', ' ', 'X', ' '], ['X', ' ', ' ', ' ', 'X']])
    def test_ex16(self):
        self.assertEqual(loops.ex16(),[1, 8, 27, 64, 125, 216])

if __name__ == "__main__":
    unittest.main()
