# Create a class BankAccount with an attribute balance.
# Implement a method withdraw(amount)
# that raises an exception if the withdrawal amount is greater than the available balance.

class WithdrawError(Exception):
    pass

class BankAccount:
    def __init__(self,balance):
        self.balance= balance

    def withdraw(self,amount):
        try:
            if self.balance < amount:
                raise WithdrawError("amount is not Insufficient ")
        except WithdrawError as e:
            print(e)
        else:
            self.balance -=amount
            print(f"{amount} withdraw is successful ")

us1 = BankAccount(100000)

us1.withdraw(2000)
us1.withdraw(100000)

