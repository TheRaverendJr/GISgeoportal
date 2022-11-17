from django.db import models

# abstract user
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

# Create your models here.
