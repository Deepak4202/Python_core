# 2.	Create a lambda that takes two numbers and returns the larger one using a conditional expression (x if x > y else y).

large = lambda a,b: a if a>b else b
a = int(input("Enter A value : "))
b = int(input("Enter B value : "))
print(large(a,b))