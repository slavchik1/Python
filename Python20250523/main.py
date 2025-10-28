class Score:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instanse, owner):
        return getattr(instanse, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int) or not 1 <= value <= 12:
            raise TypeError("Оцінка має бути від 1 до 12")
        setattr(instance, self.name, value)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"Користувач: {self.name}, Email: {self.email}"

class Student(User):
    math = Score()
    physics = Score()
    english = Score()

    def __init__(self, name, email):
        super().__init__(name, email)

    def get_info(self):
        if not isinstance(self.math, (int, float)) and not isinstance(self.physics, (int, float)) and not isinstance(self.english, (int, float)):
             average_score = "Оцінок поки немає"
        elif not isinstance(self.math, (int, float)) or not isinstance(self.physics, (int, float)) or not isinstance(self.english, (int, float)):
            average_score = "Не є всі оцінки, щоб обчисліти середній бал"
        else:
            average_score = (self.math + self.physics + self.english) / 3
        return f"Учень: {self.name}, Середній бал: {average_score}"

class Teacher(User):
    courses = []

    def get_info(self):
        strin = f"Викладач: {self.name}, Курси: "
        for i in self.courses:
            strin += i
            strin += ", "
        strin = strin[:-2]
        return strin

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def show_course_info(self):
        print(f"◯ Назва: {self.name}\n◯ Вчитель:{self.teacher.name}\n◯ Учні:")
        for i in self.students:
            print(f"  {i.get_info()}")



teacher1 = Teacher("Lesya Ukrainka", "lesya.ukrainka@pysmnennyky.ua")
student1 = Student("Zhora", "jora@gmail.com")
student2 = Student("Anya", "anya@gmail.com")

student1.math = 11
student2.math = 2
student1.physics = 12
student2.physics = 11
student1.english = 2
student2.english = 7

course = Course("Ukrainian_language", teacher1)



print(teacher1.get_info())
print()
print(student1.get_info())
print()
print(student2.get_info())
print()
course.show_course_info()

# ####
#
# course.students = [student1, student2]
# print("\n################\n")
# course.show_course_info()
