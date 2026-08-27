# 3.	Create an Student class with instance variables emp_id, name, salarys.
# Write an instance method increment_salary(amount) to increase the employee's salarys by the given amount.

class  BankAccount:

    def __init__(self):
        self.emp_id= 123
        self.name = "Deepak"
        self.salary = 10000

    def increment_salary(self,amount):
        self.salary += amount
        print("=======================================")
        print("\t\t\tDetails")
        print("=======================================")
        for i , k in self.__dict__.items():

            print(i ,"----------->", k)


obj = BankAccount()
print("salarys before ----- > {}".format(obj.salary))

obj.increment_salary(10000)