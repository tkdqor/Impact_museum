from django.http import HttpResponse
from django.urls import path, include
from . import views
from .views import BrandListView

# URL name 설정
app_name = 'posts'


urlpatterns = [
    # 입점 소셜벤처 URL
    path('brands/', BrandListView.as_view(), name='brands'),

    # 소셜벤처 디테일 URL
    path('brands/<int:brand_id>/', views.brand, name='brand'),
]


