import json

def restore_all_books():
    with open('all_books.json', 'r') as f:
        all_books = json.load(f)
    return all_books

def restore_all_borrower():
    with open('borrower_info.json', 'r') as f:
        borrowers_info = json.load(f)
    return borrowers_info