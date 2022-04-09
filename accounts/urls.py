from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [ 
    # 회원가입 페이지 URL
    path('sign_up/', views.sign_up, name='sign_up'),
    # 로그인 페이지 URL
    path('login/', views.login, name='login'),
    # 로그아웃 URL
    path('logout/', views.logout, name='logout'),
    # 마이페이지 URL
    path('mypage/', views.mypage, name='mypage'),
    # 마에페이지 수정 URL
    path('mypage/update/', views.mypage_update, name="mypage_update"),
]