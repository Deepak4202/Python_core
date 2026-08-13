class MobileRecharge:
    def recharge_plans(self):
        print("1. unlimited calls, 100 msg for 28days ---299")
        print("2. unlimited calls, 400 msg for 56days ---499")
        print("3. unlimited calls, unlimited msg for 84days ---999")
        print("4. unlimited calls, unlimited msg for 28days ---399")
        self.mobile_recharge()

    def mobile_recharge(self):
        print("Enter your choice ")
        op = int(input())
        if op == 1:
            print("Your recharge for 299 is successfully")
        elif op == 2:
            print("Your recharge for 499 is successfully")
        elif op == 3:
            print("Your recharge for 999 is successfully")
        elif op == 4:
            print("Your recharge for 399 is successfully")


class BusTicketBooking:
    def display_buses(self):
        print("1.APSRTC route Tirupati to Nellore --- 1000")
        print("2.TSRTC route  Hyderabad to Nampally --- 15")
        print("3.Sambaiah Travels route KPHB to vinukonda --- 999")
        print("4.pallavi Prasanth Travels route Tilak Nagar to KPHB --- 99")

        self.book_ticket()
    def book_ticket(self):
        n = int(input("Enter your choice : "))

        if n ==1:
            print("APSRTC route Tirupati to Nellore --- 1000")
            print("Bus Booked successfully")
        elif n ==2:
            print("TSRTC route  Hyderabad to Nampally --- 15")
            print("Bus Booked successfully")
        elif n ==3:
            print("Sambaiah Travels route KPHB to vinukonda --- 999")
            print("Bus Booked successfully")
        elif n ==4:
            print("pallavi Prasanth Travels route Tilak Nagar to KPHB --- 99")
            print("Bus Booked successfully")

class ElectricityBills():
    def bill_details(self):
        print("1.APSPDCL")
        print("2.TSSPDCL")
        print("3.CESS")
        self.pay_bill()
    def pay_bill(self):
        n = int(input("Enter your choice : "))

        if n == 1:
            print("APSPDCL")
            print("payed  successfully")
        elif n == 2:
            print("TSSPDCL route  Hyderabad to Nampally --- 15")
            print("payed  successfully")
        elif n == 3:
            print("CESS")
            print("payed  successfully")


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):
    def menu(self):
        print("Available Services:")
        print("1.Mobile Recharge")
        print("2.Bus Ticket Booking")
        print("3.Electricity Bill")

    def services(self):
        self.menu()
        choice = int(input())
        if choice == 1:
            MobileRecharge().recharge_plans()
        elif choice == 2:
            BusTicketBooking().display_buses()
        elif choice == 3:
            ElectricityBills().bill_details()
        else:
            print("Invalid Option")


a = Paytm()
a.services()