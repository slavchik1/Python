class Transport:
     def __init__(self, name, speed):
        self.name = name
        self.speed = speed

     def move(self):
        print(f"{self.name} рухається зі швидкістю {self.speed} км/год")

class Car(Transport):
    def fuel_type(self, fuel):
        return f"{self.name} використовує {fuel}"

class Bicycle(Transport):
    def type(self, type):
        return f"{self.name} є {type}"


car = Car('Мазда', 251)
bicycle = Bicycle("Ййотта", 61)

print(car.fuel_type('Газ'))
print(bicycle.type('Позашляховий'))
