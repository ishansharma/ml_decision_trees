import argparse

from data_structures import tree
from files import reader
from id3 import id3

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

# construct the tree from training data
training_tree = tree.DecisionTree()
unrooted_training_tree = id3.construct(training_data, 'Class',
                                       training_data.columns)

training_tree.root = unrooted_training_tree
# tree construction is done

print(training_tree)
