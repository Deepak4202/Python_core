# 3. Create a User class with a private variable:
# __password
# Create a method change_password() that allows the user to change the password.
# The password should not be directly accessible from outside the class.

class User:

    def __init__(self, password):
        self.__password = password

    def change_password(self, new_password):
        self.__password = new_password
        print("Password changed successfully")


# Create object
user = User("abc123")

# Change password
user.change_password("xyz789")