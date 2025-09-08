from django import forms
from django.contrib.auth.models import User 


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # <-- email validatsiya bo‘ladi

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def save(self, commit=True):
        user = super().save(commit=False)  # <-- bazaga yozmasdan obyektni olamiz
        user.set_password(self.cleaned_data["password"])  # <-- parolni hashlash
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)