# # OOP Question 6 — Library Management System
#
# #
# # 1. Create a Book class
# #
# # The Book class should contain:
# #
# # Attributes
# # title
# # author
# # isbn
# # available
#
#
# class Book:
#
#     def __init__(self,title,author,available):
#
#         self.title = title
#         self.author = author
#         self.available =True
#
#     def display(self):
#         print("Title: ",self.title,"\nauthor: ",self.author,"\nAvailable: ",self.available)
#
#     def borrow(self):
#
#         if self.available:
#             print(self.title, "borrowed successfully")
#             return True
#         else:
#             print("Book is not available")
#             return False
#
#     def return_book(self):
#
#         if not self.available:
#             self.available = True
#             print(self.title, "returned successfully")
#             return True
#         else:
#
#             print("Book is already available")
#             return False
#
# # 2. Create a Member class
# #
# # The Member class should contain:
# #
# # name
# # member_id
# # borrowed_books
# class Member:
#
#     def __init__(self,name,member_id):
#
#         self.name = name
#         self.member_id =member_id
#         self.borrowed_books = []
#
#     def borrow_book(self,book):
#
#
class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display(self):
        print("Title     :", self.title)
        print("Author    :", self.author)
        print("ISBN      :", self.isbn)
        print("Available :", self.available)

    def borrow(self):
        if self.available:
            self.available = False
            print(self.title, "borrowed successfully")
            return True
        else:
            print("Book is not available")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "returned successfully")
            return True
        else:
            print("Book is already available")
            return False


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
        else:
            print("You did not borrow this book")

    def display_borrowed_books(self):
        print("Member:", self.name)
        print("Member ID:", self.member_id)

        if len(self.borrowed_books) == 0:
            print("No books borrowed")
        else:
            print("Borrowed Books:")

            for book in self.borrowed_books:
                print("-", book.title)


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):

        for b in self.books:
            if b.isbn == book.isbn:
                print("Book with this ISBN already exists")
                return

        self.books.append(book)
        print(book.title, "added to library")

    def add_member(self, member):

        for m in self.members:
            if m.member_id == member.member_id:
                print("Member with this ID already exists")
                return

        self.members.append(member)
        print(member.name, "added as a member")

    def display_books(self):

        print("\n===== LIBRARY BOOKS =====")

        if len(self.books) == 0:
            print("No books available")
            return

        for book in self.books:

            status = "Available" if book.available else "Borrowed"

            print(
                book.title,
                "|",
                book.author,
                "|",
                book.isbn,
                "|",
                status
            )

    def display_members(self):

        print("\n===== LIBRARY MEMBERS =====")

        if len(self.members) == 0:
            print("No members registered")
            return

        for member in self.members:
            print(
                "Name:", member.name,
                "| ID:", member.member_id
            )

    def find_book(self, isbn):

        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def find_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None


# =========================
# MAIN PROGRAM
# =========================

library = Library()


# Creating books

book1 = Book("Python Basics", "John Smith", "ISBN101")
book2 = Book("SQL Fundamentals", "David", "ISBN102")
book3 = Book("Java Programming", "James", "ISBN103")
book4 = Book("Data Structures", "Robert", "ISBN104")
book5 = Book("Operating Systems", "Andrew", "ISBN105")


# Adding books

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)


# Creating members

member1 = Member("Deepak", 101)
member2 = Member("Rahul", 102)
member3 = Member("Anil", 103)


# Adding members

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)


# Display books

library.display_books()


# Display members

library.display_members()


# =========================
# BORROW BOOK
# =========================

print("\n===== BORROW OPERATION =====")

member1.borrow_book(book1)
member1.borrow_book(book2)

member1.display_borrowed_books()


# =========================
# ANOTHER MEMBER BORROWS
# =========================

print("\n===== ANOTHER BORROW OPERATION =====")

member2.borrow_book(book1)


# =========================
# RETURN BOOK
# =========================

print("\n===== RETURN OPERATION =====")

member1.return_book(book1)

member1.display_borrowed_books()


# =========================
# RAHUL BORROWS BOOK
# =========================

print("\n===== RAHUL BORROWS BOOK =====")

member2.borrow_book(book1)


# =========================
# SEARCH BOOK
# =========================

print("\n===== SEARCH BOOK =====")

isbn = "ISBN101"

book = library.find_book(isbn)

if book:
    print("Book found:")
    book.display()
else:
    print("Book not found")


# =========================
# SEARCH MEMBER
# =========================

print("\n===== SEARCH MEMBER =====")

member_id = 101

member = library.find_member(member_id)

if member:
    print("Member found:")
    print("Name:", member.name)
    print("ID:", member.member_id)
else:
    print("Member not found")


# =========================
# FINAL BOOK STATUS
# =========================

library.display_books()