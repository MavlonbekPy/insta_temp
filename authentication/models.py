from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
