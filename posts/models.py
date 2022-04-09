from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer
# from urllib3 import encode_multipart_formdata


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)



class Brand(models.Model):
    name = models.CharField(max_length=50)
    short_content = models.CharField(max_length=100)
    long_content = models.TextField()  # 많은 양의 글자를 담기 위해 TextField 설정
    logo = models.ImageField(null=True, blank=True, upload_to='posts/Brand/%Y/%m/%d')
    homepage = models.CharField(max_length=200)   # 해당 브랜드의 홈페이지 주소를 담기위해 설정
    problem = models.ForeignKey('Problem', on_delete=models.PROTECT)     # 해당 브랜드가 해결하고자 하는 사회문제를 구분해 사회문제 페이지에서 분류할 수 있도록 설정
    image = models.ImageField(null=True, blank=True, upload_to='posts/Brand/%Y/%m/%d') 

    def __str__(self):
        return f'{self.name}'


class Problem(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='posts/Problem/%Y/%m/%d')
    short_content = models.CharField(max_length=200, null=True, blank=True)  
    content = models.TextField()      # 많은 양의 글자를 담기 위해 TextField 설정

    def __str__(self):
        return f'{self.name}'    