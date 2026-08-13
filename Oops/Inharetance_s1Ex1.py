# 2.	Student Salary System
# Create an Student class with:
# •	emp_name
# •	salary
# •	display_details()
# Create a Manager class that inherits Student and adds a bonus(). Display the total salary.

class Employee():
    def __init__(self):
        self.emp_name = 'Deepak'
        self.salary = 1000000
    def display_details(self):
        print("="*50)
        print("\t\tStudent Details")
        print("="*50)
        print("Student Name: {}".format(self.emp_name))
        print("Salary : {}".format(self.salary))
        print("=" * 50)
class Manage(Employee):
    def Bonus(self):
        super().__init__()
        self.salary +=11000

obj = Manage()

obj.Bonus()
obj.display_details()
