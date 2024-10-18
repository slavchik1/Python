import math


class Circle:
    def __init__(self, r):
        self.r = r

    def S(self):
        return math.pi * math.sqrt(self.r)

    def c(self):
        return 2 * math.pi * self.r
