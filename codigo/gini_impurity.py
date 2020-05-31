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
    students_no_answer = []
    for id in list_students:
        value = students[id].data[column]
        if value not in possibles and value != None:
            possibles.append(value)
        if value == None:
            students_no_answer.append(id)

    possibles.sort()
    best_divider = None
    best_students_under_rank = []
    best_students_over_rank = []
    best_gini = 1
    for rank in possibles:
        students_under_rank = []
        students_under_rank_successful = []
        students_under_rank_unsuccessful = []
        students_over_rank = []
        students_over_rank_successful = []
        students_over_rank_unsuccessful = []
        for id in list_students:
            if students[id].data[column] >= rank:
                students_over_rank.append(id)
                if students[id].exito:
                    students_over_rank_successful.append(id)
                else:
                    students_over_rank_unsuccessful.append(id)
            else:
                students_under_rank.append(id)
                if students[id].exito:
                    students_under_rank_successful.append(id)
                else:
                    students_under_rank_unsuccessful.append(id)
        gini_over_rank = 1 - (len(students_over_rank_successful)/len(students_over_rank))**2 - (len(students_over_rank_unsuccessful)/len(students_over_rank))**2
        gini_under_rank = 1 - (len(students_under_rank_successful)/len(students_under_rank))**2 - (len(students_under_rank_unsuccessful)/len(students_under_rank))**2
        gini = (len(students_over_rank)/len(list_students))*gini_over_rank + (len(students_under_rank)/len(list_students))*gini_under_rank
        if gini < best_gini:
            best_gini = gini
            best_divider = rank
            best_students_over_rank = students_over_rank
            best_students_under_rank = students_under_rank
        return  rank

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


def gini_impurity_boolean(students, list_students, column):
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
