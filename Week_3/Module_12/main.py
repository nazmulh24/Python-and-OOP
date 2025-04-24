from food_item import FoodItem
from users import Admin, Customer
from restaurant import Restaurant


restaurant = Restaurant("nam nai!!!")


def admin_menu(admin):
    while True:
        print(
            """
--- Admin Menu ---
1. Create Customer Account
2. Remove Customer Account
3. View All Customers
4. Manage Restaurant Menu
5. Exit
            """
        )

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name : ")
            email = input("Enter email : ")
            address = input("Enter address : ")
            customer = Customer(name, email, address)
            restaurant.add_customer(customer)
            print(f"Customer : {name} added successfully...")

        elif choice == "2":
            email = input("Enter email to remove : ")
            restaurant.remove_customer(email)
            print("Customer removed...")

        elif choice == "3":
            restaurant.view_customers()

        elif choice == "4":
            manage_menu(admin)

        elif choice == "5":
            break
        else:
            print("Invalid option!")


def customer_menu(customer):
    while True:
        # print(f"\n--- {customer.name}'s Menu ---")
        print(
            f"""
--- {customer.name}'s Menu ---
1. View Restaurant Menu
2. View Balance
3. Add Balance
4. Place Order
5. View Past Orders
6. Exit
            """
        )

        choice = input("Select an option: ")

        if choice == "1":
            customer.view_menu(restaurant.menu)

        elif choice == "2":
            customer.check_balance()

        elif choice == "3":
            amount = float(input("Enter amount to add : "))
            customer.add_funds(amount)

        elif choice == "4":
            item_name = input("Enter food name to order : ")
            customer.place_order(restaurant.menu, item_name)

        elif choice == "5":
            customer.view_orders()

        elif choice == "6":
            break
        else:
            print("Invalid option")


def manage_menu(admin):
    while True:
        print(
            """
--- Manage Restaurant Menu ---
1. Add Menu Item
2. Remove Menu Item
3. Update Menu Item
4. Show Menu
5. Exit
            """
        )

        choice = input("Select an option : ")

        if choice == "1":
            name = input("Enter food name : ")
            price = float(input("Enter price : "))
            item = FoodItem(name, price)
            # restaurant.menu.add_item(item)
            admin.add_menu_item(restaurant, item)

        elif choice == "2":
            name = input("Enter food name to remove : ")
            # restaurant.menu.remove_item(name)
            admin.remove_menu_item(restaurant, name)

        elif choice == "3":
            name = input("Enter food name to update : ")
            new_price = float(input("Enter new price : "))
            # restaurant.menu.update_item(name, new_price)
            admin.update_menu_item(restaurant, name, new_price)

        elif choice == "4":
            # restaurant.menu.show_menu()
            admin.show_menu(restaurant)

        elif choice == "5":
            break
        else:
            print("Invalid option!")


def main():
    while True:
        print(
            """
--- Restaurant Management System ---
1. Admin Login
2. Customer Login
3. Exit
            """
        )

        choice = input("Select an option : ")

        if choice == "1":
            name = input("Enter Admin Name : ")
            admin = Admin(name)
            print(f"\nWelcome Admin {admin.name}")
            admin_menu(admin)

        elif choice == "2":
            email = input("Enter Customer email : ")
            customer = restaurant.find_customer(email)
            if customer:
                customer_menu(customer)
            else:
                print("Customer not found...")

        elif choice == "3":
            print("\nExiting...\n")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
