# 2. Create a BankAccount class with a private variable __balance.
# Implement:
# •	deposit(amount)
# •	withdraw(amount)
# •	get_balance()
# The balance should not be accessed directly from outside the class.
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Create object
account = BankAccount()

# Deposit money
account.deposit(5000)

# Withdraw money
account.withdraw(2000)

# Get balance
print("Balance:", account.get_balance())