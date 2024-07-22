from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.core.validators import RegexValidator

# regex phone number
phone_number_validation = RegexValidator(
    regex=r'^[0][9]\d{9}$',
    message='Please Enter A Valid Phone Number'
)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, validators=[phone_number_validation], unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_superuser:
            return True

    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.phone


class Otp(models.Model):
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
