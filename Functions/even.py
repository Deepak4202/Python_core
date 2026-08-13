# # 4.	Write a function is_even(n) that returns True if number is even otherwise False
#
def is_even(n):

    if n % 2 == 0:
        return True
    return False


a = int(input("Enter a number: "))

if is_even(a):
    print("Given number is even ")
else:
    print("Given number is not even")


