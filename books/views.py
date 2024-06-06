from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.urls import reverse_lazy
# from django.contrib.auth.views import LoginView, 
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Book, SignUp, Borrow
from .forms import AddBookForm, SignupForm, LoginForm, BorrowForm
# Create your views here.

class SignUpView(FormView):
    form_class = SignupForm
    template_name = "books/signup.html"
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        # Call form.save() to save the form data
        form.save()
        return super().form_valid(form)    

class LoginView(FormView):
    form_class = LoginForm
    template_name = "books/login.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.request.session['login_name'] = form.cleaned_data['name']
        # print(self.request.session['login_name'])
        messages.success(self.request, "Login Successfull!")
        return super().form_valid(form)
    
class HomeView(TemplateView):
    template_name = "books/home.html"

class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "books/add_book.html"
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        form.instance.publisher = self.request.session.get('login_name')    
        return super().form_valid(form)
    
class UpdateBookView(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = "books/update_book.html"
    success_url = reverse_lazy('books_list')

class DeleteBookView(DeleteView):
    model = Book
    template_name = "books/delete_book.html"
    success_url = reverse_lazy('books_list')
    context_object_name = "book"

class BorrowView(CreateView):
    model = Borrow
    form_class = BorrowForm
    template_name = "books/borrow.html"
    success_url = reverse_lazy('books_list')

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
            initial['book'] = book
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.session.get('login_name')  
        book = form.cleaned_data.get('book')
        user_has_book = Borrow.objects.filter(user=form.instance.user, book=book)
        if user_has_book:
            form.add_error('book', 'You already have this book.')
            return self.form_invalid(form)
        elif book.quantity>0:
            book.quantity -= 1
            book.save()
            return super().form_valid(form)
        else:
            form.add_error('book', 'This book is not available.')
            return self.form_invalid(form)

class UserBooksView(ListView):
    model = Borrow
    template_name = "books/user_books.html"
    context_object_name = 'books'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(user=self.request.session.get('login_name'))
        return data
    

class BooksListView(ListView):
    model = Book
    template_name = "books/books_list.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_name = self.request.session.get('login_name')
        context['login_name'] = login_name
        return context

class UsersListView(ListView):
    model = SignUp
    template_name = "books/users_list.html"
    context_object_name = "users"