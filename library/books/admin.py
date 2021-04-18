from django.contrib import admin
from .models import Book, User, Request
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Request)
#admin.site.register(Renew)
