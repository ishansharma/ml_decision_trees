import argparse

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
parser.add_argument('validation_set_path', type=str, help='Path to test set')

# whether to print the tree or not
parser.add_argument('to_print', type=str, help='Whether to print or not')

args = parser.parse_args()
