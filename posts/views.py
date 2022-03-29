from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.views.generic import ListView

# Create your views here.



# 입점 소셜벤처 보여주기
class BrandListView(ListView):              # Brand 모델 데이터 ListVIew로 가져오기
    model = Brand
    template_name = 'posts/brands.html'
    queryset = Brand.objects.all().order_by('-id')  # 쿼리셋 설정으로 데이터 순서 내림차순 정렬



def brand(request, brand_id):

    return render(request, 'posts/brand.html')


