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
        return "Feature under construction in Push 1."

def menu():
    lib = LibraryManager()
    print("--- Library Management System ---")
    print(lib.add_book("Python Automation"))
    print(lib.add_book("Kubernetes Internals"))
    print("\nCurrent Inventory Status:")
    print(lib.view_books())

if __name__ == "__main__":
    menu()
