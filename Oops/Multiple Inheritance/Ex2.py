# 1. ATM System Using Multiple Inheritance
# Class 1: SBI
# •	Create the methods deposit(amount) and check_balance().
# Class 2: UnionBank
# •	Create the methods withdraw(amount) and mini_statement().
# Class 3: ATM (inherits SBI and UnionBank)
# •	Create the methods menu() and transaction().
# •	Allow the user to perform banking operations.
# Driver Code
# •	Create an object of the ATM class.
# •	Call the transaction() method.


Amount = 10000
class SBI:
    def deposit(self,amount):
        global Amount
        Amount += amount
        print("Deposit Successful")
    def checkbalance(self):
        print("="*50)
        print("     Balance     ")
        print("=" * 50)
        print(Amount)
class UnionBank:

    def Withdraw(self,amoumt):
        amoumt =amoumt
        global Amount
        if amoumt < Amount:
            self.amount = amoumt
            Amount -=amoumt

            print("Withdraw successful")
    def ministatement(self):

        print("---------------Mini Statement--------------")
        try:
            print(self.amount,"Withdraw recently")
        except AttributeError:
            print("No previews Records")
class ATM(SBI,UnionBank):
    def menu(self):
        print("""
        1:Deposit
        2.CheckBalance
        3.Withdraw 
        4.Mini statement """)

    def Transection(self):
        while True:
            self.menu()
            choice = int(input())
            if choice == 1:
                self.deposit(int(input("Enter Deposit Amount :")))
            elif choice ==2:
                self.checkbalance()
            elif choice == 3:
                self.Withdraw(int(input("Enter your withdraw amount: ")))
            elif choice == 4:
                self.ministatement()
            op = input("Do you want perform another Transection Y/N : ")

            if op.lower() == "n":
                print("Thankyou")
                break

obj = ATM()

obj.Transection()