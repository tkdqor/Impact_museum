# :pushpin: Impact museum
- 사회적 가치를 추구하는 소셜벤처 이커머스 플랫폼
- 다양한 사회적 문제를 해결하는 소셜벤처들을 소개하고 해당 브랜드의 상품들을 확인할 수 있는 웹 서비스 

<br>

## 1. 제작 기간 & 참여 인원
- 2021년 2월 12일 ~
- 개인 프로젝트
<br>

## 2. 사용 기술
**Back-end**       

**언어**
- Python 3.9.1 

**프레임워크**
- Django 3.2.9

**개발환경**
- VSCode

**DBMS**
- MySQL 8.0.28

**DB 관리 툴**
- DBeaver 22.0.2 (GUI(Graphical User Interface)가 제공되기 때문에 손쉽게 데이터베이스를 관리할 수 있어 선택)

**클라우드 서버 활용**
- AWS(Amazon Web Service)
  - RDS (MySQL 데이터베이스 서버)

**API 활용(소셜 로그인)**
- Google Cloud Platform
- Kakao developers

**버전관리**
- Git
- Github

<br>

## 3. ERD 설계
![Untitled Diagram-Page-1](https://user-images.githubusercontent.com/95380638/162469471-75ac1835-d2c5-4a49-ad4f-9c521a140ca8.png)


- Customer 모델은 User 모델과 1:1관계로 설정
- Customer 모델과 Order 모델은 1:N관계로 설정 - 1명의 사용자가 쇼핑몰에서 여러 번 주문할 수 있기 때문
- Customer 모델 & Order 모델과 Shipping Address 모델은 1:N관계로 설정 - 1명의 사용자가 다양한 배송 주소지를 생성할 수 있고, 1개의 주문 건이 배송 취소 및 실패 등으로 다양한 배송 주소지를 가질 수 있음
- Product 모델 & Order 모델과 Order Item 모델(장바구니에 추가된 상품 데이터 모델)은 1:N관계로 설정 - 1개의 상품이 여러 번 장바구니에 포함될 수 있고, 1개의 주문 건에 많은 상품들이 장바구니에 추가될 수 있음
- Problem 모델과 Brand 모델은 1:N관계로 설정 - 1개의 사회문제를 해결하기 위해 노력하는 브랜드가 여러 개가 있을 수 있기 때문에 1:N으로 설정 
- Brand 모델과 Product 모델은 1:N관계로 설정 - 1개의 브랜드가 impactmuseum에 입점하고 여러 개의 상품들을 판매할 수 있기 때문
- Customer 모델과 Post 모델은 1:N관계로 설정 - 1명의 사용자 또는 관리자가 여러 개의 글을 남길 수 있기 때문
<br>

## 4. 핵심 기능     
- 이 서비스의 핵심 기능은 ...입니다.     => 해당 기능을 왜 구현하려고 했는지 이유 필요!
<details>
  <summary>핵심 기능 설명 펼치기</summary>
  
  4.1 상품 정보에 관련된 기본적인 CRUD 구축
  
  4.2 DRF(Django Rest Framework)를 기반으로 CRUD API 서버 구축
  
  4.3 URL Configuration으로 app별 URL 관리
  
  4.4 Template & Static Inheritance 설정 완료 및 app별 namespacing 설정 완료
  
  4.5 DB 구성 및 ERD 설계 완료(이미지 저장 및 랜더링 가능)
  
  4.6 상품 1개 조회 페이지에서 장바구니 버튼 클릭 시, 장바구니 페이지에 추가 및 DB 저장 
  
  4.7 모델 내 필드 추가 및 속성 변경      
      - Customer 모델 : user 필드 null, blank = False로 변경 / name 필드 null = False로 변경 (user와 name필드가 비어 있으면 안되기 때문)       
      - Post(Product) 모델 : price 필드를 floatField에서 PositiveIntegerField로 변경 (가격이니까 실수보다는 양의 정수로 수정하는 게 맞다고 판단) / created_at 필드는 DateTimeField에 auto_now_add=True 옵션을 추가. (상품 데이터가 언제 생성되었는지 필요하기 때문.) / updated_at 필드를 새로 생성하고 DateTimeField의 auto_now=True 옵션을 추가. (상품 데이터를 수정했을 때 기록을 남기기 위해서 날짜가 갱신되어야 한다.)       
      - OrderItem 모델 : quantity 필드가 원래 null=True, blank=True 였으나 null=False, blank=False로 수정. (수량은 비어있으면 안되고 최소 1개로 설정되어야 하기 때문)
  
  version 2.1 IPython 8.0.1 설치
      - 설치한 이유는, 문법에 따라서 색상으로 강조를 해줘서 기존의 장고 연동 shell보다 작성하기 편함. 그리고 여러 줄에 걸쳐서 코드 입력 후, 위쪽 화살표로 전체 코드를 다시 불러오기가 편리함.
  
  version 2.1 Admin 페이지 개선
      - admin.py 에서 admin모듈의 ModelAdmin 클래스를 상속받아서 모델 클래스를 정의하고, register 장식자를 이용해 admin에 등록
      - 그리고 나서 클래스의 list_display 속성을 추가하여 -> admin페이지에 모델 별 필드를 표시해서 모델 데이터를 한눈에 파악할 수 있도록 개선
  
  version 2.2 (1) Admin 페이지 개선
          - admin.py에서 mark_safe 함수를 사용해서 Post 모델 객체의 이미지 url를 admin 페이지에서 볼 수 있도록 이미지으로 표시     
          - settings.py에서 MEDIA_URL과 MEDIA_ROOT를 수정하고 models.py에서 Post 모델 ImageField에 upload_to 속성을 설정 / posts앱의 post모델 디렉터리 밑에 년/월/일 디렉터리로 구분하여 더 깔끔하게 관리할 수 있도록 설정.
  
  version 2.2 (2) 메인 화면에서 검색 기능 구현
          - index.html에서 form element를 사용 / action attribute를 비워두어서 현재 form이 있는 같은 주소로 URL를 request하게 되고 Input element에 name를 query로 설정해서 값을 전송하고 / value도 query로 설정해서 검색한 이후에도 값이 남아있게끔 설정       
          - View index 함수에서 query라는 변수를 지정하고 GET 방식으로 들어온 query라는 이름으로 담긴 값을 담아준다. 그리고 query가 있을 때(검색했을 때) Post 모델 전체를 조회한 posts 변수를 다시 정의해서, filter를 통해 검색한 값이 포함되는 데이터로 설정. Q 함수를 import 해서 제품명 또는 브랜드명을 검색할 수 있도록 설정.
  
  version 2.4 상품 목록을 보여주는 메인 페이지 상품 개수 수정
      - index View 함수에서 posts = Post.objects.all().order_by('-id')[:8] -> 이렇게 전체 Post 데이터에서 id필드를 기준으로 역순처리하고, 8개의 데이터만 가져오기.
      - 그래서 index 메인 페이지에는 DB에 그 이상의 데이터가 있을지라도, 8개의 상품 목록만 항상 보여줄 수 있도록 설정 완료.
  
  version 2.41 bootstrap의 navbar를 이용해서 반응형 웹사이트가 될 수 있게 설정
       - 아직 메인 상품 목록은 되지 않음 / navbar만 반응
       - 상품 상세 페이지도 아직 미반영
  
  version 2.42 상품 1개 조회 시, DoesNotExist 오류가 발생했을 때는 Http404, 즉 Page not found 오류를 띄울 수 있게 설정
       - 그래서 posts 앱의 views.py에 상품 1개 조회 시, 예외처리를 위해 Http404 import 진행
       - 404에러는 서버에서 요청한 리소스를 찾을 수 없는 경우를 의미
  
  version 2.5 로그인/로그아웃 및 회원가입 기능 구현   
      - Accounts App을 생성하고, 앱 내부 urls.py에서는 회원가입 / 로그인 / 로그아웃 URL 설정
      - base.html에서 로그인 및 회원가입 버튼을 누르면 -> GET방식으로 HTTP Request 진행 + {% if user.is_authenticated %} -> user라는 변수를 바로 사용할 수 있게 되므로, is_authenticated 함수를 사용 / 해당 함수는 로그인 되어있으면 True를 아니면 False를 반환하는 Boolean 함수이다. -> 따라서 로그인 되어있을 때, 로그아웃 버튼과 마이페이지 버튼을 생성하게 설정 -> 로그아웃 역시 정보 노출이 되지 않게 POST방식으로 진행  
      - sign_up.html에서는 form element로 POST방식으로 HTTP Request진행 -> 아이디 / 비밀번호 / 비밀번호 확인 / 닉네임 / 이메일을 입력받고, 관심있는 사회문제를 선택할 수 있게끔 설정      
      - login.html에서는 로그인 실패 시, 에러 메시지를 띄우고 POST방식으로 HTTP Request 진행 -> 아이디와 비밀번호만 받게끔 설정      
      - 앱 내부 views.py의 sign_up View에서는, GET방식일 경우 회원가입 페이지를 랜더링하고 POST방식일 경우 회원가입 절차 진행 => POST방식으로 전달한 username / password 데이터가 있는지 확인하고, password와 password_check데이터가 같은지 확인 -> 만약 같다면 User모델의 create_user 함수를 사용해서 username / password데이터로 User 모델에 추가(회원가입) -> 그리고 회원가입 시 입력한 nickname / email 데이터를 변수에 저장하고 User 모델과 OnetoOne관계인 Customer 모델에 해당 유저 및 데이터 추가 -> 위 과정을 다 진행한 다음, 자동으로 auth모듈의 login함수를 통해 로그인을 시키고 메인 페이지로 redirect해주기 -> 만약, 회원가입 정보를 다 받지 못한다면 context 딕셔너리에 error라는 key를 저장해서 에러 메세지 띄우기        
      - 앱 내부 views.py의 login View에서는, GET방식일 경우 로그인 페이지를 랜더링하고 POST방식일 경우 로그인 절차 진행 => POST방식으로 전달한 username / password 데이터가 있다면, auth 모듈의 authenticate 함수를 사용해서 username / password 데이터를 가진 유저가 있는지 확인 진행 -> 유저가 있다면 user 인스턴스를 return하므로, 그렇다면 auth 모듈의 login함수를 사용해서 로그인 시켜주고 바로 메인페이지로 redirect -> 만약, 그런 유저가 없다면 context에 error key 저장해서 에러 메세지 띄우기 -> 로그인 정보를 다 받지 못한다면 모두 입력하라는 에러 메세지 띄우기      
      - 앱 내부 views.py의 logout View는 POST방식일 경우 auth모듈의 logout함수를 사용해서 로그아웃 진행 -> 서버 내 쿠키와 세션 정보를 초기화        
      - +++ 추가해야 할 사항 : Customer 모델의 필드가 현재 user / name / email 이렇게 되어있는데, 여기에 사회문제와 관련된 필드를 추가해서 -> 회원가입 시 받은 정보를 DB에 저장하게끔 하기
  
  version 2.6 모델 이름을 Post에서 -> Product로 수정
      - 상품과 관련된 필드들이 Post라는 이름의 모델에 정의되어 있는 것이 맞지 않다고 판단        
      - 먼저 python manage.py migrate posts zero -> 이렇게 입력하고나서 앱이름/migrations/ 내의 마이그레이션 파일을 모두 삭제       
      - 그리고 앱 내부 파일들을 하나씩 보면서 모델명 변경으로 인해 수정해야 할 사항들 수정         
      - 그리고 나서 python manage.py make migrations posts 를 진행 -> migrations 파일 0001 생성        
      - 마지막으로 python manage.py migrate posts 진행
  
  version 2.7 Customer 모델에 problem이라는 필드 추가    
      - 회원가입 시 유저의 관심있는 사회문제를 1개 받고 그 값을 Customer 모델에 추가하기 위함 / 관심있는 한가지의 문제가 없을수도 있으니 null=True 설정    
      - Admin.py에 Customer 모델 관련해서 list_display 리스트에 problem 필드 추가.     
      - accounts 앱의 views.py -> sign_up View에서 problem = request.POST.get('social') -> 이렇게 유저가 회원가입 시 선택한 사회문제를 받아서 변수로 저장하고 customer = Customer(user=new_user, name=name, email=email, problem=problem) -> 이렇게 Customer 모델에 값을 입력하도록 설정      
  
  version 2.7 마이페이지 메뉴 클릭 시, 유저의 정보를 출력해서 보여주기      
      - accounts App 내부에 urls.py에서 마이페이지 URL를 설정하고, mypage라는 View 함수 설정     
      - 그리고 accounts 디렉터리 내부에 mypage.html을 생성해서 유저 정보 출력 / request.user.is_staff로 관리자 여부를 True/False로 확인 가능 
  
  version 2.8 products App 생성 및 모델 위치 수정      
      - 원래 posts 앱에 있었던 Customer 모델을 accounts 앱에 models.py로 이동시킴 -> 이유는 posts 앱에 모든 모델을 구성하는 것이 비효율적이라고 생각했기 때문       
      - products라는 App 생성 -> 이유는 posts App에 게시판이 아닌 상품들 관련 기능들이 있었기에 products라는 App에 해당 기능을 수행할 수 있도록 수정        
      - 기존 posts App에는 게시판을 위한 Post 모델을 posts 앱 내부 models.py에 설정
  
  version 2.9 posts App에 Brand 모델 생성   
      - posts App에 Brand 모델 생성 / 추가한 이유는, 입점 소셜벤처 페이지에서 브랜드를 소개 및 브랜드 상세 페이지를 보여주기 위해 추가   
      - 또한, Brand모델과 Product 모델 관계를 1:N으로 설정해서 입점된 브랜드의 상품들을 관리하게끔 설정
      - ERD에 해당 내용 반영    
      - Product 모델에 이미지 필드 2개 추가 → 상품 상세 페이지에서 추가 이미지를 보여주기 위함
      - 입점 소셜벤처 페이지는 ListView를 상속받아서 View로 설정     
      - 상품 상세페이지 수정 + 입점 소셜벤처 페이지 생성
  
  version 2.91 Brand 모델 및 Customer 모델 수정      
      - Brand 모델에 problem 필드 추가 / 해당 브랜드가 해결하고자 하는 사회문제를 구분해 카테고리 페이지에서 분류할 수 있도록 설정         
      - Customer 모델 user/name/email 필드에 unique 속성 부여 / 사용자ID와 닉네임, 이메일이 중복되지 않게 설정
  
  version 2.92 Brand 모델 수정      
      - Brand 모델에 image 필드 추가 / 브랜드 상세 페이지에서 보여줄 대표 이미지를 위해 필드 추가
  
  version 2.93 브랜드 상세페이지 업데이트      
      - 홈페이지 버튼 클릭 시 DB에 저장된 url로 해당 브랜드 홈페이지로 이동      
      - Brand DB에 저장된 short_content / long_content 표시      
      - 현재 판매되고 있는 해당 브랜드 제품을 Carousel을 이용해 자동으로 보여주기      
      - 이 때, 해당 상품 이미지 클릭 시 제품 상세페이지가 나오게끔 설정     
      - 제품 상세페이지에서 브랜드명 클릭 시, 브랜드 상세페이지가 나오게끔 설정
  
  version 3.0 DBMS를 MySQL로 설정     
      - MySQL로 설정한 이유는, 현재 시점에서 Oracle다음으로 가장 많이 사용하는 DBMS이기 때문에 안정적이라고 판단해서 MySQL로 설정하게 됨(https://db-engines.com/en/ranking 여기서 확인 가능)
      - 먼저 AWS에 들어가서 RDS로 들어감 -> 그리고 데이터베이스 생성 클릭. MySQL 버전은 8.0.28      
      - 해당 템플릿은 프리티어로 1년 무료 선택       
      - 해당 DB인스턴스는 → db.t3.micro 사양으로 2 vCPUs, 1GiB RAM, 네트워크: 2,085Mbps / 스토리지는 범용 SSD(gp2), 할당된 스토리지는 20 GiB / 최대 스토리지 임계값은 1,000 GiB       - AWS RDS에서 VPC 보안 그룹 설정하기       
      - DB 관리 툴인 DBeaver를 사용해서 우리가 생성한 데이터베이스 서버 연결 / DBeaver는 22.0.2버전 사용       
      - 그리고나서 DBeaver를 이용해서 impactmuseum이라는 이름의 DB생성 → DBeaver의 좌측 Navigator에 DB 생성 확인      
      - 이제 django의 settings.py로 가서 DB 엔진을 sqlite3에서 mysql로 바꾸고 값 추가해서 설정       
      - DB에 붙는 것을 도와주는 어댑터 역할, 콘센트 역할을 하는 클라이언트인 mysqlclient 설치         
      - 다시 python manage.py migrate를 진행        
        - **이 과정에서 해당 경고 발생, 알아보기** --> WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-sql-mode       
      - DBeaver에서 새로고침하면 테이블이 생성되어 데이터 추가 완료
  
  version 3.1 Posts 앱 내부 models.py에 Problem이라는 모델 클래스 추가    
      - 사회문제 모델 테이블을 만들어서 “사회문제” 페이지에서 각 문제들을 소개하고 그 문제에 속해있는 입점 브랜드들을 보여주기 위해 추가     
      - 일단은 name / image / content 필드로 구성     
      - 그리고 Brand 모델에 있는 problem 필드를 ForeignKey로 바꿔서 Problem 모델과 Brand 모델이 1:N관계가 되게끔 설정      
      - ForeignKey 설정 시, on_delete=models.PROTECT로 설정한 이유는 규정한 사회문제가 없어져도 일단 입점된 브랜드의 정보들은 그대로 유지하기 위함
  
  version 3.11 사회문제 페이지 구성 진행     
      - 사회문제 페이지를 클릭했을 때, 우리나라에 존재하는 사회문제 리스트를 보여주고 해당 문제 클릭 시 문제에 대한 설명과 함께 그 문제를 해결하기 위해 노력하는 소셜벤처 보여주기      
      - Problem 모델에 short_content 필드 추가
  
  version 3.12 마이페이지에서 본인 정보 수정 기능 추가      
      - 마이페이지에서 정보 수정하기 버튼 클릭 시, 본인이 회원가입 시 입력한 아이디와 닉네임, 이메일, 관심있는 사회문제를 변경할 수 있게 코드 추가      
      - id 정보는 request.user.username으로 접근하고 나머지 정보들은 request.user.customer로 접근한 customer의 필드를 변경하는 방식으로 설정     
      - 추가로 관리자 계정의 경우, {% if request.user.is_staff %} 라는 if문을 사용해서 관리자 여부 : O 이렇게 표시되도록 수정
  
  version 3.2 allauth 라이브러리 설치    
      - 소셜 로그인을 위한 django allauth 라이브러리 설치      
      - settings.py INSTALLED_APPS에 추가로 'django.contrib.sites' 등록 / 어드민 상에서 카카오 또는 구글 인증 정보 설정을 위해 sites 모델 등록     
      - settings.py INSTALLED_APPS에 추가로 'allauth'와 'allauth.account' 등록 / allauth에서 사용하는 계정 set들과 관련된 기능들을 가지고 올 수 있게 설정    
        - 'allauth.socialaccount' 을 등록해서 allauth로 SNS 계정 연동이 가능하게 해주는 모듈 설정     
        - 그 모듈안에 providers 다음에 auth0 / google / kakao 이렇게 우리가 연동하기를 원하는 provider를 각각 설정     
      - settings.py에 allauth 관련 설정 추가    
        - 로그인이 성공할 경우 redirect 해주는 페이지 설정, 로그아웃이 성공할 경우 redirect 해주는 페이지 설정, 로그아웃 시, URL로 GET으로 접근해도 로그아웃 처리가 가능할 수 있도록 설정   
      - 프로젝트 디렉터리 내부 urls.py에 소셜 로그인 리디렉션 URI를 위한 설정 추가    
        - path('oauth/', include('allauth.urls')), 이렇게 추가      
      - migrate 진행 이후, sites 앱의 Sites라는 모델 / socialaccount 앱의 socialaccount, socialapp, socialapp_sites, socialtoken 모델이 추가됨
  
  version 3.21 구글 및 카카오 소셜 로그인 기능 구현(내 구글 및 카카오 계정만 가능)    
      - Google Cloud Platform 사이트에 가서 새로운 impact-museum 프로젝트 생성    
        - 지금은 게시 상태가 테스트이기 때문에 테스트 사용자로 등록된 구글이메일만이 소셜 로그인이 가능 / OAuth 동의 화면 메뉴에서 내 구글 이메일만 등록
        - 리디렉션 URI는 http://localhost:8000/oauth/google/login/callback/ 이렇게 설정     
      - settings.py에 설정 추가 / allauth에서 account 로그인을 지원하기 위한 인증 로직 및 백엔드 로직을 설정하기 위해 AUTHENTICATION_BACKENDS 변수 설정     
        - 해당 모듈을 설정해서 클라이언트 ID랑 비밀번호를 어드민에 입력해서 그 값을 가지고 OAuth에 필요한 값들을 해당 SNS 서버에 전송할 수 있게됨      
        - SOCIALACCOUNT_PROVIDERS 변수를 딕셔너리로 추가로 설정해서 google로부터 profile이랑 email를 받아오도록 설정     
      - 어드민 페이지에 들어가서 Sites 모델에 도메인 값 추가    
        - 해당 모델은 우리 사이트의 도메인 값을 넣어주는 역할을 해준다. 그래서 나중에 socialaccount에서 연동을 할 때 SNS한테 전달 할 우리 서버의 도메인 정보를 불러오는 역할도 해주기 때문에 이 모델에 우리의 디폴트 URL를 입력해주기(127.0.0.1:8000) / 지금 테스트 서버이기 때문에 나중에는 배포된 도메인으로 수정해야 함     
        - 이렇게 설정해주면 redirection URI 요청이 들어갈 때 127.0.0.1:8000 정보를 읽어서 보내기 때문에 구글에서 '아, 내가 승인한 도메인 리디렉션 URI가 맞구나' 라고 인식을 해서 승인을 해줄 수 있게됨      
      - 어드민 페이지에 들어가서 Social applications 모델 데이터 추가    
        - 해당 모델에 Google Provider 추가 / 여기에 클라이언트 ID와 Secret Key 저장하여 나중에 새로 발급 시 바로 바꿀 수 있게 하드코딩 하지 않고 DB에 저장     
      - 로그인 및 회원가입 페이지 template에 socialaccount 모듈을 load 해주고 socialaccount 안에 있는 필요한 자바스크립트들을 불러올 수 있게 해주는 필터인 providers_media_js를 호출해주기     
        - 추가로 a element를 이용해서 provider_login_url이라는 필터를 사용하고 google provider에 로그인 주소를 가지고 올 수 있게 설정       
        - 여기까지 구글 소셜 로그인 기능 구현 완료
      - **해당 과정에서 구글 로그인 버튼 클릭 시, 오류 발생**    
        - **소셜 로그인 시, customer 모델에 데이터가 들어간게 아니기 때문에 메인페이지와 장바구니 페이지에 들어가면 오류가 발생하고 있음**    
        - **그리고 마이페이지 클릭 시, 닉네임만 데이터가 뜨고 나머지는 customer 모델을 기준으로 코드를 작성했기 때문에 다른 정보가 없음**     
      - 카카오 개발자 사이트에 가서 새로운 애플리케이션 추가 / Web 플랫폼을 등록하고 Redirect URI를 http://localhost:8000/oauth/kakao/login/callback/ 로 설정   
        - 카카오에서는 REST API 키가 클라이언트 ID역할을 하게 됨 / 추가로 Client Secret를 생성
        - 구글 소셜 로그인 기능과 마찬가지로 template에 소셜 로그인 관련 코드 추가 
        - 구글 소셜 로그인 기능과 마찬가지로 Social applications 모델에 들어간 다음, 새롭게 카카오 로그인을 위한 Provider 1개를 추가     
        - 추가로 카카오 로그인을 하게 되면 기본적으로 소셜 로그인을 할 때 마다 확인 이메일을 발송하도록 내부 디폴트 로직이 되어있어 이 부분을 꺼줘야 한다. / settings.py # All auth 부분에 ACCOUNT_EMAIL_REQUIRED = False, ACCOUNT_EMAIL_VERIFICATION = 'none' 다음과 같은 변수를 설정해서 카카오 로그인 시 해당 유저의 이메일을 가져오지 않게 설정. 그리고 none 설정은 확인 이메일이 반복해서 가지 않게 설정     
      - **이러한 소셜 로그인 성공 시 --> django User 모델에 계정 데이터가 추가된다. 그리고 Social accounts 모델에도 계정 데이터가 추가된다.**



</details>
<br>

## 5. 핵심 트러블 슈팅
### 5.1 ...

<br>

## 6. 그 외 트러블 슈팅    ==> 이러한 오류가 왜 발생했는지 & 그리고 어떤 문제를 해결해서 & 결국 내가 얻어낸 성과가 뭔지 
- models.py 설정 시 FloatField 및 IntegerField의 경우 default=0 처럼 default 값 설정 필요

- DB에서 ImageField 설정 시 이미지를 업로드 하지 않으면 html template에서 ValueError 발생 -> models.py에서 관련 모델에 @property를 설정해서 오류 방지

- Javascript 파일 - 새로 생성한 함수에서 url를 정의할 때, 상품 1개 조회 화면에서 장바구니 버튼을 클릭하기 때문에 url에 post_id(product_id) 값이 들어가야 했는데 그러지 않아 **uncaught (in promise) syntaxerror: unexpected token < in json at position 0** 와 같은 오류 발생 -> url 정의할 때 미리 정의한 post_id 변수를 +연산자로 url에 포함시키서 오류 해결   

- 상품 1개 조회 후 결제버튼 클릭해서 상품 1개만 결제 페이지에 보여주는 기능 / 장바구니 페이지에서 결제버튼 클릭해서 장바구니 상품들 결제 페이지에 보여주는 기능 -> 만약 상품 1개 조회 페이지에서 결제 버튼을 눌렀다면 Order 모델에 기존 주문과 다른 새로운 데이터가 추가되어야 하지 않을까 생각한다. 아직 하지 못했다. 또한, Order 모델의 date_ordered 필드가 어드민 페이지에서는 보이지가 않는다.. 상품 1개에 대한 이미지, 상품명, 가격은 DB에서 가져왔으나 해당 상품과 관련된 orderitem 모델에 있는 quantity를 연동해서 보여주지 못했고, 그래서 수량 * 가격 = 총액도 아직 구현하지 못했다...

- 상품 1개 조회 후 결제버튼 클릭해서 상품 1개만 결제 페이지에 보여주는 기능 / 장바구니 페이지에서 결제버튼 클릭해서 장바구니 상품들 결제 페이지에 보여주는 기능 관련 추가 오류 
  - 장바구니 페이지에서 결제 버튼 눌렀을 때, **TypeError: checkout() missing 1 required positional argument: 'post_id'** 다음과 같은 에러가 있었다. views.py에서 설정한 함수의 필수 파라미터를 request, user_id로 설정했더니 장바구니 페이지에서 버튼을 눌렀을 때는 user_id가 없어서 생긴 오류였다. 이 문제를 해결하기 위해 장바구니 페이지에서 결제 버튼을 눌렀을 때 연결되는 views 함수(request만 파라미터 설정)를 따로 만들고 / 상품 1개 조회 페이지에서 결제 버튼을 눌렀을 때 연결되는 views 함수(request와 user_id를 파라미터로 설정)도 따로 만들어줘서 오류를 해결할 수 있었다.

- Customer 모델의 name과 user 필드의 null, blank를 False로 변경했으나 -> migrations에서 문제 발생. 필드를 non-nullable로 바꾸는데 default를 주지 않았던 게 문제였음. 그래서 name과 user 필드에 default='미지정' 이라고 수정한 다음 migrations를 진행하고 migrate를 했으나 ValueError: Field 'id' expected a number but got '미지정' 라는 오류 발생. 해당 오류를 보고 default=0으로 수정하고 다시 migration/migrate 진행했으나 똑같은 오류발생.
  - Customer 모델의 user필드는 User모델과의 OneToOneField로 설정되어 있기 때문에, default값이 문자나 0이 아닌 1이상의 숫자로 설정해야 User모델의 pk와 충돌하지 않게 된다. pk는 자동적으로 1부터 증가하기 때문이다. 그래서 Customer 모델의 user와 name 필드 모두 default=1로 수정하고 / python manage.py showmigrations 명령어를 통해 아직 적용되지 않은 2개의 migration 파일을 삭제한 다음, 다시 migration / migrate 진행하여 오류 해결.


- 상품 상세 페이지에서 장바구니 버튼을 눌렀을 때 추가가 되지 않았음     
  - https://born-dev.tistory.com/28 처럼 Broken pipe 오류 였는데, HTTP Request가 최초에 진행되고 서버에서 작업을 완료해서 Response를 하기전에 네트워크가 끊겨서 생기는 문제였다.    
  - cart.js 파일에서 .then((data) =>{ console.log('data:', data) location.reload() 이러한 코드가 있었는데, 이렇게 location.reload() 로 응답을 받기전에 새로고침이 되어서 오류가 발생.     - 이 부분을 주석처리 하니까 오류가 해결됨


- 새로운 username으로 회원가입 시, IntegrityError at /accounts/sign_up/ 그리고 UNIQUE constraint failed: auth_user.username 라는 에러가 발생함
  - 알고보니, 이미 가입된 username으로 다시 회원가입을 시도해서 발생하는 에러
  - 이걸 막기 위해 코드를 추가해야 한다. 중복된 username이 있는 경우, 회원가입을 막을 수 있도록 해보기.


- Django database is locked 라는 에러가 발생      
  - python manage.py migrate posts zero를 실행하는 과정에서 위에 에러가 발생      
  - 에러가 발생하는 이유는 DB Browser for SQLite 라는 프로그램을 통해 SQLite 데이터를 조회하고 있었기 때문 / 즉, migration 하려는 데이터베이스를 다른 프로그램을 통해 조회 또는 수정중이었기 때문     
  - 해당 SQLite 를 조회하고 있던 프로그램(DB Browser for SQLite)을 종료한 뒤, migrate 명령을 다시 실행하면 에러없이 진행됨


- Related Field got invalid lookup: icontains 라는 에러 발생
  - Product 모델의 brand 필드를 Brand 모델과 1:N 관계로 설정한 이후, 검색 시 해당 에러가 발생 
  - products = Product.objects.all().filter(Q(product_name__icontains=query) | Q(brand__icontains=query)) -> 다음과 같이 ForeignKey가 검색 필드에 포함되서 나타나는 문제
  - products = Product.objects.all().filter(Q(product_name__icontains=query) | Q(brand__name__icontains=query)) -> 이렇게 ForeingKey로 연결된 필드는 필드 이름만 입력하는 게 아니라 해당 모델의 필드를 자세히 입력해주기. 그래서 brand가 아니라 brand__name으로 필드를 설정하면 검색이 되고 에러가 발생하지 않는다. 


- Bootstrap Carousel로 입력 시, for문의 첫번째 항목에는 div element의 class가 carousel-item active로 되어 있어야 하는 부분이 있었음      
  - {% for product in products %} 다음에 {% if forloop.first %} 이렇게 입력       
  - forloop은 https://docs.djangoproject.com/en/4.0/ref/templates/builtins/ django 공식 문서에 나와있듯이, for문에서 사용할 수 있는 변수로 forloop.first가 for문의 첫번째 항목이기에 해당 항목일 경우 div class="carousel-item active"를 출력하고 아닐 경우에는 class="carousel-item"로 출력해서 Carousel 기능 설정


- version 3.0에서 .gitignore를 설정했으나 적용 안됨     
  - https://stackoverflow.com/questions/11451535/gitignore-is-ignored-by-git
  - https://coding-groot.tistory.com/59
  - https://jojoldu.tistory.com/307
  - 해당 글들을 참고하여 git에 있는 인덱스 파일만 삭제하여 git 캐시를 전부 삭제하고 다시 git 커밋을 실행해서 적용 완료
  - **아직 settings.py는 적용 안됨 -> 알아보기**


- AWS로 연결한 MySQL이 DBeaver에서 connect timed out 에러가 발생    
  - https://stackoverflow.com/questions/9500803/cant-connect-to-mysql-remote 해당 답변에서 connect timed out은 server가 busy하거나 방화벽 문제 둘 중 한가지 원인이라는 것을 확인     
  - 그래서, AWS Console의 DB 인스턴스 인바운드 규칙에 설정된 내용을 전부 삭제한 뒤 다시 재설정하고 DBeaver에 연결했더니 성공
  - 추가로, https://www.codingfactory.net/12934 해당 내용을 참고해서 데이터베이스를 잠시 연결하지 않으면 끊어지는 상황을 방지하기 위해, 작업을 하지 않아도 연결이 되게끔 DBeaver의 Keep-Alive을 120으로 설정


- Posts 앱 내부 models.py 코드 설정 시 오류     
  - Posts 앱 내부 models.py에 problem = models.ForeignKey(Problem, on_delete=models.PROTECT)와 같이 코드를 입력했을 때, 같은 위치에 있는 Problem이라는 모델을 VSCode가 인식하지 못함
  - 그래서 https://docs.djangoproject.com/en/4.0/ref/models/fields/ 해당 공식문서에 내용을 바탕으로, problem = models.ForeignKey('Problem', on_delete=models.PROTECT) 이렇게 모델 이름을 문자열로 설정했더니 인식이 되어 migration, migrate를 실행할 수 있었음


- 지속적으로 AWS로 연결한 MySQL이 DBeaver에서 connect timed out 에러가 계속 발생      
  - DBeaver의 Keep-Alive을 120으로 설정한 이후에도, 계속 connect timed out 에러가 발생됨     
  - 기존에는 AWS에서 인바운드 규칙을 **22포트(SSH) / 내 IP, HTTPS / Anywhere-IPv4, HTTP / Anywhere-IPv4, 3306포트(MySQL) / 내 IP** 이렇게 설정했었는데, 접속 환경 상 매번 접속 아이피가 변경될 수 있다는 점을 확인      
  - (대부분 우리가 인터넷을 사용할 때 유동IP로 접속할때마다 IP가 변경이 된다. 전용 회선이나 고정 IP를 신청한 게 아니라면, IP가 할당될 때 일정 시간 동안만 그 IP를 사용할 수 있게 할당을 해주고, 유효시간이 지나면 IP를 나눠주는 서버인 DHCP서버가 우리의 컴퓨터가 꺼져있으면 해당 IP에 대한 사용이 끝났다고 인지하고 IP를 회수한다고 한다. 그래서 다시 컴퓨터를 켰을 때, 컴퓨터가 자동으로 DHCP에게 IP할당을 요청하고 사용하던 IP가 비어있으면 이전 IP를 할당해주지만, 누가 쓰고있다면 남아있는 IP 중 하나를 할당해준다.)      
  - 그래서 인바운드 규칙에서 **3306포트(MySQL) / Anywhere-IPv4** 이렇게 모든 IP로 접속할 수 있게 수정했더니, 컴퓨터를 끄고 다시 접속해도 해당 오류가 발생하지 않고 연결이 되는 것을 확인할 수 있었음


- 소셜 로그인을 위한 allauth 라이브러리 설치 및 settings.py 설정 후 migrate를 진행한 다음, 어드민 페이지가 뜨지 않고 DoesNotExist at /admin/ Site matching query does not exist 에러 발생      
  - Django 프로젝트의 Site 객체가 없다고 생각해서 발생한 문제     
  - 소셜 로그인을 위해 Site 객체를 처음 등록한 다음, settings.py에서 SITE_ID 변수를 새로 등록한 Site 객체 ID와 일치시켜야 된다. 그래서 settings.py에 # All auth 부분에 SITE_ID = 1 이렇게 추가해서 오류를 해결      
  - 관련 내용 : https://stackoverflow.com/questions/11476210/getting-site-matching-query-does-not-exist-error-after-creating-django-admin

 



<br>

## 7. 회고 / 느낀점
- ㅇㅇㅇ

