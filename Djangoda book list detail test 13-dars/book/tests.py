from django.test import TestCase

from django.urls import reverse
from book.models import Book


class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(response("books:list"))

        self.assertContains(response, "No books found.")

        
    def test_books_list(self):
        pass
    def test_detail_page(self):
        pass