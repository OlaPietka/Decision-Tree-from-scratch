from DecisionTree.tree import Tree


def read_input(file_name):
    data = []

    with open(file_name) as input_file:
        for i_row, row in enumerate(input_file.readlines()):
            row = row.split(' ')

            if i_row == 0:
                data.append(['label', *[attribute.split(':')[0] for attribute in row[1:]]])
            data.append([])
            for i_item, item in enumerate(row):
                if i_item == 0:
                    item = int(item)
                else:
                    item = float(item.split(':')[1])

                data[i_row+1].append(item)
    return data


if __name__ == "__main__":
    train_set = read_input("SampleData/sample_train.txt")
    test_set = read_input("SampleData/sample_test.txt")

    tree = Tree()
    tree.fit(train_set)

    tree.predict(test_set)
