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

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(
                    f"Congratulations! You have successfully bought '{product_name}'."
                )
                return
        print(f"Sorry, the product '{product_name}' is not available in the shop.")

    def __repr__(self):
        return f"Shop --> name: {self.name}, address: {self.address}\nproducts: {self.products})"


myShop = Shop("naz", "Dhaka")
myShop.add_product(Product("Pen", 10))
myShop.add_product(Product("Book", 50))
# print(myShop)
myShop.buy_product("Pen")
myShop.buy_product("Laptop")
print(myShop)
