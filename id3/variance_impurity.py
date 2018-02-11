def variance_heuristic(data, cols, target, fixed_values):
    """
    Accepts the data, column names, target attribute name and values that have to remain fixed
    Calculates IF for each column and return the column with highest gain

    Parameters
    ----------
    data: DataFrame
        Pandas DataFrame that contains all the data
    cols: ArrayLike
        An array of keys from which we choose the column with higest gain
    target: str
        Target attribute. Usually 'Class'
    fixed_values: Dict
        Dictionary containing already fixed values

    Returns
    -------
    str
    """
    column_with_highest_gain = ""
    highest_gain = 0

    # remove data not matching our values
    for key in fixed_values:
        data = data.loc[(data(key) == fixed_values[key])]

    for column in cols:
        if column == target:
            continue

        value_counts = getattr(data, target).value_counts()

        # if all values are 0 or 1, variance impurity is 0
        if 0 not in value_counts:
            negatives = 0
        else:
            negatives = value_counts[0]

        if 1 not in value_counts:
            positives = 0
        else:
            positives = value_counts[1]

        # total number of columns. Just adding here because that'll be faster than asking Pandas
        total = positives + negatives

        # column's variance impurity
        vi_overall = calculate_variance_impurity(positives, negatives)

        # variance impurity for positively classified attributes
        positive_df = data.loc[(data[column] == 1)]
        positives_vi_points = getattr(positive_df, target).value_counts()

        if 0 not in positives_vi_points:
            p_negatives = 0
        else:
            p_negatives = positives_vi_points[0]

        if 1 not in positives_vi_points:
            p_positives = 0
        else:
            p_positives = positives_vi_points[1]

        p_vi = calculate_variance_impurity(p_positives, p_negatives)
        p_total = p_negatives + p_positives

        # variance impurity for negatively classified points
        negative_df = data.loc[(data[column] == 0)]
        negatives_vi_points = getattr(negative_df, target).value_counts()

        if 0 not in negatives_vi_points:
            n_negatives = 0
        else:
            n_negatives = negatives_vi_points[0]

        if 1 not in negatives_vi_points:
            n_positives = 0
        else:
            n_positives = negatives_vi_points[0]

        n_vi = calculate_variance_impurity(n_positives, n_negatives)
        n_total = n_negatives + n_positives

        information_gain = vi_overall - (((p_total / total) * p_vi) + (n_total / total) * n_vi)

        if information_gain > highest_gain:
            highest_gain = information_gain
            column_with_highest_gain = column

    return column_with_highest_gain


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
