# 4.	Write a generator that yields characters of a string in reverse order.
def stringReverse(n):
    for i in range(1,len(n)+1):
        yield n[len(n)-i]

a = stringReverse(input("Enter a Number : "))

for i in a:
    print(i)