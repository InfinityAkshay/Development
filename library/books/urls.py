from django.urls import path
from django.conf.urls import url
from . import views

app_name='books'
urlpatterns = [
    # books/
    path("", views.index,name='index'),

    # books/id
    url(r'^(?P<id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^create_book/$', views.create_book, name='create_book'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete_book, name='delete_book'),
    url(r'book/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name="book-update")

    
]