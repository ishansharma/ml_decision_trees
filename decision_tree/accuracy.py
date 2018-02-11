def measure(decision_tree, test_set, target_attribute):
    """
    Measure the accuracy of tree on the given test set.

    Parameters
    ----------
    decision_tree: DecisionTree
    test_set: DataFrame
    target_attribute: str

    Returns
    -------
    accuracy: float
        Number between 0.00 and 1.00. Multiply by 100 to get percentage
    """
    total_data_points = test_set.shape[0]  # shape is a tuple in format rows x columns

    accurate = 0
    inaccurate = 0

    root = decision_tree.root

    for row in test_set.itertuples():
        current = root
        while current.label not in [0, 1]:
            if getattr(row, current.label) == 0:
                current = current.left
            elif getattr(row, current.label) == 1:
                current = current.right
        predicted = current.label
        actual = getattr(row, target_attribute)

        if predicted == actual:
            accurate += 1
        else:
            inaccurate += 1

    accuracy = round(accurate / total_data_points, 5)

    return accuracy
