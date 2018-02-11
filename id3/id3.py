import copy

from data_structures import tree
from id3 import heuristics


def construct(data, target_attribute, attributes_to_test):
    """
    Construct the tree using given parameters and return the tree
    Parameters
    ----------
    data : DataFrame
        Pandas DataFrame containing given data

    target_attribute: str
        Decision tree will be constructed to guess this attribute

    attributes_to_test: DataFrame
        List of all other attributes which will be used in tree construction

    Returns
    -------
    node: Node
        Node that may contain children. It's essentially a search tree without root.
    """
    attributes_to_test = list(attributes_to_test)  # needed to make sure we can iterate

    value_test = test_for_all_same(data, target_attribute)  # Check if all values are same

    # if all values are same, we return that value in root
    if value_test[0]:
        return tree.Node(value_test[1])

    # if we don't have any attributes, return most common value in root node
    if len(attributes_to_test) == 0:
        # found this elegant solution on Stack Overflow, https://stackoverflow.com/a/15139677/616941
        most_common_value = getattr(data, target_attribute).value_counts().idxmax()
        return tree.Node(target_attribute)

    # check the best heuristic
    selected_heuristic = heuristics.ig_heuristic(data, attributes_to_test, target_attribute, {})

    # insert the best heuristic at root
    node = tree.Node(selected_heuristic)

    for i in [0, 1]:
        examples_vi = data.loc[(data[selected_heuristic] == i)]
        if examples_vi.count == 0:
            mode = examples_vi.mode()
            mode = mode[selected_heuristic]
            if i == 0:
                node.left = tree.Node(mode)
            else:
                node.right = tree.Node(mode)
        else:
            if i == 0:
                new_attributes = copy.copy(attributes_to_test)
                if selected_heuristic in new_attributes:
                    new_attributes.remove(selected_heuristic)
                node.left = construct(examples_vi, target_attribute, new_attributes)
            else:
                new_attributes = copy.copy(attributes_to_test)
                if selected_heuristic in new_attributes:
                    new_attributes.remove(selected_heuristic)
                node.right = construct(examples_vi, target_attribute, new_attributes)

    return node


def test_for_all_same(data, target_attribute):
    """
    Test if all of the data in target attribute is same.

    Parameters
    ----------
    data : DataFrame
        Pandas DataFrame

    target_attribute: str
        String value of attribute to check

    Returns
    -------
    tuple
    """
    unique_values = getattr(data, target_attribute).unique()
    if len(unique_values) == 1:
        return True, unique_values[0]
    return False, []
