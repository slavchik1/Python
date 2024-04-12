import random


class Apple:
    def __init__(self, size, weight, color):
        self.size = size
        self.weight = weight
        self.color = color

class Point:
    def __init__(self, x, y, color="Чорний"):
        self.x = x
        self.y = y
        self.color = color

apple = Apple(68, 56, "Червоний")

list = []

min = 0
max = 1000

for i in range(100):
    list.append(Point(random.randint(min, max), random.randint(min, max), str(random.randint(min, max))))

for object in list:
    print(f"x: {object.x}\ny: {object.y}\ncolor: {object.color}\n")
