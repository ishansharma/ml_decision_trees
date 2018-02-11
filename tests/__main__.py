# code reference: https://docs.python.org/3.6/library/unittest.html#module-unittest
import unittest

from tests import test_accuracy
from tests import test_id3_heuristics
from tests import test_pruner
from tests import test_tree_construction


def suite():
    test_suite = unittest.TestSuite()

    # tests for entropy function
    test_suite.addTest(test_id3_heuristics.TestHeuristics('test_calculate_entropy'))

    # tests for information gain
    test_suite.addTest(test_id3_heuristics.TestInformationGainHeuristic('test_ig_heuristic'))

    # tests for tree construction
    test_suite.addTest(test_tree_construction.TestTreeConstruction('test_binary_expression'))

    # tests for accuracy
    test_suite.addTest(test_accuracy.TestAccuracy('test_for_booleans'))
    test_suite.addTest(test_accuracy.TestAccuracy('test_inaccurate'))

    # tests for pruning
    test_suite.addTest(test_pruner.TestPruner('test_list_ordering'))
    test_suite.addTest(test_pruner.TestPruner('test_list_order_without_filter'))
    test_suite.addTest(test_pruner.TestPruner('test_majority_class_search'))
    test_suite.addTest(test_pruner.TestPruner('test_node_pruning'))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
