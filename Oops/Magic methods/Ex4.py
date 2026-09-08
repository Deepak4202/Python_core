# 4.	Create a Distance class with meters.
# Implement __add__() to add two distances and return a new Distance object.
# Test with Distance(100) + Distance(250).

class Distance:

    def __init__(self,meters):

        self.meters = meters

    def __add__(self, other):

        return self.meters + other.meters

d1 = Distance(20)
d2 = Distance(40)

print((d1+d2))