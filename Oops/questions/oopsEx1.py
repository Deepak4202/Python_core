# 1. Create a Banking System using OOP.
# Requirements:
# •	Create an abstract class BankAccount.
# •	Keep __account_number, __holder_name, and __balance as private variables.
# •	Create properties to access and modify the required data.
# •	Create an abstract method calculate_interest().
# Create the following child classes:
# •	SavingsAccount
# •	CurrentAccount
# Each child class should implement calculate_interest() differently.
# Create a method display_details() in the parent class and override it in child classes where required.


from  abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,acc_num,holder_name,balance):

        self.__account_number = acc_num
        self.__holder_name = holder_name
        self.__balance =balance

    @abstractmethod
    def calculate_interest(self):
        pass

    @property
    def getaccnum(self):
        return self.__account_number

    @getaccnum.setter
    def getaccnum(self,accnumber):
        self.__account_number = accnumber

    @property
    def holder_name(self):
        return self.__holder_name

    @holder_name.setter
    def holder_name(self,name):

        self.__holder_name = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        self.__balance =amount

    def display_details(self):
        pass

class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("SavingsAccount")
        print("Print 10 % interest")
        print(f"interest{self.balance*0.1}")
        self.balance = (self.balance)+(self.balance*0.1)
        print(f"Total amount {self.balance}")


    def display_details(self):
        print("SavingsAccount")
        print("*"*50)
        print(f"Name {self.holder_name}")
        print(f"Account_number {self.getaccnum}")
        print(f"Balance : {self.balance}")
        print("*" * 50)

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("CurrentAccount")
        print("Print 10 % interest")
        print(f"interest{self.balance * 0.1}")
        self.balance = (self.balance) + (self.balance * 0.1)
        print(f"Total amount {self.balance}")

    def display_details(self):
        print("CurrentAccount")
        print("*" * 50)
        print(f"Name {self.holder_name}")
        print(f"Account_number {self.getaccnum}")
        print(f"Balance : {self.balance}")
        print("*" * 50)

obj = SavingsAccount(98764523,"Deepak",10000)
obj.calculate_interest()
obj.display_details()

obj = CurrentAccount(98764523,"Deepak",10000)
obj.calculate_interest()
obj.display_details()