

restaurant_management_system/
            │
            ├── main.py              # Entry point of the program
            ├── food_item.py         # Defines the FoodItem class
            ├── menu.py              # Manages the list of food items
            ├── orders.py            # Manages a customer's order
            ├── restaurant.py        # Handles customers and the restaurant menu
            └── users.py             # Abstract User class + Admin and Customer



            Diagram----------->

                                             ┌──────────────────────────────┐
                                             │       main.py (Entry)        │
                                             └────────────┬─────────────────┘
                                                          │
                                                          ▼
                                                  User Chooses Role:
                                                 ┌────────────────────┐
                                                 │ Admin or Customer? │
                                                 └─────────┬──────────┘
                                                           │
                                                ┌──────────▼───────────┐
                                                │   Admin (Admin Class)│
                                                └─────────┬────────────┘
                                                          │
                                 ┌───────────────────────▼────────────────────────────────┐
                                 │ Admin Actions:                                         │
                                 │ 1. Add/Remove Customer → restaurant.customers          │
                                 │ 2. View Customers       → restaurant.view_customers()  │
                                 │ 3. Manage Menu:                                        │
                                 │    ├── Add/Remove/Update Menu Items                    │
                                 │    └── View Menu                                       │
                                 └────────────────────────────────────────────────────────┘
                                                           │
                                                           ▼
                                             ┌──────────────────────────┐
                                             │Customer (Customer class) │
                                             └─────────────┬────────────┘
                                                           │
                              ┌────────────────────────────▼──────────────────────────────────┐
                              │ Customer Actions:                                             │
                              │ 1. View Menu              → menu.show_menu()                  │
                              │ 2. Add Balance            → self.balance                      │
                              │ 3. Place Order            → self.orders.add_item(FoodItem)    │
                              │ 4. View Orders            → self.orders.show_order()          │
                              └───────────────────────────────────────────────────────────────┘
                                                             │
                                                             ▼
                                                ┌────────────────────────────┐
                                                │      restaurant.py         │
                                                │  - Holds Menu & Customers  │
                                                └────────┬─────────┬─────────┘
                                                         │         │
                                                         ▼         ▼
                                               ┌──────────────┐ ┌──────────────────────────┐
                                               │  menu.py     │ │   customers (list)       │
                                               │  └── items[] │ └── Customer instances     │
                                               │      ▲       │                            │
                                               │      │       └─────────────┬──────────────┘
                                               │      │                     ▼
                                               │      └── FoodItem(name, price) ← food_item.py
                                               └────────────────────────────┘

                                             Orders are managed per customer:
                                             ┌──────────────────────┐
                                             │ orders.py (per user) │
                                             └──────────┬───────────┘
                                                        ▼
                                               - add_item(FoodItem)
                                               - total_price()
                                               - show_order()


