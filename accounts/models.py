from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # 특정 데이터 저장 직후 signal인 post_save import
from django.dispatch import receiver           # reciever 데코레이터 사용을 위해 import
from allauth.socialaccount.models import SocialAccount # 소셜로그인 모델 import

# Create your models here.

# Customer 모델
class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=1, unique=True)    # User모델과 1대1 관계 / on delete를 사용해서 회원이 지워지면 고객도 지워지게 한다.
    name = models.CharField(max_length=100, null=False, default="None", unique=True)          
    email = models.CharField(max_length=100, unique=True)
    problem = models.CharField(max_length=100, null=True, default="disabled")
    # user/name/email 필드의 경우, 회원가입 시 중복을 막기 위해 unique=True 속성을 추가

    def __str__(self):
        return f'{self.user}'
    


# 소셜로그인 후, Customer 모델 데이터 저장 Signal
@receiver(post_save, sender=User)
def on_save_user(sender, instance, **kwargs):                  # on_save_user 라는 이름으로 함수 설정
    customer = Customer.objects.filter(user=instance).first()  # 소셜로그인으로 생성된 user 인스턴스가 customer 인스턴스에도 있는지 확인
    social_account = SocialAccount.objects.filter(user=instance).first() # 소셜로그인 모델인 SocialAccount에 해당 user가 있는지 확인

    if customer is None and social_account is not None:        # customer가 없고 social_account가 있다면
        name = instance.email.split('@')[0]                    # Customer 모델 name 필드에 이메일 @을 기준으로 앞에 있는 아이디를 저장
        email = instance.email                                 # Customer 모델 email 필드에 소셜로그인 이메일을 저장
        Customer.objects.create(                               # Customer 모델 데이터 생성
            user = instance,
            name = name,
            email = email,
        )