from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.urls import reverse_lazy
# from django.contrib.auth.views import LoginView, 
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.core.exceptions import ValidationError

from .models import Book, SignUp
from .forms import BooksForm, SignupForm, LoginForm
# Create your views here.

class SignUpView(FormView):
    form_class = SignupForm
    template_name = "books/signup.html"
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        # Call form.save() to save the form data
        form.save()
        return super().form_valid(form)    

class BookView(CreateView):
    model = Book
    form_class = BooksForm
    template_name = "books/form.html"
    success_url = reverse_lazy('books:books')

class LoginView(FormView):
    form_class = LoginForm
    template_name = "books/login.html"
    success_url = 'form'
    
    def form_valid(self, form):
        form
        return super().form_valid(form)

class BooksListView(ListView):
    template_name = "books/books.html"

    model = Book
    context_object_name = "books"

class UsersListView(ListView):
    template_name = "books/all_signup.html"

    model = SignUp
    context_object_name = "signup"