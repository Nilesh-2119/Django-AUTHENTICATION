from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, username,email, is_admin, password, **other):
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            is_admin = is_admin,
            password = password,
            **other,
        )
        user.set_password(password)
        user.save()
        return user



class CustomUserModel(AbstractUser):
    username = models.CharField(unique=True, null=True, max_length=100)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(null=True)
