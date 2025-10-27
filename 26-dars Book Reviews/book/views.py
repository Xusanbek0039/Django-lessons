from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from book.models import Book
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator
from .models import Book, Comment
from .forms import CommentForm
# CRUD 
# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = "books"





class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        comments = book.comments.all().order_by('-created_at')
        form = CommentForm()
        return render(request, 'books/detail.html', {
            'book': book,
            'comments': comments,
            'form': form
        })

    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            if request.user.is_authenticated:
                comment.name = request.user.username
            else:
                comment.name = "Anonim foydalanuvchi"
            comment.save()
            return redirect('book_detail', id=book.id)

        comments = book.comments.all().order_by('-created_at')
        return render(request, 'books/detail.html', {
            'book': book,
            'comments': comments,
            'form': form
        })

class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")

        search_query = request.GET.get("search")
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 3)  # har bir sahifada 3 ta kitob
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        context = {
            "page_obj": page_obj,
            "search_query": search_query, 
        }

        return render(request, "books/list.html", context)

# class BookDetailView(View):
#     def get(self,request,id):
#         book= Book.objects.get(id=id)
#         return render(request,'books/detail.html',{"book":book})