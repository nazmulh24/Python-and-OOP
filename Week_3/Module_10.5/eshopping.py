from users import Customer, Seller


class EShopping:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def register_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        print(f"Customer account created for {email}.")

    def register_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        print(f"Seller account created for {email}.")

    def login_user(self, email, password):
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                return customer
        for seller in self.sellers:
            if seller.email == email and seller.password == password:
                return seller
        return None

    def list_products(self):
        print("Available Products:")
        for product in self.products:
            if product.stock > 0:
                print(f"{product.name} - ${product.price} - Stock: {product.stock}")

    def add_product(self, product):
        self.products.append(product)
