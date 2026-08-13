# 4. Create a decorator to check whether a number is even or odd before executing a function.
# Example:
# @check_number
# def show(n):
#     print("Number accepted")
# Input:
# show(10)
# Output:
# Positive number
# Number accepted
n = int(input())
def check_number(fun):
    def check(a):
        if a & 1:
            print("Positive Number")
        else:
            print("Positive Number")
        fun(a)
    return check

@check_number
def show(n):
    print("Number accepted")

show(n)
