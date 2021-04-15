from django.shortcuts import render,get_object_or_404
from .models import Book

# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request, 'books/index.html', {"books":books})

def details(request, book_id):
    books=get_object_or_404(Book,pk=book_id)
    return render(request, 'books/detail.html', {"books":books})