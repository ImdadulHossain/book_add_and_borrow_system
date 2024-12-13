from add_books import add_books
from view_all_books import view_all_books
from remove_books import remove_book
from restore_books import restore_all_books, restore_all_borrower
from update_books import update_all_books
from borrow_system import borrow_book, return_book

all_books = []
borrowers_info = []


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Borrow Book")
    print("6. Return Book")

    all_books = restore_all_books()
    borrowers_info = restore_all_borrower()

    choice = input("Select any number: ")

    if choice == "0":
        print("Thanks for using Library Management System ")
        break
    elif choice == "1":
        all_books = add_books(all_books)
    elif choice == "2":
        view_all_books(all_books)
    elif choice == "3":
        update_all_books(all_books)
    elif choice == "4":
        remove_book(all_books)
    elif choice == "5":
        borrow_book(all_books, borrowers_info)
    elif choice == "6":
        return_book(all_books, borrowers_info)
    else:
        print("Choose a valid number")