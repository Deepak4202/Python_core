# 2. Food Delivery System Using Hybrid Inheritance
# Class 1: Restaurant
# •	Create the methods menu() and price().
# Class 2: Swiggy (inherits Restaurant)
# •	Create the method order_food().
# Class 3: Zomato (inherits Restaurant)
# •	Create the method order_food().
# Class 4: Customer (inherits Swiggy and Zomato)
# •	Create the methods menu() and order().
# Class 1
class Restaurant:
    def menu(self):
        print("Restaurant Menu: Pizza, Burger, Biryani")

    def price(self):
        print("Pizza = ₹250")
        print("Burger = ₹120")
        print("Biryani = ₹200")


# Class 2
class Swiggy(Restaurant):
    def order_food(self):
        print("Food ordered through Swiggy")
        # super().order_food()


# Class 3
class Zomato(Restaurant):
    def order_food(self):
        print("Food ordered through Zomato")


# Class 4
class Customer(Swiggy, Zomato):
    def menu(self):
        print("Customer is viewing the menu")
        super().menu()

    def order(self):
        print("Customer is placing the order")
        super().order_food()


# Driver Code
c = Customer()

c.menu()
c.price()
c.order()