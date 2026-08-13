# 5.	Create an custom iterator that returns only even numbers from a given list.

l = [int(val) for val in input().strip().split()]


class Even:
    def __init__(self):

        self.l  = l
        self.count = 0
    def __iter__(self):
        return self

    def __next__(self):
        while self.count < len(self.l):
            value = self.l[self.count]
            self.count += 1

            if value % 2 == 0:
                return value

        raise StopIteration

obj = Even()

for i in obj:
    print(i ,end=" ")