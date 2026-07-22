# from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    #objects = None
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}:{self.text[:5]}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True,null=True)

    def __str__(self):
        return self.user.username