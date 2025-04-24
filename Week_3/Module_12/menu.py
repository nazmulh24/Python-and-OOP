from food_item import FoodItem


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def find_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted...")
        else:
            print("Item Not Found...")

    def update_item(self, name, new_price):
        item = self.find_item(name)
        if item:
            item.price = new_price
            print("Item Updated...")
        else:
            print("Item Not Found...")

    def show_menu(self):
        if not self.items:
            print("Menu is empty!")
        else:
            print("------ Show Menu Items ------")
            print("Name\t\tPrice")
            for item in self.items:
                print(f"{item.name}\t\t{item.price:.2f}")
