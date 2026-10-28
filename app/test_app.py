import pytest
from app.app import LibraryManager

def test_add_and_view_books():
    lib = LibraryManager()
    assert "added successfully" in lib.add_book("Docker Deep Dive")
    assert "- Docker Deep Dive (Available)" in lib.view_books()

def test_issue_book_functionality():
    lib = LibraryManager()
    lib.add_book("Cloud Architecture")
    assert lib.issue_book("Cloud Architecture") == "Book 'Cloud Architecture' has been issued successfully."
    assert "- Cloud Architecture (Issued)" in lib.view_books()
