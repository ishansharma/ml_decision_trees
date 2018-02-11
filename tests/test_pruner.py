import unittest

import pandas as pd

from data_structures import tree
from id3 import id3
from post_pruning import random


class TestPruner(unittest.TestCase):
    def test_list_ordering(self):
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

        p = random.Pruner(dt, 5, 10)
        ordered_nodes = p._order_non_leaf_nodes(dt)
        expected_nodes = ['a', 'b', 'c', 'c', 'd', 'd']

        self.assertCountEqual(ordered_nodes, expected_nodes)
