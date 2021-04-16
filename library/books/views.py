from  django.views import generic
from django.contrib.auth import logout
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import UserForm
from django.db.models import Q


def index(request):
    if not request.user.is_authenticated:
        return redirect('/books/login_user')
    elif request.user.is_staff:
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

class DetailView(generic.DetailView):
    model=Book
    context_object_name="books"
    template_name="books/detail.html"

def detail(request, book_id):
    if not request.user.is_authenticated:
        return render(request, 'books/login.html')
    else:
        user = request.user
        books = get_object_or_404(Book, id=book_id)
        return render(request, 'books/detail.html', {'books': books, 'user': user})

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
                if user.is_staff:
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



