from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth.models import User  
# Create your views here.
from users.forms import UserCreateFrom


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateFrom()
        context = {
            "form": create_form
        }
        return render(request, 'users/register.html', context)
    

    def post(self, request):
        create_form = UserCreateFrom(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
            "form": create_form
            }
            return render(request, "users/register.html",context)
    
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')