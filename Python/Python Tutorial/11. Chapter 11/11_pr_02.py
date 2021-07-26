# Create a class pets from a class animals and further create class Dog from pets . Add a method bark to class Dog.

class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")

d  = Dog()
d.bark()