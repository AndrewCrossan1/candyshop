from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'
    # this field means that when you try to sign in the username field will be the email
    # change it to whatever you want django to see as the username when authenticating the user
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' - ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True