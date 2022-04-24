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
]


