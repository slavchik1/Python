class User:
    def __init__(self, age, name, email):
        self.age = age
        self.name = name
        self.email = email

    def showinfo(self):
        print(str(self.age) + "\n" +
              self.name + "\n" +
              self.email + "\n")

user1 = User(17, "Їсуйдтей", "yisuydtey@slavchik.net")
user2 = User(46, "Джуян", "dzhuyan@slavchik.net")
user3 = User(38, "Юйзо", "yuyzo@slavchik.net")

user1.showinfo()
user2.showinfo()
user3.showinfo()
