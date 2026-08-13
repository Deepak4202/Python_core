class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


# Creating book using constructor
title = "Python"
author = "Deepak"

if Book.is_valid_title(title):
    b1 = Book(title, author)
    print("Book created:", b1.title, "-", b1.author)
else:
    print("Invalid title")


# Creating book using class method
book_str = "Django-Ravi"
title = book_str.split("-")[0]

if Book.is_valid_title(title):
    b2 = Book.from_string(book_str)
    print("Book created:", b2.title, "-", b2.author)
else:
    print("Invalid title")


# Invalid title
title = "AI"

if Book.is_valid_title(title):
    b3 = Book(title, "Kiran")
    print("Book created")
else:
    print("Invalid title:", title)


print("Total books:", Book.total_books)