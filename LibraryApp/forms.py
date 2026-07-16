from django.forms import ModelForm
from LibraryApp.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'annotation', 'year', 'quantity']
        labels = {
            'name': 'Name',
            'author': 'Author',
            'annotation': 'Annotation',
            'year': 'Year',
            'quantity': 'Quantity',
        }