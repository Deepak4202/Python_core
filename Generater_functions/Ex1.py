# 1.	Write a generator that yields numbers from 1 to N.

def Number1t0N(n):
    for i in range(1,n+1):
        yield i

a = Number1t0N(int(input("Enter a Number : ")))

for i in a:
    print(i)