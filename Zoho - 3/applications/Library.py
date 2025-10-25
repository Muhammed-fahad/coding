# Library Management System without SQL

from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.book_id = 1
        self.user_id = 1
        self.borrowed_books = {}
        self.fine_per_day = 5

    def add_book(self, title, author):
        self.books[self.book_id] = {'title': title, 'author': author, 'borrowed': False , 'borrowed_by': None}
        print(f"Book '{title}' by {author} added with ID {self.book_id}.")
        self.book_id += 1

    def register_user(self, name):
        self.users[self.user_id] = {'name': name, 'borrowed_books': {}}
        print(f"User '{name}' registered with User ID {self.user_id}.")
        self.user_id += 1

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("Invalid user ID.")
            return
        if book_id not in self.books or self.books[book_id]['borrowed']:
            print("Invalid book ID or book already borrowed.")
            return
        
        self.books[book_id]['borrowed'] = True
        self.books[book_id]['borrowed_by'] = user_id
        due_date = datetime.now() + timedelta(days=14)
        self.users[user_id]['borrowed_books'][book_id] = due_date
        self.borrowed_books[book_id] = user_id
        print(f"Book '{self.books[book_id]['title']}' borrowed successfully. Due date: {due_date.strftime('%Y-%m-%d')}")

    def return_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.users[user_id]['borrowed_books']:
            print("Invalid book ID or book was not borrowed by this user.")
            return
        
        due_date = self.users[user_id]['borrowed_books'][book_id]
        return_date = datetime.now()
        
        days_late = max((return_date - due_date).days, 0)
        fine = days_late * self.fine_per_day if days_late > 0 else 0
        
        self.books[book_id]['borrowed'] = False
        del self.users[user_id]['borrowed_books'][book_id]
        del self.borrowed_books[book_id]
        
        print(f"Book '{self.books[book_id]['title']}' returned successfully.")
        if fine > 0:
            print(f"Late return! Fine to be paid: {fine} units.")

    def search_book(self, title):
        found_books = [book_id for book_id, details in self.books.items() if title.lower() in details['title'].lower()]
        if found_books:
            print("Search Results:")
            for book_id in found_books:
                status = "Borrowed" if self.books[book_id]['borrowed'] else "Available"
                print(f"{book_id} | {self.books[book_id]['title']} | {self.books[book_id]['author']} | {status}")
        else:
            print("No books found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("ID | Title | Author | Status")
            print("-----------------------------------")
            for book_id, details in self.books.items():
                status = "Borrowed" if details['borrowed'] else "Available"
                print(f"{book_id} | {details['title']} | {details['author']} | {status}")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Display Books")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(title, author)
        elif choice == "2":
            name = input("Enter User Name: ")
            library.register_user(name)
        elif choice == "3":
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to borrow: "))
            library.borrow_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(user_id, book_id)
        elif choice == "5":
            title = input("Enter Book Title to search: ")
            library.search_book(title)
        elif choice == "6":
            library.display_books()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
