"""

Project Name --> Library Management System
******* This is my 1st Python Project with OOP

"""


class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__availability

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        self.__availability = True

    def view_book_info(self):
        print(
            f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {'Available' if self.__availability else 'Not Available'}"
        )


Book("B001", "Amar Bondhu Rashed", "Muhammed Zafar Iqbal")
Book("B002", "Pather Panchali", "Bibhutibhushan Bandyopadhyay")
Book("B003", "Padma Nadir Majhi", "Manik Bandopadhyay")
Book("B004", "Lalsalu", "Syed Waliullah")
Book("B005", "Shesher Kobita", "Rabindranath Tagore")
Book("B006", "Chander Pahar", "Bibhutibhushan Bandyopadhyay")
Book("B007", "Debdas", "Sarat Chandra Chattopadhyay")
Book("B008", "Abar Jodi Ichha Koro", "Humayun Ahmed")
Book("B009", "Nondito Noroke", "Humayun Ahmed")
Book("B010", "Kobi", "Tarashankar Bandopadhyay")
Book("B011", "Titash Ekti Nadir Naam", "Adwaita Mallabarman")
Book("B012", "Banglar Mukh", "Jasimuddin")
Book("B013", "Hajar Bochor Dhore", "Zahir Raihan")
Book("B014", "Surjo Dighal Bari", "Abu Ishaque")
Book("B015", "Gitanjali", "Rabindranath Tagore")

while True:
    print(
        """
---- Welcome to the Library ----
1. View All Books
2. Borrow Book
3. Return Book
4. Exit"""
    )
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nList of Books:")
        for book in Library.book_list:
            book.view_book_info()

    elif choice == "2":
        book_id = input("Enter the Book ID to borrow: ").lower()
        for book in Library.book_list:
            if book.get_book_id().lower() == book_id:
                if book.borrow_book():
                    print(f"Book: '{book.get_title()}' borrowed successfully.")
                else:
                    print("Book is not available.")
                break
        else:
            print("Book ID not found.")

    elif choice == "3":
        book_id = input("Enter the Book ID to return: ").lower()
        for book in Library.book_list:
            if book.get_book_id().lower() == book_id:
                if not book.is_available():
                    book.return_book()
                    print(f"Book: '{book.get_title()}' returned successfully.")
                else:
                    print(f"Book: '{book.get_title()}' was not borrowed.")
                break
        else:
            print("Book ID not found.")

    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
