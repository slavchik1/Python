class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("На рахунку недостатньо коштів.")
    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50) # баланс 150
acc.withdraw(70) # баланс 80
print(acc.get_balance())