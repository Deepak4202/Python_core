# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self,celsius):
        self.celsius =celsius

    @staticmethod
    def to_fahrenheit(celsius):

        return ((180/100)*celsius) +32
    def show_conversion(self):
        print("Celsius    :", self.celsius)
        print("Fahrenheit :", self.to_fahrenheit(self.celsius))

# Create object
t1 = Temperature(25)

# Display conversion
t1.show_conversion()