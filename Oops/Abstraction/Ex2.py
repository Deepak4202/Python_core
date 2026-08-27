import abc
from abc import abstractclassmethod,ABC,abstractmethod

class A(ABC):
    #old method process
    @abstractclassmethod
    def speed(cls):
        pass
    # new process
    @classmethod
    @abstractmethod
    def speed2(cls):
        pass

class B(A):
    def speed2(cls):
        print("Speed 2")

    def speed(cls):
        print("Over speed")



B.speed(B)
B.speed2(B)


print(A.__abstractmethods__)