# 2. Create an Employee Payroll System using all four OOP concepts.
# Requirements:
# Create an abstract class Employee with:
# •	Private variables __name, __id, and __salary
# •	Properties for accessing employee information
# •	Abstract method calculate_salary()
# Create three child classes:
# •	FullTimeEmployee
# •	PartTimeEmployee
# •	ContractEmployee
# Each class should calculate salary differently.
# For example:
# •	Full-time → fixed salary + bonus
# •	Part-time → hours × hourly rate
# •	Contract → contract amount
# Create a method display_details() to display employee information.
# Create objects for all employee types and call calculate_salary() using the same method call.

from abc import  ABC ,abstractmethod

class Employee(ABC):

    def __init__(self,name,id,salary):

        self.__name =name
        self.__id = id
        self.__salary = salary
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,names):
        self.name = names

    @property
    def ide(self):
        return self.__id

    @ide.setter
    def ide(self,id):
        self.__id = id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,sal):
        self.__salary =sal

    def display_details(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self,bonus):
        # Full - time → fixed
        # salary + bonus
        self.salary = self.salary + bonus

    def display_details(self):
        print("="*50)
        print("FullTimeEmployee")
        print(f"Name: {self.name}")
        print(f"Id: {self.ide}")
        print(f"Salary: {self.salary}")
        print("=" * 50)
class PartTimeEmployee(Employee):
    # Part - time → hours × hourly
    # rate
    def calculate_salary(self, hours):
        # Full - time → fixed
        # salary + bonus
        self.salary = self.salary * hours

    def display_details(self):
        print("=" * 50)
        print("PartTimeEmployee")
        print(f"Name: {self.name}")
        print(f"Id: {self.ide}")
        print(f"Salary: {self.salary}")
        print("=" * 50)


class 	ContractEmployee:
    # Contract → contract
    # amount
    def calculate_salary(self, bonus):
        # Full - time → fixed
        # salary + bonus
        self.salary = self.salary

    def display_details(self):
        print("=" * 50)
        print("calculate_salary")
        print(f"Name: {self.name}")
        print(f"Id: {self.ide}")
        print(f"Salary: {self.salary}")
        print("=" * 50)