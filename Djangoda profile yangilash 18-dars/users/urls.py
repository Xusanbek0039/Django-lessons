from django.urls import path
from .views import RegisterView, LoginView, ProfilView, LogoutView, profile_update

app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profil/', ProfilView.as_view(), name='profil'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', profile_update, name='profile_update'),
]
