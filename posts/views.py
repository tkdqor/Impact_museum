from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.


# 메인 화면
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'posts/index.html', context)


# 상품 1개 조회
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


# 상품 1개 생성
def new(request):
    return render(request, 'posts/new.html')


# 상품 1개 생성
def create(request):
    product_name = request.POST.get('product_name')
    brand = request.POST.get('brand')
    post = Post(product_name=product_name, brand=brand, created_at=timezone.now())
    post.save()

    return redirect('posts:detail', post_id=post.id)


# 상품 1개 수정
def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }

    return render(request, 'posts/edit.html', context)


# 상품 1개 수정
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    post.product_name = request.POST.get('product_name')
    post.brand = request.POST.get('brand')
    post.save()

    return redirect('posts:detail', post_id=post.id)


# 상품 1개 삭제
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:index')



# 장바구니 화면
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 완료된 주문인지 잡아준다는게 뭘까..
        # 로그인한 customer에 해당하는 사람을 Order 모델에서도 찾아서, 즉 같은 customer를 찾아서 그 사람이 주문한 order만
        # 가져와주는 것 아닐까? 
        # 그리고 이 코드를 쓰는 이유는, 그냥 DB상 데이터 생성의 중복을 막을 수 있기 때문이다!!
        # 그리고 생각해보니!!!! 위의 코드에서 complete=False를 아예 안써야 하는 거 아닌가?!?!?!
        items = order.orderitem_set.all()   
    else:
        items = []  # cart.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것   

    context = {'items': items, 'order':order}

    return render(request, 'posts/cart.html', context)




# 결제 화면
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        items = order.orderitem_set.all()   
    else:
        items = []  # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것   

    context = {'items': items, 'order':order}

    return render(request, 'posts/checkout.html', context)






# RDF를 이용한 문자열 응답 API
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello World!")


# RDF를 이용한 상품 정보 1개에 대한 API
@api_view(['GET'])
def Postinfo(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)

    return Response(serializer.data)


# RDF를 이용한 CRUD API 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


