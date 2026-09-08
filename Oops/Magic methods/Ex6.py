# 6.	Create a Student class with roll_no and name.
# Implement __eq__() to check whether two students have the same roll number.
# Test with two student objects.

class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_no = roll_number


    def __eq__(self, other):

        return self.roll_no == other.roll_no


s1 = Student("raju",12345678)
s2 = Student("Ram",12345678)

print(s1==s2)
