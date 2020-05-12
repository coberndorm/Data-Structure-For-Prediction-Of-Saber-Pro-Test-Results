class Student:
    def __init__(self, codigo, data):
        self.codigo = codigo
        self.data = data


def get_all_students():
    students = {}

    with open('../datos/datos4.csv', encoding='utf-8', mode='r') as file:
        next(file)

        for i, row in enumerate(file):
            data = row.split(";")
            # No es necesario prealocar el espacio para el diccionario porque tiene cercano a O(1) de insercion
            students[data[0]] = Student(data[0], data[1:])
    return students


if __name__ == '__main__':
    print(get_all_students())
