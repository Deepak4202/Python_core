# 2.	Create an custom iterator that prints numbers from N to 1.
N = int(input())
class FromNto1:
    def __init__(self):

        self.start = N
    def __iter__(self):

        return self
    def __next__(self):

        if self.start >=1:
            self.value = self.start
            self.start -=1
            return self.value
        else:
            raise StopIteration

obj = FromNto1()

for i in obj:
    print(i,end=" ")