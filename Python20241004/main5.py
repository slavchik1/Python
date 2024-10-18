import math


class Triangle:
    def triangle(a, b, c):
        if a + b > c:
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            return "Трикутник неможливий"


print(Triangle.triangle(7, 7, 7))
