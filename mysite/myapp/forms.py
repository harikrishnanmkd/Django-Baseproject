from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','price','pub_date','description','cover_image']
        widgets = {'book_name': forms.TextInput(attrs={'class':'form-control'}),}
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username',"email","password1","password2"]
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form username-input'}),
            'email':forms.EmailInput(attrs={'class':'form email-input'}),
            'password1':forms.TextInput(attrs={'class':'form password1'}),
            'password2':forms.PasswordInput(attrs={'class':'form password2'})
        }
        
class UserLoginForm(AuthenticationForm):
    pass
        
        
    
    
    