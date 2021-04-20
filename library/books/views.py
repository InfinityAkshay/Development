from  django.views import generic
from django.contrib.auth import logout
from .models import Book, Request, Renew
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import UserForm, BookForm
from django.db.models import Q
from datetime import datetime, timedelta, date

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    if not request.user.is_authenticated:
        return redirect('/books/login_user')
    elif request.user.is_admin:
        return redirect("/admin")
    else:
        books = Book.objects.all()
        query = request.GET.get("q")
        if query:
            books = books.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(publisher__icontains=query) |
                Q(genre__icontains=query) |
                Q(summary__icontains=query) |
                Q(ISBN__icontains=query) |
                Q(location__icontains=query)
            ).distinct()
        return render(request, 'books/index.html', {'books': books,})


def create_book(request):
    if not request.user.is_authenticated:
        return redirect('/books/login_user')
    elif not request.user.is_librarian:
        return redirect('/books/')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.picture = request.FILES['picture']
            file_type = book.picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'book': book,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'books/create_book.html', context)
            book.save()
            return redirect("/books")
        context = {
            "form": form,
        }
        return render(request, 'books/create_book.html', context)

def detail(request, id, error=None):
    if not request.user.is_authenticated:
        return render(request, 'books/login.html')
    else:
        user = request.user
        books = get_object_or_404(Book, id=id)
        connection = Request.objects.filter(user=request.user, book=books).first()
        return render(request, 'books/detail.html', {'books': books, 'user': user, "connection": connection, "error": error})
        

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('/books/login_user')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all()
                if user.is_admin:
                    return redirect('/admin')
                return redirect('/books')
            else:
                return render(request, 'books/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'books/login.html', {'error_message': 'Invalid login'})
    return render(request, 'books/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all
                return redirect('/books')
    context = {
        "form": form,
    }
    return render(request, 'books/register.html', context)

def delete_book(request, id):
    if (request.user.is_admin or request.user.is_librarian):
        book = Book.objects.get(pk=id)
        book.delete()
    return redirect('/books')

class BookUpdate(UpdateView):
    model=Book
    fields="__all__"
    template = 'books/create_book.html'

def return_book(request, id):
    user = request.user
    books = get_object_or_404(Book, id=id)
    connection = Request.objects.filter(user=request.user, book=books).first()
    
    if(connection and connection.state=="1"):
        connection.book.availability += 1
        connection.book.save()
        connection.delete()
    return redirect('/books')

def request_book(request, id):
    user = request.user
    book = get_object_or_404(Book, id=id)
    connection = Request()
    connection.user=user
    connection.book=book
    connection.state="3"
    if request.POST["return_date"]:
        connection.return_date=request.POST["return_date"]
        connection.save()
        return redirect('/books')
    else:
        return detail(request, id, "Enter date")

def home(request):
    if request.user.is_librarian:
        return redirect("/books")
    borrowed = Request.objects.filter(user=request.user, state = "1")
    pending = Request.objects.filter(user=request.user, state = "3")
    return render(request, 'books/home.html', {'borrowed': borrowed, 'pending': pending, "user": request.user})

def request_page(request):
    if not request.user.is_librarian:
        return redirect('/books/home')
    else:
        pending = []
        for i in Request.objects.filter(state = "3"):
            if i.book.availability:
                pending.append(i)
            else:
                i.delete()
        renews = Renew.objects.all()
        return render(request, 'books/request_page.html', {'pending': pending, "renew": renews, "user": request.user})

def accept(request, id):
    if not  request.user.is_librarian:
        return redirect('/books/home')
    else:
        connection = Request.objects.get(pk=id)
        connection.state="1"
        connection.book.availability -= 1
        connection.book.save()
        connection.save()
        return redirect('/books/requests')

def reject(request, id):
    if not  request.user.is_librarian:
        return redirect('/books/home')
    else:
        connection = Request.objects.get(pk=id)
        connection.delete()
        return redirect('/books/requests')

def renew(request, id):
    if request.user.is_librarian:
        return redirect('/books')
    book=Book.objects.get(pk=id)
    user=request.user
    connection = Request.objects.get(user=user,book=book)
    renew = Renew()
    renew.request = connection
    if request.POST["renew_date"]:
        renew.change_date = request.POST["renew_date"]
        renew.save()
        return redirect('/books')
    else:
        return detail(request, id, "Enter Date")


def renew_accept(request, id):
    if not request.user.is_librarian:
        return redirect('/books/home')
    else:
        renew = Renew.objects.get(pk=id)
        renew.request.return_date = renew.change_date
        renew.request.save()
        renew.delete()
        return redirect('/books/requests')

def renew_reject(request, id):
    if not request.user.is_librarian:
        return redirect('/books/home')
    else:
        renew = Renew.objects.get(pk=id)
        renew.delete()
        return redirect('/books/requests')
