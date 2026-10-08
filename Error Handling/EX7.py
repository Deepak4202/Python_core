# Create a class UserInput with a method get_integer(value).
# Handle ValueError and TypeError using separate except blocks.

class UserInput:

    def get_integer(self,value):

        try:
            num = int(value)

            print("Number is ", num)
        except ValueError as e:
            print(e,"From Value error")
        except TypeError as e:
            print(e,"from Type error")

obj = UserInput()

obj.get_integer([30])
obj.get_integer(("wweesfv2"))

# obj.get_integer(None)


