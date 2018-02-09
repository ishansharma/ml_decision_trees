import math


def ig_heuristic(data, cols, fixed_values):
    """
    Accepts the data and column names. Calculates IG for each column and returns the column with highest gain
    Parameters
    ----------
    data: DataFrame
        Pandas DataFrame
    cols: ArrayLike
        An array of keys we'd like to calculate for
    fixed_values: Dict
        Dictionary that will contain tree that we have already fixed
    Returns
    -------
    str
    """

    column_with_highest_gain = ""
    highest_gain = 0

    # filter to remove data that doesn't fix our fixed_values
    for key in fixed_values:
        data = data.loc[(data[key] == fixed_values[key])]

    for column in cols:
        # we won't need to calculate IG for class
        if column == 'Class':
            continue

        value_counts = data.Class.value_counts()

        # quick check to make sure we don't fail when all values are 0 or 1
        if 0 not in value_counts:
            negatives = 0
        else:
            negatives = value_counts[0]

        if 1 not in value_counts:
            positives = 0
        else:
            positives = value_counts[1]

        # total data points in this column
        total = positives + negatives

        # total entropy for column
        entropy = calculate_entropy(positives, negatives)

        # entropy of positive data points
        # Logic: filter current column for positives, then use Class for entropy
        positive_df = data.loc[(data[column] == 1)]
        positives_entropy_points = positive_df.Class.value_counts()

        if 0 not in positives_entropy_points:
            p_negatives = 0
        else:
            p_negatives = positives_entropy_points[0]

        if 1 not in positives_entropy_points:
            p_positives = 0
        else:
            p_positives = positives_entropy_points[1]

        p_entropy = calculate_entropy(p_positives, p_negatives)
        p_total = p_negatives + p_positives

        # print("Positive", column, "Counts")
        # print(positives_entropy_points)
        # print("Entropy is", p_entropy)
        # print("===")

        # entropy for negative data points
        negative_df = data.loc[(data[column] == 0)]
        negatives_entropy_points = negative_df.Class.value_counts()

        if 0 not in negatives_entropy_points:
            n_negatives = 0
        else:
            n_negatives = negatives_entropy_points[0]

        if 1 not in negatives_entropy_points:
            n_positives = 0
        else:
            n_positives = negatives_entropy_points[1]

        n_entropy = calculate_entropy(n_positives, n_negatives)
        n_total = n_negatives + n_positives

        # print("Negative", column, "Counts")
        # print(negatives_entropy_points)
        # print("Entropy is", n_entropy)
        # print("===")
        #
        # print("\n**********\n")

        information_gain = entropy - (((p_total / total) * p_entropy) + ((n_total / total) * n_entropy))

        if information_gain > 0:
            information_gain = round(information_gain, 5)

        if information_gain > highest_gain:
            highest_gain = information_gain
            column_with_highest_gain = column

    return column_with_highest_gain


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
