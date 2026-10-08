class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Calculate total price
    def total_price(self):
        return self.price * self.quantity

    # __str__() -> display product details
    def __str__(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Quantity: {self.quantity}"

    # __add__() -> add total prices of two products
    def __add__(self, other):
        return self.total_price() + other.total_price()

    # __mul__() -> multiply product price by a number
    def __mul__(self, number):
        return self.price * number

    # __gt__() -> compare total values
    def __gt__(self, other):
        return self.total_price() > other.total_price()

    # __eq__() -> compare prices
    def __eq__(self, other):
        return self.price == other.price

    # __getattr__() -> called when attribute is not found
    def __getattr__(self, name):
        return "Attribute not found"

    # __setattr__() -> prevent negative price
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            print("Price cannot be less than 0.")
            return

        super().__setattr__(name, value)


# Creating two products
product1 = Product("Laptop", 50000, 2)
product2 = Product("Mouse", 1000, 5)


# __str__()
print("\n--- Product Details ---")
print(product1)
print(product2)


# total_price()
print("\n--- Total Price ---")
print(product1.total_price())
print(product2.total_price())


# __add__()
print("\n--- Addition ---")
print("Combined total:", product1 + product2)


# __mul__()
print("\n--- Multiplication ---")
print("Laptop price × 3:", product1 * 3)


# __gt__()
print("\n--- Greater Than ---")
print("Is product1 total greater?", product1 > product2)


# __eq__()
print("\n--- Equality ---")
print("Do products have same price?", product1 == product2)


# __getattr__()
print("\n--- Missing Attribute ---")
print(product1.color)


# __setattr__()
print("\n--- Negative Price Test ---")
product1.price = -500

print("Current price:", product1.price)