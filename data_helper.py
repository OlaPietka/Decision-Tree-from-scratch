from math_helper import entropy


def get_column(data, column):
    if type(column) is int:
        return [item[column] for item in data[1:]]
    elif type(column) is str:
        return get_column(data, data[0].index(column))


def get_labels(data):
    return get_column(data, 'label')


def get_features(data):
    return data[0][1:]


def calculate_entropy(data):
    labels = get_labels(data)
    return entropy(labels)


def split_data(data, split_pint, column):
    left, right = [data[0]], [data[0]]
    values = get_column(data, column)

    for i, value in enumerate(values):
        if value <= split_pint:
            left.append(data[i+1])
        else:
            right.append(data[i+1])
    return left, right


def possible_split_points(data, column):
    values = sorted(get_column(data, column))
    return [(values[i] + values[i + 1]) / 2 for i in range(len(values) - 1)]


def best_split_point(data, features):
    best_point, best_feature, best_gain = -1, -1, -1
    p = lambda x: len(x) / len(data)

    for feature in features:
        possible_points = possible_split_points(data, feature)

        for split_point in possible_points:
            left, right = split_data(data, split_point, feature)

            gain = calculate_entropy(data) - p(left) * calculate_entropy(left) - p(right) * calculate_entropy(right)

            if gain > best_gain and len(left) and len(right):
                best_point, best_feature, best_gain = split_point, feature, gain
    return best_point, best_feature


def splitting_criterion(data, features):
    split_point, split_feature = best_split_point(data, features)
    left, right = split_data(data, split_point, split_feature)

    return split_point, split_feature, left, right
