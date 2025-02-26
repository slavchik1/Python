class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < self.__balance and amount > 0:
            self.__balance += amount
        else:
            print("Помилка")

    def withdraw(self, amount):
        if amount < self.__balance and amount > 0:
            self.__balance -= amount
        else:
            print("Помилка")

accaunt = BankAccount(400)
print(accaunt.get_balance())
accaunt.withdraw(500)
print(accaunt.get_balance())
