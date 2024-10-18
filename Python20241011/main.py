class Tank:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

tank = Tank(70, 100)
print("Потужність:", tank.power, "Швидкість:", tank.speed)
