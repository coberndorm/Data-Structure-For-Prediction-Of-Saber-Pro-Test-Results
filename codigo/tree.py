from codigo import lectura_datos
from codigo import gini_impurity

class Node:
    def __init__(self, divider, column, list_students, gini, gini_left, gini_right):
        self.right = self.left = None
        self.divider = divider
        self.column = column
        self.list_students = list_students
        self.gini = gini
        self.gini_right = gini_right
        self.gini_left = gini_left
        

def tree():
    students, column_size = lectura_datos.get_all_students()
    checked_columns = [False]*column_size
    height = 0

    root, list_students_left_root, list_students_right_root, checked_columns = \
        node_calculator(column_size, checked_columns, students, students.keys())
    root.left, list_students_left_leaf_left, list_students_left_leaf_right, checked_columns_left = \
        node_calculator(column_size, checked_columns, students, list_students_left_root)
    root.right, list_students_right_leaf_left, list_students_right_leaf_right, checked_columns_right = \
        node_calculator(column_size, checked_columns, students, list_students_right_root)

    tree_maker(root.left, checked_columns_left, height + 1, students,
               list_students_left_leaf_left, list_students_left_leaf_right)
    tree_maker(root.right, checked_columns_right, height + 1, students,
               list_students_right_leaf_left, list_students_right_leaf_right)

    return root


def tree_maker(father_node, checked_columns, height, students, list_students_left, list_students_right):
    if height <= 5:
        father_node.left, list_students_left_leaf_left, list_students_left_leaf_right, checked_columns_left = \
            node_calculator(len(checked_columns), checked_columns, students, list_students_left)

        if father_node.gini_left <= father_node.left.gini:
            father_node.left = None
        else:
            tree_maker(father_node.left, checked_columns_left, height + 1, students,
                       list_students_left_leaf_left, list_students_left_leaf_right)

        father_node.right, list_students_right_leaf_left, list_students_right_leaf_right, checked_columns_right = \
            node_calculator(len(checked_columns), checked_columns, students, list_students_right)

        if father_node.gini_right <= father_node.right.gini:
            father_node.right = None
        else:
            tree_maker(father_node.right, checked_columns_right, height + 1, students,
                   list_students_right_leaf_left, list_students_right_leaf_right)
    else:
        father_node.left = None
        father_node.right = None


def node_calculator(column_size, columns_visited, students, list_students):
    checked_columns = columns_visited.copy()
    divider = None
    best_students_left = best_students_right = []
    best_gini = best_gini_left = best_gini_right = 1
    col = -1

    for column in range(column_size):
        try:
            if not checked_columns[column]:
                gini, gini_left, gini_right, divider, students_left, students_right = \
                    gini_impurity.separacion_datos(students, list_students, column)

                if gini < best_gini:
                    best_gini = gini
                    best_gini_left = gini_left
                    best_gini_right = gini_right
                    divider = divider
                    best_students_left = students_left
                    best_students_right = students_right
                    col = column
        except:
            checked_columns[column] = True

    checked_columns[col] = True
    node = Node(divider, col, list_students, best_gini, best_gini_left, best_gini_right)
    return node, best_students_left, best_students_right, checked_columns

