from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('users must have an email')
        user = self.model(
            email=self.normalize_email(email=email),
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('users must have an email')
        user = self.model(
            email=self.normalize_email(email=email),
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
