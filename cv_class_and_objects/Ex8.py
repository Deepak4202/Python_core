# 8.	Create a class MovieTicket.
# Write a static method ticket_price(age).
# Rules Age below 12 → ₹100,
# Age between 12 and 60 → ₹200 ,
# Age above 60 → ₹150 , Return the ticket price.

class MovieTicket:

    @staticmethod
    def ticket_price(age):
        if age in range(1,12+1):
            print("₹100")
        elif age in range(12,60):
            print("₹200")
        elif age in range(60,150):
            print("₹150")

MovieTicket.ticket_price(11)
MovieTicket().ticket_price(15)
MovieTicket().ticket_price(61)