class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instanse, owner):
        return getattr(instanse, self.name)

    def __set__(self, instance, value):
        if not value < 0:
            raise TypeError("Value must be not less then zero")
        setattr(instance, self.name, value)

class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price
