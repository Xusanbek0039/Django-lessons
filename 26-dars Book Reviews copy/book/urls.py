from django.urls import path
from .views import BooksView, BookDetailView

urlpatterns = [
    path('', BooksView.as_view(), name='book_list'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
]
