from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Profile


# 1️⃣ — Ro‘yxatdan o‘tish (register) formasi
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Parolingizni kiriting"}),
    )
    password2 = forms.CharField(
        label="Parolni takrorlang",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Parolni qayta kiriting"}),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Foydalanuvchi nomi"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ism"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Familiya"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        }

    def clean_password2(self):
        """Parollar bir xil kiritilganligini tekshiradi"""
        cd = self.cleaned_data
        if cd.get("password") != cd.get("password2"):
            raise forms.ValidationError("Parollar bir xil bo‘lishi kerak!")
        return cd["password2"]

    def save(self, commit=True):
        """Parolni xavfsiz tarzda saqlaydi (hash bilan)"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Foydalanuvchi uchun avtomatik profil yaratish (ixtiyoriy)
            Profile.objects.get_or_create(user=user)
        return user


# 2️⃣ — Kirish (login) formasi
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Parol"}),
    )


# 3️⃣ — Foydalanuvchini yangilash formasi
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "profile_picture"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


# 4️⃣ — Profil ma’lumotlarini yangilash formasi
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio"]  # Profile modelida, masalan, bio yoki boshqa qo‘shimcha maydonlar bo‘ladi
        widgets = {
            "bio": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "O‘zingiz haqingizda qisqacha yozing..."}
            ),
        }
