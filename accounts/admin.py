from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Customer)                 # register 장식자를 이용해서 Customer 모델을 admin에 등록하기
class CustomerAdmin(admin.ModelAdmin):    # admin(패키지)모듈의 ModelAdmin 클래스를 상속받아서 Customer 클래스 설정
    list_display = ['user', 'name', 'email', 'problem']   # # ModelAdmin 클래스를 상속받아 생성한 클래스의 옵션으로 admin페이지 상 필드 표시