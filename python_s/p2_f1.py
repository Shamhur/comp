class Student:
    print('Hi!')

    def __init__(self, height=160):
         self.height = height
         print('I Am alive')

first_student = Student()
second_student = Student(height=170)
print(first_student.height)
print(second_student.height)