def separacion_datos(students, list_students, column):
    cont = 0
    students_unknown_data = []

    for id in list_students:
        if students[id].data[column] == "":
            cont = cont + 1
            students_unknown_data.append(id)

    if cont / len(list_students) >= 0.1:
        raise Exception("insuficient data on this variable")

    for id in list_students:
        if isinstance(students[id].data[column], bool):
            # used for boolean data
            return gini_impurity_boolean(students, list_students, column, students_unknown_data)
        elif isinstance(students[id].data[column], float):
            # used for numeric data
            return gini_impurity_numeric(students, list_students, column, students_unknown_data)
        elif isinstance(students[id].data[column], int):
            # used for ranked data
            return gini_impurity_ranked(students, list_students, column, students_unknown_data)
        elif isinstance(students[id].data[column], str):
            # used for cualitative
            return gini_impurity_cualitative(students, list_students, column, students_unknown_data)


def no_data_fix(left_group, right_group, students_unknown_data):
    if len(left_group) >= len(right_group):
        left_group.extend(students_unknown_data)
    else:
        right_group.extend(students_unknown_data)


def gini_impurity_ranked(students, list_students, column, students_unknown_data):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if value != '' and value not in possibles:
            possibles.append(value)

    possibles.sort()

    best_divider = None
    best_students_under_rank = []
    best_students_over_rank = []
    best_gini = 1
    best_gini_over_rank = 1
    best_gini_under_rank = 1

    for rank in possibles[1:]:
        students_under_rank = []
        students_under_rank_successful = []
        students_under_rank_unsuccessful = []
        students_over_rank = []
        students_over_rank_successful = []
        students_over_rank_unsuccessful = []
        for id in list_students:
            if students[id].data[column] != "" and students[id].data[column] >= rank:
                students_over_rank.append(id)
                if students[id].exito:
                    students_over_rank_successful.append(id)
                else:
                    students_over_rank_unsuccessful.append(id)
            elif students[id].data[column] != "":
                students_under_rank.append(id)
                if students[id].exito:
                    students_under_rank_successful.append(id)
                else:
                    students_under_rank_unsuccessful.append(id)
        no_data_fix(students_under_rank, students_over_rank, students_unknown_data)
        gini_over_rank = 1 - (len(students_over_rank_successful) / len(students_over_rank)) ** 2 - (
                len(students_over_rank_unsuccessful) / len(students_over_rank)) ** 2
        gini_under_rank = 1 - (len(students_under_rank_successful) / len(students_under_rank)) ** 2 - (
                len(students_under_rank_unsuccessful) / len(students_under_rank)) ** 2
        gini = (len(students_over_rank) / len(list_students)) * gini_over_rank + (
                len(students_under_rank) / len(list_students)) * gini_under_rank

        if gini < best_gini:
            best_gini = gini
            best_gini_over_rank = gini_over_rank
            best_gini_under_rank = gini_under_rank
            best_divider = rank
            best_students_over_rank = students_over_rank
            best_students_under_rank = students_under_rank

    return best_gini, best_gini_under_rank, best_gini_over_rank, best_divider, best_students_under_rank, best_students_over_rank


def gini_impurity_numeric(students, list_students, column, students_unknown_data):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if (value not in possibles and value != None):
            possibles.append(value)
    possibles.sort()
    if len(possibles)==1:
        raise Exception('unsufficient possibilities')

    best_average = None
    best_students_under_average = []
    best_students_over_average = []
    best_gini = 1
    best_gini_over_splitter = 1
    best_gini_under_splitter = 1

    for i in (range(len(possibles)-1)):
        average = (possibles[i] + possibles[i + 1]) / 2
        students_under_average = []
        students_under_average_successful = []
        students_under_average_unsuccessful = []
        students_over_average = []
        students_over_average_successful = []
        students_over_average_unsuccessful = []

        for id in list_students:
            if students[id].data[column] != "" and students[id].data[column] >= average:
                students_over_average.append(id)
                if students[id].exito:
                    students_over_average_successful.append(id)
                else:
                    students_over_average_unsuccessful.append(id)
            elif students[id].data[column] != "":
                students_under_average.append(id)
                if students[id].exito:
                    students_under_average_successful.append(id)
                else:
                    students_under_average_unsuccessful.append(id)

        no_data_fix(students_under_average, students_over_average, students_unknown_data)

        gini_over_splitter = 1 - (len(students_over_average_successful) / len(students_over_average)) ** 2 - (
                len(students_over_average_unsuccessful) / len(students_over_average)) ** 2
        gini_under_splitter = 1 - (len(students_under_average_successful) / len(students_under_average)) ** 2 - (
                len(students_under_average_unsuccessful) / len(students_under_average)) ** 2
        gini = (len(students_over_average) / len(list_students)) * gini_over_splitter + (
                len(students_under_average) / len(list_students)) * gini_under_splitter

        if gini < best_gini:
            best_gini = gini
            best_gini_over_splitter = gini_over_splitter
            best_gini_under_splitter = gini_under_splitter
            best_average = average
            best_students_over_average = students_over_average
            best_students_under_average = students_under_average
    return best_gini, best_gini_under_splitter, best_gini_over_splitter, best_average, best_students_under_average, best_students_over_average


