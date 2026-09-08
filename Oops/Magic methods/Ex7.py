# 7.	Create a Product class with name and price.
# Implement __lt__(), __gt__(), and __eq__().
# Compare two products based on price.

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):

        return self.price > other.price

    def __eq__(self, other):

        return self.price == other.price


p1 = Product("car toy" ,2000)

p2 = Product("bike toy",1999)

print(p1 > p2)
print(p1 <p2)
print(p1==p2)