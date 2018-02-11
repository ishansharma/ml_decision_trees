from collections import deque


class Pruner:
    def __init__(self, dt, l, k):
        self.initial = dt
        self.best = dt  # input tree is the best initially
        self.l = l
        self.k = k

    # def prune(self):

    def _order_non_leaf_nodes(self, tree):
        """
        Returned a list of nodes, breadth first
        Parameters
        ----------
        tree : DecisionTree

        Returns
        -------
        node_list: list
        """
        node_list = []
        traversal_queue = deque([tree.root])

        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()

            # we only need attribute list
            if node.label not in [0, 1]:
                node_list.append(node.label)

            if node.left:
                traversal_queue.append(node.left)

            if node.right:
                traversal_queue.append(node.right)

        return node_list
