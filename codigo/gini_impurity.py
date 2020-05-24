def separacion_datos(students, list_students, column):
    possibles = []
    for id in list_students:
        if isinstance(students[id].data[column], int):
            # used for ranked data
            gini_impurity_ranked(students, list_students, column)
            break
        elif isinstance(students[id].data[column], float):
            # used for numeric data
            gini_impurity_numeric(students, list_students, column)
            break
        elif isinstance(students[id].data[column], bool):
            # used for boolean data
            break
        elif isinstance(students[id].data[column], str):
            # used for cualitative
            break


def gini_impurity_ranked(students, list_students, column):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if value not in possibles:
            possibles.append(value)
    possibles.sort()
    best_gini = -1

    for rank in possibles:
        for id in list_students:
            pass


def gini_impurity_numeric(students, list_students, column):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if value not in possibles:
            possibles.append(value)
    possibles.sort()
    best_gini = -1

    for rank in possibles:
        for id in list_students:
            pass


def gini_impurity_ranked(students, list_students, column):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if value not in possibles:
            possibles.append(value)
    possibles.sort()
    best_gini = -1

    for rank in possibles:

        for id in list_students:
            pass


def gini_impurity(charecteristic):
    pass


if __name__ == '__main__':
    pass
