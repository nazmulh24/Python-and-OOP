class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name: {self.name}, price: {self.price})"


myProduct = Product("Pen", 10)
print(myProduct)

myProduct = Product("Book", 40)
print(myProduct)

# -----------------------------------------------------------------------------


class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Shop --> name: {self.name}, address: {self.address}"


myShop = Shop("naz", "Dhaka")
print(myShop)
