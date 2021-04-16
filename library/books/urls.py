from django.urls import path
from django.conf.urls import url
from . import views

app_name='books'
urlpatterns = [
    # books/
    path("", views.index,name='index'),

    # books/id
    url(r'^(?P<book_id>[0-9]+)/$',views.detail, name='detail'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    
]