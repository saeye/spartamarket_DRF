from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    GENDER_CHOICES = (
        ('male', '남'), 
        ('female', '여'),
    )

    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    birth = models.DateField(null=False, blank=False)  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)