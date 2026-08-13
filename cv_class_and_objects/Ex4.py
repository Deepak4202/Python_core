# 4.	Create an Student class with a class variable company = "Infosys" .
# Write a class method change_company(new_company) to change the company name.

class Employee:
    company = "Infosys"

    @classmethod

    def change_company(cls,new_company):
        print("before ---------> {}".format(cls.company))

        cls.company = new_company

        print("After ---------> {}".format(cls.company))

Employee.change_company("TCS")




