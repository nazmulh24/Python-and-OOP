class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print("Item deleted!!!")
        else:
            print("Item not found...")

    def show_menu(self):
        print("------- Show Menu Items -------")
        print("Name\t\tPrice\t\tQuantity")
        for item in self.items:
            print(f"{item.name}\t\t{item.price}\t\t{item.quantity}")
