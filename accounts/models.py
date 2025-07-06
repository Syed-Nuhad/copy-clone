from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    We'll add Vinted-related fields here.
    """
    vinted_username = models.CharField(max_length=150, blank=True, null=True)
    vinted_password = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username

