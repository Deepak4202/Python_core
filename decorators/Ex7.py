# 2. Create two decorators
# First decorator:
# 	Before calculation
# 	After calculation
# Second decorator:
# 	Checking inputs
# Apply both decorators to:
# 	@log
# 	@validate
# 	def add(a,b):
#     		print(a+b)
from functools import reduce


def First_decorator(fun):
    def bc(*a):
        print("After calculation ")
        fun(*a)
    return bc
def second_decorator(fun):
    def ac(*c):
        print("Checking inputs")
        fun(*c)
        print("completed")
    return ac
@First_decorator
@second_decorator
def add(*a):
    c = reduce(lambda x,y:x+y,a)
    print(c)

add(1,2,3,4,3)