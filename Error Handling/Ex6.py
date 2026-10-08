# Create a class PasswordValidator with a method validate(password).
# Raise an exception if the password length is less than 8 characters.

class PasswordValidator:

    def validate(self,password):
        try:
            if len(password) <8:

                raise
        except Exception :
            print("length must grater than 8")

        else:
            print("Password is strong ")

obj = PasswordValidator()
obj.validate("deepak2")
obj.validate("deepak2@")