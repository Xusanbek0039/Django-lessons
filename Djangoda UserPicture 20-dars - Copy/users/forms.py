from django import forms
from .models import CustomUser
from .models import Profile

class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # <-- email validatsiya bo‘ladi

    class Meta:
        model = CustomUser
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


from django import forms
from .models import CustomUser
from .models import Profile  # Profil modeli ham kerak bo'ladi

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"last_name", 'email',"first_name","profile_picture"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"last_name", 'email',"first_name","profile_picture"]
