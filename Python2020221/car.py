class Car:
    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def accelerate(self, amount):
        new_speed = self.__speed + amount
        if 0 < new_speed < 200:
            self.__speed = new_speed
        else:
            print("Помилка")

    def brake(self, amount):
        new_speed = self.__speed - amount
        if amount > 0:
            self.__speed = new_speed
        else:
            print("Помилка")

car = Car(200)
