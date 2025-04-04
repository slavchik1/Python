class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instanse, owner):
        return getattr(instanse, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Value must be a float")
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, val = 0.0):
        self.value = val

class Sheet:
    def __init__(self, n, m):
        self.sheet = []
        row = []
        for j in range(m):
            row.append(Cell())
        for i in range(n):
            self.sheet.append(row)

table = Sheet(7, 10)

for i in range(table.sheet):
    for j in range
