from django.shortcuts import render
from django.views import View
from book.models import Book
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

# CRUD 
# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = "books"



class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = "id"
    model = Book


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")
        peginator = Paginator(books, 2)
        page_num = request.GET.get('page',1)
        page_obj = peginator.get_page(page_num)

        return render(request, 'books/list.html',{"page_obj": page_obj})
    


# class BookDetailView(View):
#     def get(self,request,id):
#         book= Book.objects.get(id=id)
#         return render(request,'books/detail.html',{"book":book})