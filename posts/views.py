from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.views.generic import ListView
from products.cartitems_tag import *      # 중복되는 코드들을 가져오기 위해 products App 내부 cartitems_tag 모듈 가져오기

# Create your views here.



# 입점 소셜벤처 보여주기
class BrandListView(ListView):              # Brand 모델 데이터 ListVIew로 가져오기
    model = Brand
    template_name = 'posts/brands.html'
    queryset = Brand.objects.all().order_by('-id')  # 쿼리셋 설정으로 데이터 순서 내림차순 정렬

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cartItems_data = cartitems_count(self.request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
        cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기
        context['cartItems'] = cartItems
        return context



# 브랜드 상세페이지 보여주기
def brand(request, brand_id):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    brand = Brand.objects.get(id=brand_id)   # brand_id로 brand 데이터 1개 조회

    products = brand.brand_product.all()     # 해당 brand에 속한 products 데이터만 조회하기

    context = {
        'brand': brand,
        'products': products,
        'cartItems': cartItems,
    }

    return render(request, 'posts/brand.html', context)


# 사회문제 페이지 보여주기
def socialproblem(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    problems = Problem.objects.all()     # Problem 모델에 담겨있는 모든 사회문제들 가져오기

    
    selected_problem = int(request.GET.get('socialproblem', 1))   # 사회문제 페이지에서 선택된 문제의 pk 받기 / int()로 정수화 / default로 0 설정
    if selected_problem:                                          # 만약 사회문제가 선택되었다면,
        selected_problem = Problem.objects.get(id=selected_problem)  # Problem 모델에서 받은 pk로 조회한 데이터를 저장
        selected_brands = selected_problem.brand_set.all()        # 선택된 문제와 1:N관계를 가지는 브랜드들을 조회

    context = {
        'problems': problems,
        'selected_problem': selected_problem,
        'selected_brands': selected_brands,
        'cartItems': cartItems,
    }

    return render(request, 'posts/socialproblem.html', context)


# 공지사항 게시판 보여주기
def board(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    posts = Post.objects.all().order_by('-created_at')  # Post 모델 데이터 최신순으로 가져오기

    context = {
        'cartItems': cartItems,
        'posts': posts,
    }

    return render(request, 'posts/board.html', context)


# 공지사항 게시판 생성하기
def board_create(request):
    posts_category = Post.Category.choices  # GET 방식으로 request 시, 카테고리 선택할 수 있도록 Post 모델의 Category 클래스에 접근해서 항목들을 보내주기
    context = {
        'posts_category': posts_category,
    }

    if request.method == 'POST':            # POST 방식으로 request 시 글 생성할 수 있도록 하기
        title = request.POST.get('title')
        category = request.POST.get('category')
        print(category)
        body = request.POST.get('body')
        Post.objects.create(author=request.user.customer, title=title, category=category, body=body)  
        # Post 모델 데이터 생성 시, author 필드는 로그인 된 유저로 설정 
        # 단, request.user의 customer로 접근해야 한다. author 필드는 Customer 모델이랑 1:N관계이기 때문
        return redirect('posts:board')

    return render(request, 'posts/board_create.html', context)


# 공지사항 게시판 글 조회하기
def board_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # login_user = request.user.customer       # 로그인된 유저의 customer 정보 가져오기
    # post_author = post.author                # 게시글 작성자 정보 가져오기
    # print(login_user == post_author)         # True로 출력이 되므로 위의 2개의 변수가 서로 같다는 것을 확인

    context = {
        'post': post,
        # 'user': login_user,
        # 'author': post_author,
    }

    return render(request, 'posts/board_detail.html', context)


# 공지사항 게시판 글 수정하기
def board_edit(request, post_id):
    posts_category = Post.Category.choices  # GET 방식으로 request 시, 카테고리 수정할 수 있도록 Post 모델의 Category 클래스에 접근해서 항목들을 보내주기
    post = Post.objects.get(id=post_id)

    context = {
        'posts_category': posts_category,
        'post': post,
    }

    if request.method == 'POST':               # POST 방식으로 request 되었을 때 수정 페이지에서 받은 데이터로 Post 데이터 수정하기
        post.title = request.POST.get('title')
        post.category = request.POST.get('category')
        post.body = request.POST.get('body')
        post.save()
        return redirect('posts:board')

    return render(request, 'posts/board_edit.html', context)


# 공지사항 게시판 글 삭제하기
def board_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:board')


