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
    url(r'^(?P<id>[0-9]+)/return/$', views.return_book, name='return_book'),
    url(r'^(?P<id>[0-9]+)/request/$', views.request_book, name='request_book'),
    url(r'book/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name="book-update"),
    url(r'^home/$', views.home, name='home'),
    url(r'^requests/$', views.request_page, name='request'),
    url(r'^requests/(?P<id>[0-9]+)/accept/$', views.accept, name='accept'),
    url(r'^requests/(?P<id>[0-9]+)/reject/$', views.reject, name='reject'),
    url(r'^(?P<id>[0-9]+)/renew/$', views.renew, name='renew'),
    url(r'^renew/(?P<id>[0-9]+)/accept/$', views.renew_accept, name='renew_accept'),
    url(r'^renew/(?P<id>[0-9]+)/reject/$', views.renew_reject, name='renew_reject'),
]