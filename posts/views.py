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

    problems = Problem.objects.all()     # Problem 모델에 담겨있는 모든 사회문제들 가져오기

    
    selected_problem = int(request.GET.get('socialproblem', 1))   # 사회문제 페이지에서 선택된 문제의 pk 받기 / int()로 정수화 / default로 0 설정
    if selected_problem:                                          # 만약 사회문제가 선택되었다면,
        selected_problem = Problem.objects.get(id=selected_problem)  # Problem 모델에서 받은 pk로 조회한 데이터를 저장
        selected_brands = selected_problem.brand_set.all()        # 선택된 문제와 1:N관계를 가지는 브랜드들을 조회

    context = {
        'problems': problems,
        'selected_problem': selected_problem,
        'selected_brands': selected_brands,
    }

    return render(request, 'posts/socialproblem.html', context)


