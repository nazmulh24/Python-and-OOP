class Calculator:
    brand = "Casio MS990"

    def add(self, num1, num2):
        return num1 + num2

    def deduct(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2


my_calculator = Calculator()

result = my_calculator.add(4, 5)
result = my_calculator.deduct(4, 5)
result = my_calculator.multiply(4, 5)
result = my_calculator.divide(40, 5)

print(result)
