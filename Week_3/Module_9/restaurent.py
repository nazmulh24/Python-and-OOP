from menu import Menu


class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []  # --> To store Employee
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added!!!")

    def view_employee(self):
        print("Employee List -->")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

    # def add_items(self, item):
    #     self.items.append(item)
