import unittest

import pandas as pd

from data_structures import tree
from id3 import id3


class TestTreeConstruction(unittest.TestCase):
    def test_binary_expression(self):
        # TODO: Fix this test. Needs tree comparisons
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

        expected_tree = """a = 0: 
|b = 0: 0
|b = 1: 
||c = 0: 
|||d = 0: 0
|||d = 1: 1
||c = 1: 1
a = 1: 
|c = 0: 
||d = 0: 0
||d = 1: 1
|c = 1: 1"""

        self.assertEquals(expected_tree, str(dt))
