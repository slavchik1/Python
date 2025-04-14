class LimitedString:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instanse, owner):
        return getattr(instanse, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) and value.len > 20:
            raise TypeError("Characters in string must be less or equal to 20")
        setattr(instance, self.name, value)

class Message:
    text = LimitedString()

    def __init__(self, text):
        self.text = text
