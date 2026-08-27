# 3. Create a Person class with private __first_name and __last_name.
# Create properties for both. Create a read-only property full_name that returns:
# first_name + " " + last_name

class Person:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


# Create object
person = Person("Deepak", "Kumar")

# Access first name
print(person.first_name)

# Access last name
print(person.last_name)

# Access full name
print(person.full_name)

# Change first and last name
person.first_name = "Rahul"
person.last_name = "Reddy"

print(person.full_name)