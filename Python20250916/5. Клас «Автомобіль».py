class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        pass
    def brake(self, amount):
        if self.speed >= amount:
            self.speed -= amount
        else:
            print("Неможливо зменшити швидкість менше 0")
    def info(self):
        print(self.brand + "\n" + str(self.speed))

c = Car("Tesla")
c.accelerate(50)
c.brake(20)
c.info()