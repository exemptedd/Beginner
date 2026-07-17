from django.shortcuts import render
from LibraryApp.models import *
from django.contrib.auth.models import User
from django.views.generic import *
from LibraryApp.forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookCreateView( LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'create_book.html'
    form_class = BookForm
    success_url = '/book_list/'

@login_required
def borrow_list(request):
    reader, created = Reader.objects.get_or_create(
        user=request.user,
        defaults={
            'name': request.user.username, 
            'email': request.user.email
        }
    )
    
    borrow_list = BorrowRecord.objects.filter(reader=reader)
    return render(request, 'profile_user.html', {'borrow_list': borrow_list})



class RegisterView(CreateView):
    form_class = UserCreationForm
    
    template_name = 'registration/register.html'
    
    success_url = reverse_lazy('login')