import copy
import random
from collections import deque, Counter

from data_structures import tree as t
from decision_tree import accuracy


class Pruner:
    def __init__(self, dt, l, k, validation_data):
        """
        Setup our class
        Parameters
        ----------
        dt: DecisionTree
        l: int
        k: int
        validation_data: DataFrame
            We test our accuracy against these samples
        """
        self.initial_tree = dt
        self.best = dt  # input tree is the best initially
        self.l = l
        self.k = k
        self.validation_data = validation_data

    def prune(self):
        """
        Randomly prune the tree L * K times
        Returns
        -------
        DecisionTree
            Best decision tree encountered
        """
        current_accuracy = accuracy.measure(self.initial_tree, self.validation_data, 'Class')
        for i in range(1, self.l):
            new_tree = copy.copy(self.initial_tree)
            replacements = random.randrange(2, self.k)

            for j in range(3, replacements):
                number_of_nodes = len(self._order_nodes(new_tree))
                p = random.randrange(1, number_of_nodes)

                new_tree = self._replace_node_with_majority_class(new_tree, p)

            pruned_tree_accuracy = accuracy.measure(new_tree, self.validation_data, 'Class')

            if pruned_tree_accuracy > current_accuracy:
                self.best = copy.copy(new_tree)

        return self.best

    def _order_nodes(self, tree, filter_leaves=True):
        """
        Returned a list of nodes, breadth first
        Parameters
        ----------
        tree : DecisionTree
        filter_leaves : bool
            True to filter 0 and 1, False otherwise

        Returns
        -------
        list
        """
        node_list = []
        traversal_queue = deque([tree.root])

        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()

            # we only need attribute list
            if filter_leaves:
                if node.label not in [0, 1]:
                    node_list.append(node.label)
            else:
                node_list.append(node.label)

            if node.left:
                traversal_queue.append(node.left)

            if node.right:
                traversal_queue.append(node.right)

        return node_list

    def _replace_node_with_majority_class(self, tree, index):
        """
        Accepts a tree and index of node to remove from the tree.
        Replaces the node at that index with majority class

        Parameters
        ----------
        tree: DecisionTree
            Full Tree from which node has to be removed
        index: int
            Index of node in the node list. Index is 1 based for readability (plus assignment specifies this)

        Returns
        -------
        DecisionTree
        """
        # we will do breadth first traversal and stop at the given index
        nodes_traversed = 0
        traversal_queue = deque([tree.root])
        node = None

        while nodes_traversed < index:
            node = traversal_queue.popleft()

            if node.label not in [0, 1]:
                nodes_traversed += 1

            if node.left:
                traversal_queue.append(node.left)

            if node.right:
                traversal_queue.append(node.right)

        node_to_prune = node
        dt = t.DecisionTree()

        # in case we are given a 0 or negative index
        # we prune everything except node
        # TODO: Fix the bug when we get 0 or 1
        if node_to_prune is not None:
            dt.root = node_to_prune
        else:
            dt.root = copy.copy(tree.root)
            node_to_prune = tree.root  # Note: this is by being passed by value, not reference

        replacement_label = self._find_majority_class(dt)
        node_to_prune.label = replacement_label
        node_to_prune.left = None
        node_to_prune.right = None

        return tree

    def _find_majority_class(self, tree):
        """
        Find majority class form leaf nodes

        Parameters
        ----------
        tree: DecisionTree

        Returns
        -------
        int
            Majority class, either 0 or 1
        """
        nodes = self._order_nodes(tree, False)
        element_count = Counter(nodes)

        if len(element_count) >= 2 and element_count[0] < element_count[1]:
            return 1
        elif len(element_count) >= 2 and element_count[0] > element_count[1]:
            return 0
        elif len(element_count) == 1:  # when we are pruning everything below root node
            return element_count[0]
        else:  # should throw an exception
            return 0
