from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer
from django.utils.translation import gettext_lazy as _   # 해당 함수로 문자열을 정의해서 다국어 처리 가능


# Create your models here.


class Post(models.Model):

    class Category(models.TextChoices):     # 공지사항의 종류를 카테고리 클래스로 정의하기
        NORMAL = 'NORMAL', _('일반')
        DISABLED = 'DISABLED', _('장애인')
        ENVIRONMENT = 'ENVIRONMENT', _('환경')
        EMPLOYMENT = 'EMPLOYMENT', _('고용')
        EDUCATION = 'EDUCATION', _('교육')
        ELDERS = 'ELDERS', _('노인')

    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='author_post')
    title = models.CharField(max_length=100, default='None')
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.NORMAL)   # 위에서 정의한 Category 클래스로 선택할 수 있게 설정
    body = models.TextField()  # 많은 양의 글자를 담기 위해 TextField 설정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   # 글 수정일자 자동으로 DB에 저장하기

    def __str__(self):
        return f'{self.title}'



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