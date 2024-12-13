from datetime import datetime
from save_all_books import save_all_books_json, save_all_borrower

def borrow_book(all_books, borrowers_info):
    print("\n--- Borrow Book ---")
    book_title = input("Enter the title of the book to borrow: ")
    borrower_name = input("Enter your name: ")
    borrower_phone = input("Enter your phone number: ")

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                borrow_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                borrowers_info.append({
                    "name": borrower_name,
                    "phone": borrower_phone,
                    "book_title": book["title"],
                    "borrow_time": borrow_time
                })
                print(f"\nBook '{book['title']}' has been borrowed successfully!")
                print(f"Borrower: {borrower_name}, Phone: {borrower_phone}, Borrow Time: {borrow_time}")
                save_all_books_json(all_books)
                save_all_borrower(borrowers_info)
                return borrowers_info
            else:
                print(f"\nSorry, the book '{book['title']}' is out of stock.")
                return borrowers_info

    print("\nBook not found.")
    return borrowers_info

def return_book(all_books, borrowers_info):
    print("\n--- Return Book ---")
    borrower_name = input("Enter your name: ")
    borrower_phone = input("Enter your phone number: ")
    book_title = input("Enter the title of the book to return: ")

    for borrower in borrowers_info:
        if (borrower["name"].lower() == borrower_name.lower() and
                borrower["phone"] == borrower_phone and
                borrower["book_title"].lower() == book_title.lower()):

            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    break

            return_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            borrowers_info.remove(borrower)
            print(f"\nBook '{book_title}' has been returned successfully!")
            print(f"Return Time: {return_time}")
            save_all_books_json(all_books)
            save_all_books_json(borrowers_info)
            return borrowers_info

    print("\nBorrower or book information not found.")
    return borrowers_info