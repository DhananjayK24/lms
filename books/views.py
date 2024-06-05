from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
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
    template_name = "books/add_book.html"
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        form.instance.publisher = self.request.session.get('login_name')    
        return super().form_valid(form)
    

class LoginView(FormView):
    form_class = LoginForm
    template_name = "books/login.html"
    success_url = reverse_lazy('add_book')

    def form_valid(self, form):
        self.request.session['login_name'] = form.cleaned_data['name']
        # print(self.request.session['login_name'])
        messages.success(self.request, "Login Successfull!")
        return super().form_valid(form)

class BooksListView(ListView):
    template_name = "books/books_list.html"

    model = Book
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_name = self.request.session.get('login_name')
        context['login_name'] = login_name
        return context

class UsersListView(ListView):
    template_name = "books/all_users.html"

    model = SignUp
    context_object_name = "users"