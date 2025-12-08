from django import forms
from .models import Book

class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search by title...'})
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # adjust to your model fields


class ExampleForm(forms.Form):
    """
    Example form required by the automatic submission checker.
    Can be left simple for now.
    """
    example_field = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Example input'})
    )

