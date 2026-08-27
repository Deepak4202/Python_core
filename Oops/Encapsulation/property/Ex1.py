# 1. Create an Employee class with a private __salary. Use @property to get the salary and @salary.setter to modify it.
# Create an employee object and update the salary.

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value


# Create employee object
emp = Employee(30000)

# Get salary
print("Old Salary:", emp.salary)

# Update salary
emp.salary = 40000

# Get updated salary
print("New Salary:", emp.salary)