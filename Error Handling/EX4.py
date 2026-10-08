# Create a custom exception named InvalidAgeError.
# Create a class Voter with a method check_eligibility(age)
# that raises this exception if age is less than 18

class InvalidAgeError(Exception):
    pass

class Voter:
    def check_eligibility(self,age):

        try:
            if age <18:
                raise InvalidAgeError("You are not Eligible for vote")
        except InvalidAgeError as e:
            print(e)
        else:
            print("You are eligible for vote")

voter1 = Voter()
a =int(input("Enter your age : "))
voter1.check_eligibility(a)