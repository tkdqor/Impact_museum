from django.http import HttpResponse
from django.urls import path, include
from . import views
from .views import BrandListView, PostModelViewSet, BrandModelViewSet, ProblemModelViewSet

from rest_framework import routers



# DRF routers 설정
router = routers.DefaultRouter()           # DefaultRouter이기 때문에 API - ROOT 페이지가 생성됨
router.register('posts', PostModelViewSet)       # PostModelViewSet 설정
router.register('brands', BrandModelViewSet)     # BrandModelViewSet 설정
router.register('problems', ProblemModelViewSet) # ProblemModelViewSet 설정


# URL name 설정
app_name = 'posts'


urlpatterns = [
    # 입점 소셜벤처 URL
    path('brands/', BrandListView.as_view(), name='brands'),
    # 소셜벤처 디테일 URL
    path('brands/<int:brand_id>/', views.brand, name='brand'),

    # 사회문제 URL
    path('socialproblem/', views.socialproblem, name='socialproblem'),

    # 공지사항 게시판 URL
    path('board/', views.board, name='board'),
    # 공지사항 게시판 생성 URL
    path('board/create/', views.board_create, name='board_create'),
    # 공지사항 게시판 조회 URL
    path('board/<int:post_id>/', views.board_detail, name='board_detail'),
    # 공지사항 게시판 수정 URL
    path('board/<int:post_id>/edit/', views.board_edit, name='board_edit'),
    # 공지사항 게시판 삭제 URL
    path('board/<int:post_id>/delete/', views.board_delete, name='board_delete'),

    # DRF(Django Rest Framework) URL 
    path('drf/', include(router.urls)), # posts/drf/로 API ROOT 설정
]


