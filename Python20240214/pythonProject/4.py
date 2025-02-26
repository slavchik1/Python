class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def get_info(self):
        return f"''{self.name}'' - {self.author}, {self.pages} сторінок"

class PrintedBook(Book):
    def __init__(self, author, title, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type

class EBook(Book):
    def __init__(self, author, title, pages, size):
        super().__init__(title, author, pages)
        self.size = size
