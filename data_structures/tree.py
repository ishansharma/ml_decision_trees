"""
Implementation of data structure for Decision Tree

Node is building block for the tree. This class defines the node
"""

from data_structures import stack  # useful when traversing or printing the stack


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

    def __str__(self):
        """
        Return the string representation of the tree in required format.

        This is just pre-order traversal without recursion.

        Returns
        -------
        str
        """
        current = self.root
        final_output = ""
        if current is None or current.label is None:
            return final_output

        st = stack.Stack()
        current, side = current, 0  # side keeps track of the direction. 0 = visit left, 1 = right, 2 = ignore
        st.push((current, side))

        while not st.is_empty():
            current, side = st.pop()
            output_line = ""

            # if we have to visit left
            if side == 0:
                output_line += str('|' * st.size()) + str(current.label) + " = 0: "

                if current.left is not None:
                    if current.left.label in [0, 1]:
                        output_line += str(current.left.label)
                        st.push((current, 1))
                    else:
                        st.push((current, 1))
                        st.push((current.left, 0))

            # if we have to visit right
            if side == 1:
                output_line += str('|' * st.size()) + str(current.label) + " = 1: "

                if current.right is not None:
                    if current.right.label in [0, 1]:
                        output_line += str(current.right.label)
                        st.push((current, 2))
                    else:
                        st.push((current, 2))
                        st.push((current.right, 0))

            if output_line != '':
                final_output += "\n" + output_line

        return final_output
