import json
import os

FILE = "library.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_book(data):
    book_id = input("Book ID: ").strip()
    if book_id in data:
        print("Book ID already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    data[book_id] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None
    }
    save_data(data)
    print("Book added.")

def search_book(data):
    key = input("Search by title/author/ID: ").lower()
    found = False
    for bid, info in data.items():
        if key in bid.lower() or key in info["title"].lower() or key in info["author"].lower():
            status = "Available" if info["available"] else f"Borrowed by {info['borrower']}"
            print(f"{bid} | {info['title']} | {info['author']} | {status}")
            found = True
    if not found:
        print("No matching book found.")

def borrow_book(data):
    bid = input("Book ID: ").strip()
    if bid not in data:
        print("Book not found.")
        return
    if not data[bid]["available"]:
        print("Book already borrowed.")
        return
    name = input("Borrower name: ").strip()
    data[bid]["available"] = False
    data[bid]["borrower"] = name
    save_data(data)
    print("Book borrowed.")

def return_book(data):
    bid = input("Book ID: ").strip()
    if bid not in data:
        print("Book not found.")
        return
    if data[bid]["available"]:
        print("Book is not borrowed.")
        return
    data[bid]["available"] = True
    data[bid]["borrower"] = None
    save_data(data)
    print("Book returned.")

def show_all(data):
    if not data:
        print("No books in library.")
        return
    for bid, info in data.items():
        status = "Available" if info["available"] else f"Borrowed by {info['borrower']}"
        print(f"{bid} | {info['title']} | {info['author']} | {status}")

def main():
    data = load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("0. Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1":
            add_book(data)
        elif choice == "2":
            search_book(data)
        elif choice == "3":
            borrow_book(data)
        elif choice == "4":
            return_book(data)
        elif choice == "5":
            show_all(data)
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


# The Library Management System is designed to perform basic CRUD operations—adding books, searching for books, borrowing books, and returning books—through a console-based interface. The system uses a JSON file as a lightweight database to store book records permanently. This ensures that the data remains available even after the program is closed. The core logic is structured around simple dictionary operations, user inputs, and file handling.

# The program begins by defining a file name that will store the data. The first step in the system is loading existing records. A function is used to check whether the JSON file exists; if it does, the file is opened and its contents are parsed into a Python dictionary. If the file doesn’t exist or contains invalid data, an empty dictionary is returned. This dictionary becomes the main in-memory storage during the program's execution. Any time changes are made to the data, a separate function writes the entire dictionary back into the JSON file. This ensures synchronization between memory and file storage.

# Adding a book is performed by collecting a unique book ID, title, and author from the user. The system first checks whether the provided book ID already exists in the dictionary to prevent duplication. If the ID is new, the program creates a dictionary entry containing the title, author, availability status, and borrower information. The availability is initially set to true, indicating that the book can be borrowed. Once the new book is added to the in-memory dictionary, the JSON file is updated to store the new entry permanently.

# Searching for a book uses keyword matching across book ID, title, and author fields. The user enters a search term, which is converted to lowercase to make the search case-insensitive. The program loops through all stored books and prints the details of any book where the search term appears in its ID, title, or author fields. If no matches are found, an appropriate message is displayed. This logic allows flexible searching rather than requiring exact matches.

# Borrowing a book involves checking whether a book exists and whether it is currently available. Once the user enters a book ID, the system verifies the ID. If the book exists but is already borrowed, the user is informed that the book is unavailable. If the book is available, the system asks for the borrower’s name, changes the availability status to false, records the borrower’s name, and saves the updated data to the file.

# Returning a book is the reverse process. The program checks whether the book exists and whether it is currently borrowed. If the book is already marked as available, the system informs the user that it does not need to be returned. Otherwise, the availability is set back to true and the borrower information is cleared.

# All actions are presented through a simple console menu. The menu loops continuously until the user selects the exit option, making the system easy to use for repeated operations.