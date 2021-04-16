from  django.views import generic
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name="books/index.html"
    context_object_name="books"

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model=Book
    context_object_name="books"
    template_name="books/detail.html"

class BookCreate(CreateView):
    model=Book
    fields="__all__"

class BookUpdate(UpdateView):
    model=Book
    fields="__all__"

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("books:index")


