from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Customer 모델
class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=1, unique=True)    # User모델과 1대1 관계 / on delete를 사용해서 회원이 지워지면 고객도 지워지게 한다.
    name = models.CharField(max_length=100, null=False, default="None", unique=True)          
    email = models.CharField(max_length=100, unique=True)
    problem = models.CharField(max_length=100, null=True)
    # user/name/email 필드의 경우, 회원가입 시 중복을 막기 위해 unique=True 속성을 추가

    def __str__(self):
        return f'{self.user}'