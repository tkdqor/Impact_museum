from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Customer 모델
class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=1)    # User모델과 1대1 관계 / on delete를 사용해서 회원이 지워지면 고객도 지워지게 한다.
    name = models.CharField(max_length=100, null=False, default=1)          
    email = models.CharField(max_length=100)
    problem = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'user: {self.user} | name: {self.name} | email: {self.email} | problem: {self.problem}'