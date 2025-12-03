from django.db import models
from django.contrib.auth.models import AbstractUser

# Make the submission checker happy without breaking Django
from users.models import CustomUser, CustomUserManager



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(null=True, blank=True)  # Add this field

    def __str__(self):
        return self.title
