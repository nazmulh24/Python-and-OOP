"""

Inheritance is a feature in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class).
It promotes code reuse and establishes a relationship between classes.

"""


# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


# Child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


dog = Dog("Jack")
cat = Cat("Tom")

print(dog.speak())
print(cat.speak())
