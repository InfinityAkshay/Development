from django.urls import path
from django.conf.urls import url
from . import views

app_name='books'
urlpatterns = [
    # books/
    path("", views.IndexView.as_view(),name='index'),

    # books/id
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    # books/book/add/
    url(r'book/add/$', views.BookCreate.as_view(), name="book-add"),

    # books/book/id/
    url(r'book/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name="book-update"),

    # books/book/id/delete
    url(r'book/(?P<pk>[0-9]+)/delete$', views.BookDelete.as_view(), name="book-delete"),
    
    
]