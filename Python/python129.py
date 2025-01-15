from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)
    
    def speak(self):
        print(f"{self.name} is barking")

d=Dog("Rover", 3, "Street Dog")
d.speak()
