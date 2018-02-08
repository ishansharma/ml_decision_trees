import unittest

from id3 import heuristics


class TestHeuristics(unittest.TestCase):
    def test_calculate_entropy(self):
        # known value
        self.assertAlmostEqual(heuristics.calculate_entropy(positives=9, negatives=5), 0.94029)

        # known value
        self.assertAlmostEqual(heuristics.calculate_entropy(positives=16, negatives=14), 0.99679)

        # edge case: equal distribution
        self.assertAlmostEqual(heuristics.calculate_entropy(positives=15, negatives=15), 1.0)

        # edge case: no entropy
        self.assertAlmostEqual(heuristics.calculate_entropy(positives=10, negatives=0), 0.0)


if __name__ == '__main__':
    unittest.main()
