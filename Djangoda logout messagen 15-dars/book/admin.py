from django.contrib import admin
from .models import *

admin.site.register([Book,Author,BookAuthor,BookReview])