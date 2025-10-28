class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return str(self.title) + "\n" + str(self.author)

b = Book("Python для дітей", "Джон Доу")
print(b.describe())