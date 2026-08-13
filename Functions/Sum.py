# 7.	Write a function called add(a, b) that returns the sum of two numbers.

def add(a,b):
    return a+b
a = int(input("Enter  value for A: "))
b = int(input("Enter  value for B: "))
print("Sum ({},{}) = {}".format(a,b,add(a,b)))
