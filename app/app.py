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

def menu():
    lib = Library()
    print("\n--- Library Management System ---")
 
    lib.add_book("Python Basics")
    lib.add_book("Kubernetes Guide")
    
    print("Available Books:")
    print(lib.view_books())

if __name__ == "__main__":
    menu()
