# 4. Bank Account
# Create an abstract class BankAccount with two abstract methods:
# deposit(amount)
# withdraw(amount)
# Create:
# •	SavingsAccount
# •	CurrentAccount
# Maintain the balance using an instance variable.

from  abc import ABC ,abstractmethod
class BankAccount(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass
    def Withdraw(self,amount):
        pass



class SavingsAccount(BankAccount):

    def deposit(self,amount):
        print("SavingsAccount")
        print(f"{amount} deposit Successfully ")

    def Withdraw(self,amount):
        print("SavingsAccount")
        print(f"{amount} Withdraw Successfully ")


class CurrentAccount(BankAccount):

    def deposit(self, amount):
        print("CurrentAccount")
        print(f"{amount} deposit Successfully ")

    def Withdraw(self, amount):
        print("CurrentAccount")
        print(f"{amount} Withdraw Successfully ")


obj = SavingsAccount()
obj.deposit(1000)
obj.Withdraw(1000)

obj = CurrentAccount()
obj.deposit(1000)
obj.Withdraw(1000)

