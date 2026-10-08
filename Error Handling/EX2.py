# • Create a class Person whose constructor takes age as an argument.
# Raise a ValueError if the age is less than 0.

class Person:

    def __init__(self,age):

        try:
            if age <0:
                raise ValueError("Age Cant be less then 0")
        except ValueError as s:
            print(s)
        else:
            print(f"{age} valid age")


try:
    a = int(input("Enter your age :"))
except ValueError:
    print("Dot enter alphabets ")
else:
    obj = Person(a)