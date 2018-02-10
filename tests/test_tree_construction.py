import unittest

import pandas as pd

from data_structures import tree
from id3 import id3


class TestTreeConstruction(unittest.TestCase):
    def test_binary_expression(self):
        # dataframe for ((a OR b) AND (c or d)
        truth_table = {
            'a': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            'b': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            'c': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            'd': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            'Class': [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        }
        df = pd.DataFrame(data=truth_table)

        dt = tree.DecisionTree()
        unrooted_tree = id3.construct(df, 'Class', df.columns)
        dt.root = unrooted_tree

        # dt.print(dt.root)
        # self.assertEqual(tree, '')
        # self.assertEqual('', '')
        # self.assertEqual()
