"""impactmuseum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings             # settings.py 참조를 위한 import
from posts import views


urlpatterns = [
    # admin 페이지 관련 URL
    path('admin/', admin.site.urls),

    # posts App과 관련된 URL
    path('', views.index),                   # request URL이 없이 도메인으로 접속했을 떄 메인화면 보여주기
    path('posts/', include('posts.urls')),

    # accounts App과 관련된 URL
    path('accounts/', include('accounts.urls')),
]


# 이미지 URL 설정 - media 파일의 경우, django 개발 서버에서 서빙을 지원하지 않으므로 직접 URL를 추가해야 한다.
if settings.DEBUG:                                            # settings의 DEBUG 옵션이 TRUE일 경우에만 이미지 파일 serving 허용
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





