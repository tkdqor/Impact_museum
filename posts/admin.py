from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Customer)                        # register 장식자를 이용해서 Customer 모델을 admin에 등록하기
class CustomerAdmin(admin.ModelAdmin):           # admin(패키지)모듈의 ModelAdmin 클래스를 상속받아서 Customer 클래스 설정
    list_display = ['user', 'name', 'email']     # ModelAdmin 클래스를 상속받아 생성한 클래스의 옵션으로 admin페이지 상 필드 표시


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'price', 'image', 'created_at', 'updated_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'complete', 'transaction_id']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'city', 'zipcode', 'date_added']






