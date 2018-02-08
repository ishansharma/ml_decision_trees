import math


def calculate_entropy(positives, negatives):
    """
    Given a column, calculate entropy for it
    Parameters
    ----------
    positives: int
        Number of positive attributes

    negatives: int
        Number of negative attributes

    Returns
    -------
    float
    """

    # since the calculations are reused, doesn't make sense to do every single time
    total = positives + negatives
    positive_ratio = positives / total
    negative_ratio = negatives / total

    # need to handle case of 0 separately, as that throws error
    if positive_ratio == 0:
        positive_entropy = 0
    else:
        positive_entropy = positive_ratio * math.log(positive_ratio, 2)

    if negative_ratio == 0:
        negative_entropy = 0
    else:
        negative_entropy = negative_ratio * math.log(negative_ratio, 2)

    return round(-1 * (positive_entropy + negative_entropy), 5)
