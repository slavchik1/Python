class DataBase:
    def __init__(self, tittle, author, views):
        self.tittle = tittle
        self.author = author
        self.views = views

dataBase = DataBase("Класи ООП", "Слава", 1432)
print(f"Назва: {dataBase.tittle}, Автор: {dataBase.author}, Перегляди: {dataBase.views}")
