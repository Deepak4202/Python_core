class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


# Create object
account = BankAccount(5000)

# Check balance
print("Initial Balance:", account.balance)

# Deposit
account.deposit(2000)
print("After Deposit:", account.balance)

# Withdraw
account.withdraw(1000)
print("After Withdrawal:", account.balance)