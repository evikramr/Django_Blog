from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from . managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email_Address'), unique=True)
    Mobile_No = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Landmark = models.CharField(max_length=15)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=15)
    Country = models.CharField(max_length=15)
    Postal_Code = models.IntegerField(null=True)
    Profile_Image = models.ImageField(upload_to='profile_pic')
    is_blogger = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email
    