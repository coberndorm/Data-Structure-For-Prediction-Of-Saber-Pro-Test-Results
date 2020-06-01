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

    divider = None
    best_students_left = best_students_right = []
    best_gini = best_gini_left = best_gini_right = 1
    col = -1

    for column in range(column_size):
        try:
            gini, gini_left, gini_right, divider, students_left, students_right= \
                gini_impurity.separacion_datos(students, students.keys(), column)
            if gini < best_gini:
                best_gini = gini
                best_gini_left = gini_left
                best_gini_right = gini_right
                divider = divider
                best_students_left = students_left
                best_students_right = students_right
                col = column
        except:
            checked_columns [column] = True

    root = Node(divider,col,students.keys(),best_gini,best_gini_left,best_gini_right)
    print (best_gini, divider, col)
    return root


def tree_maker(checked_columns, height, students, list_students):
    columns_visited = checked_columns.copy()
    pass

if __name__ == '__main__':
    node = Node(2,2,2,2,2,2)
    def nod (node):
        node = Node(3,3,3,3,3,3)
        node.left = nod(node.left)
        return node
    node.left=nod(node.left)
    print(node.left.gini)