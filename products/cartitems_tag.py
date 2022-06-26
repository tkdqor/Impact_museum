from django import template
from .models import Order


def cartitems_count(request):              # 로그인이 되었을 경우, 로그인된 유저의 정보와 연동된 customer 인스턴스를 customer 변수에 저장
    if request.user.is_authenticated: 
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 그 customer 인스턴스가 pk로 있는 order 인스턴스를 저장
        items = order.orderitem_set.select_related('product').all()  # order 모델에서 orderitem 모델에 접근하여 -> 해당 order의 orderitem DB 전부를 가져오기
        # select_related 메소드로 lazy-loading를 방지하고 product 데이터를 ORM 코드에서 같이 가져오기

        cartItems = order.get_cart_items   # 특정 order에 해당되는 orderitem의 수량을 전부 합한 값을 가져오기 - Order모델에 정의된 get_cart_items 함수 사용
    
    else:
        items = []                         # checkout.html에 아무것도 보내주지 않는다는 것을 의미 
        order = {'get_cart_total':0, 'get_cart_items':0}   # 로그인하지 않아도 화면을 볼 수 있게 order 변수를 정의해주는 것 
        cartItems = order['get_cart_items']                # 마찬가지로 로그인하지 않아도 화면을 볼 수 있게 설정 
        # 오류가 나지 않게 하기 위해 바로 윗줄에서 정의한 order 변수에 키값으로 접근해서 get_cart_items이 0이 되게끔 설정
    
    return {
        'items': items,
        'order':order,
        'cartItems': cartItems,
    }


