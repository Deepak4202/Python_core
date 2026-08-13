# 8.	Create an custom iterator that prints each character of a string one by one.


N = input()

class Charracter:

    def __init__(self):
        self.String = N
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.count < len(self.String):

            val = self.String[self.count]
            self.count +=1
            return val
        else:
            raise StopIteration

obj = Charracter()

for i in obj:
    print(i)

