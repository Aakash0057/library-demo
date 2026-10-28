import time

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        if not title or not title.strip():
            return "Error: Title cannot be empty."
        cleaned_title = title.strip()
        self.books[cleaned_title] = True
        return f"Book '{cleaned_title}' added successfully."

    def view_books(self):
        if not self.books:
            return "No books available in the library."
        return "\n".join([f"- {title} ({'Available' if available else 'Issued'})" for title, available in self.books.items()])

    def issue_book(self, title):
        cleaned_title = title.strip()
        if cleaned_title not in self.books:
            return f"Error: Book '{cleaned_title}' does not exist."
        if not self.books[cleaned_title]:
            return f"Error: Book '{cleaned_title}' is already issued."
        self.books[cleaned_title] = False
        return f"Book '{cleaned_title}' has been issued successfully."

def menu():
    lib = LibraryManager()
    print("--- Library Management System ---")
    print(lib.add_book("Python Basics"))
    print(lib.add_book("Kubernetes Guide"))
    print("\nInitial State:")
    print(lib.view_books())
    print("\nIssuing 'Python Basics'...")
    print(lib.issue_book("Python Basics"))
    print("\nUpdated State:")
    print(lib.view_books())
    
    while True:
        time.sleep(3600)

if __name__ == "__main__":
    menu()
