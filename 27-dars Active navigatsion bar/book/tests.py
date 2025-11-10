from django.test import TestCase
from django.urls import reverse
from book.models import Book



class BookTestCase(TestCase):
    def test_no_book(self):
        url = reverse("books:list")  
        response = self.client.get(url)  

        self.assertContains(response, "No books found.")  # Javobni tekshirish



    def test_books_list(self):
        Book.objects.create(title="book1",description="Kitob haqida",isbn="123456")
        Book.objects.create(title="book2",description="Kitob haqida",isbn="356445")
        Book.objects.create(title="book3",description="Kitob haqida",isbn="567653")
        url = reverse("books:list")  
        response = self.client.get(url)  

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)



    def test_detail_page(self):
        book = Book.objects.create(title="book3",description="Kitob haqida",isbn="567653")
        url = reverse("books:detail", kwargs={"id":book.id}) 
        response = self.client.get(url)  

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

