from django.urls import path
from . import views

urlpatterns = [
    path('form', views.BookView.as_view(), name='form'),
    path('', views.LoginView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('books', views.BooksListView.as_view(), name='books'),
    path('users', views.UsersListView.as_view()),
]