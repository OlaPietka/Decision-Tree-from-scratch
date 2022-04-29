class DecisionNode:
    def __init__(self, feature, split_point, left, right):
        self.split_feature = feature
        self.split_point = split_point
        self.left = left
        self.right = right
