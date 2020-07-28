from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    number = models.IntegerField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='main/profile_pics')
    site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
