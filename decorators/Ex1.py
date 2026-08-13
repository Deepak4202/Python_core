# 1. Create a decorator that prints a message before and after executing a function.
# 	Expected output:
# 	Before function execution
# 	Hello Student
# 	After function execution

def greet(fun):
    def exe():
        print("Before function execution")
        fun()
        print("After function execution")
    return exe

def suply():
    print("Hello Student")

a = greet(suply)
a()
