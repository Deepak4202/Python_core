# 3. Create a decorator that accepts a function with parameters.
# Example:
# @calculate
# def add(a,b):
#     print(a+b)
#
# add(10,20)
# Output:
# Addition result: 30


def calculate(fun):
    def exe(a,b):
        fun(a,b)
    return exe

@calculate
def add(a,b):
    print(f"Addition :{a+b}")

add(10,30)