class Course:
    def fee(self, n):
        match n:
            case 1:
                return "Python", 5000
            case 2:
                return "Java", 6000
            case 3:
                return "Data Science", 8000
            case _:
                return None


class Academy(Course):

    def courses(self):
        print("=" * 50)
        print("\tAvailable Courses")
        print("=" * 50)
        print("""
1. Python        -------- ₹5000
2. Java          -------- ₹6000
3. Data Science  -------- ₹8000
""")

    def enroll(self):
        self.values = []
        self.total = 0

        while True:
            self.courses()

            item = int(input("Select the course (1/2/3): "))

            course = self.fee(item)

            if not course:
                print("Invalid Choice")
                continue

            self.values.append(course)
            self.total += course[1]

            ch = input("Do you want to enroll in another course (y/n): ")
            if ch.lower() == 'n':
                break

        self.billing()

    def billing(self):
        print("\n" + "-" * 50)
        print("BILL")
        print("-" * 50)

        for i in self.values:
            print(f"{i[0]} -------- Rs{i[1]}")

        print("-" * 50)
        print(f"Course Fee        : Rs{self.total}")

        registration_fee = 100
        print(f"Registration Fee  : Rs{registration_fee}")

        print("-" * 50)
        print(f"Grand Total       : Rs{self.total + registration_fee}")
        print("-" * 50)


class Student(Academy):
    pass


obj = Student()
obj.enroll()