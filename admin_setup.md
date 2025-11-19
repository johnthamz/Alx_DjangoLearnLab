# Django Admin Setup for Book Model

## Steps Completed:

1. Registered the `Book` model in `bookshelf/admin.py`.
2. Created a custom admin class (`BookAdmin`) with:
   - `list_display` to show title, author, and publication year.
   - `list_filter` to filter by publication year.
   - `search_fields` to search by title or author.
3. Created a superuser account using `python manage.py createsuperuser`.
4. Accessed the admin at `http://127.0.0.1:8000/admin/`.
5. Verified that books can be created, updated, deleted, filtered, and searched from the admin interface.
