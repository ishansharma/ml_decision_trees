from tree_implementation import tree


def construct(data, target_attribute, attributes_to_test):
    """
    Construct the tree using given parameters and return the tree
    Parameters
    ----------
    data : DataFrame
        Pandas DataFrame containing given data

    target_attribute: str
        Decision tree will be constructed to guess this attribute

    attributes_to_test: array
        List of all other attributes which will be used in tree construction

    Returns
    -------

    """
    value_test = test_for_all_same(data, target_attribute)  # Check if all values are same

    # if all values are same, we return that value in root
    if value_test[0]:
        return tree.Node('', value_test[1])

    # dummy node for now
    root = tree.Node('XA', 0)

    return root


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
