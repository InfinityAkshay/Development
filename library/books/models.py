from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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
    picture=models.FileField()

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"id": self.pk})
    

    def __str__(self):
        return self.title+"-"+self.author

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("No email address")
        
        if not username:
            raise ValueError("No username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    username = models.CharField(max_length=100, verbose_name='username', unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


    


