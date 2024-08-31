class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) - {status}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        if isbn in self.books:
            print(f"A book with ISBN {isbn} already exists in the library.")
            return
        book = Book(isbn, title, author, year)
        self.books[isbn] = book
        print(f"'{title}' by {author} ({year}) has been added to the library with ISBN {isbn}.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books.values():
                print(book)

    def borrow_book(self, isbn):
        book = self.books.get(isbn)
        if book:
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"'{book.title}' is currently borrowed.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if book:
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
            else:
                print(f"'{book.title}' was not borrowed.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            library.add_book(isbn, title, author, year)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            library.borrow_book(isbn)

        elif choice == '4':
            isbn = input("Enter the ISBN of the book you want to return: ")
            library.return_book(isbn)

        elif choice == '5':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
