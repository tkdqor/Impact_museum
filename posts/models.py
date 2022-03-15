from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer
# from urllib3 import encode_multipart_formdata


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

        

        