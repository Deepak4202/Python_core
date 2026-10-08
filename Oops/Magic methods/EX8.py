# Question 1: Bank Account Operations
# Create a class BankAccount with:
# •	attributes: account_holder, balance
# •	instance method: deposit(amount)
# •	instance method: withdraw(amount)
# Implement these magic methods:
# •	__str__() → display account details
# •	__add__() → add balances of two accounts
# •	__sub__() → subtract balances
# •	__eq__() → compare if two accounts have same balance
# •	__lt__() → check which account has lower balance
# •	__getattribute__() → print a message whenever an attribute is accessed
# •	__setattr__() → prevent setting negative balance
# Demonstrate creating two accounts and using all operations.
# ________________________________________
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # __str__() -> display account details
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}"

    # __add__() -> add balances of two accounts
    def __add__(self, other):
        return self.balance + other.balance

    # __sub__() -> subtract balances
    def __sub__(self, other):
        return self.balance - other.balance

    # __eq__() -> compare balances
    def __eq__(self, other):
        return self.balance == other.balance

    # __lt__() -> check which account has lower balance
    def __lt__(self, other):
        return self.balance < other.balance

    # __getattribute__() -> called whenever an attribute is accessed
    def __getattribute__(self, name):
        print(f"Attribute '{name}' is accessed")
        return object.__getattribute__(self, name)

    # __setattr__() -> prevent negative balance
    def __setattr__(self, name, value):

        if name == "balance" and value < 0:
            print("Error: Balance cannot be negative.")
            return

        object.__setattr__(self, name, value)


# Creating two accounts
account1 = BankAccount("Deepak", 10000)
account2 = BankAccount("Rahul", 7000)

print("\n--- Account Details ---")
print(account1)
print(account2)


# Deposit
print("\n--- Deposit ---")
account1.deposit(2000)
print(account1)


# Withdraw
print("\n--- Withdraw ---")
account2.withdraw(2000)
print(account2)


# __add__()
print("\n--- Addition ---")
print("Total balance:", account1 + account2)


# __sub__()
print("\n--- Subtraction ---")
print("Balance difference:", account1 - account2)


# __eq__()
print("\n--- Equality ---")
print("Same balance?", account1 == account2)


# __lt__()
print("\n--- Less Than ---")
print("Is account1 balance lower?", account1 < account2)
print("Is account2 balance lower?", account2 < account1)


# __setattr__() negative balance test
print("\n--- Negative Balance Test ---")
account1.balance = -500


# __getattribute__() test
print("\n--- Attribute Access Test ---")
print(account1.account_holder)
print(account1.balance)

print(account1.nani)