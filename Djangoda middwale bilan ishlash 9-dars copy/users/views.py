from django.shortcuts import render, redirect
from django.views import View 
from users.forms import UserCreateForm  # <-- nomini to‘g‘riladik


class RegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        return render(request, "users/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")
