import os
import sys
import django

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from .models import Author, Book, Library, Librarian

# Create sample data
def seed_data():
    # Authors
    a1, _ = Author.objects.get_or_create(name="John Doe")
    a2, _ = Author.objects.get_or_create(name="Jane Smith")

    # Books
    b1, _ = Book.objects.get_or_create(title="Django Basics", author=a1)
    b2, _ = Book.objects.get_or_create(title="Advanced Django", author=a2)
    b3, _ = Book.objects.get_or_create(title="Python Tips", author=a1)

    # Library
    library, _ = Library.objects.get_or_create(name="Central Library")
    library.books.add(b1, b2, b3)

    # Librarian
    librarian, _ = Librarian.objects.get_or_create(name="Alice Johnson", library=library)

# Run sample queries
def run_queries():
    # Query all books by a specific author
    author_name = "John Doe"
    author = Author.objects.get(name=author_name)
    print(f"\nBooks by {author_name}:")
    for book in author.books.all():
        print(f" - {book.title}")

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print(f" - {book.title}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    seed_data()
    run_queries()
