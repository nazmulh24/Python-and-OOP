from users import Customer, Seller
from eshopping import EShopping

# app = EShopping()

# # Register a seller and add products
# app.register_seller("seller@example.com", "123")
# seller = app.sellers[0]
# seller.publish_product("Laptop", 1000, 10)
# seller.publish_product("Phone", 500, 5)
# for product in seller.products:
#     app.add_product(product)

# # Register a customer and place orders
# app.register_customer("customer@example.com", "123")
# customer = app.customers[0]
# app.list_products()
# customer.place_order(app.products[0], 2)
# app.list_products()


def main_menu():
    print(
        """
Welcome to E-Shopping App
1. Customer Sign Up
2. Seller Sign Up
3. Login
4. Exit\n"""
    )


def run_app():
    app = EShopping()

    app.register_seller("admin@admin.com", "admin")
    seller = app.sellers[-1]
    initial_products = [
        ("Walton Laptop", 55000, 5),
        ("Symphony Phone", 8500, 10),
        ("Samsung TV", 70000, 3),
        ("Jamuna Refrigerator", 42000, 4),
        ("Singer Washing Machine", 30000, 2),
        ("Vision Blender", 2800, 8),
        ("Nova Trimmer", 1100, 15),
        ("Walton Microwave Oven", 9500, 3),
        ("Marcel Air Conditioner", 45000, 2),
        ("Realme Phone", 14000, 6),
    ]
    for name, price, stock in initial_products:
        product = seller.publish_product(name, price, stock)
        app.add_product(product)

    while True:
        main_menu()
        choice = input("Select an option : ")
        if choice == "1":
            email = input("Enter Customer E-mail: ")
            password = input("Enter Customer password: ")
            app.register_customer(email, password)

        elif choice == "2":
            email = input("Enter Seller E-mail: ")
            password = input("Enter Seller password: ")
            app.register_seller(email, password)

        elif choice == "3":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = app.login_user(email, password)

            if user:
                print(f"Login successful! Welcome, {email}")
                if isinstance(user, Customer):
                    while True:
                        # app.list_products()
                        for i, product in enumerate(app.products):
                            if product.stock > 0:
                                print(
                                    f"{i}. {product.name} - ${product.price} - Stock: {product.stock}"
                                )

                        buy = input("Would you like to place an order? (y/n): ").lower()
                        if buy == "y":
                            index = int(input("Enter product index to buy: "))
                            quantity = int(input("Enter quantity: "))
                            if 0 <= index < len(app.products):
                                user.place_order(app.products[index], quantity)
                            else:
                                print("Invalid product index.")
                        else:
                            break
                elif isinstance(user, Seller):
                    while True:
                        action = input("Add a new product? (y/n): ").lower()
                        if action == "y":
                            name = input("Product name: ")
                            price = float(input("Price: "))
                            stock = int(input("Stock: "))
                            product = user.publish_product(name, price, stock)
                            app.add_product(product)
                        else:
                            break
            else:
                print("Invalid email or password.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Option...try again...")


if __name__ == "__main__":
    run_app()
