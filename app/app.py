class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        if not title:
            return "Invalid title"
        self.books[title] = True
        return f"Book '{title}' added successfully."

    def view_books(self):
        if not self.books:
            return "No books available in the library."
        return "\n".join([f"- {title} ({'Available' if status else 'Issued'})" for title, status in self.books.items()])

    def issue_book(self, title):
        if title not in self.books:
            return f"Error: Book '{title}' does not exist in the library."
        if not self.books[title]:
            return f"Error: Book '{title}' is already issued."
        
        self.books[title] = False  
        return f"Book '{title}' has been issued successfully."

def menu():
    lib = Library()
    print("\n--- Library Management System ---")
    lib.add_book("Python Basics")
    lib.add_book("Kubernetes Guide")
    
    print("\nInitial State:")
    print(lib.view_books())
    
    print("\nIssuing 'Python Basics'...")
    print(lib.issue_book("Python Basics"))
    
    print("\nUpdated State:")
    print(lib.view_books())

if __name__ == "__main__":
    menu()
