class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def info(self):
        print(f"Ім'я: {self.name}, Клас: {self.grade}")

s = Student("Оля", 7)
s.info()
