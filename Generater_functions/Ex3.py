# 3.	Write a generator that yields each character of a string.

def Charecter(n):
    for i in range(0,len(n)):

            yield n[i]

a = Charecter(input("Enter a Number : "))

for i in a:
    print(i)