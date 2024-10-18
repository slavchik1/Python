class Car:
    pass

car = Car()

setattr(car, "power", 200)
setattr(car, "mass", 1000)
setattr(car, "isElectro", False)

print(car.power, car.mass, car.isElectro)
