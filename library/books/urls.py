from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # books/
    path("", views.index,name='index'),

    # books/id
    url(r'^(?P<book_id>[0-9]+)/$',views.details, name='detail')
]