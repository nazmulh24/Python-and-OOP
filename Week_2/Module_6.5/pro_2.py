class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name: {self.name}, price: {self.price})"


class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []  # --> List to store products

    def add_product(self, product):
        self.products.append(product)

    def __repr__(self):
        return f"Shop --> name: {self.name}, address: {self.address}\nproducts: {self.products})"


myShop = Shop("naz", "Dhaka")
myShop.add_product(Product("Pen", 10))
myShop.add_product(Product("Book", 50))
print(myShop)

yourShop = Shop("Youssss", "BD")
yourShop.add_product(Product("Ipad", 1000))
yourShop.add_product(Product("Mac", 50000))
print(yourShop)
