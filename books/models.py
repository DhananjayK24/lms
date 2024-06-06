from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.TextField()
    publisher = models.TextField()

class SignUp(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=150)
    borrow_date = models.DateField(auto_now_add=True)