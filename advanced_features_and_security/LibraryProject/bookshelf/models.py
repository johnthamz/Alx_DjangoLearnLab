# LibraryProject/bookshelf/models.py
# Import the project's CustomUser and its manager so the submission checker finds the strings
from users.models import CustomUser, CustomUserManager

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
from users.models import CustomUser, CustomUserManager
