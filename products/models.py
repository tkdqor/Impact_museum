from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer
from posts.models import Brand


# Create your models here.


# Products 모델
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, related_name='brand_product') # Brand 모델과 1:N관계 / 자체 PB 상품일수도 있으니 null, blank True 설정
    price = models.PositiveIntegerField(default=0)              # 가격이니까 실수가 아닌 정수 필드로 수정 / 가격이 음수가 될 수 없으니 타이트하게 필드 설정
    image = models.ImageField(null=True, blank=True, upload_to='products/product/%Y/%m/%d')            # 이미지이니까 Image 필드 선택
    image2 = models.ImageField(null=True, blank=True, upload_to='products/product/%Y/%m/%d')
    image3 = models.ImageField(null=True, blank=True, upload_to='products/product/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)        # 상품 db에 추가할 때 날짜 설정
    updated_at = models.DateTimeField(auto_now=True)            # 수정될 떄마다 날짜 설정

    def __str__(self):
        return f'product_name: {self.product_name} | brand: {self.brand} | price: {self.price} | image: {self.image} |created_at: {self.created_at}'


    class Meta:              # Product 모델안에 Meta 클래스 속성으로 id필드에 대한 역순을 설정할 수도 있음 -> 최신 상품목록을 보여주기 위함
        ordering = ['-id']   # 그런데, View 함수에서 Product.objects.all().order_by로 설정하면 Meta 클래스는 무시됨


    @property
    def imageURL(self):      # 이미지가 있다면 보여주고 없다면 상품 목록 페이지로 redirect 시켜주기
        try:
            url = self.image.url
        except:
            url = 'products/'
        return url            


# Order 모델
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, default=1)    # Customer가 회원탈퇴 하더라도 주문 내역을 유지하기 / 어뷰징 회원일 수도 있기 때문에 주문 내역 자료가 필요할 수 있다.
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'id: {self.id} | customer: {self.customer} | date_ordered: {self.date_ordered} | complete: {self.complete} | transaction_id: {self.transaction_id}'


    @property
    # 장바구니에 담은 모든 상품들의 총 금액을 계산하는 코드
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    # 장바구니에 담은 모든 상품들의 수를 계산하는 코드
    def get_cart_items(self):                   
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total




# Order item 모델
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)   # Product 모델과 1:N관계 / 장바구니 기록을 남기기 위해 Post가 사라져도 남게끔 설정
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)    # Order 모델과 1:N관계 / 주문내역이 사라져도 장바구니 기록을 남길 수 있게 설정
    quantity = models.IntegerField(default=0, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.id} | product: {self.product} | order: {self.order} | quantity: {self.quantity} | date_added: {self.date_added}'


    # 장바구니에서 총 합계를 볼 수 있도록 property operator를 설정
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



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


