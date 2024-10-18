class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show_info(self):
        print(f"Name: {self.name}\nAuthor:{self.author}")
