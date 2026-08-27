# 1. Create a Student class with a private variable __marks.
# Create methods:
# •	set_marks() → to assign marks
# •	get_marks() → to retrieve marks
# Create an object and access the marks using these methods.
class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


# Create object
s1 = Student()

# Assign marks using setter method
s1.set_marks(85)

# Retrieve marks using getter method
print(s1.get_marks())