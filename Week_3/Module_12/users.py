from abc import ABC
from orders import Order


class User(ABC):
    def __init__(self, name):
        self.name = name


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name)
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = Order()

    def add_funds(self, amount):
        if amount <= 0:
            print("Amount must be positive...")
        else:
            self.balance += amount
            print(f"${amount:.2f} added to your balance...")

    def check_balance(self):
        print(f"Current balance : ${self.balance:.2f}")

    def view_menu(self, menu):
        menu.show_menu()

    def place_order(self, menu, item_name):
        item = menu.find_item(item_name)
        if item:
            if self.balance >= item.price:
                self.balance -= item.price
                self.orders.add_item(item)
                print(f"Ordered: {item.name}")
            else:
                print("Insufficient balance...")
        else:
            print("Item not found...")

    def view_orders(self):
        self.orders.show_order()


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def add_customer(self, restaurant, customer):
        restaurant.add_customer(customer)

    def remove_customer(self, restaurant, email):
        restaurant.remove_customer(email)

    def view_customers(self, restaurant):
        restaurant.view_customers()

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_menu_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def update_menu_item(self, restaurant, item_name, new_price):
        restaurant.menu.update_item(item_name, new_price)

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()
