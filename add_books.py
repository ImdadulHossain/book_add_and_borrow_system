from save_all_books import save_all_books_json
import random
from datetime import datetime
from valid_input import safe_input


def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = safe_input("Enter Publishing Year Number: ")
    price = safe_input("Enter Book Price: ")
    quantity = safe_input("Enter Quantity Number: ")


    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        'BookAddedAt': bookAddedAt,
    }

    all_books.append(book)
    save_all_books_json(all_books)

    print("Books Added Successully")

    return all_books
