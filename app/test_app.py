import pytest
from app import Library

def test_add_and_view_books():
    lib = Library()
    assert lib.add_book("Docker Deep Dive") == "Book 'Docker Deep Dive' added successfully."
    assert "Docker Deep Dive (Available)" in lib.view_books()

def test_issue_book():
    lib = Library()
    lib.add_book("Kubernetes Guide")
    assert lib.issue_book("Kubernetes Guide") == "Book 'Kubernetes Guide' has been issued successfully."
    assert "Kubernetes Guide (Issued)" in lib.view_books()
    assert lib.issue_book("Kubernetes Guide") == "Error: Book 'Kubernetes Guide' is already issued."
    
    assert lib.issue_book("Missing Book") == "Error: Book 'Missing Book' does not exist in the library."
