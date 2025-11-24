# LibraryProject/relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: render list_books.html
def list_books(request):
    qs = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': qs})


# Class-based view: Library Detail using DetailView and template
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'           # template will use {{ library }}
    template_name = 'relationship_app/library_detail.html'
    pk_url_kwarg = 'pk'                       # matches urls.py <int:pk>

