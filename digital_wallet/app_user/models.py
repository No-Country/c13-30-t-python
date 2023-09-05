from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import MyUserManager
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser, PermissionsMixin):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address', max_length=255,  unique=True)
    identification_type = models.CharField(max_length=20, null=False)
    identification_number = models.CharField(max_length=20, null=False, unique=True)
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email