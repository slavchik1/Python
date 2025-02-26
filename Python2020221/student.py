class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def add_grades(self, grade):
        if 0 < grade < 13:
            self.__grades.append(grade)
        else:
            print("Invalid grade")

    def get_information(self):
        return f"Student: {self.__name}, Age: {self.__age}"

student = Student("Mark", 15)
student.add_grades(10)
student.add_grades(15)
print(student.get_information())
