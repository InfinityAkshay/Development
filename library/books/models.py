from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    summary=models.CharField(max_length=2000)
    ISBN=models.CharField(max_length=13)
    location=models.CharField(max_length=100)
    availability=models.CharField(max_length=100)
    picture=models.CharField(max_length=100)

    def __str__(self):
        return self.title+"-"+self.author