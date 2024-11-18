class Point:
    def __new__(cls, *args, **kwargs):
        print("Викликаємо клас:", str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

point = Point(1, 2)
print(point)
