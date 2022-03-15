from django.http import HttpResponse
from django.urls import path, include
from . import views
from .views import helloAPI, Productinfo
from rest_framework import routers


# DefaultRouter 설정
router = routers.DefaultRouter()
router.register('viewset', views.ProductViewSet)


# URL name 설정
app_name = 'products'


urlpatterns = [
    # 메인화면 URL
    path('', views.index, name='index'),

    # product CRUD URL
    path('<int:product_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:product_id>/edit/', views.edit, name='edit'),
    path('<int:product_id>/update/', views.update, name='update'),
    path('<int:product_id>/delete/', views.delete, name='delete'),

    # DRF(Django Rest Framework) URL 
    path('hello/', helloAPI),
    path('<int:product_id>/productinfo', Productinfo),
    path('', include(router.urls)),

    # 장바구니 URL
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout1, name='checkout'),     # 장바구니 페이지에서 클릭한 결제 버튼
    path('<int:product_id>/checkout/', views.checkout2, name='checkout_id'),     # 상품 1개 조회 페이지에서 클릭한 결제 버튼
    path('<int:product_id>/update_item/', views.updatedItem, name='update_item'),
]

