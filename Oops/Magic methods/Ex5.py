# 5.	Create a Student class with name and marks.
# Implement __gt__() to compare the marks of two students.
# Test which student has higher marks

class Student:

    def __init__(self,name,marks):
        self.name= name
        self.marks =marks

    def __ge__(self, other):

        return self.marks > other.marks


s1 = Student("Deepak",21)
s2 = Student("Nani",9)
print(s1>=s2)