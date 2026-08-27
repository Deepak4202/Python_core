# 3. Create a Person class with private __first_name and __last_name. Create properties for both.
# Create a read-only property full_name that returns: first_name + " " + last_name

class ShoppingCart:

    def __init__(self):
        self.__total = 0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value

    def add_item(self, price):
        self.total = self.total + price

    def remove_item(self, price):
        if price <= self.total:
            self.total = self.total - price
        else:
            print("Cannot remove item")


# Create object
cart = ShoppingCart()

# Add items
cart.add_item(500)
cart.add_item(200)

print("Total:", cart.total)

# Remove item
cart.remove_item(200)

print("Total after removing:", cart.total)