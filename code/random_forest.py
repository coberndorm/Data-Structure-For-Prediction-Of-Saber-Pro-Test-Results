from codigo import tree
from codigo import lectura_datos
import random


def trees(students, column_size, checked_columns, list_students):
    height = 0
    root, list_students_left_root, list_students_right_root, checked_columns = \
        tree.node_calculator(column_size, checked_columns, students, list_students)
    root.left, list_students_left_leaf_left, list_students_left_leaf_right, checked_columns_left = \
        tree.node_calculator(column_size, checked_columns, students, list_students_left_root)
    root.right, list_students_right_leaf_left, list_students_right_leaf_right, checked_columns_right = \
        tree.node_calculator(column_size, checked_columns, students, list_students_right_root)

    tree.tree_maker(root.left, checked_columns_left, height + 1, students,
                    list_students_left_leaf_left, list_students_left_leaf_right)
    tree.tree_maker(root.right, checked_columns_right, height + 1, students,
                    list_students_right_leaf_left, list_students_right_leaf_right)

    return root


def random_forest(datos_train):
    students, column_size, list_students = lectura_datos.get_all_students(datos_train)
    checked_columns = [False] * column_size
    tree_array = [trees(students, column_size, checked_columns, list_students)]
    for i in range(10):
        checked_columns = [False] * column_size
        checked_columns = random_censorship(tree_array[0], checked_columns)
        tree_array.append(trees(students, column_size, checked_columns, list_students))

    return tree_array


def random_censorship(node, checked_columns):
    while not node.leaf_node:
        if random.choice([True, False]):
            checked_columns[node.column] = True
        if random.choice([True, False]):
            node = node.right
        else:
            node = node.left

    return checked_columns


def runClassify_forest(datos_train, datos_test):
    test_students, column_size, list_students = lectura_datos.get_all_students(datos_test)
    tree_array = random_forest(datos_train)
    prediction_percentage = 0

    for id in list_students:
        tree_prediction = 0
        for root in tree_array:
            if tree.classify(id, root, test_students):
                tree_prediction += 1
        if tree_prediction / len(tree_array) >= 0.5:
            prediction = True
        else:
            prediction = False

        if prediction == test_students[id].exito:
            prediction_percentage += 1

    return prediction_percentage / len(list_students)


if __name__ == '__main__':
    print(runClassify_forest('../datos/datos_train0.csv', '../datos/datos_test0.csv'))
