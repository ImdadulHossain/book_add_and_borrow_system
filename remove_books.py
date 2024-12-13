from save_all_books import save_all_books_json

def remove_book(all_books):
    search_book = input("Enter the name of the book to remove: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books_json(all_books)
            print("Book removed")
            return all_books

    print("Book not found")


