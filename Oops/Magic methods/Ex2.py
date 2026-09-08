# 2.	Create a BookCollection class containing book names.
# Implement __len__() and __contains__().
# Add 5 books and check the number of books and whether a particular book is present.
class Bookcollection:
    def __init__(self):
        self.books = list(map(str,input().split()))

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        return  item in self.books

obj = Bookcollection()

print(obj.__len__())

print(obj.__contains__(input()))