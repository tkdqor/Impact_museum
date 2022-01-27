from django.urls import path, include
from . import views
from .views import helloAPI, Postinfo
from rest_framework import routers


# DefaultRouter 설정
router = routers.DefaultRouter()
router.register('viewset', views.PostViewSet)

# URL 설정
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('hello/', helloAPI),
    path('<int:post_id>/postinfo', Postinfo),
    path('', include(router.urls)),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:post_id>/update_item/', views.updatedItem, name='update_item'),
]

