from django.contrib import admin
from .models import Book, User, Request, Renew, Rating, Comment
# Register your models here.
# admin.site.register(Book)
admin.site.register(User)
admin.site.register(Comment)
# admin.site.register(Rating)
