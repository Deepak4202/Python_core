# 3.	Create a Number class and implement __add__(), __sub__(), __mul__(), and __truediv__().
# Test all four operations using two objects.

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


# Create two objects
n1 = Number(20)
n2 = Number(5)

# Test all operations
print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)
print("Division:", n1 / n2)