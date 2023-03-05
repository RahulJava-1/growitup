from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    choose=models.CharField(max_length=100)

class AdminLogin(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)