# Create a Person class with name and age.
# Create an Employee class that inherits from Person and adds department.
# Create a Manager class that inherits from Employee and adds team_size.
# Use super() to call the parent class _init_() method.
# Override the describe() method in each child class and use super() to reuse the parent method.
# Create a Manager object with:
# Name = "Alice"
# Age = 35
# Department = "Engineering"
# Team Size = 10
# Display the complete details of the manager.
#
# Expected Output:
#
# Alice, age 35, dept: Engineering, team: 10 people

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
class Employee(person):
    def __init__(self,department,name,age):
        self.department = department
        super().__init__(name,age)

    def describe(self):
        super().describe()
        print(f"Department = {self.department}")
class Manager(Employee):
    def __init__(self,teamsize,department,name,age):
        super().__init__(department,name,age)
        self.teamsize =teamsize



    def describe(self):
        super().describe()
        print(f"Team size = {self.teamsize}")


obj = Manager(10,"HR","Nani",21)

obj.describe()