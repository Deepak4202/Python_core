# 3. Student Result System
# Create a Student class with:
# •	Name
# •	marks
# •	display_marks()
# Create a Result class that inherits Student and calculates whether the student has passed or failed.

class Student():
    def __init__(self):
        self.Name = 'Deepak'
        self.marks = 90
    def display_Marks(self):
        print("="*50)
        print("\t\tStudent Details")
        print("="*50)
        print("Student Name: {}".format(self.Name))
        print("Marks: {}".format(self.marks))
        print("=" * 50)
class Manage(Student):
    def claulate(self):
        super().__init__()
        if self.marks > 60:
            print("Pass")
        elif self.marks <= 60:
            print("Fail")

obj = Manage()
obj.display_Marks()
obj.claulate()
