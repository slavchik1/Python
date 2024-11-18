class EvenNumbers:
    def __new__(cls, string):
        if 'a' in string.lower():
            return super().__new__(cls)
        else:
            return None

    def __init__(self, number):
        self.number = number

num1 = EvenNumbers("ABETKA")
print(num1)
print(num1.number if num1 else "None")
