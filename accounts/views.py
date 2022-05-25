from django.shortcuts import redirect, render
from django.contrib.auth.models import User  # django에 내장된 User 모델 import
from django.contrib import auth              # django에 내장된 auth 모델 import
from .models import Customer            # posts앱의 Customer 모델 import
from products.cartitems_tag import *    # 중복되는 코드들을 가져오기 위해 products App 내부 cartitems_tag 모듈 가져오기

# Create your views here.


# 회원가입 기능
def sign_up(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기
    context = { 'cartItems': cartItems, }

    if request.method == 'POST':              # HTTP Request가 POST방식일 때, 
        if (request.POST.get('username') and  # POST로 전달한 username 데이터가 있고, 
            request.POST.get('password') and  # password 데이터가 있고,
            request.POST.get('password') == request.POST.get('password_check')):   # password와 password_check 데이터가 같다면

            new_user = User.objects.create_user(          # User 모델에 새로운 회원을 추가해주기 
                username = request.POST.get('username'),  # username과 password라는 이름으로 받은 데이터로 회원가입 진행
                password = request.POST.get('password'),
            )

            name = request.POST.get('nickname')           # 회원가입 시 입력한 nickname 데이터를 name 변수에 저장
            email = request.POST.get('email')             # 회원가입 시 입력한 email 데이터를 email 변수에 저장
            problem = request.POST.get('social')          # 회원가입 시 선택한 problem 데이터를 problem 변수에 저장
            customer = Customer(user=new_user, name=name, email=email, problem=problem)   
            # 회원가입이 되면, User 모델과 1:1관계로 되어있는 Customer 모델의 user 필드 / name 필드 / email 필드 / problem 필드에 값을 저장
            customer.save()


            auth.login(request, new_user)             # 회원가입이 완료 되면, auth 모듈의 login 함수를 이용해서 해당 유저를 로그인 시키기

            return redirect('products:index')            # 로그인이 된 다음에는 메인 페이지 보여주기

        else:
            context['error'] = '아이디와 비밀번호를 다시 입력해주세요.' 
            # 만약, 조건을 만족하지 못할 때는 context 딕셔너리에 error라는 key를 저장해서 오류 메세지를 출력하게끔 하기     


    return render(request, 'accounts/sign_up.html', context)   # POST방식이 아닌 GET방식의 HTTP Request라면 회원가입 페이지 보여주기



# 로그인 기능
def login(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기


    if request.method == 'POST':                      # HTTP Request가 POST방식일 때, 
        if request.POST.get('username') and request.POST.get('password'): # POST로 전달한 username 데이터와 password 데이터가 있다면

            user = auth.authenticate(                 # auth 모듈의 authenticate 함수를 통해서 해당 정보로 가입된 유저가 있는지 체크
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            if user is not None:             # authenticate 함수 결과로 유저가 있으면 user 인스턴스가 return되고 없으면 None를 return
                auth.login(request, user)    # 유저가 인증되면 login 함수로 로그인 시켜주기
                return redirect('products:index')  # 로그인 후 메인페이지 보여주기

            else:                               # authenticate 함수 결과로 None를 반환하면, context 딕셔너리에 error key를 저장
                context['error'] = '아이디와 비밀번호를 다시 입력해주세요!' 

        else:                                   # 아이디와 비밀번호 둘 중 하나라도 입력하지 않으면, 모두 입력하라는 에러 메시지 저장
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요!'         

    context = { 'cartItems': cartItems, }

    return render(request, 'accounts/login.html', context)  # POST방식이 아니라면 로그인 페이지 보여주기



# 로그아웃 기능
def logout(request):
    if request.method == 'POST':                # 만약 HTTP Request가 POST방식이라면,
        auth.logout(request)                    # auth 모듈의 logout 함수를 통해 쿠키와 세션 정보를 초기화해서 로그아웃 시키기

    return redirect('products:index')              # POST방식이 아니라면 메인 페이지 보여주기



# 마이페이지 기능
def mypage(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    context = { 'cartItems': cartItems, }

    return render(request, 'accounts/mypage.html', context)


# 마이페이지 수정
def mypage_update(request):
    cartItems_data = cartitems_count(request)  # products 앱 내부 cartitems_tag 모듈에 있는 cartitems_count 함수 가져오기
    cartItems = cartItems_data['cartItems']    # cartitems_count 함수의 cartItems 값 가져오기

    if request.method == 'POST':                         # 마이페이지 정보 수정인 POST방식으로 요청이 올 때
        request.user.username = request.POST.get('id')   # 로그인한 유저의 id를 수정하기 위해 해당 코드 작성
        customer = request.user.customer                 # 로그인한 유저의 customer 정보에 접근
        customer.name = request.POST.get('nickname')     # 해당 customer의 정보 수정
        customer.email = request.POST.get('email')
        customer.problem = request.POST.get('problem')
        request.user.save()                              # 수정된 id 정보 저장
        customer.save()                                  # 수정된 customer 정보 저장

        return redirect('accounts:mypage')

    context = { 'cartItems': cartItems, }

    return render(request, 'accounts/mypage_update.html', context)