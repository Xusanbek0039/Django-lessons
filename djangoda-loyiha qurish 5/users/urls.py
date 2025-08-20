from django.urls import path
from users.views import RegisterView, LoginView
app_name = "users"

urlpatterns = [
    path('vgcjknsaljknhbgvcjhbknmljks/', RegisterView.as_view(), name='register'),
    path('hisobga_kirish/', LoginView.as_view(), name='login'),

    ]