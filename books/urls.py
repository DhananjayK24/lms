from django.urls import path
from . import views

urlpatterns = [
    path('add_book', views.AddBookView.as_view(), name='add_book'),
    path('', views.LoginView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('books_list', views.BooksListView.as_view(), name='books_list'),
    path('all_users', views.UsersListView.as_view()),
    path('update_book/<int:pk>', views.UpdateBookView.as_view(), name='update_book'),
]