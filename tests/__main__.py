# code reference: https://docs.python.org/3.6/library/unittest.html#module-unittest
import unittest

from tests import test_id3_heuristics
from tests import test_tree_construction


def suite():
    test_suite = unittest.TestSuite()

    # tests for entropy function
    test_suite.addTest(test_id3_heuristics.TestHeuristics('test_calculate_entropy'))

    # tests for information gain
    test_suite.addTest(test_id3_heuristics.TestInformationGainHeuristic('test_ig_heuristic'))

    # tests for tree construction
    test_suite.addTest(test_tree_construction.TestTreeConstruction('test_binary_expression'))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
