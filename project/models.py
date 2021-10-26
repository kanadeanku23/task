from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser, models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    hashed_password = models.CharField(max_length=100, default="", null=False)
    email = models.EmailField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

