from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, default='default_name', null=False, blank=False)
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    birth = models.DateField(null=False, blank=False)  
    gender = models.CharField(max_length=10, blank=True, null=True)  
    introduction = models.TextField(blank=True, null=True)
