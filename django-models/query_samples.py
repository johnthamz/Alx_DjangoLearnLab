import os
import django

# Tell Django which settings to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.db import transaction

def seed_data():
    with transaction.atomic():
        # Create Authors
        a1, _ = Author.objects.get_or_create(name="John Doe")
        a2, _ = Author.objects.get_or_create(name="Jane Smith")

        # Create Books
        b1, _ = Book.objects.get_or_create(title="Django for Beginners", author=a1)
        b2, _ = Book.objects.get_or_create(title="Advanced Django", author=a2)

        # Create Library
        library, _ = Library.objects.get_or_create(name="Central Library")
        library.books.add(b1, b2)

        # Create Librarian
        librarian, _ = Librarian.objects.get_or_create(name="Alice Johnson", library=library)

def show_queries():
    print("\nAuthors:")
    for a in Author.objects.all():
        print(f"  {a.name}")

    print("\nBooks and Authors:")
    for b in Book.objects.select_related('author').all():
        print(f"  {b.title} by {b.author.name}")

    print("\nLibrary and Books:")
    for lib in Library.objects.prefetch_related('books').all():
        books = ', '.join([book.title for book in lib.books.all()])
        print(f"  {lib.name} has books: {books}")

    print("\nLibrarians and Libraries:")
    for l in Librarian.objects.select_related('library').all():
        print(f"  {l.name} works at {l.library.name}")

if __name__ == "__main__":
    seed_data()
    show_queries()
