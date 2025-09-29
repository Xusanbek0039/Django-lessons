from django.urls import path
from users.views import RegisterView, LoginView, ProfilView, LogoutView
app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("profile/",ProfilView.as_view(),name="profile"),
    path("logout/",LogoutView.as_view(),name="logout"),

    ]