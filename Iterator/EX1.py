# 1.Create an custom iterator that prints numbers from 1 to N, where N is given by the user.
N = int(input())
class A:
    def __init__(self,num):
        self.start =  num
    def __iter__(self):
        return self

    def __next__(self):

        if self.start <= N:
            val = self.start
            self.start += 1
            return val
        else:
            raise StopIteration

obj = A(int(input("Enter Starting value : ")))

for i in obj:
    print(i)