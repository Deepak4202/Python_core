# 5.Create a Student class with private variables __name and __marks.
# Create properties name and marks with getter and setter methods.
# Create a read-only property result that returns "Pass" if marks are 40 or above, otherwise "Fail".

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value

    @property
    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


# Create object
student = Student("Deepak", 75)

print("Name:", student.name)
print("Marks:", student.marks)
print("Result:", student.result)

# Update marks
student.marks = 35

print("Updated Marks:", student.marks)
print("Updated Result:", student.result)