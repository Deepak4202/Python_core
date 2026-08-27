# 2.Create a BankAccount class with instance variables name , salarys.
# Write an instance method deposit(amount) to add the given amount to the salarys and display the updated salarys.

class  BankAccount:
    def __init__(self):
        self.account_holder = "Deepak"
        self.balance = 10000

    def display_details(self,amount):
        self.balance += amount
        print("=======================================")
        print("\t\t\tDetails")
        print("=======================================")
        for i , k in self.__dict__.items():

            print(i ,"----------->", k)


obj = BankAccount()
print("Balance before ----- > {}".format(obj.balance))

obj.display_details(10000)