from DecisionTree.decison_node import DecisionNode
from DecisionTree.leaf import Leaf
from data_helper import get_labels, get_column, splitting_criterion, get_features
from math_helper import most_common, as_unique


class Tree:
    def __init__(self):
        self.depth = 2
        self.root = None

    def build_tree(self, data, depth=2):
        labels = as_unique(get_labels(data))
        features = get_features(data)

        if len(labels) == 1:
            return Leaf(labels[0])
        if len(features) == 0:
            return Leaf(most_common(labels))
        if depth == 0:
            return Leaf(most_common(labels))

        split_point, split_feature, left, right = splitting_criterion(data, features)

        left_branch = self.build_tree(left, depth - 1)
        right_branch = self.build_tree(right, depth - 1)

        return DecisionNode(split_feature, split_point, left_branch, right_branch)

    def fit(self, train_set):
        self.root = self.build_tree(train_set, self.depth)

    def classify(self, row, node):
        if isinstance(node, Leaf):
            return node.label

        if get_column(row, node.split_feature)[0] <= node.split_point:
            return self.classify(row, node.left)
        else:
            return self.classify(row, node.right)

    def predict(self, test_set):
        print("{:^6} | {:^6}".format("Actual", "Prediction"))
        for row in test_set[1:]:
            one_row_data = [test_set[0], row]
            prediction = self.classify(one_row_data, self.root)
            print("{:^6} | {:^6}".format(row[0], prediction))
