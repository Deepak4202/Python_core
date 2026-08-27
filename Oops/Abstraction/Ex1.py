from  abc import ABC , abstractmethod

class  animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(animal):
    def sound(self):
        print("Bow Bow")

class Cat(animal):
    def sound(self):
        print("meow")


print(type(animal))
obj = Dog()
print(animal.sound.__isabstractmethod__)
print(animal.__abstractmethods__)

print(animal.__isabstractclass__)