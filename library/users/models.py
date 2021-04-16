from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=254)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    book=models.CharField(max_length=100,default="None")

    def __str__(self):
        return self.username

