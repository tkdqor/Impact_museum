from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
import json
from django.db.models import Q     # 검색기능구현 시, filter 조건을 or로 설정하기 위해 Q 함수 import
from django.http import Http404    # 상품 1개 조회 시, 예외처리를 위한 Http404 import 
from .cartitems_tag import *       # 중복되는 코드들을 가져오기 위해 products App 내부 cartitems_tag 모듈 가져오기

# DRF 관련 import
from .serializers import ProductModelSerializer, OrderModelSerializer, OrderItemModelSerializer
from rest_framework.viewsets import ModelViewSet


# 메인 화면
def index(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    products = Product.objects.all().order_by('-id')[:8] # Product 모델 데이터 전체에서 id필드 기준 역순으로 8개만 가져오기


    # 검색기능을 위해 query라는 변수를 지정하고 GET 방식으로 들어온 데이터를 조회
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.all().filter(Q(product_name__icontains=query) | Q(brand__name__icontains=query))  
        # 만약 검색한 데이터가 있다면, Product 모델에서 필터기능으로 해당 단어가 포함된 데이터만 전달 / 상품명 또는 브랜드를 검색할 수 있게 Q 함수 사용

    context = {
        'products': products,
        'cartItems': cartItems,    # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.
        'query': query if query else '상품 이름이나 브랜드를 검색해 보세요!',
        }
    return render(request, 'products/products.html', context)



# 상품 1개 조회
def detail(request, product_id):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    # try:
    #     product = Product.objects.get(id=product_id)
    #     context = {
    #         'product': product,
    #         'cartItems': cartItems,
    #     }
    # except Product.DoesNotExist:           # DoesNotExist 오류가 발생했을 때는 Http404, 즉 Page not found 오류를 띄우게 설정
    #     raise Http404

    product = get_object_or_404(Product, pk=product_id)  # get_object_or_404를 사용해서 더 간결하게 에외처리 설정 완료

    context = {
            'product': product,
            'cartItems': cartItems,
        }

    return render(request, 'products/product.html', context)



# 상품 1개 생성 페이지
def new(request):
    return render(request, 'products/product_new.html')



# 상품 1개 생성 기능
def create(request):
    product_name = request.POST.get('product_name')
    brand = request.POST.get('brand')
    product = Product(product_name=product_name, brand=brand, created_at=timezone.now())
    product.save()

    return redirect('products:detail', product_id=product.id)



# 상품 1개 수정 페이지
def edit(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/product_edit.html', context)



# 상품 1개 수정 기능
def update(request, product_id):
    product = Product.objects.get(id=product_id)
    product.product_name = request.POST.get('product_name')
    product.brand = request.POST.get('brand')
    product.save()

    return redirect('products:detail', product_id=product.id)



# 상품 1개 삭제
def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    return redirect('products:index')



# 장바구니 화면
def cart(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기
    items = cartItems_data['items']            # cartitems_count 함수의 items 값 가져오기
    order = cartItems_data['order']            # cartitems_count 함수의 order 값 가져오기

    context = {
        'items': items, 
        'order':order, 
        'cartItems': cartItems
    }  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.

    return render(request, 'products/cart.html', context)



# 상품 1개 조회 페이지 -> 결제 화면
def checkout2(request, product_id):
    if request.user.is_authenticated:
        
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        items = order.orderitem_set.all()   

        cartItems = order.get_cart_items    # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기

        product = Product.objects.get(id=product_id)     # 해당 상품 데이터를 Product 모델에서 가져오고
        # Order 모델에 새로운 일자로 데이터 생성해야 됨..?!   

    else:
        items = []  # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}  # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것   
        cartItems = order['get_cart_items']               
        # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정
        return redirect('products:index')

    context = {'product': product, 'items': items, 'order':order, 'cartItems': cartItems}  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.

    return render(request, 'products/checkout.html', context)



# 장바구니 페이지 -> 결제 화면
def checkout1(request):

    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기
    items = cartItems_data['items']            # cartitems_count 함수의 items 값 가져오기
    order = cartItems_data['order']            # cartitems_count 함수의 order 값 가져오기

    context = {'items': items, 'order':order, 'cartItems': cartItems}  # 장바구니 개수를 표현하기 위해 cartItems 변수를 같이 보내줘야 한다.     
    
    return render(request, 'products/checkout.html', context)



# 장바구니 추가 기능
def updatedItem(request, product_id):
    data = json.loads(request.body)      # cart.js에서 보내준 body의 정보를 json 형태로 불러오기 
    productID = data['productID']        # cart.js의 fetch -> body에서 정의한 변수의 이름과 같게 설정
    action = data['action']
    print(data)                          # 장바구니 버튼을 클릭할 때 받은 데이터가 cart.js로부터 전달되었는지 터미널로 먼저 확인하기
    print('productID:' , productID)      # 해당 정보들을 id와 action으로 구분지어서 확인해보기
    print('action:' , action)

    customer = request.user.customer    # 로그인 된 해당 유저를 Customer 모델에서 가져온다는 의미(user모델에서 OneonOne관계로 customer모델로 접근)
    product = Product.objects.get(id=productID)  # 장바구니를 누른 해당 상품의 id로 Post DB에 저장되어있는 정보 가져오기
    order, created = Order.objects.get_or_create(customer=customer, complete=False)     
    # Order 모델에서 로그인 된 해당 customer의 order가 이미 있다면 -> 생성하지 말고 그냥 가져오기 / 없다면 order DB 생성하기
    # 또한, complete=False로 설정했기 때문에 가져올 때 주문이 완료 되지 않은 정보만 가져오라는 의미
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)     
    # OrderItem 모델 - order 필드에 위에서 가져온 order와 동일한 order_id 그리고 product 필드에는 장바구니를 누른 해당 상품이 
    # 새롭게 들어가야 하므로 DB에서 새로운 데이터가 생성됨(기존에는 이러한 값을 가진 데이터가 없었기 때문 / order_id는 같을지라도 상품은 없었다.)

    if action == 'add':
        orderItem.quantity += 1    # 만약 button을 누를 때 action이 add이면 orderItem 변수에 있는 db정보의 quantity를 1 증가 시키기
    elif action == 'remove':
        orderItem.quantity -= 1    # 만약 button를 누를 때 action이 remove이면 orderItem 변수에 있는 db정보의 quantity를 1 감소 시키기

    orderItem.save()      # 위에서 변경된 내용 저장

    if orderItem.quantity < 1:         # 만약 장바구니로 추가된 상품의 수량이 1보다 작으면 해당 데이터 삭제
        orderItem.delete()

    return JsonResponse('Item quantity modify', safe=False)


# 장바구니 상품 제거
def cart_delete(request, product_id):
    customer = request.user.customer              # 로그인된 customer 정보 가져오기
    product = Product.objects.get(id=product_id)  # product_id에 해당하는 상품 정보 가져오기
    order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 조건에 맞는 order 데이터 조회   
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product) # 조건에 맞는 orderItem 데이터 조회  

    orderItem.delete() # orderItem 데이터 삭제

    return redirect('products:cart') 




# DRF View 설정

# Product 모델
class ProductModelViewSet(ModelViewSet):      # ModelViewSet을 상속받아 기본적인 CRUD가 가능한 Product Model API 서버 설정
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer # serializers.py에서 정의한 ProductModelSerializer 설정

# Order 모델
class OrderModelViewSet(ModelViewSet):        
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

# OrderItem 모델
class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemModelSerializer




