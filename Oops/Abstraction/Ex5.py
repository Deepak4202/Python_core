# 1. Payment System
# Create an abstract class Payment with an abstract method pay(amount)
# Create:
# •	UPI
# •	CreditCard
# •	Cash
# Each class should implement pay() differently.

from  abc import ABC ,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):

    def pay(self):

        print("From Upi")

class CreditCard(Payment):

    def pay(self):

        print("From CreditCard")

class Cash(Payment):

    def pay(self):

        print("From Cash")


obj = UPI()
obj.pay()

obj1 = CreditCard()
obj1.pay()

obj3 = Cash()
obj3.pay()