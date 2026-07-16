from django.contrib import admin
from LibraryApp.models import Author, Book, Reader, BorrowRecord

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthdate', 'bio']
    search_fields = ['name', 'last_name']
    list_filter = ['birthdate']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'annotation', 'year', 'quantity']
    search_fields = ['name', 'author__name', 'author__last_name']
    list_filter = ['author', 'year']


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'borrow_date', 'return_date']