def gini_impurity_boolean(students, list_students, column, students_unknown_data):
    students_true = []
    students_true_succesful = []
    students_true_unsuccesful = []
    students_false = []
    students_false_succesful = []
    students_false_unsuccesful = []

    for id in list_students:
        if students[id].data[column] != "" and students[id].data[column]:
            students_true.append(id)
            if students[id].exito:
                students_true_succesful.append(id)
            else:
                students_true_unsuccesful.append(id)
        elif students[id].data[column] != "":
            students_false.append(id)
            if students[id].exito:
                students_false_succesful.append(id)
            else:
                students_false_unsuccesful.append(id)

    if len(students_true)==0 or len(students_false)==0:
        raise Exception('unsufficient possibilities')

    no_data_fix(students_false, students_true, students_unknown_data)

    gini_true = 1 - (len(students_true_succesful) / len(students_true))**2 - (
            len(students_true_unsuccesful) / len(students_true))**2
    gini_false = 1 - (len(students_false_succesful) / len(students_false)) ** 2 - (
            len(students_false_unsuccesful) / len(students_false))**2
    gini = (len(students_true) / len(list_students)) * gini_true + (
            len(students_false) / len(list_students))*gini_false
    return gini, True, gini_false, gini_true, students_false, students_true


def gini_impurity_cualitative(students, list_students, column, students_unknown_data):
    possibles = []
    for id in list_students:
        value = students[id].data[column]
        if value != '' and value not in possibles:
            possibles.append(value)

    if len(possibles)  > 100:
        raise Exception ('Too many possibilities')
    if len(possibles)==1:
        raise Exception('unsufficient possibilities')

    best_divider = None
    best_students_with_divider = []
    best_students_without_divider = []
    best_gini_with_divider = 1
    best_gini_without_divider = 1
    best_gini = 1

    for characteristic in possibles:
        students_with_divider = []
        students_with_divider_successful = []
        students_with_divider_unsuccessful = []
        students_without_divider = []
        students_without_divider_successful = []
        students_without_divider_unsuccessful = []

        for id in list_students:
            if students[id].data[column] != "" and students[id].data[column] == characteristic:
                students_without_divider.append(id)
                if students[id].exito:
                    students_without_divider_successful.append(id)
                else:
                    students_without_divider_unsuccessful.append(id)
            elif students[id].data[column] != "":
                students_with_divider.append(id)
                if students[id].exito:
                    students_with_divider_successful.append(id)
                else:
                    students_with_divider_unsuccessful.append(id)
        no_data_fix(students_with_divider, students_without_divider, students_unknown_data)
        gini_with_divider = 1 - (len(students_without_divider_successful) / len(students_without_divider)) ** 2 - (
                len(students_without_divider_unsuccessful) / len(students_without_divider)) ** 2
        gini_without_divider = 1 - (len(students_with_divider_successful) / len(students_with_divider)) ** 2 - (
                len(students_with_divider_unsuccessful) / len(students_with_divider)) ** 2
        gini = (len(students_without_divider) / len(list_students)) * gini_with_divider + (
                len(students_with_divider) / len(list_students)) * gini_without_divider

        if gini < best_gini:
            best_gini = gini
            best_gini_with_divider = gini_with_divider
            best_gini_without_divider = gini_without_divider
            best_divider = characteristic
            best_students_with_divider = students_without_divider
            best_students_without_divider = students_with_divider

    return best_gini, best_gini_without_divider, best_gini_with_divider, best_divider, best_students_without_divider, best_students_with_divider

