class Book:
    def __init__(self, isbn, title, author, year):
        """
        Initialize a new Book instance.
        :param isbn: ISBN of the book
        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year of the book
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # Indicates whether the book is currently borrowed

    def __str__(self):
        """
        Return a string representation of the book's status.
        :return: String representation of the book
        """
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) - {status}"

class Library:
    def __init__(self):
        """
        Initialize a new Library instance with an empty book collection.
        """
        self.books = {}  # Dictionary to store books with ISBN as keys

    def add_book(self, isbn, title, author, year):
        """
        Add a new book to the library.
        :param isbn: ISBN of the book
        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year of the book
        """
        # Check if the book with this ISBN already exists
        if isbn in self.books:
            print(f"A book with ISBN {isbn} already exists in the library.")
            return
        
        # Create a new Book instance and add it to the library's collection
        book = Book(isbn, title, author, year)
        self.books[isbn] = book
        print(f"'{title}' by {author} ({year}) has been added to the library with ISBN {isbn}.")

    def view_books(self):
        """
        Display all books in the library.
        """
        # Check if there are any books in the library
        if not self.books:
            print("No books available in the library.")
        else:
            # Print each book's details
            for book in self.books.values():
                print(book)

    def borrow_book(self, isbn):
        """
        Borrow a book from the library.
        :param isbn: ISBN of the book to borrow
        """
        book = self.books.get(isbn)  # Retrieve the book using its ISBN
        if book:
            # Check if the book is already borrowed
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"'{book.title}' is currently borrowed.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def return_book(self, isbn):
        """
        Return a borrowed book to the library.
        :param isbn: ISBN of the book to return
        """
        book = self.books.get(isbn)  # Retrieve the book using its ISBN
        if book:
            # Check if the book was borrowed
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
            else:
                print(f"'{book.title}' was not borrowed.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

def main():
    """
    Main function to run the Library Management System.
    """
    library = Library()  # Create an instance of Library

    while True:
        # Display the menu options
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Gather book information from the user
            isbn = input("Enter ISBN: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            library.add_book(isbn, title, author, year)

        elif choice == '2':
            # Display all books in the library
            library.view_books()

        elif choice == '3':
            # Borrow a book by its ISBN
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            library.borrow_book(isbn)

        elif choice == '4':
            # Return a borrowed book by its ISBN
            isbn = input("Enter the ISBN of the book you want to return: ")
            library.return_book(isbn)

        elif choice == '5':
            # Exit the program
            print("Exiting the Library Management System.")
            break

        else:
            # Handle invalid choices if user enters another number beyond specified range
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()  # Run the main function to start the program
