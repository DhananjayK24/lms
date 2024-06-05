from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('add_book', views.AddBookView.as_view(), name='add_book'),
    path('update_book/<int:pk>', views.UpdateBookView.as_view(), name='update_book'),
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'),
    path('books_list', views.BooksListView.as_view(), name='books_list'),
    path('users_list', views.UsersListView.as_view()),
]