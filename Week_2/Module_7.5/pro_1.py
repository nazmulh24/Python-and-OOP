class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --> Operator Overloading: Redefining the behavior of the '+' operator for the Point class
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # --> Method Overriding: Redefining the __str__ method to customize string representation
    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # Uses the __add__ method
print(p3)  # Output: (4, 6) - Uses the overridden __str__ method
