class DataBase:
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
    def connect(self):
        print(f"з'єднання з БД: {self.user}, {self.psw}, {self.port}")
    def close(self) :
        print("Закриття з'єднання з БД")
    def read(self) :
        return "Дані з БД"
    def write(self, data):
        print(f"Запис у БД {data}")

obj = DataBase("root", 137, 40)
obj1 = DataBase("root2", 136560, 20)
print(id(obj), id(obj1))
print(obj.user)
