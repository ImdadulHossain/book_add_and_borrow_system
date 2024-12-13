from datetime import datetime
from save_all_books import save_all_books_json
from valid_input import safe_input

def update_all_books(all_books):
    search_book = input("Enter the book name: ")
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = safe_input("Enter Publishing Year Number: ")
            price = safe_input("Enter Book Price: ")
            quantity = safe_input("Enter Quantity Number: ")

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["BookAddedAt"] = book_last_updated_at

            save_all_books_json(all_books)
            return all_books