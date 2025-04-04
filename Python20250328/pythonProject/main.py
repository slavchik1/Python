class Mark:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int) or not (1 <= value <= 12):
            raise TypeError("Значення має бути цілим числом / значення має бути у діапозоні від 1 до 12")
        setattr(instance, self.private_name, value)


class Person:
    math = Mark("Mathematics")

    def __init__(self, name, age):
        self.name = name
        self.age = age

Person1 = Person("Artem", 14)
Person2 = Person("Sashko", 14)

Person1.math = 13
Person2.math = 11

print(Person1.math)
print(Person2.math)
