# # # property
# # from abc import ABC, abstractmethod, abstractproperty, update_abstractmethods
# #
# #
# # class A(ABC):
# #     def __init__(self):
# #         self.salarys = 0
# #     @abstractproperty
# #     def salarys(self):
# #         pass
# #     @update_
# #     def update(self):
# #         pass
# # class B(A):
# #
# #     @property
# #     def salarys(self):
# #         return self.salarys
# #     @
# #     def update(self,amount):
# #         self.salarys = amount
# #
# #
# # obj = B()
# # print(obj.salarys)
# # obj.salarys = 20
# 
# 
# 
from abc import ABC, abstractproperty


class Employee(ABC):

    def get_salary(self):
        pass

    def set_salary(self, value):
        pass

    salarys = abstractproperty(get_salary, set_salary)


class Developer(Employee):

    def __init__(self):
        self._salary = 0

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = value

    salarys =property(get_salary, set_salary)
d = Developer()

# Setter
d.salarys = 50000

# Getter
print(d.salarys)

# 
# 
# from abc import ABC, abstractmethod
#
#
# class Employee(ABC):
#
#     @property
#     @abstractmethod
#     def salarys(self):
#         pass
#
#     @salarys.setter
#     @abstractmethod
#     def salarys(self, value):
#         pass
#
#
# class Developer(Employee):
#
#     def __init__(self):
#         self._salary = 0
#
#     @property
#     def salarys(self):
#         return self._salary
#
#     @salarys.setter
#     def salarys(self, value):
#         self._salary = value
#
#
# d = Developer()
#
# # Setter
# d.salarys = 50000
#
# # Getter
# print(d.salarys)