class EvenNumbers:
    def __new__(cls, number):
        if number % 2 == 0:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, number):
        self.number = number

num1 = EvenNumbers(4)
print(num1)
print(num1.number if num1 else "None")
