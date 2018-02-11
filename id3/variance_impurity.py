def calculate_variance_impurity(positives, negatives):
    """
    Calculate the variance impurity for data given positives and negatives
    Parameters
    ----------
    positives: int
        Number of rows with positive attributes
    negatives
        Number of rows with negative attributes

    Returns
    -------
    float
    """
    total = positives + negatives

    # for empty set, variance impurity is going to be 0
    if total == 0:
        return 0.0

    positive_ratio = positives / total
    negative_ratio = negatives / total

    result = round(positive_ratio * negative_ratio, 5)

    return result
