##from pympler.asizeof import asizeof
##import time

##print(asizeof(self.data)/1024/1024)
##start = time.time()
##print(tiem.time()-start)


class Lectura:
    data = []
    column = []
    students = []

    def main(self):
        size = -1
        with open('datos4.csv', encoding='utf-8', mode='r') as file:
            for row in file:
                if (size == -1):
                    self.column = row.split(';')
                    size += 1
                else:
                    size += 1
            file.close()
        with open('datos4.csv', encoding='utf-8', mode='r') as file:
            self.data = [0] * size
            self.students = [0] * size
            first_line = True;
            i = 0
            for row in file:
                if (first_line):
                    first_line = False
                else:
                    self.data[i] = row.split(";")
                    self.students[i] = self.data[i][0]
                    i = i + 1
            file.close()

    def get_student(self,student_code):
        for i in range(len(self.data)):
            if (student_code == self.data[i][0]):
                print(self.data[i])

    def get_student_data(self, student_code, column_name):
        column_num = -1
        for i in range(len(self.column)):
            if (self.column[i] == column_name):
                column_num = i

        for i in range(len(self.data)):
            if (student_code == self.data[i][0]):
                print(self.data[i][column_num])

    def add_student(self,student):
        self.data.append(student)
