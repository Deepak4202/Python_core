# 2. Movie Ticket Booking System Using Multilevel Inheritance
# Class 1: Movie
# •	Create a method ticket(movie) that returns the ticket price.
# Class 2: Booking (inherits Movie)
# Create the following methods:
# •	movies() – Display the available movies.
# •	selection() – Allow the user to book multiple tickets.
# •	billing() – Display the total amount and add a booking charge of ₹30.
# Class 3: Customer (inherits Booking)
# •	Create an object and call the selection() method.

class Movie:
    def ticket(self,n):
        match n:
            case 1:
                return "Spyder man" , 350
            case 2:
                return "Dragon" , 400
            case 3:
                return "Devara" ,300
            case _:
                return None

class Booking(Movie):
    def movies(self):
        print("\t\t\t","="*50)
        print("\t\t\t\t\t\tMovies")
        print("\t\t\t","=" * 50)
        print("""
                1. Spyder man ---------------- Rs350
                2. Dragon     ---------------- Rs400
                3. Devara     ---------------- Rs300
                """)

    def selection(self):
        self.values = []
        self.total = 0
        while True:

            self.movies()
            self.item = int(input("Select the movie 1/2/3: "))
            if self.item not in [1,2,3]:
                print("Invalid input")
                continue
            self.NoofTickets = int(input("Number of tickets you want : "))

            self.a = self.ticket(self.item)

            if not self.a:
                print("Invalid Input")
                continue

            self.values.append((self.a[0], self.NoofTickets, self.a[1]))
            self.total += self.a[1] * self.NoofTickets

            ch = input("If you want to book another ticket y/n")
            if ch.lower() == 'n':
                break
        self.billing()

    def billing(self):

        print("-" * 50)
        print("Bill")
        print("-" * 50)

        for i in self.values:
            print(f"{i[0]}  {i[1]} x {i[2]} = {i[1] * i[2]}")

        print("-" * 50)
        print(f"Ticket Amount : ₹{self.total}")

        booking_charge = 30
        print(f"Booking Charge : ₹{booking_charge}")

        print("-" * 50)
        print(f"Grand Total : ₹{self.total + booking_charge}")
        print("-" * 50)


class Customer(Booking):

    pass

obj = Customer()
obj.selection()