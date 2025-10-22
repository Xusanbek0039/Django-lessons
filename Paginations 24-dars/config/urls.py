from django.contrib import admin
from django.urls import path, include
from .views import landing_page
from django.conf import settings
from django.conf.urls.static import static

app_name = "config"

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("users/", include("users.urls")),
    path("books/", include("book.urls"),name="books"),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)