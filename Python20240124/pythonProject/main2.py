class Library:
    books = []

    @classmethod
    def addBook(cls, name, author, date):
        cls.books.append({
            "name": name,
            "author": author,
            "date": date
        })

    @classmethod
    def showBooks(cls):
        for i in cls.books:
            print(f"Name: {i['name']}\nAuthor: {i['author']}\nDate: {i['date']}\n")

    @classmethod
    def showTotal(cls):
        print(f"Total {len(cls.books)}.")


library = Library

library.addBook("Лісова Пісня", "Леся Україка", "XIX ст.")
library.addBook("Гаррі Поттер та філософський камінь", "Дж. К. Ролінґ", "XX ст.")
library.showBooks()
library.showTotal()

