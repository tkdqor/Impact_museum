from attr import field, fields
from rest_framework.serializers import ModelSerializer
from .models import Product, Order, OrderItem

# Product 모델
class ProductModelSerializer(ModelSerializer):  # ModelSerializer를 상속해서 모델만 설정하고 필드 쉽게 가져오기
    class Meta:
        model = Product
        fields = ('product_name', 'brand', 'price', 'created_at', 'updated_at')


# Order 모델
class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'date_ordered', 'complete', 'transaction_id')


# OrderItem 모델
class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 1          # depth = 1 코드를 추가해서 -> OrderItem 모델과 1:N관계로 설정되어있는 Product와 Order 모델 데이터를 
                           # 자세하게 보여주기