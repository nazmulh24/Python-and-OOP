from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        # super().__init__()
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)

        if item is not None:
            item.quantity = quantity
            self.cart.add_item(item)
            print("Item added!!!")
        else:
            print("Item not found!!!")

    def view_cart(self):
        print("------- View Cart -------")

        print("Name\t\tPrice\t\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t\t{item.price}\t\t{quantity}")
        print(f"Total price: {self.cart.total_price}")


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)


# emp = Employee("Naz", 1234, "naz@gmail.com", "Dhaka", 22, "MD", 100000)
# print(emp.name)

# ad = Admin("Naz", 1234, "naz@gmail.com", "Dhaka")
# ad.add_employee("sagor", 212, "sagp@gmail.com", " Dhak", 23, "Wmpolur", 30000)
# ad.view_employee()


# mamar_res = Restaurent("Mamarresturent")
# mn = Menu()
# item = Food_Item("Pizza", 400, 1)
# item2 = Food_Item("Burger", 40, 20)
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# mn.show_menu()


# Customer1 = Customer("Rahim", 348, "bgg@gmail.com", "BD")
# Customer1.view_menu(mamar_res)
