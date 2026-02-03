books = [
    {"book_id": 1, "name": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"book_id": 2, "name": "Pride and Prejudice", "author": "Jane Austen"}
]

def display_book_details(book):
    print(f"  ID: {book['book_id']}, Name: {book['name']}, Author: {book['author']}")

def view_all_books():
    if not books:
        print("The book list is currently empty.")
    else:
        print("\n--- Current Book Inventory ---")
        for book in books:
            display_book_details(book)
        print("------------------------------")

def add_book():
    try:
        book_id = int(input("Enter Book ID: "))
        for book in books:
            if book['book_id'] == book_id:
                print(f"Error: Book with ID {book_id} already exists.")
                return
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        new_book = {"book_id": book_id, "name": name, "author": author}
        books.append(new_book)
        print(f"Book '{name}' added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numerical Book ID.")
def update_book():
    try:
        book_id = int(input("Enter the Book ID to update: "))
        found = False
        for book in books:
            if book['book_id'] == book_id:
                found = True
                print(f"Found book: {book['name']}. Enter new details (leave blank to keep current value).")
                new_name = input(f"Enter new Name ({book['name']}): ")
                new_author = input(f"Enter new Author ({book['author']}): ")

                if new_name:
                    book['name'] = new_name
                if new_author:
                    book['author'] = new_author
                print(f"Book ID {book_id} updated successfully!")
                break
        if not found:
            print(f"Error: Book with ID {book_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical Book ID.")

def search_books():
    """Searches for books by name or author."""
    search_term = input("Enter book name or author to search: ").lower()
    results = [book for book in books if search_term in book['name'].lower() or search_term in book['author'].lower()]

    if not results:
        print(f"No books found matching '{search_term}'.")
    else:
        print(f"\n--- Search Results for '{search_term}' ---")
        for book in results:
            display_book_details(book)
        print("------------------------------------------")

def delete_book():
    """Deletes a book from the inventory."""
    try:
        book_id = int(input("Enter the Book ID to delete: "))
        global books
        initial_count = len(books)
        books = [book for book in books if book['book_id'] != book_id]

        if len(books) < initial_count:
            print(f"Book ID {book_id} deleted successfully.")
        else:
            print(f"Error: Book with ID {book_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical Book ID.")

def menu():
    """Displays the menu and handles user choices."""
    while True:
        print("\n===== Book Management System Menu =====")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Search for a book")
        print("5. Delete a book")
        print("6. Exit")
        print("=======================================")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_all_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()
