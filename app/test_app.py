import pytest
from app.app import LibraryManager

def test_add_and_view_books():
    lib = LibraryManager()
    assert "added successfully" in lib.add_book("Docker Deep Dive")
    assert "- Docker Deep Dive (Available)" in lib.view_books()
