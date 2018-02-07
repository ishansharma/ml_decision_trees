"""
Implementation of data structure for Decision Tree

Node is building block for the tree. This class defines the node
"""


class Node:
    def __init__(self, attribute, value):
        self.value = value  # should be 0 for negative, 1 for positive
        self.attribute = attribute  # label in our Pandas data structure

    def __str__(self):
        return str(self.attribute) + " = " + str(self.value)
