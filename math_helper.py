import math


def as_unique(array):
    return list(set(array))


def count_occurrence(array):
    occurrence = {}
    for element in array:
        if element in occurrence.keys():
            occurrence[element] += 1
        else:
            occurrence[element] = 1
    return list(occurrence.values())


def entropy(array):
    counts = count_occurrence(array)

    p = lambda x: x / sum(counts)

    return sum([-p(count) * math.log2(p(count)) for count in counts if p(count) != 0])


def most_common(array):
    return max(set(array), key=array.count)
