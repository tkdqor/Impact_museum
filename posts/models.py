from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Customer 모델
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    # User모델과 1대1 관계 / null=True는 비워도 괜찮다는 것. / on delete를 사용해서 회원이 지워지면 고객도 지워지게 한다.
    name = models.CharField(max_length=100, null=True)          # 캐릭터 필드
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


# Products 모델
class Post(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.TextField()
    price = models.FloatField(default=0)              # 숫자니까 Float 필드 선택
    image = models.ImageField(null=True, blank=True)     # 이미지이니까 Image 필드 선택
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.product_name}: {self.brand}'


# Order 모델
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id}'


# Order item 모델
class OrderItem(models.Model):
    product = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'


# Shipping Address 모델
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.address}'