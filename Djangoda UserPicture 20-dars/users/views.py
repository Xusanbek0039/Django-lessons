from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm


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
        login_form = UserLoginForm()
        return render(request, "users/login.html", {"login_form": login_form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request,"Login qilindi!")
            return redirect("landing_page")
        else:
            return render(request, "users/login.html", {"login_form": login_form})
        
class ProfilView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"users/profil.html", {"user:request":"user"})
    
    
class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.info(request,"Tizimdan chiqildi!")
        return redirect("landing_page")





@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile')  # endi to'g'ri URL name ishlatiladi
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile_update.html', context)
