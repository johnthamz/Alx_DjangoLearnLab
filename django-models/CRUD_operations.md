# CRUD Operations for Book Model

This document demonstrates the creation, retrieval, update, and deletion of a `Book` instance in the Django `bookshelf` app using the Django shell.

---

## **1. Create a Book**

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

# Retrieve the book by title
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output:
# ('1984', 'George Orwell', 1949)


# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title
# Expected Output:
# 'Nineteen Eighty-Four'

# Delete the book instance
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()
# Expected Output:
# <QuerySet []>


4. Save the file in the same folder where `manage.py` is located (your current folder) and close Notepad.

---

### **Step 2: Add the File to Git**

Now run:

```cmd
git add bookshelf CRUD_operations.md

