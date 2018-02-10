"""
Implementation of data structure for Decision Tree

Node is building block for the tree. This class defines the node
"""


class Node:
    def __init__(self, label):
        self.label = label  # should will be class name if it's an internal node, 0 or 1 if leaf
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.label)


class DecisionTree:
    def __init__(self):
        self.root = None
