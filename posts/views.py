from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework import viewsets
import json
from django.db.models import Q     # 검색기능구현 시, filter 조건을 or로 설정하기 위해 Q 함수 import

# Create your views here.


# 메인 화면
def index(request):
    if request.user.is_authenticated:      # 로그인이 되었을 경우, 로그인된 유저의 정보와 연동된 customer 인스턴스를 customer 변수에 저장
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) # 그 customer 인스턴스가 pk로 있는 order 인스턴스를 저장

        print(order)
        print(created)

        items = order.orderitem_set.all()  

        cartItems = order.get_cart_items                  # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기 - Order모델에 정의된 get_cart_items 함수 사용
    else:
        items = []                                        # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것 
        cartItems = order['get_cart_items']    
        # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정


    posts = Post.objects.all().order_by('-id')[:8] # Post 모델 데이터 전체에서 id필드 기준 역순으로 8개만 가져오기

    # 검색기능을 위해 query라는 변수를 지정하고 GET 방식으로 들어온 데이터를 조회
    query = request.GET.get('query', '')
    if query:
        posts = Post.objects.all().filter(Q(product_name__icontains=query) | Q(brand__icontains=query))  
        # 만약 검색한 데이터가 있다면, Post 모델에서 필터기능으로 해당 단어가 포함된 데이터만 전달 / 상품명 또는 브랜드를 검색할 수 있게 Q 함수 사용

    context = {
        'posts': posts,
        'cartItems': cartItems,    # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.
        'query': query,
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
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  
        # 로그인한 customer에 해당하는 사람을 Order 모델에서도 찾아서, 즉 같은 customer를 찾아서 그 사람이 주문한 order를 가져오는데,
        # complete 필드가 False인 DB 정보를 가져와주는 것(만약 없다면 생성)
        # 그리고 이 코드를 쓰는 이유는, 그냥 DB상 데이터 생성의 중복을 막을 수 있기 때문이다!!
        items = order.orderitem_set.all()  # order 모델에서 orderitem 모델에 접근하여 -> 해당 order의 orderitem DB 전부를 가져오기 

        cartItems = order.get_cart_items   # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기
    else:
        items = []  # cart.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것 
        cartItems = order['get_cart_items']              
        # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정 

    context = {'items': items, 'order':order, 'cartItems': cartItems}  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.

    return render(request, 'posts/cart.html', context)




# 상품 1개 조회 페이지 -> 결제 화면
def checkout2(request, post_id):
    if request.user.is_authenticated:
        
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        items = order.orderitem_set.all()   

        cartItems = order.get_cart_items    # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기

        post = Post.objects.get(id=post_id)     # 해당 상품 데이터를 Post 모델에서 가져오고
        # Order 모델에 새로운 일자로 데이터 생성해야 됨..?!   

    else:
        items = []  # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것   
        cartItems = order['get_cart_items']               
        # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정

    context = {'post': post, 'items': items, 'order':order, 'cartItems': cartItems}  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.

    return render(request, 'posts/checkout.html', context)



# 장바구니 페이지 -> 결제 화면
def checkout1(request):
    if request.user.is_authenticated:
        
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        items = order.orderitem_set.all()   

        cartItems = order.get_cart_items    # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기

        
    else:
        items = []  # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것   
        cartItems = order['get_cart_items']               
        # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정

    context = {'items': items, 'order':order, 'cartItems': cartItems}  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.     
    
    return render(request, 'posts/checkout.html', context)






# 장바구니 추가 기능
def updatedItem(request, post_id):
    data = json.loads(request.body)     # cart.js에서 보내준 body의 정보를 json 형태로 불러오기 
    postID = data['postID']             # cart.js의 fetch -> body에서 정의한 변수의 이름과 같게 설정.
    action = data['action']
    print(data)                         # 장바구니 버튼을 클릭할 때 받은 데이터가 cart.js로부터 전달되었는지 터미널로 먼저 확인하기.
    print('postID:' , postID)           # 해당 정보들을 id와 action으로 구분지어서 확인하기.
    print('action:' , action)

    customer = request.user.customer    # 로그인 된 해당 유저를 Customer 모델에서 가져온다는 의미(user모델에서 OneonOne관계로 customer모델로 접근)
    post = Post.objects.get(id=postID)  # 장바구니를 누른 해당 상품의 id로 Post DB에 저장되어있는 정보 가져오기.
    order, created = Order.objects.get_or_create(customer=customer, complete=False)     
    # Order 모델에서 로그인 된 해당 customer의 order가 이미 있다면 -> 생성하지 말고 그냥 가져오기  /  없다면 order DB 생성하기
    # .get_or_create(~~~, ~~~) -> 이렇게 괄호안에 있는 내용들이 모두 조건인가? 그래서 해당 조건을 만족하는 DB가 있으면 가져오고 없으면 생성?
    # 또한, complete=False로 설정했기 때문에 가져올 때 주문이 완료 되지 않은 정보만 가져오라는 의미인 것 같다! 
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=post)     
    # OrderItem 모델 - order 필드에 위에서 가져온 order와 동일한 order_id 그리고 product 필드에는 장바구니를 누른 해당 상품이 
    # 새롭게 들어가야 하므로 DB에서 새로운 데이터가 생성된다!(기존에는 이러한 값을 가진 데이터가 없었기 때문 / order_id는 같을지라도 상품은 없었다.)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)    # 만약 button을 누를 때 action이 add이면 orderItem 변수에 있는 db정보의 quantity를 1 증가 시키기.
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)    # 만약 button를 누를 때 action이 remove이면 orderItem 변수에 있는 db정보의 quantity를 1 감소 시키기.

    orderItem.save()      # 위에서 변경된 내용 저장.

    if orderItem.quantity <= 0:         # 만약 장바구니로 추가된 상품의 수량이 0과 같거나 작으면 해당 데이터 삭제
        orderItem.delete()

    return JsonResponse('Item added', safe=False)






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






