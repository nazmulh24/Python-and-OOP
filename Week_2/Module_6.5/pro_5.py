"""

What are Encapsulation and Access Modifiers? Explain with examples

"""


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # --> Public attribute
        self._balance = balance  # --> Protected attribute
        self.__pin = "1234"  # --> Private attribute

    # --> Public method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Invalid deposit amount.")

    # --> Protected method
    def _check_balance(self):
        return self._balance

    # --> Private method
    def __valid_pin(self, pin):
        return pin == self.__pin

    # --> Public method to access private method
    def withdraw(self, amount, pin):
        if self.__valid_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. New balance is {self._balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid PIN.")


account = BankAccount("Nazmul", 1000)

# --> Accessing public method
account.deposit(500)

# --> Accessing protected method (not recommended)
print("Balance (protected):", account._check_balance())

# --> Accessing private method (not allowed directly)
# account.__validate_pin("1234")  # --> This will raise an AttributeError

# --> Using public method to withdraw
account.withdraw(300, "1234")
account.withdraw(300, "0000")
