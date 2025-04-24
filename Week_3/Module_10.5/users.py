from abc import ABC
from product import Product


class User(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []

    def place_order(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.orders.append((product, quantity))
            print(f"Order placed for {quantity} of {product.name}")
        else:
            print(f"Sorry, {product.name} is out of stock.")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def publish_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        print(f"Product {name} published with stock {stock}.")
        return product
