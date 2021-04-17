from .models import User, Book
from  django import  forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","email","password"]

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'genre', 'summary', 'ISBN', 'availability', 'picture']
