# test_book_manager.py

import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()

    def test_add_book(self):
        book1 = Book("123456", "Book Title 1", "Author 1")
        book2 = Book("789012", "Book Title 2", "Author 2")

        self.manager.add_book(book1)
        self.assertEqual(self.manager.list_books(), [book1])

        # Adding the same book again should not change the list
        self.manager.add_book(book1)
        self.assertEqual(self.manager.list_books(), [book1])

        self.manager.add_book(book2)
        self.assertEqual(self.manager.list_books(), [book1, book2])

    def test_remove_book(self):
        book1 = Book("123456", "Book Title 1", "Author 1")
        book2 = Book("789012", "Book Title 2", "Author 2")

        self.manager.add_book(book1)
        self.manager.add_book(book2)

        self.manager.remove_book("123456")
        self.assertEqual(self.manager.list_books(), [book2])

        # Removing a non-existent book should not change the list
        self.manager.remove_book("987654")
        self.assertEqual(self.manager.list_books(), [book2])

    def test_list_books(self):
        book1 = Book("123456", "Book Title 1", "Author 1")
        book2 = Book("789012", "Book Title 2", "Author 2")

        self.manager.add_book(book1)
        self.manager.add_book(book2)

        books = self.manager.list_books()
        self.assertEqual(len(books), 2)
        self.assertIn(book1, books)
        self.assertIn(book2, books)

if __name__ == '__main__':
    unittest.main()
