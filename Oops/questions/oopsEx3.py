# 3. Create a Food Delivery System using all four OOP concepts.
# Requirements:
# Create an abstract class FoodOrder.
# It should contain:
# •	Private variables __order_id, __customer_name, and __amount
# •	Properties for accessing and modifying these values
# •	Abstract method calculate_delivery_charge()
# Create child classes:
# •	SwiggyOrder
# •	ZomatoOrder
# •	RestaurantOrder
# Each class should implement calculate_delivery_charge() differently.

from abc import ABC,abstractmethod

class FoodOrder(ABC):
    def __init__(self):
        self.__ide = 1
        self.__customer_name = "Deepak"
        self.__amount = 200


    @property
    def ide(self):
        return self.__ide

    @ide.setter
    def ide(self,ide):
        self.__ide =ide


    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self,name):
        self.__customer_name = name

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,amount):
        self.__amount =amount


