class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items ordered yet.")
        else:
            print("\nYour Order:")
            for item in self.items:
                print(f"{item.name} -> ${item.price:.2f}")
            print(f"Total: ${self.total_price():.2f}")
