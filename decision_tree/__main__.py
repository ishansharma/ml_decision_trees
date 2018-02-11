import argparse
import copy

from data_structures import tree
from decision_tree import accuracy
from files import reader
from id3 import id3
from post_pruning import random

parser = argparse.ArgumentParser(description="""Creates a decision tree from given files with Information Gain and Variance Impurity heuristics. 
 After constructing, it will do post pruning Then outputs accuracies and if asked, prints the decision tree""")

# argument L
parser.add_argument('l', metavar='L', type=int, help='Value for L')

# argument K
parser.add_argument('k', metavar='K', type=int, help='Value for K')

# path to training set
parser.add_argument('training_set_path', type=str, help='Path to training set')

# path to validation set
parser.add_argument('validation_set_path', type=str, help='Path to validation set')

# path to test set
parser.add_argument('test_set_path', type=str, help='Path to test set')

# whether to print the tree or not
parser.add_argument('to_print', type=str, help='Whether to print or not')

args = parser.parse_args()

# read all data. If wrong path is given, we exit here
training_data = reader.read_csv(args.training_set_path)
validation_data = reader.read_csv(args.validation_set_path)
test_data = reader.read_csv(args.test_set_path)

# construct the tree with information gain heuristic from training data
ig_training_tree = tree.DecisionTree()
unrooted_training_tree = id3.construct(training_data, 'Class', training_data.columns)

ig_training_tree.root = unrooted_training_tree

# construct the tree with variance impurity heuristic from training data
vi_training_tree = tree.DecisionTree()
unrooted_training_tree = id3.construct(training_data, 'Class', training_data.columns, "vi")

vi_training_tree.root = unrooted_training_tree

# prune the trees
ig_pruner = random.Pruner(copy.deepcopy(ig_training_tree), 10, 9, validation_data)
pruned_ig_tree = ig_pruner.prune()

vi_pruner = random.Pruner(copy.deepcopy(vi_training_tree), 10, 9, validation_data)
pruned_vi_tree = vi_pruner.prune()

# accuracy of our original tree
ig_original_accuracy = accuracy.measure(copy.deepcopy(ig_training_tree), copy.deepcopy(test_data), 'Class')
vi_original_accuracy = accuracy.measure(copy.deepcopy(vi_training_tree), copy.deepcopy(test_data), 'Class')

# accuracy of pruned ig tree
pruned_accuracy_for_ig = accuracy.measure(copy.deepcopy(pruned_ig_tree), copy.deepcopy(test_data), 'Class')
pruned_accuracy_for_vi = accuracy.measure(copy.deepcopy(pruned_vi_tree), copy.deepcopy(test_data), 'Class')

# print(training_tree)
print("Original IG accuracy:", ig_original_accuracy)
print("Original VI accuracy:", vi_original_accuracy)
print("Pruned IG tree accuracy:", pruned_accuracy_for_ig)
print("Pruned VI tree accuracy:", pruned_accuracy_for_vi)
