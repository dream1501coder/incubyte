# incubyte
Add Book: Add new books to the library's inventory.
View Available Books: Display a list of all books in the library along with their current status (Available/Borrowed).
Borrow Book: Borrow a book from the library if it is available.
Return Book: Return a borrowed book to the library.
Exit: Exit the application.

Requirements:
Python 3.x

Run the Application:
python library_management_system.py

Output Example: 
------------------*-----------------
Library Management System
1. Add Book
2. View Available Books
3. Borrow Book
4. Return Book
5. Exit

Enter your choice (1-5): 1
Enter ISBN: 9780135166307
Enter book title: Python Crash Course
Enter book author: Eric Matthes
Enter publication year: 2019
'Python Crash Course' by Eric Matthes (2019) has been added to the library with ISBN 9780135166307.

Enter your choice (1-5): 2
[9780135166307] Python Crash Course by Eric Matthes (2019) - Available

Enter your choice (1-5): 3
Enter the ISBN of the book you want to borrow: 9780135166307
You have borrowed 'Python Crash Course'.

Enter your choice (1-5): 4
Enter the ISBN of the book you want to return: 9780135166307
You have returned 'Python Crash Course'.

Enter your choice (1-5): 5
Exiting the Library Management System.

