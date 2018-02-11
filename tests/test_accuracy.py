import unittest

import pandas as pd

from data_structures import tree
from decision_tree import accuracy
from id3 import id3


class TestAccuracy(unittest.TestCase):
    def test_for_booleans(self):
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

        expected_accuracy = 1.00
        measured_accuracy = accuracy.measure(dt, df, 'Class')

        self.assertAlmostEquals(expected_accuracy, measured_accuracy)

    def test_inaccurate(self):
        # dataframe for ((a OR b) AND (c or d)
        truth_table = {
            'a': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            'b': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            'c': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            'd': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            'Class': [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        }
        df = pd.DataFrame(data=truth_table)

        validation_table = {
            'a': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            'b': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            'c': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            'd': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            'Class': [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
        }
        dv = pd.DataFrame(data=validation_table)

        dt = tree.DecisionTree()
        unrooted_tree = id3.construct(df, 'Class', df.columns)
        dt.root = unrooted_tree

        expected_accuracy = 0.8125
        measured_accuracy = accuracy.measure(dt, dv, 'Class')

        self.assertAlmostEquals(expected_accuracy, measured_accuracy)
