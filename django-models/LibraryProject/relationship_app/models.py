from django.db import models

from django.db import models

# -------------------------------
# Author model
# -------------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name  # Shows the author name in admin or shell

# -------------------------------
# Book model
# -------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    # ForeignKey = many books can belong to one author
    # on_delete=models.CASCADE = if author deleted, delete their books

    def __str__(self):
        return self.title

# -------------------------------
# Library model
# -------------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)  # Library name
    books = models.ManyToManyField(Book)  
    # ManyToManyField = library can have many books, and a book can be in many libraries

    def __str__(self):
        return self.name

# -------------------------------
# Librarian model
# -------------------------------
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Librarian name
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    # OneToOneField = each librarian manages exactly one library

    def __str__(self):
        return self.name

