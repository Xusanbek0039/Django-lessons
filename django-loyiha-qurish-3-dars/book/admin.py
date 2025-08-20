from django.contrib import admin
from book.models import Book,Author


class BookAdmin(admin.ModelAdmin):
    search_fields = ("title","isbn","descriptions")
    # list_filter = ('title',)
    list_display = ("title","isbn","descriptions")

class AuthonAdmin(admin.ModelAdmin):
    search_fields = ("firt_name","last_name","email")
    # list_filter = ('title',)
    list_display = ("firt_name","last_name","email")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthonAdmin)