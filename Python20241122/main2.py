SHAPE_TYPE = "Circle"

class Circle:
    name_class = "Circle"

class Square:
    name_class = "Square"

class Shape:
    def __new__(cls, *args, **kwargs):
        obj = None

        if SHAPE_TYPE == "Circle":
            obj = super().__new__(Circle)
        elif SHAPE_TYPE == "Square":
            obj = super().__new__(Square)

        obj.name = args[0]

        return obj

shape = Shape('First Shape')
print(shape.name_class, shape.name, sep="\n")