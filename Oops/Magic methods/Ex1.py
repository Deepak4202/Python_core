# 1.	Create a ShoppingCart class with a list of product names.
# Implement __len__() to return the number of products and __contains__() to check whether a product exists.
# Add at least 5 products and test both methods.

class ShoppingCart:
    def __init__(self):
        self.cart =[]

    def addproducts(self):
        n = int(input("Enter how many products you want to enter :"))
        for i in range(n):
            self.cart.append(input(f"Enter product {i+1} : "))

    def __len__(self):

        return len(self.cart)

    def __contains__(self, item):

        return item in self.cart



obj = ShoppingCart()
obj.addproducts()
print(len(obj))
print(obj.__contains__(input("Enter search element : ")))
