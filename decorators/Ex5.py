# 5. Create a login verification decorator.
# Requirement:
# If user is logged in:
# 	Access granted
# 	Welcome to profile
# Otherwise:
# 	Please login first
# Example:
# @login_required
# def profile():
#print("Welcome to profile")
# Login status
logged_in = False      # Change to False to test
print("="*50)

user_name = input("Enter your user name : ")

password =input("Enter your conform your password : ")
print("="*50)
# Decorator
def login_required(func):
    def wrapper():
        print("\t\tEnter your login Details")
        print("=" * 50)
        if user_name == input("Enter your name : ") and password == input("Enter Your password: "):
            print("="*50)
            print("\t\tAccess granted")
            print("=" * 50)
            func()
        else:
            print("=" * 50)
            print("Please login first")
            print("=" * 50)
    return wrapper


@login_required
def profile():
    print("Welcome to profile")


# Function call
profile()