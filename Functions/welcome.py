# 2.	Write a function welcome(name) that prints "Welcome" followed by the given name.

def welcome(name:str):
    print("Welcome {}".format(name))

n= input("Enter your name: ")
welcome(n)