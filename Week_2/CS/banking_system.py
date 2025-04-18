# BanKing System


from abc import ABC, abstractmethod


class Account(ABC):
    account = []

    def __init__(self, name, acc_no, password, type):
        self.name = name
        self.acc_no = acc_no
        self.password = password
        self.type = type
        self.balance = 0

        Account.account.append(self)

    def cng_Info(self, newName=None, newPass=None):
        if newName:
            self.name = newName
        if newPass:
            self.password = newPass
        print(f"Name: {self.name}")
        print(f"Pass: {self.password}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount

    @abstractmethod
    def showInfo(self):
        pass


class Saving_Acc(Account):
    def __init__(self, name, acc_no, password, inter):
        super().__init__(name, acc_no, password, "savings")

        self.inter = inter

    def showInfo(self):
        print(f"Account Name: {self.name}")
        print(f"Account Type: {self.type}")


class Spacial_Acc(Account):
    def __init__(self, name, acc_no, password, limit):
        super().__init__(name, acc_no, password, "spacial")

        self.limit = limit

    def showInfo(self):
        print(f"Account Name: {self.name}")
        print(f"Account Type: {self.type}")

    # --> Method Overwrite
    def withdraw(self, amount):
        if amount > 0 and amount <= self.limit and self.balance >= amount:
            self.balance -= amount


myAcc = Saving_Acc("Nazmul", 123, "1qaz", 5)

# myAcc.cng_Info("nazmul")
# myAcc.cng_Info("nazmul", 12)


print("===== TESTING ENCAPSULATION =====")
print(f"Name: {myAcc.name}, Acc No: {myAcc.acc_no}, Balance: {myAcc.balance}")
myAcc.deposit(1000)
print(f"Balance after deposit: {myAcc.balance}")
myAcc.withdraw(200)
print(f"Balance after withdraw: {myAcc.balance}")

print("\n===== TESTING ABSTRACTION =====")
myAcc.showInfo()

print("\n===== TESTING INHERITANCE =====")
print("Is myAcc an Account? ->", isinstance(myAcc, Account))
print("Is myAcc a Saving_Acc? ->", isinstance(myAcc, Saving_Acc))

print("\n===== TESTING POLYMORPHISM =====")
specialAcc = Spacial_Acc("Abir", 456, "2wsx", 300)
specialAcc.deposit(1000)
print(f"Before withdraw: {specialAcc.balance}")
specialAcc.withdraw(250)
print(f"After withdraw (within limit): {specialAcc.balance}")
specialAcc.withdraw(400)  # Over limit
print(f"After withdraw (over limit): {specialAcc.balance}")

print("\n===== TESTING METHOD OVERLOADING (Simulated via Defaults) =====")
myAcc.cng_Info("Nazmul Islam")  # Only name
myAcc.cng_Info(newPass="newpass123")  # Only password
myAcc.cng_Info("N Hossain", "finalPass123")  # Both
