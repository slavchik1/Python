class Client:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

    def show(self):
        print(f"""Ім'я: клієнта {self.name}
Вік клієнта: {self.age}
Номер клієнта: {self.number}
Електрона пошта: {self.email}
""")

client1 = Client("Abdul", 17, "+38009993838", "Abu@slavchik.net")
client2 = Client("Olena", 48, "+38005747899", "Olenalalalalichenko@slavchik.net")
client3 = Client("Vladick", 7, "+3804839202", "Vlad2010@slavchik.net")

client1.show()
client2.show()
client3.show()

client1.age = 19
print("\n" * 5)

client1.show()
client2.show()
client3.show()
