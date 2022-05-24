from django.http import HttpResponse
from django.urls import path, include
from . import views

from rest_framework import routers
from .views import ProductModelViewSet, OrderModelViewSet, OrderItemModelViewSet


# DRF routers 설정
router = routers.DefaultRouter()                      # DefaultRouter이기 때문에 API - ROOT 페이지가 생성됨
router.register('products', ProductModelViewSet)      # ProductModelViewSet 설정
router.register('orders', OrderModelViewSet)          # OrderModelViewSet 설정
router.register('orderitems', OrderItemModelViewSet)  # OrderItemModelViewSet 설정


# URL name 설정
app_name = 'products'


urlpatterns = [
    # 메인화면 URL
    path('', views.index, name='index'),

    # product 관련 URL
    path('<int:product_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:product_id>/edit/', views.edit, name='edit'),
    path('<int:product_id>/update/', views.update, name='update'),
    path('<int:product_id>/delete/', views.delete, name='delete'),

    # DRF(Django Rest Framework) URL 
    path('drf/', include(router.urls)), # products/drf/로 API ROOT 설정

    # 장바구니 관련 URL
    path('cart/', views.cart, name='cart'),                                       # 장바구니 페이지 URL
    path('checkout/', views.checkout1, name='checkout'),                          # 장바구니 페이지에서 클릭한 결제 버튼
    path('<int:product_id>/checkout/', views.checkout2, name='checkout_id'),      # 상품 1개 조회 페이지에서 클릭한 결제 버튼
    path('<int:product_id>/update_item/', views.updatedItem, name='update_item'), # 장바구니 추가 기능
    path('<int:product_id>/cart_delete', views.cart_delete, name='cart_delete'),  # 장바구니 상품 삭제
]


