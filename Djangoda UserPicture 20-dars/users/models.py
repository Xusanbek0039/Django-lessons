from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="media-faylar/default.png")


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
