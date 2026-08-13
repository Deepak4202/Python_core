# 2.	Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?

def sub(a,b):
    return a-b
a,b = int(input("Enter value for A: ")),int(input("Enter value for B : "))
print("subtraction ({},{}) = {} ".format(a,b,sub(a,b)))