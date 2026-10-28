import pytest
from app import Library

def test_add_and_view_books():
    lib = Library()
    assert lib.add_book("Docker Deep Dive") == "Book 'Docker Deep Dive' added successfully."
    assert "Docker Deep Dive (Available)" in lib.view_books()
