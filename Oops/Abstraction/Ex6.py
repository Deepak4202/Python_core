# 2. Notification System
# Create an abstract class Notification with:
# send(message)
# Create:
# •	Email
# •	SMS
# •	WhatsApp
# Each child class should implement send() differently.


from  abc import ABC ,abstractmethod

class Notification(ABC):

    @abstractmethod
    def message(self):
        pass

class Email(Notification):

    def message(self):

        print("From Email")

class Sms(Notification):

    def message(self):

        print("From sms")

class WhatsApp(Notification):

    def message(self):

        print("From WhatsApp")


obj = Email()
obj.message()

obj1 = Sms()
obj1.message()

obj3 = WhatsApp()
obj3.message()