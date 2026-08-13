# 2.find out given number is super number or not input = 153  1**1 +5**2 +3**3
a = int(input("Enter a number : "))
def dcount(n):
    c =0
    while n>0:
        c+=1
        n //=10
    return c
def supernumber(n):
    c = dcount(n)
    s =0
    i =0
    while n >0:
        r = n%10
        s += r ** (c - i)
        i+=1
        n //=10
    return s

if a == supernumber(a):
    print(f"{a} is super number")
else:
    print(f"{a} is not super number")
