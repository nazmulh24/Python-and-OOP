"""
Explain the difference between inheritance and composition with proper examples.
"""


# Inheritance Example
class Animal:
    def speak(self):
        return "I make a sound"


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"


# Composition Example
class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, engine):
        self.engine = engine  # Car has an Engine

    def start(self):
        return self.engine.start()


# Demonstration
# Inheritance
dog = Dog()
print(dog.speak())  # Output: Woof!

# Composition
engine = Engine()
car = Car(engine)
print(car.start())  # Output: Engine started
