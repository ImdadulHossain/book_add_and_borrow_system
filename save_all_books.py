import json

def save_all_books_json(all_books):
    with open("all_books.json", "w") as fp:
        json.dump(all_books, fp, indent=4)

    print("Book updated successfully.")

def save_all_borrower(borrowers_info):
    with open("borrower_info.json", "w") as fp:
        json.dump(borrowers_info, fp, indent=4)

    print("Book updated successfully.")