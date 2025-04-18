"""

# 1. Class methods take `cls` as the first parameter, while static methods do not.
class Example:
    @classmethod
    def class_method(cls):
        return f"This is a class method. cls: {cls}"

    @staticmethod
    def static_method():
        return "This is a static method."


print(Example.class_method())  # Accesses the class
print(Example.static_method())  # Does not access the class

"""

""" 

# 2. Class methods can modify class state, while static methods cannot.
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def display_message():
        return "Static methods cannot modify class state."


Counter.increment()
print(Counter.count)  # Output: 1
print(Counter.display_message())

"""

""" 

# 3. Class methods are bound to the class, while static methods are not bound to anything.
class BoundExample:
    @classmethod
    def class_bound(cls):
        return f"Bound to class: {cls}"

    @staticmethod
    def not_bound():
        return "Not bound to class or instance."


print(BoundExample.class_bound())
print(BoundExample.not_bound())

"""

""" 

# 4. Class methods can be used as factory methods, while static methods are utility methods.
class FactoryExample:
    def __init__(self, value):
        self.value = value

    @classmethod
    def create_instance(cls, value):
        return cls(value)

    @staticmethod
    def utility_function(x, y):
        return x + y


instance = FactoryExample.create_instance(10)
print(instance.value)  # Output: 10
print(FactoryExample.utility_function(5, 7))  # Output: 12

"""
