import unittest

import pandas as pd

from id3 import information_gain


class TestHeuristics(unittest.TestCase):
    def test_calculate_entropy(self):
        # known value
        self.assertAlmostEqual(information_gain.calculate_entropy(positives=9, negatives=5), 0.94029)

        # known value
        self.assertAlmostEqual(information_gain.calculate_entropy(positives=16, negatives=14), 0.99679)

        # boolean tree value
        self.assertAlmostEqual(information_gain.calculate_entropy(positives=5, negatives=3), 0.95443)

        # edge case: equal distribution
        self.assertAlmostEqual(information_gain.calculate_entropy(positives=15, negatives=15), 1.0)

        # edge case: no entropy
        self.assertAlmostEqual(information_gain.calculate_entropy(positives=10, negatives=0), 0.0)


class TestInformationGainHeuristic(unittest.TestCase):
    def test_ig_heuristic(self):
        # dummy test to get started
        self.assertEqual(information_gain.ig_heuristic("", [], 'Class', {}), "")

        # create our dataframe (this is for boolean function a OR (b AND c)
        tt = {'a': [0, 0, 0, 0, 1, 1, 1, 1],
              'b': [0, 0, 1, 1, 0, 0, 1, 1],
              'c': [0, 1, 0, 1, 0, 1, 0, 1],
              'Class': [0, 0, 0, 1, 1, 1, 1, 1]}
        df = pd.DataFrame(data=tt)

        # a will have most IG since if it's true, everything's true
        self.assertEqual(information_gain.ig_heuristic(df, ['a', 'b', 'c'], 'Class', {}), 'a')

        # c will have next biggest IG (equal to b), but our algorithm gives preference to first one
        self.assertEqual(information_gain.ig_heuristic(df, ['b', 'c'], 'Class', {'a': 0}), 'b')


if __name__ == '__main__':
    unittest.main()
