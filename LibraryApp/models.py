from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    annotation = models.TextField()
    year = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book} borrowed by {self.reader}"