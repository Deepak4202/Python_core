class Bank_Management_system():
    def __init__(self):

        self.balance = 1000000
    def deposit(self,amount):

        self.balance+=amount

        print("Amount Deposited successfully ")
        print("Balance {}".format(self.balance))

    def withdraw(self,amount):

        if self.balance >=  amount :

            self.balance -=amount
        else:
            print("Insufficient funds")

    def check_balance(self):

        return self.balance

class User(Bank_Management_system):

    def __init__(self,username):

        super().__init__()
        self.user = username

        print(self.user)

    def operations(self,n):
        match (n):
            case 1 :
                self.deposit(int(input("Enter your deposit amount: ")))

            case 2:
                self.withdraw(int(input("Enter your withdrew amount :")))

            case 3:
                print(self.check_balance())

            case _:
                print("You chose wrong operation")


opp = User("Deepak")

print("""
    1.deposit
    2.withdraw
    3.check balance
    
    """)
ope = int(input("Enter your choice of operation from 1/2/3 : "))

opp.operations(ope)



