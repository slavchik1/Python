from random import randint

min = 1
max = 1000

class Line:
    def __init__(self, sp, ep):
        self.x = sp
        self.y = ep

class Rect:
    def __init__(self, sp, ep):
        self.x = sp
        self.y = ep

class Ellipse:
    def __init__(self, sp, ep):
        self.x = sp
        self.y = ep

shapes = []

for i in range(270):
    randint_ = randint(1, 3)
    sp = randint(min, max)
    se = randint(min, max)
    if randint_ == 1:
        shapes.append(Line(sp, se))
    if randint_ == 2:
        shapes.append(Rect(sp, se))
    if randint_ == 3:
        shapes.append(Ellipse(sp, se))

print(shapes)
