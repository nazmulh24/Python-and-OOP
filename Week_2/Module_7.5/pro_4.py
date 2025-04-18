class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age  # Protected attribute

    # --> Using property decorators for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Invalid name")

    # --> Normal getter and setter for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Invalid age")


person = Person("Nazmul", 22)

print(person.name)
print(person.get_age())

person.name = "Hossain"
person.set_age(23)

print(person.name)
print(person.get_age())
