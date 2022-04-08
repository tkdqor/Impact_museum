from multiprocessing import context
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



# 브랜드 상세페이지 보여주기
def brand(request, brand_id):

    brand = Brand.objects.get(id=brand_id)   # brand_id로 brand 데이터 1개 조회

    products = brand.brand_product.all()     # 해당 brand에 속한 products 데이터만 조회하기

    context = {
        'brand': brand,
        'products': products,
    }

    return render(request, 'posts/brand.html', context)


# 사회문제 페이지 보여주기
def socialproblem(request):

    problems = Problem.objects.all()

    context = {
        'problems': problems,
    }

    return render(request, 'posts/socialproblem.html', context)


