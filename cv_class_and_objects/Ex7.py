# 7.	Create a class Voting. Write a static method is_eligible(age).
# If age is 18 or above, print "Eligible to Vote". Otherwise print "Not Eligible".

class Voting:
    @staticmethod
    def is_eligible(age):
        if age >18:
            print("Eligible to Vote")
        else:
            print("Not Eligible")

Voting.is_eligible(20)
Voting.is_eligible(17)