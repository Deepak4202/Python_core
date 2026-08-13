# 2. Create a decorator my_decorator for the below function:
# 	def greet():
#     		print("Good Morning")
# Output should be:
# Welcome Message
# Good Morning
# Thank You Message
def my_decorator(fun):
    def welcome():
        print("Welcome Message")
        fun()
        print("Thank You Message")
    return welcome

def greet():
    print("Good Morning")

a  = my_decorator(greet)
a()