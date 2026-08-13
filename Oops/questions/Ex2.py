# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
class Employee:
    name = "Deepak"
    Company_name = "TechCorp"
    @classmethod
    def change(cls,new_name):

        cls.Company_name =new_name

obj = Employee()

obj.change("CVCORP")
print(obj.name,obj.Company_name)