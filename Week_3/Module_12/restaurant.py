from menu import Menu


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_customer(self, customer):
        if self.find_customer(customer.email):
            print("Customer with this email already exists...")
        else:
            self.customers.append(customer)

    def remove_customer(self, email):
        self.customers = [c for c in self.customers if c.email != email]

    def find_customer(self, email):
        for c in self.customers:
            if c.email.lower() == email.lower():
                return c
        return None

    def view_customers(self):
        if not self.customers:
            print("No customers registered...")
        else:
            print("--- Customer Info ---")
            print("Name:\t\t\tEmail:\t\t\tAddress:")
            for c in self.customers:
                print(f"{c.name}\t\t\t{c.email}\t\t{c.address}")
