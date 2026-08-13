# 2.	Write a generator that yields even numbers from 1 to N
def Even(n):
    for i in range(1,n+1):
        if i % 2==0:
            yield i

a = Even(int(input("Enter a Number : ")))

for i in a:
    print(i)