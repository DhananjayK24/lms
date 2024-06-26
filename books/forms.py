from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Book, SignUp, Borrow

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity', 'description']
        labels = {
            "title": "Book Title",
            "author": "Book Author",
            "quantity": "Book Quantity",
            "description": "Book Description",
        }

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']
        widgets = {
            'book': forms.TextInput(attrs={'readonly':'readonly'})
        }

class SignupForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=100, widget=forms.TextInput(attrs={'class': 'signup-password-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'signup-password-input'}))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'signup-password-input'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        name = self.cleaned_data['name']
        password = self.cleaned_data['password']
        # confirm_password = self.cleaned_data['confirm_password']

        user = SignUp(name=name, password=password)
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-password-input'}))
    
    class Meta:
        model = SignUp
        fields = "__all__"
        labels = {
            "name": "Name",
            "password": "Password"
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'login-name-input'}),
            "password": forms.PasswordInput(attrs={'class': 'login-password-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')

        try:
            user = SignUp.objects.get(name=name)
            if user.password != password:
                raise ValidationError("Invalid password")
        except SignUp.DoesNotExist:
            raise ValidationError("User does not exist")

        return cleaned_data