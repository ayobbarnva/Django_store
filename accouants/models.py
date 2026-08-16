from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15,unique=True)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    profile_image=models.ImageField(upload_to='profile/',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    objects=UserManager()
    USERNAME_FIELD="phone_number"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.phone_number