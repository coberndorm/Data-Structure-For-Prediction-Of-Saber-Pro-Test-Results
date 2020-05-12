import time



class catchtime(object):
    def __enter__(self):
        self.t = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.t = time.time() - self.t
        print(self.t)

class Student:
    def __init__(self, codigo, data):
        self.codigo = codigo
        self.data = data


class Lectura:

    def main(self):
        with catchtime():
            size = -1

            with open('datos4.csv', encoding='utf-8', mode='r') as file:
                for _ in file:
                    size += 1

            self.students = [0] * size
            student_id = [0] * size

            with open('datos4.csv', encoding='utf-8', mode='r') as file:

                next(file)

                for i, row in enumerate(file):
                    data = row.split(";")
                    self.students[i] = Student(data[0], data[1:])
                    student_id[i] = data[0]

            self.diccionario = dict(zip(student_id, self.students))


if __name__ == '__main__':
    Lectura().main()
