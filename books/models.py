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

