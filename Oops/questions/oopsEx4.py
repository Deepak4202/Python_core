# 4. Design a banking system with:
# •	An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# •	Subclasses: SavingsAccount,  CurrentAccount, FixedDepositAccount.
# •	Each account must:
# o	Encapsulate balance (private)
# o	Provide controlled access through properties
# o	Override interest calculation differently
# •	Include a static method to validate amount.
# •	Include a class method to update bank-wide interest policies.

from abc import ABC,abstractmethod

from abc import ABC, abstractmethod


class Account(ABC):

    # Bank-wide interest policies
    savings_rate = 4.0
    current_rate = 2.0
    fixed_rate = 7.0

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    # Property - getter
    @property
    def balance(self):
        return self.__balance

    # Property - setter
    @balance.setter
    def balance(self, amount):
        if self.validate_amount(amount):
            self.__balance = amount
        else:
            print("Invalid balance")

    # Static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # Deposit
    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
            print("Deposited:", amount)
            print("Balance:", self.__balance)
        else:
            print("Invalid deposit amount")

    # Withdraw
    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.__balance)

    # Abstract method
    @abstractmethod
    def calculate_interest(self):
        pass

    # Class method - update bank-wide policies
    @classmethod
    def update_interest_policy(cls, savings=None, current=None, fixed=None):

        if savings is not None:
            cls.savings_rate = savings

        if current is not None:
            cls.current_rate = current

        if fixed is not None:
            cls.fixed_rate = fixed

        print("\nInterest policies updated successfully")


# -------------------------------------------------
# Savings Account
# -------------------------------------------------

class SavingsAccount(Account):

    def calculate_interest(self):
        interest = self.balance * Account.savings_rate / 100

        print("\nSavings Account")
        print("Interest Rate:", Account.savings_rate, "%")
        print("Interest:", interest)

        return interest


# -------------------------------------------------
# Current Account
# -------------------------------------------------

class CurrentAccount(Account):

    def calculate_interest(self):
        interest = self.balance * Account.current_rate / 100

        print("\nCurrent Account")
        print("Interest Rate:", Account.current_rate, "%")
        print("Interest:", interest)

        return interest


# -------------------------------------------------
# Fixed Deposit Account
# -------------------------------------------------

class FixedDepositAccount(Account):

    def calculate_interest(self):
        interest = self.balance * Account.fixed_rate / 100

        print("\nFixed Deposit Account")
        print("Interest Rate:", Account.fixed_rate, "%")
        print("Interest:", interest)

        return interest


# -------------------------------------------------
# Creating objects
# -------------------------------------------------

s1 = SavingsAccount("S101", "Deepak", 50000)

c1 = CurrentAccount("C101", "Rahul", 80000)

f1 = FixedDepositAccount("F101", "Arun", 100000)


# -------------------------------------------------
# Deposit
# -------------------------------------------------

s1.deposit(10000)


# -------------------------------------------------
# Withdraw
# -------------------------------------------------

s1.withdraw(5000)


# -------------------------------------------------
# Property access
# -------------------------------------------------

print("\nCurrent Balance:", s1.balance)


# -------------------------------------------------
# Interest calculation
# -------------------------------------------------

s1.calculate_interest()

c1.calculate_interest()

f1.calculate_interest()


# -------------------------------------------------
# Static method
# -------------------------------------------------

print("\nAmount Validation:")
print(Account.validate_amount(5000))
print(Account.validate_amount(-500))


# -------------------------------------------------
# Class method
# -------------------------------------------------

Account.update_interest_policy(
    savings=5.0,
    current=2.5,
    fixed=8.0
)


# -------------------------------------------------
# Interest after policy update
# -------------------------------------------------

s1.calculate_interest()
c1.calculate_interest()
f1.calculate_interest()