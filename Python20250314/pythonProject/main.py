class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Error: no arguments given")

Persona = Person(17)

print(Persona.get_age())

Persona.set_age(0)

print(Persona.get_age())
