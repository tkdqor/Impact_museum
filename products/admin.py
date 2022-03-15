from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'price', 'image_tag', 'created_at', 'updated_at']

    def image_tag(self, product):                        # image_tag라는 함수를 정의해서 image 필드에 경로가 있는 경우 admin에도 보여줄 수 있도록 설정
        if product.image:
            return mark_safe(f'<img src="{product.image.url}" style="width: 150px; height: 150px;" />') # mark_safe 함수로 안전함을 표시해야 admin 페이지에 사진 표시 가능
        return None    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'complete', 'transaction_id']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'city', 'zipcode', 'date_added']
