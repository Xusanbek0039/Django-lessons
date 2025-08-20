from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    isbn = models.CharField(max_length=17)
    def __str__(self):
        return self.title
    
class Author(models.Model):
    firt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =models.EmailField()
    bio = models.TextField()
    def __str__(self):
        return f"{self.firt_name} {self.last_name}"

class BookAuthor(models.Model):
    book =models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    start_given = models.IntegerField(
        validators=(MinValueValidator(1),MaxValueValidator(5))
    )