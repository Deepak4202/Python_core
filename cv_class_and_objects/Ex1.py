# 1.	Create a Student class with the instance variables name , age , marks.
# Write an instance method display_details() to print all the student's details.


class Student:
    def __init__(self):
        self.name = "Deepak"
        self.age = 22

    def display_details(self):
        print("=======================================")
        print("\t\t\tDetails")
        print("=======================================")
        for i , k in self.__dict__.items():

            print(i ,"----------->", k)


obj = Student()

obj.display_details()