from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [ 
    # 회원가입 페이지 URL
    path('sign_up/', views.sign_up, name='sign_up'),
    # 로그인 페이지 URL
    path('login/', views.login, name='login'),
]