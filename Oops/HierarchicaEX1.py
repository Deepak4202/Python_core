# # HierarchicaEX1.py
#
# 1. Cab Booking System Using Hierarchical Inheritance
# Class 1: Cab
# •	Create methods to calculate the fare for Bike, Auto, and Car rides.
# Class 2: Uber (inherits Cab)
# •	Create the methods menu(), booking(), and billing().
# •	Add 10% GST and apply a 15% discount if the bill is above ₹1000.
# Class 3: Ola (inherits Cab)
# •	Create the methods menu(), booking(), and billing().
# •	Add 12% GST and apply a 20% discount if the bill is above ₹1500.
# Driver Code
# •	Ask the user to choose Uber or Ola and call the booking() method.

import sys
class cab:

    def claculatefair(self,n,Km):
        match n:
            case 1:
                return  20*Km,'Auto'
            case 2:
                return  40*Km, 'Cab'
            case 3:
                return  10*Km, 'Bike'
            case _:
                print("Invalid Input")
                sys.exit()

class Uber(cab):
    def menu(self):
        print("="*50)
        print("----------Uber----------")
        print("Select your vehicle")
        print("=" * 50)
        print("""
                1.Auto  ----------------------  =Rs20/Km
                2.Cab   ----------------------  =Rs40/Km
                3.Bike  ----------------------  =Rs10?Km
        """)
    def booking(self):
        self.l = []
        self.Total = 0
        self.menu()
        self.choice = int(input("Select your vehicle :"))
        self.Km = int(input("How many KM you need to Travel : "))

        self.s = self.claculatefair(self.choice,self.Km)
        self.l.append(self.s)
        self.Total = self.s[0]
        self.billing()
    def billing(self):
        if self.Total >=1000:
            self.gst = 0.1*self.Total
            self.Total += self.gst
            self.discount = 0.15 * self.Total
            self.Total -=self.discount
        print("===================================")
        print("Bill")
        print("===================================")
        for i in self.l:
            print(f"{i[1]} --->  {i[0]}/Km{self.Km} ")
        print(f" Gst ---------------{self.gst}")
        print(f"Discount -----------{self.discount}")
        print("====================================")

        print(f"Total {self.Total}")

class Ola(cab):
    def menu(self):
        print("=" * 50)
        print("----------OLA----------")
        print("Select your vehicle")
        print("=" * 50)
        print("""
                   1.Auto  ----------------------  =Rs22/Km
                   2.Cab   ----------------------  =Rs42/Km
                   3.Bike  ----------------------  =Rs13?Km
           """)

    def booking(self):
        self.l = []
        self.Total = 0
        self.menu()
        self.choice = int(input("Select your vehicle :"))
        self.Km = int(input("How many KM you need to Travel : "))

        self.s = self.claculatefair(self.choice, self.Km)
        self.l.append(self.s)
        self.Total = self.s[0]
        self.billing()

    def billing(self):
        self.gst =0
        self.discount =0
        if self.Total >= 1500:
            self.gst = 0.12 * self.Total
            self.Total += self.gst
            self.discount = 0.20 * self.Total
            self.Total -= self.discount
        print("===================================")
        print("Bill")
        print("===================================")
        for i in self.l:
            print(f"{i[1]} --->  {i[0]}/Km{self.Km} ")

        print(f" Gst ---------------{self.gst}")
        print(f"Discount -----------{self.discount}")
        print("====================================")

        print(f"Total {self.Total}")

# obj = Uber()
# obj.booking()
obj1 = Ola()
obj1.booking()