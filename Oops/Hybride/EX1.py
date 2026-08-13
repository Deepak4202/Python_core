# 1. ATM Banking System Using Hybrid Inheritance
# Write a Python program to implement an ATM Banking System using hybrid inheritance.
# Class 1: RBI
# •	Create the methods deposit(amount) and check_balance().
# Class 2: SBI (inherits RBI)
# •	Create the method sbi_services().
# Class 3: Kotak (inherits RBI)
# •	Create the method kotak_services().
# Class 4: Union (inherits RBI)
# •	Create the method union_services().
# Class 5: ATM (inherits SBI, Kotak, and Union)
# Create the following methods:
# •	menu() – Display the list of available banks.
# •	transaction() – Allow the user to:
# o	Select a bank.
# o	Deposit money.
# o	Check the account balance.
# o	Display the selected bank's services.
# Driver Code
# •	Create an object of the ATM class.
# •	Call the transaction() method.

Amount = 10000
class RBI:
    def deposit(self,amount):
        global Amount
        Amount +=amount
        print(f"{amount} Deposit successful ")
    def checkBalance(self):

        print("="*50)
        print(f"Balance = {Amount}")
        print("="*50)
class SBI(RBI):
    def SBI_sevices(self):
        print("=" * 50)
        print("Welcome to SBI")
        print("=" * 50)
        print("1.Deposit")
        print("2.Check balance")
        print("=" * 50)
        a = int(input("Enter your choice: "))
        if a == 1:
            self.cash = int(input("Enter your Deposit : "))
            super().deposit(self.cash)
        elif a == 2:
            super().checkBalance()
        else:
            print("You select invalid input")
class kotak(RBI):
    def Kotak_sevices(self):
        print("=" * 50)
        print("Welcome to Kotak")
        print("=" * 50)
        print("1.Deposit")
        print("2.Check balance")
        print("=" * 50)
        a = int(input("Enter your choice: "))
        if a == 1:
            self.cash = int(input("Enter your Deposit : "))
            super().deposit(self.cash)
        elif a == 2:
            super().checkBalance()
        else:
            print("You select invalid input")
class union(RBI):
    def Union_sevices(self):
        print("=" * 50)
        print("Welcome to union")
        print("=" * 50)
        print("1.Deposit")
        print("2.Check balance")
        print("=" * 50)
        a = int(input("Enter your choice: "))
        if a == 1:
            self.cash = int(input("Enter your Deposit : "))
            super().deposit(self.cash)
        elif a == 2:
            super().checkBalance()
        else:
            print("You select invalid input")

class ATM(SBI,kotak,union):

    def menu(self):
        print("=" * 50)
        print("Available Banks")
        print("=" * 50)
        print("1.SBI\n2.Kotak\n3.Union")

    def transection(self):
        self.menu()
        self.option = int(input("Select your Bank : "))

        if self.option ==1:
            super().SBI_sevices()
        elif self.option ==2:
            super().Kotak_sevices()
        elif self.option ==3:
            super().Union_sevices()
        else:
            print("Invalid Input")

        print("***********Thankyou*************")

obj = ATM()
obj.transection()