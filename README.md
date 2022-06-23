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
  - EC2
  - RDS (MySQL 데이터베이스 서버)

**API 활용(소셜 로그인)**
- Google Cloud Platform
- Kakao developers

**버전관리**
- Git
- Github

**API 서버**
- DRF(Django REST Framework)
- Postman

**디버깅 툴**
- django-debug-toolbar

**인메모리 Database**
- Redis 5.0.7

**배포**
- AWS Route 53
- Nginx
- uWSGI

<br>

## 3. ERD 설계
![Untitled Diagram-Page-1](https://user-images.githubusercontent.com/95380638/164652569-aac5f937-414b-4796-a933-f9622375b4a7.png)


- Customer 모델은 User 모델과 1:1관계로 설정 - 사용자에 대한 정보를 더 자유롭게 받기 위해 Customer라는 모델을 1:1관계로 추가
- Customer 모델과 Order 모델은 1:N관계로 설정 - 1명의 사용자가 쇼핑몰에서 여러 번 주문할 수 있기 때문
- Customer 모델 & Order 모델과 Shipping Address 모델은 1:N관계로 설정 - 1명의 사용자가 다양한 배송 주소지를 생성할 수 있고, 1개의 주문 건이 배송 취소 및 실패 등으로 다양한 배송 주소지를 가질 수 있음
- Product 모델 & Order 모델과 Order Item 모델(장바구니에 추가된 상품 데이터 모델)은 1:N관계로 설정 - 1개의 상품이 여러 번 장바구니에 포함될 수 있고, 1개의 주문 건에 많은 상품들이 장바구니에 추가될 수 있음
- Problem 모델과 Brand 모델은 1:N관계로 설정 - 1개의 사회문제를 해결하기 위해 노력하는 브랜드가 여러 개가 있을 수 있기 때문에 1:N으로 설정 
- Brand 모델과 Product 모델은 1:N관계로 설정 - 1개의 브랜드가 impactmuseum에 입점하고 여러 개의 상품들을 판매할 수 있기 때문
- Customer 모델과 Post 모델은 1:N관계로 설정 - 1명의 사용자 또는 관리자가 여러 개의 글을 남길 수 있기 때문
<br>

## 4. API 문서
- [Product 모델 CRUD API 문서](https://documenter.getpostman.com/view/20920872/Uz5KkEUi)
- [Post 모델 CRUD API 문서](https://documenter.getpostman.com/view/20920872/Uz5KkEUk)
- 개발한 API를 테스트하는 플랫폼인 Postman을 이용해서 API 문서 작성 완료

- ex) Product API 문서 예시
<img width="1419" alt="image" src="https://user-images.githubusercontent.com/95380638/172448350-23b410fc-7d93-4b06-987c-73041996828c.png">



## 5. 핵심 기능
- **메인 페이지 : DB에 저장된 상품을 보여주고 상품 검색이 가능하도록 구현**
  - Product 모델 데이터를 id필드 기준 역순으로 8개의 상품만 화면에 나오도록 설정
  - 검색 기능의 경우, 상품명이나 해당 상품의 브랜드(회사명)를 검색하면 나올 수 있도록 기능 구현 

- **회원가입 & 로그인 페이지 : 자체적인 회원가입 및 구글 또는 카카오 계정으로 소셜 로그인 가능**
  - 회원가입 시, 입력 정보 누락 및 중복된 정보로 가입 시 예외 처리 진행
  - Google Cloud Platform과 Kakao developers를 활용해서 소셜 로그인 기능 구현
  - 로그인 이후 마이 페이지에서 개인 정보 수정 가능
  - django signal를 이용해서 소셜 로그인 시, 기존 User 모델 이외에 Customer 모델에도 데이터 생성

- **입점 소셜벤쳐 페이지 : 소셜벤처 브랜드 별 페이지 확인 가능 및 해당 브랜드에 속한 상품 확인 가능**
  - DB에 저장된 브랜드들을 최근에 등록된 순으로 보여주기
  - 브랜드 이미지를 클릭했을 때, 해당 브랜드가 현재 판매하고 있는 상품들을 Carousel 기능으로 보여주기
  - 사회문제 페이지에서는, 나열된 사회문제를 해결하려는 브랜드들을 확인 가능

- **공지사항 페이지 : 상단 고정 게시글 및 페이지네이션이 구축된 공지사항 게시판 구축**
  - Paginator 메서드를 사용하여 한 페이지에 10개씩 보여주는 페이지네이션 설정
  - 글을 생성할 때, 상단 고정 여부에 체크하고 생성하면 고정이 될 수 있도록 DB에 BooleanField 설정
  - 글 생성 시, 성격에 따라 카테고리 설정이 가능하고 카테고리 별로 색깔 다르게 보여주기
  - template 필터를 사용해 게시글 순서 숫자를 DB 데이터의 id가 아닌 순서대로 나열하게끔 설정
  - 공지사항의 성격을 고려, 관리자 계정으로 로그인 했을 경우에만 글 생성 버튼 활성화 설정 / 상세 페이지에서는 로그인된 유저와 해당 글 작성자가 같은 경우에만 수정 및 삭제 버튼 활성화 설정

- **서버 관련 : AWS RDS로 MySQL DBMS 서버 구축**
  - AWS RDS를 이용해서 어떤 환경에서 접속해도 connect timed out 에러가 발생하지 않도록 MySQL 3306 포트를 Anywhere-IPv4로 설정
  - MySQL이 현재 시점에서 Oracle다음으로 가장 많이 사용하는 DBMS이기 때문에 안정적이라고 판단해서 MySQL로 DBMS를 설정
  - 데이터의 무결성을 MySQL에서 체크해주는 기능인 Strict MODE 설정 ex) NOT NULL로 설정하면 무조건 값을 넣어줘야 에러가 발생하지 않게 됨

- **DRF를 바탕으로 API 서버 구현**
  - DRF(Django REST Framework) 라이브러리를 설치하여 API 서버 구축
  - products와 posts 앱 내부에 있는 Product/Post 모델과 관련한 CRUD API 서버 설정
  - Postman를 이용해서 Product/Post API 문서 작성 완료

- **인메모리 Database : AWS EC2로 Redis 서버 구축**
  - AWS EC2를 생성해 디스크가 아닌, 메모리에 데이터를 저장하는 인메모리 Database인 Redis 서버를 구축
  - 서비스에서 로그인 시, 기존 django_session 모델이 아닌 Redis 서버에서 메모리에 세션이 저장된 것을 확인할 수 있게 됨
  - 이렇게 설정함으로써 그 전 보다는 더 빠르게 기존 사용자를 파악할 수 있고 세션 값을 영구적으로 저장할 필요는 없기 때문에 Redis로 관리하는 것이 적합하다고 판단됨

- **http://www.impactmuseum.com 라는 주소로 배포 완료**
  - AWS EC2에 웹 서버인 nginx와 django 앱 서버를 연결해주는 uWSGI를 설치 진행
  - nginx으로 django의 8000포트를 80포트로 포트포워딩 진행
  - EC2 ubuntu에서 uWSGI를 백그라운드에서 실행시켜 runserver를 실행하지 않고 터미널을 종료해도 웹 서비스가 구동할 수 있게 유지
  - 가비아에서 구매한 도메인을 AWS Route 53에서 호스팅 영역 생성 진행
  - 가비아 도메인을 AWS의 네임서버와 연동시켜서 이후에 도메인과 관련된 모든 작업을 AWS 내부에서만 수행할 수 있게끔 변경
  - www.impactmuseum.com 라는 주소로 배포 완료

<br>

## 6. 트러블 이슈
- **models.py 설정 시 FloatField 및 IntegerField 관련 에러 발생**
  - models.py 설정 시 FloatField 및 IntegerField의 경우, default=0 처럼 default 값 설정 필요

- **DB에서 ImageField 설정 시 이미지를 업로드 하지 않으면 html template에서 ValueError 발생**
  - models.py에서 관련 모델에 @property를 설정해서 imageURL 이라는 함수 정의
  - 그래서 이미지가 있다면 보여주고 없다면 상품 목록 페이지로 redirect 시켜주기
  - 참고 자료 : https://hwan-hobby.tistory.com/148

- **상품 1개 조회 후 결제버튼 클릭해서 상품 1개만 결제 페이지에 보여주는 기능 / 장바구니 페이지에서 결제버튼 클릭해서 장바구니 상품들 결제 페이지에 보여주는 기능 관련 추가 오류**
  - 장바구니 페이지에서 결제 버튼 눌렀을 때, **TypeError: checkout() missing 1 required positional argument: 'product_id'** 다음과 같은 에러가 있었다. views.py에서 설정한 함수의 필수 파라미터를 request, product_id로 설정했더니 장바구니 페이지에서 버튼을 눌렀을 때는 product_id가 없어서 생긴 오류였다. 이 문제를 해결하기 위해 장바구니 페이지에서 결제 버튼을 눌렀을 때 연결되는 views 함수(request만 파라미터 설정)를 따로 만들고 / 상품 1개 조회 페이지에서 결제 버튼을 눌렀을 때 연결되는 views 함수(request와 product_id를 파라미터로 설정)도 따로 만들어줘서 오류를 해결

- **Customer 모델의 name과 user 필드의 null, blank를 False로 변경했으나 -> migrations에서 에러 발생**
  - 필드를 non-nullable로 바꾸는데 default를 주지 않았던 게 문제였다. 그래서 name과 user 필드에 default='미지정' 이라고 수정한 다음 migrations를 진행하고 migrate를 했으나 ValueError: Field 'id' expected a number but got '미지정' 라는 오류 발생. 해당 오류를 보고 default=0으로 수정하고 다시 migration/migrate 진행했으나 똑같은 오류 발생.
  - Customer 모델의 user필드는 User모델과의 OneToOneField로 설정되어 있기 때문에, default값이 문자나 0이 아닌 1이상의 숫자로 설정해야 User모델의 pk와 충돌하지 않게 된다. pk는 자동적으로 1부터 증가하기 때문이다. 그래서 Customer 모델의 user와 name 필드 모두 default=1로 수정하고 / python manage.py showmigrations 명령어를 통해 아직 적용되지 않은 2개의 migration 파일을 삭제한 다음, 다시 migration / migrate 진행하여 오류 해결.

- **새로운 username으로 회원가입 시, IntegrityError at /accounts/sign_up/ 그리고 UNIQUE constraint failed: auth_user.username 라는 에러가 발생함**
  - 알고보니, 이미 가입된 username으로 다시 회원가입을 시도해서 발생하는 에러
  - 이걸 막기 위해 코드를 추가해야 한다. 중복된 username이 있는 경우, 회원가입을 막을 수 있도록 해보기
  - Customer 모델 user 필드에 unique=True라는 속성을 추가해 중복되는 ID가 없도록 설정

- **Django database is locked 라는 에러가 발생**      
  - python manage.py migrate posts zero를 실행하는 과정에서 위에 에러가 발생      
  - 에러가 발생하는 이유는 DB Browser for SQLite 라는 프로그램을 통해 SQLite 데이터를 조회하고 있었기 때문 / 즉, migration 하려는 데이터베이스를 다른 프로그램을 통해 조회 또는 수정중이었기 때문     
  - 해당 SQLite를 조회하고 있던 프로그램(DB Browser for SQLite)을 종료한 뒤, migrate 명령을 다시 실행하여 에러없이 진행 완료

- **Related Field got invalid lookup: icontains 라는 에러 발생**
  - Product 모델의 brand 필드를 Brand 모델과 1:N 관계로 설정한 이후, 검색 기능 수행 시 해당 에러가 발생 
  - products = Product.objects.all().filter(Q(product_name__icontains=query) | Q(brand__icontains=query)) -> 다음과 같이 ForeignKey가 검색 필드에 포함되서 나타나는 문제
  - products = Product.objects.all().filter(Q(product_name__icontains=query) | Q(brand__name__icontains=query)) -> 이렇게 ForeingKey로 연결된 필드는 필드 이름만 입력하는 게 아니라 해당 모델의 필드를 자세히 입력해주기. 그래서 brand가 아니라 brand__name으로 필드를 설정하면 검색이 되고 에러가 발생하지 않는다. 

- **Bootstrap Carousel로 코드 입력 시, for문의 첫번째 항목에는 div element의 class가 carousel-item active로 되어 있어야 하는 부분이 있었음**      
  - {% for product in products %} 다음에 {% if forloop.first %} 이렇게 입력       
  - forloop은 https://docs.djangoproject.com/en/4.0/ref/templates/builtins/ django 공식 문서에 나와있듯이, for문에서 사용할 수 있는 변수로 forloop.first가 for문의 첫번째 항목이기에 해당 항목일 경우 div class="carousel-item active"를 출력하고 아닐 경우에는 class="carousel-item"로 출력해서 Carousel 기능 설정

- **version 3.0에서 .gitignore를 설정했으나 적용 안됨**     
  - https://stackoverflow.com/questions/11451535/gitignore-is-ignored-by-git
  - https://coding-groot.tistory.com/59
  - https://jojoldu.tistory.com/307
  - 해당 글들을 참고하여 git에 있는 인덱스 파일만 삭제하여 git 캐시를 전부 삭제하고 다시 git 커밋을 실행해서 적용 완료

- **AWS로 연결한 MySQL이 DBeaver에서 connect timed out 에러가 발생**    
  - https://stackoverflow.com/questions/9500803/cant-connect-to-mysql-remote 해당 답변에서 connect timed out은 server가 busy하거나 방화벽 문제 둘 중 한가지 원인이라는 것을 확인     
  - 그래서, AWS Console의 DB 인스턴스 인바운드 규칙에 설정된 내용을 전부 삭제한 뒤 다시 재설정하고 DBeaver에 연결했더니 성공
  - 추가로, https://www.codingfactory.net/12934 해당 내용을 참고해서 데이터베이스를 잠시 연결하지 않으면 끊어지는 상황을 방지하기 위해, 작업을 하지 않아도 연결이 되게끔 DBeaver의 Keep-Alive을 120으로 설정

- **Posts 앱 내부 models.py 코드 설정 시 오류**     
  - Posts 앱 내부 models.py에 problem = models.ForeignKey(Problem, on_delete=models.PROTECT)와 같이 코드를 입력했을 때, 같은 위치에 있는 Problem이라는 모델을 VSCode가 인식하지 못함
  - 그래서 https://docs.djangoproject.com/en/4.0/ref/models/fields/ 해당 공식문서에 내용을 바탕으로, problem = models.ForeignKey('Problem', on_delete=models.PROTECT) 이렇게 모델 이름을 문자열로 설정했더니 인식이 되어 migration, migrate를 실행할 수 있었음
  - 해당 오류가 발생한 이유는, 아직 models.py에서 Problem이라는 모델 클래스가 생성되지 않았기 때문에 읽을수가 없었기 때문이다. 그래서 나중에 lazy하게 읽게 하기 위해서 문자열로 넣어두면 정상적으로 migration과 migrate가 진행될 수 있었던 것이다.

- **지속적으로 AWS로 연결한 MySQL이 DBeaver에서 connect timed out 에러가 계속 발생**      
  - DBeaver의 Keep-Alive을 120으로 설정한 이후에도, 계속 connect timed out 에러가 발생됨     
  - 기존에는 AWS에서 인바운드 규칙을 **22포트(SSH) / 내 IP, HTTPS / Anywhere-IPv4, HTTP / Anywhere-IPv4, 3306포트(MySQL) / 내 IP** 이렇게 설정했었는데, 접속 환경 상 매번 접속 아이피가 변경될 수 있다는 점을 확인      
  - (대부분 우리가 인터넷을 사용할 때 유동IP로 접속할때마다 IP가 변경이 된다. 전용 회선이나 고정 IP를 신청한 게 아니라면, IP가 할당될 때 일정 시간 동안만 그 IP를 사용할 수 있게 할당을 해주고, 유효시간이 지나면 IP를 나눠주는 서버인 DHCP서버가 우리의 컴퓨터가 꺼져있으면 해당 IP에 대한 사용이 끝났다고 인지하고 IP를 회수한다고 한다. 그래서 다시 컴퓨터를 켰을 때, 컴퓨터가 자동으로 DHCP에게 IP할당을 요청하고 사용하던 IP가 비어있으면 이전 IP를 할당해주지만, 누가 쓰고있다면 남아있는 IP 중 하나를 할당해준다.)      
  - 그래서 인바운드 규칙에서 **3306포트(MySQL) / Anywhere-IPv4** 이렇게 모든 IP로 접속할 수 있게 수정했더니, 컴퓨터를 끄고 다시 접속해도 해당 오류가 발생하지 않고 연결이 되는 것을 확인할 수 있었음

- **소셜 로그인을 위한 allauth 라이브러리 설치 및 settings.py 설정 후 migrate를 진행한 다음, 어드민 페이지가 뜨지 않고 DoesNotExist at /admin/ Site matching query does not exist 에러 발생**      
  - Django 프로젝트의 Site 객체가 없다고 생각해서 발생한 문제     
  - 소셜 로그인을 위해 Site 객체를 처음 등록한 다음, settings.py에서 SITE_ID 변수를 새로 등록한 Site 객체 ID와 일치시켜야 된다. 그래서 settings.py에 # All auth 부분에 SITE_ID = 1 이렇게 추가해서 오류를 해결      
  - 관련 내용 : https://stackoverflow.com/questions/11476210/getting-site-matching-query-does-not-exist-error-after-creating-django-admin

- **template에서 Post 모델 내부에 정의한 Category 클래스 항목들을 드롭다운으로 보여주는 과정에서 에러**  
  - view에서 단순히 Post 모델 데이터들만 다 보내주고 template에서 post.category로 하면 Post 인스턴스의 모든 데이터를 출력하게 되서 카테고리를 중복으로 선택하게 되는 문제가 발생
  - view에서 posts_category = Post.Category.choices 이렇게 Post 모델의 Category 클래스에 접근해서 항목들을 보내주고 template에서는 {% for category in posts_category %} 이렇게 하나씩 뽑으면 category가 튜플로 출력이 되는 것을 확인. 그래서 {{ category.1 }} 이렇게 튜플의 두번째 항목을 뽑아서 내가 원하는 한글 목록이 출력되게끔 설정, 오류 해결

- **로그인 이후에도 디테일 페이지로 들어가면 Navbar에서 로그인/회원가입 버튼이 출력되는 문제 발생**
  - 로그인이 되었을 경우, {% if user.is_authenticated %} 와 같은 if문으로 마이페이지와 로그아웃 버튼이 출력되어야 하나 게시판 디테일 페이지로 들어갔을 경우에는 로그인/회원가입 버튼이 출력됨
  - board_detail View에서 login_user = request.user.customer와 같이 request.user를 사용한 변수를 주석처리 하고 나서 브라우저를 새로고침 하니까 다시 정상적으로 {% if user.is_authenticated %} 코드가 작동되서 오류를 해결 

- **version 3.53 - 소셜 로그인 시, django signal를 이용하여 자동으로 Customer 모델에 데이터를 생성해서 오류 해결**
  - 소셜 로그인 시, User 모델에만 데이터가 생성되고 Customer 모델에는 생기지 않아 오류가 발생했음
  - 그래서, accounts 앱 내부 models.py에 특정 데이터 저장 직후 signal인 post_save와 reciever 데코레이터를 import 해서 소셜로그인 이후에 Customer 모델에 데이터를 저장할 수 있도록 Signal 함수 설정
    - User 모델에서 post_save가 발생하면, 즉 소셜 로그인이 되서 데이터가 추가될 때 -> 해당 함수가 실행됨
    - Customer 모델과 SocialAccount 모델을 확인해서 customer가 없고 social_account가 있다면 Customer 모델 name 필드, email 필드에 소셜로그인 계정 이메일 아이디와 이메일 자체를 저장하고 Customer 모델 데이터를 생성하게끔 설정
  - **이렇게 django signal를 이용하여 소셜 로그인 시, Customer 모델에 자동으로 데이터가 생성되어 정상적으로 웹 서비스를 이용할 수 있게 수정 완료**
  - 카카오 로그인 시, 아직 Customer 모델의 name과 email 필드는 공백으로 남아있게됨
  - 구글 로그인 시, ConnectionRefusedError at /oauth/social/signup/ [Errno 61] Connection refused 다음과 같은 에러 발생
    - [해당 내용](https://stackoverflow.com/questions/21563227/django-allauth-example-errno-61-connection-refused)을 참고해서 전자 메일(SMTP) 서버가 없어 allauth가 확인 메일을 보낼 수 없어 발생한 문제라고 파악 
    - 그래서 settings.py에 EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 이렇게 추가해서 전자 메일이 콘솔에 인쇄되서 SMTP 서버가 필요하지 않도록 설정

- **version 3.71 - 회원가입 관련 UnboundLocalError 오류 해결**
  - 회원가입 시, 입력받아야 할 정보들을 입력하지 않고 회원가입 버튼을 누르면 **UnboundLocalError at /accounts/sign_up/    
    local variable 'context' referenced before assignment** 다음과 같은 오류 발생
  - def sign_up이라는 함수 내부에 지역 변수 context를 정의하지 않은 채로, 함수 내부에서 회원가입 정보가 입력되지 않을 시 context에 error라는 key를 저장한 것이 원인으로 파악함
  - 에러 메세지를 해석해보면, 할당 전에 지역 변수 'context’가 참조되었다고 얘기해주고 있음
  - **그래서 -> def sign_up 함수 바로 밑에 context = { 'cartItems': cartItems, } 이렇게 지역변수 context를 정의함으로써 오류 해결. 그러면 그 밑에 if문이 진행되면서 context 변수를 사용할 수 있게 된다.**

- **version 3.72 - 회원가입 관련 IntegrityError 오류 예외처리**
  - Customer 모델의 user/name/email 필드에 unique=True 속성을 추가한 이후에, 중복된 정보로 회원가입을 시도할 경우 **IntegrityError at /accounts/sign_up/    
    (1062, "Duplicate entry 'sss' for key 'auth_user.username'")** 다음과 같은 오류 발생
  - 그래서 try-except로 예외처리 진행 완료
    - **accounts 앱 내부 views.py에 정의되어 있는 회원가입 함수인 sign_up 내부의 회원가입 if문을 try-except로 묶고 -> IntegrityError가 발생할 때 context['error'] = '이미 가입된 회원 정보입니다. 다른 정보를 입력해주세요.' 이렇게 context에 에러메세지를 추가해서 template에 띄우도록 설정 완료**
    - 이제 중복된 정보로 가입 시, 해당 메세지가 나와서 다른 정보로 회원가입을 시도하게끔 설정

  - **version 3.71에서 수정했던 회원가입 오류를 로그인 오류에서도 확인하여 똑같은 방법으로 수정**

- **version 3.73 - version 3.72와 유사한 오류 수정**
  - 로그인을 하지 않은 상태에서 -> 상품1개 조회 페이지에서 “결제하기” 버튼 클릭 시, **UnboundLocalError at /products/9/checkout/
local variable 'product' referenced before assignment** 다음과 같은 오류 발생
    - 그래서 else문에 return redirect('products:index') 해당 코드를 추가해서 로그인을 하지 않을 때 구매하기 버튼을 누르면 메인 페이지로 돌아가게끔 설정
  - posts 앱의 views.py에서 공지사항 게시판 글을 조회하는 board_detail 함수와 게시판 글을 수정하는 board_edit 함수 내부에서 Post 모델의 데이터를 조회할 때, **post = get_object_or_404(Post, id=post_id)** 이렇게 잘못된 접근을 했을 때 데이터가 없다는 의미의 404에러를 띄워줄 수 있도록 수정

- **배포 과정 중, AWS EC2에서 requirements.txt 적용 오류 발생**
  - 새롭게 생성한 AWS EC2에 pip install -r requirements.txt 명령어로 필요한 라이브러리 설치 시, **ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.** 다음과 같은 오류 발생
  - 처음에는 pip 버전이 문제라고 판단하여 **pip install pip==18.1.** 명령어로 버전을 다운그레이드 한 다음, 다시 시도 했으나 setuptools와 관련된 메세지가 뜨고 똑같이 오류 발생
  - 다시 pip 버전을 최신으로 업데이트하고, **pip install --upgrade setuptools** 명령어로 setuptools를 업데이트 후 다시 시도
  - 그 다음으로는 **error: subprocess-exited-with-error... python setup.py egg_info did not run successfully.** 와 **error: metadata-generation-failed** 라는 오류가 발생. 즉, 하위 프로세스와 패키지 메타데이터에서 오류가 발생
  - **sudo -H pip3 install --upgrade --ignore-installed pip setuptools** 해당 명령어로 pip와 setuptools 재설치를 진행했으나, **ERROR: launchpadlib 1.10.13 requires testresources, which is not installed.** 라는 에러 발생
  - **sudo apt install python3-testresources** 라는 명령어로 testresources를 설치 후 다시 requirements.txt를 실행했으나 똑같은 오류 발생
  - **error: subprocess-exited-with-error** 해당 에러를 자세히 읽어봤을 때, mysqlclient이 설치가 되지 않아 발생하는 것으로 추측
  - **sudo apt-get install mysql-server, mysql-client** 해당 명령어로 설치하려 했으나 **OSError: mysql_config not found** 이렇게 찾을 수 없다고 확인
  - **sudo apt-get install python3-dev libmysqlclient-dev** 이후에 다음과 같은 명령어로 mysql 관련 라이브러리 설치 완료
  - **pip install mysqlclient** 명령어로 mysqlclient 설치 완료
  - 이제 다시 **pip install -r requirements.txt** 해당 명령어를 시도했을 때 requirements.txt에 있는 내용들을 바탕으로 필요한 패키지들을 전부 설치 완료
    - **결론적으로 mysql과 관련된 문제였음을 확인할 수 있었음**

- **배포 과정 중, AWS EC2에서 runserver 실행 오류 발생**
  - Ubuntu EC2에서 www라는 디렉터리를 생성하고 git clone를 통해 impact museum 소스코드를 가져온 이후, manage.py가 있는 위치에서 **python manage.py runserver 0.0.0.0:8000** 다음과 같은 코드를 입력했을 때, **django.core.exceptions.ImproperlyConfigured: Set the SECRET_KEY environment variable** 라는 오류가 발생
  - github 저장소에 있는 소스코드에는 .gitignore 파일로 환경변수들을 설정한 .env 파일이 없어 settings.py에 있는 코드들이 실행되지 못한 것으로 확인
  - **vi .env** 해당 명령어로 .env 파일을 EC2 내부에 생성하고 기존의 설정 값들을 그대로 입력해주기 / 단, DEBUG 항목은 False로 수정
  - .env 파일 작성 후, 브라우저에 EC2 IP주소:8000으로 접속했을 때 정상적으로 접속이 되는 것을 확인

- **uWSGI 설치 이후, uwsgi.ini이라는 설정 파일 관련 오류**
  - wsgi가 django를 실행할 때 어떻게 실행할지, 그리고 python 프로젝트나 실행 포인트는 어디인지 설정해주는 uwsgi.ini 파일 관련 오류 발생
  - uwsgi.ini 파일 내부에서 chdir의 경우, django 프로젝트 폴더의 경로를 설정해줘야 한다. 즉, manage.py 파일이 위치해있는 경로를 의미한다.
  - 해당 부분을 잘못 설정하여 **moduleNotFoundError** 발생
  - 그래서 chdir=/home/ubuntu/www/Impact_museum 이렇게 EC2 내부의 프로젝트 폴더 경로를 설정해서 오류 해결

- **배포 과정 중, media 디렉터리 파일 적용 오류 발생**
  - static 파일의 경우, 루트 디렉터리에 위치한 static 디렉터리에 모두 옮겨서 적용 진행
  - 그러나 media 파일의 경우 배포된 서비스에 적용되지 못함

<br>

## 7. 개발 이력
- **version 1.1 상품 추가, 수정, 삭제 등 기본적인 CRUD 구축**
  
- **version 1.4 URL Configuration으로 app별 URL 관리 / Template & Static Inheritance 설정 완료 및 app별 namespacing 설정 완료**
  
- **version 1.5 DB 구성 및 ERD 설계 시작**   
  - ImageField를 위한 Pillow 라이브러리 설치
  - 프로젝트 루트 디렉터리 내부 urls.py에 settings의 DEBUG 옵션이 TRUE일 경우에만 이미지 파일 serving 허용할 수 있도록 코드 추가
  
- **version 1.9 어드민 페이지 변경 코드 추가**
  - 어드민 페이지 내 모델의 필드명 표시하기
  
- **version 2.0 모델 내 필드 추가 및 속성 변경**      
  - Customer 모델 : user 필드 null, blank = False로 변경 / name 필드 null = False로 변경 (user와 name필드가 비어 있으면 안 되기 때문)       
  - Post(Product) 모델 : price 필드를 floatField에서 PositiveIntegerField로 변경 (가격이니까 실수보다는 양의 정수로 수정하는 게 맞다고 판단) / created_at 필드는 DateTimeField에 auto_now_add=True 옵션을 추가. (상품 데이터가 언제 생성되었는지 필요하기 때문.) / updated_at 필드를 새로 생성하고 DateTimeField의 auto_now=True 옵션을 추가. (상품 데이터를 수정했을 때 기록을 남기기 위해서 날짜가 갱신되어야 한다.)       
  - OrderItem 모델 : quantity 필드가 원래 null=True, blank=True 였으나 null=False, blank=False로 수정. (수량은 비어있으면 안되고 최소 1개로 설정되어야 하기 때문)
  
- **version 2.1 IPython 8.0.1 설치**
  - 설치한 이유는, 문법에 따라서 색상으로 강조를 해줘서 기존의 장고 연동 shell보다 작성하기 편함. 그리고 여러 줄에 걸쳐서 코드 입력 후, 위쪽 화살표로 전체 코드를 다시 불러오기가 편리함.
  
- **version 2.1 Admin 페이지 개선**
  - admin.py 에서 admin모듈의 ModelAdmin 클래스를 상속받아서 모델 클래스를 정의하고, register 장식자를 이용해 admin에 등록
  - 그리고 나서 클래스의 list_display 속성을 추가하여 -> admin페이지에 모델 별 필드를 표시해서 모델 데이터를 한눈에 파악할 수 있도록 개선
  
- **version 2.2  Admin 페이지 개선 및 메인 화면에서 검색 기능 구현**   
  - Admin 페이지 개선    
    - admin.py에서 mark_safe 함수를 사용해서 Post 모델 객체의 이미지 url를 admin 페이지에서 볼 수 있도록 이미지으로 표시     
    - settings.py에서 MEDIA_URL과 MEDIA_ROOT를 수정하고 models.py에서 Post 모델 ImageField에 upload_to 속성을 설정 / posts앱의 post모델 디렉터리 밑에 년/월/일 디렉터리로 구분하여 더 깔끔하게 관리할 수 있도록 설정.
  - 메인 화면에서 검색 기능 구현    
    - index.html에서 form element를 사용 / action attribute를 비워두어서 현재 form이 있는 같은 주소로 URL를 request하게 되고 Input element에 name를 query로 설정해서 값을 전송하고 / value도 query로 설정해서 검색한 이후에도 값이 남아있게끔 설정   
    - View index 함수에서 query라는 변수를 지정하고 GET 방식으로 들어온 query라는 이름으로 담긴 값을 담아준다. 그리고 query가 있을 때(검색했을 때) Post 모델 전체를 조회한 posts 변수를 다시 정의해서, filter를 통해 검색한 값이 포함되는 데이터로 설정. Q 함수를 import 해서 제품명 또는 브랜드명을 검색할 수 있도록 설정
  
- **version 2.4 상품 목록을 보여주는 메인 페이지 상품 개수 수정**
  - index View 함수에서 posts = Post.objects.all().order_by('-id')[:8] -> 이렇게 전체 Post 데이터에서 id필드를 기준으로 역순처리하고, 8개의 데이터만 가져오기.
  - 그래서 index 메인 페이지에는 DB에 그 이상의 데이터가 있을지라도, 8개의 상품 목록만 항상 보여줄 수 있도록 설정 완료.
  
- **version 2.41 bootstrap의 navbar를 이용해서 반응형 웹사이트가 될 수 있게 설정**
  - 아직 메인 상품 목록은 되지 않음 / navbar만 반응
  - 상품 상세 페이지도 아직 미반영
  
- **version 2.42 상품 1개 조회 시, DoesNotExist 오류가 발생했을 때는 Http404, 즉 Page not found 오류를 띄울 수 있게 설정**
  - 그래서 posts 앱의 views.py에 상품 1개 조회 시, 예외처리를 위해 Http404 import 진행
  - 404에러는 서버에서 요청한 리소스를 찾을 수 없는 경우를 의미
  
- **version 2.5 로그인/로그아웃 및 회원가입 기능 구현**   
  - Accounts App을 생성하고, 앱 내부 urls.py에서는 회원가입 / 로그인 / 로그아웃 URL 설정
  - base.html에서 로그인 및 회원가입 버튼을 누르면 -> GET방식으로 HTTP Request 진행 + {% if user.is_authenticated %} -> user라는 변수를 바로 사용할 수 있게 되므로, is_authenticated 함수를 사용 / 해당 함수는 로그인 되어있으면 True를 아니면 False를 반환하는 Boolean 함수이다. -> 따라서 로그인 되어있을 때, 로그아웃 버튼과 마이페이지 버튼을 생성하게 설정 -> 로그아웃 역시 정보 노출이 되지 않게 POST방식으로 진행  
  - sign_up.html에서는 form element로 POST방식으로 HTTP Request진행 -> 아이디 / 비밀번호 / 비밀번호 확인 / 닉네임 / 이메일을 입력받고, 관심있는 사회문제를 선택할 수 있게끔 설정      
  - login.html에서는 로그인 실패 시, 에러 메시지를 띄우고 POST방식으로 HTTP Request 진행 -> 아이디와 비밀번호만 받게끔 설정      
  - 앱 내부 views.py의 sign_up View에서는, GET방식일 경우 회원가입 페이지를 랜더링하고 POST방식일 경우 회원가입 절차 진행 => POST방식으로 전달한 username / password 데이터가 있는지 확인하고, password와 password_check데이터가 같은지 확인 -> 만약 같다면 User모델의 create_user 함수를 사용해서 username / password데이터로 User 모델에 추가(회원가입) -> 그리고 회원가입 시 입력한 nickname / email 데이터를 변수에 저장하고 User 모델과 OnetoOne관계인 Customer 모델에 해당 유저 및 데이터 추가 -> 위 과정을 다 진행한 다음, 자동으로 auth모듈의 login함수를 통해 로그인을 시키고 메인 페이지로 redirect해주기 -> 만약, 회원가입 정보를 다 받지 못한다면 context 딕셔너리에 error라는 key를 저장해서 에러 메세지 띄우기        
  - 앱 내부 views.py의 login View에서는, GET방식일 경우 로그인 페이지를 랜더링하고 POST방식일 경우 로그인 절차 진행 => POST방식으로 전달한 username / password 데이터가 있다면, auth 모듈의 authenticate 함수를 사용해서 username / password 데이터를 가진 유저가 있는지 확인 진행 -> 유저가 있다면 user 인스턴스를 return하므로, 그렇다면 auth 모듈의 login함수를 사용해서 로그인 시켜주고 바로 메인페이지로 redirect -> 만약, 그런 유저가 없다면 context에 error key 저장해서 에러 메세지 띄우기 -> 로그인 정보를 다 받지 못한다면 모두 입력하라는 에러 메세지 띄우기      
  - 앱 내부 views.py의 logout View는 POST방식일 경우 auth모듈의 logout함수를 사용해서 로그아웃 진행 -> 서버 내 쿠키와 세션 정보를 초기화        
  - +++ 추가해야 할 사항 : Customer 모델의 필드가 현재 user / name / email 이렇게 되어있는데, 여기에 사회문제와 관련된 필드를 추가해서 -> 회원가입 시 받은 정보를 DB에 저장하게끔 하기
  
- **version 2.6 모델 이름을 Post에서 -> Product로 수정**
  - 상품과 관련된 필드들이 Post라는 이름의 모델에 정의되어 있는 것이 맞지 않다고 판단        
  - 먼저 python manage.py migrate posts zero -> 이렇게 입력하고나서 앱이름/migrations/ 내의 마이그레이션 파일을 모두 삭제       
  - 그리고 앱 내부 파일들을 하나씩 보면서 모델명 변경으로 인해 수정해야 할 사항들 수정         
  - 그리고 나서 python manage.py make migrations posts 를 진행 -> migrations 파일 0001 생성        
  - 마지막으로 python manage.py migrate posts 진행
  
- **version 2.7 Customer 모델에 problem이라는 필드 추가**    
  - 회원가입 시 유저의 관심있는 사회문제를 1개 받고 그 값을 Customer 모델에 추가하기 위함 / 관심있는 한가지의 문제가 없을수도 있으니 null=True 설정    
  - Admin.py에 Customer 모델 관련해서 list_display 리스트에 problem 필드 추가.     
  - accounts 앱의 views.py -> sign_up View에서 problem = request.POST.get('social') -> 이렇게 유저가 회원가입 시 선택한 사회문제를 받아서 변수로 저장하고 customer = Customer(user=new_user, name=name, email=email, problem=problem) -> 이렇게 Customer 모델에 값을 입력하도록 설정      
  
- **version 2.7 마이페이지 메뉴 클릭 시, 유저의 정보를 출력해서 보여주기**      
  - accounts App 내부에 urls.py에서 마이페이지 URL를 설정하고, mypage라는 View 함수 설정     
  - 그리고 accounts 디렉터리 내부에 mypage.html을 생성해서 유저 정보 출력 / request.user.is_staff로 관리자 여부를 True/False로 확인 가능 
  
- **version 2.8 products App 생성 및 모델 위치 수정**      
  - 원래 posts 앱에 있었던 Customer 모델을 accounts 앱에 models.py로 이동시킴 -> 이유는 posts 앱에 모든 모델을 구성하는 것이 비효율적이라고 생각했기 때문       
  - products라는 App 생성 -> 이유는 posts App에 게시판이 아닌 상품들 관련 기능들이 있었기에 products라는 App에 해당 기능을 수행할 수 있도록 수정        
  - 기존 posts App에는 게시판을 위한 Post 모델을 posts 앱 내부 models.py에 설정
  
- **version 2.9 posts App에 Brand 모델 생성**   
  - posts App에 Brand 모델 생성 / 추가한 이유는, 입점 소셜벤처 페이지에서 브랜드를 소개 및 브랜드 상세 페이지를 보여주기 위해 추가   
  - 또한, Brand모델과 Product 모델 관계를 1:N으로 설정해서 입점된 브랜드의 상품들을 관리하게끔 설정
  - ERD에 해당 내용 반영    
  - Product 모델에 이미지 필드 2개 추가 → 상품 상세 페이지에서 추가 이미지를 보여주기 위함
  - 입점 소셜벤처 페이지는 ListView를 상속받아서 View로 설정     
  - 상품 상세페이지 수정 + 입점 소셜벤처 페이지 생성
  
- **version 2.91 Brand 모델 및 Customer 모델 수정**      
  - Brand 모델에 problem 필드 추가 / 해당 브랜드가 해결하고자 하는 사회문제를 구분해 카테고리 페이지에서 분류할 수 있도록 설정         
  - Customer 모델 user/name/email 필드에 unique 속성 부여 / 사용자ID와 닉네임, 이메일이 중복되지 않게 설정
  
- **version 2.92 Brand 모델 수정**      
  - Brand 모델에 image 필드 추가 / 브랜드 상세 페이지에서 보여줄 대표 이미지를 위해 필드 추가
  
- **version 2.93 브랜드 상세페이지 업데이트**      
  - 홈페이지 버튼 클릭 시 DB에 저장된 url로 해당 브랜드 홈페이지로 이동      
  - Brand DB에 저장된 short_content / long_content 표시      
  - 현재 판매되고 있는 해당 브랜드 제품을 Carousel을 이용해 자동으로 보여주기      
  - 이 때, 해당 상품 이미지 클릭 시 제품 상세페이지가 나오게끔 설정     
  - 제품 상세페이지에서 브랜드명 클릭 시, 브랜드 상세페이지가 나오게끔 설정
  
- **version 3.0 DBMS를 MySQL로 설정**     
  - MySQL로 설정한 이유는, 현재 시점에서 Oracle다음으로 가장 많이 사용하는 DBMS이기 때문에 안정적이라고 판단해서 MySQL로 설정하게 됨(https://db-engines.com/en/ranking 여기서 확인 가능)
  - 먼저 AWS에 들어가서 RDS로 들어감 -> 그리고 데이터베이스 생성 클릭. MySQL 버전은 8.0.28      
  - 해당 템플릿은 프리티어로 1년 무료 선택       
  - 해당 DB인스턴스는 → db.t3.micro 사양으로 2 vCPUs, 1GiB RAM, 네트워크: 2,085Mbps / 스토리지는 범용 SSD(gp2), 할당된 스토리지는 20 GiB / 최대 스토리지 임계값은 1,000 GiB   
  - AWS RDS에서 VPC 보안 그룹 설정 완료       
  - DB 관리 툴인 DBeaver를 사용해서 우리가 생성한 데이터베이스 서버 연결 / DBeaver는 22.0.2버전 사용       
  - 그리고나서 DBeaver를 이용해서 impactmuseum이라는 이름의 DB생성 → DBeaver의 좌측 Navigator에 DB 생성 확인      
  - 이제 django의 settings.py로 가서 DB 엔진을 sqlite3에서 mysql로 바꾸고 값 추가해서 설정       
  - DB에 붙는 것을 도와주는 어댑터 역할, 콘센트 역할을 하는 클라이언트인 mysqlclient 설치         
  - 다시 python manage.py migrate를 진행        
    - **이 과정에서 해당 경고 발생, 알아보기** --> WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-sql-mode       
  - DBeaver에서 새로고침하면 테이블이 생성되어 데이터 추가 완료
  
- **version 3.1 Posts 앱 내부 models.py에 Problem이라는 모델 클래스 추가**    
  - 사회문제 모델 테이블을 만들어서 “사회문제” 페이지에서 각 문제들을 소개하고 그 문제에 속해있는 입점 브랜드들을 보여주기 위해 추가     
  - 일단은 name / image / content 필드로 구성     
  - 그리고 Brand 모델에 있는 problem 필드를 ForeignKey로 바꿔서 Problem 모델과 Brand 모델이 1:N관계가 되게끔 설정      
  - ForeignKey 설정 시, on_delete=models.PROTECT로 설정한 이유는 규정한 사회문제가 없어져도 일단 입점된 브랜드의 정보들은 그대로 유지하기 위함
  
- **version 3.11 사회문제 페이지 구성 진행**     
  - 사회문제 페이지를 클릭했을 때, 우리나라에 존재하는 사회문제 리스트를 보여주고 해당 문제 클릭 시 문제에 대한 설명과 함께 그 문제를 해결하기 위해 노력하는 소셜벤처 보여주기      
  - Problem 모델에 short_content 필드 추가
  
- **version 3.12 마이페이지에서 본인 정보 수정 기능 추가**      
  - 마이페이지에서 정보 수정하기 버튼 클릭 시, 본인이 회원가입 시 입력한 아이디와 닉네임, 이메일, 관심있는 사회문제를 변경할 수 있게 코드 추가      
  - id 정보는 request.user.username으로 접근하고 나머지 정보들은 request.user.customer로 접근한 customer의 필드를 변경하는 방식으로 설정     
  - 추가로 관리자 계정의 경우, {% if request.user.is_staff %} 라는 if문을 사용해서 관리자 여부 : O 이렇게 표시되도록 수정
  
- **version 3.2 allauth 라이브러리 설치**    
  - **소셜 로그인을 위한 django allauth 라이브러리 설치** 
    - **django-allauth 라이브러리를 선택한 이유는, 거의 대부분의 소셜 로그인을 지원하고 회원가입 시킬 수 있는 범용성이 좋다는 판단으로 선택**
  - settings.py INSTALLED_APPS에 추가로 'django.contrib.sites' 등록 / 어드민 상에서 카카오 또는 구글 인증 정보 설정을 위해 sites 모델 등록
    - django_site 모델에 127.0.0.1:8000 이런식으로 domain과 name 필드를 설정해줘야, redirect url를 우리가 정한대로 설정할 수 있다. settings.py에 있는 SITE_ID가 해당 모델의 pk값을 의미하게 된다.     
  - settings.py INSTALLED_APPS에 추가로 'allauth'와 'allauth.account' 등록 / allauth에서 사용하는 계정 set들과 관련된 기능들을 가지고 올 수 있게 설정    
    - 'allauth.socialaccount' 을 등록해서 allauth로 SNS 계정 연동이 가능하게 해주는 모듈 설정     
    - 그 모듈안에 providers 다음에 auth0 / google / kakao 이렇게 우리가 연동하기를 원하는 provider를 각각 설정     
  - settings.py에 allauth 관련 설정 추가    
    - 로그인이 성공할 경우 redirect 해주는 페이지 설정, 로그아웃이 성공할 경우 redirect 해주는 페이지 설정, 로그아웃 시, URL로 GET으로 접근해도 로그아웃 처리가 가능할 수 있도록 설정   
  - 프로젝트 디렉터리 내부 urls.py에 소셜 로그인 리디렉션 URI를 위한 설정 추가    
    - path('oauth/', include('allauth.urls')), 이렇게 추가      
  - migrate 진행 이후, sites 앱의 Sites라는 모델 / socialaccount 앱의 socialaccount, socialapp, socialapp_sites, socialtoken 모델이 추가됨
  
- **version 3.21 구글 및 카카오 소셜 로그인 기능 구현(내 구글 및 카카오 계정만 가능)**    
  - **Google Cloud Platform 사이트에 가서 새로운 impact-museum 프로젝트 생성**    
    - 지금은 게시 상태가 테스트이기 때문에 테스트 사용자로 등록된 구글이메일만이 소셜 로그인이 가능 / OAuth 동의 화면 메뉴에서 내 구글 이메일만 등록
    - 리디렉션 URI는 http://localhost:8000/oauth/google/login/callback/ 이렇게 설정     
  - settings.py에 설정 추가 / allauth에서 account 로그인을 지원하기 위한 인증 로직 및 백엔드 로직을 설정하기 위해 AUTHENTICATION_BACKENDS 변수 설정     
    - 해당 모듈을 설정해서 클라이언트 ID랑 비밀번호를 어드민에 입력해서 그 값을 가지고 OAuth에 필요한 값들을 해당 SNS 서버에 전송할 수 있게됨      
    - SOCIALACCOUNT_PROVIDERS 변수를 딕셔너리로 추가로 설정해서 google로부터 profile이랑 email를 받아오도록 설정     
  - 어드민 페이지에 들어가서 Sites 모델에 도메인 값 추가    
    - 해당 모델은 우리 사이트의 도메인 값을 넣어주는 역할을 해준다. 그래서 나중에 socialaccount에서 연동을 할 때 SNS한테 전달 할 우리 서버의 도메인 정보를 불러오는 역할도 해주기 때문에 이 모델에 우리의 디폴트 URL를 입력해주기(127.0.0.1:8000) / 지금 테스트 서버이기 때문에 나중에는 배포된 도메인으로 수정해야 함     
    - 이렇게 설정해주면 redirection URI 요청이 들어갈 때 127.0.0.1:8000 정보를 읽어서 보내기 때문에 구글에서 '아, 내가 승인한 도메인 리디렉션 URI가 맞구나' 라고 인식을 해서 승인을 해줄 수 있게됨      
  - 어드민 페이지에 들어가서 Social applications 모델 데이터 추가    
    - Social applications 모델에서는 우리가 데이터를 이용할 provider(ex. Google, Kakao 등)에 대한 정보를 입력. provider 필드에는 google이나 kakao가 들어가고 각각 등록할 때 받은 클라이언트 id와 클라이언트 secret를 저장하여 나중에 새로 발급 시 바로 바꿀 수 있게 하드코딩 하지 않고 DB에 저장
   
  - 로그인 및 회원가입 페이지 template에 socialaccount 모듈을 load 해주고 socialaccount 안에 있는 필요한 자바스크립트들을 불러올 수 있게 해주는 필터인 providers_media_js를 호출해주기     
    - 추가로 a element를 이용해서 provider_login_url이라는 필터를 사용하고 google provider에 로그인 주소를 가지고 올 수 있게 설정       
    - 여기까지 구글 소셜 로그인 기능 구현 완료
  - **해당 과정에서 구글 로그인 버튼 클릭 시, 오류 발생**    
    - **소셜 로그인 시, customer 모델에 데이터가 들어간게 아니기 때문에 메인페이지와 장바구니 페이지에 들어가면 오류가 발생하고 있음**    
    - **그리고 마이페이지 클릭 시, 닉네임만 데이터가 뜨고 나머지는 customer 모델을 기준으로 코드를 작성했기 때문에 다른 정보가 없음**     
  - **카카오 개발자 사이트에 가서 새로운 애플리케이션 추가 / Web 플랫폼을 등록하고 Redirect URI를 http://localhost:8000/oauth/kakao/login/callback/ 로 설정**  
    - 카카오에서는 REST API 키가 클라이언트 ID역할을 하게 됨 / 추가로 Client Secret를 생성
    - 구글 소셜 로그인 기능과 마찬가지로 template에 소셜 로그인 관련 코드 추가 
    - 구글 소셜 로그인 기능과 마찬가지로 Social applications 모델에 들어간 다음, 새롭게 카카오 로그인을 위한 Provider 1개를 추가     
    - 추가로 카카오 로그인을 하게 되면 기본적으로 소셜 로그인을 할 때 마다 확인 이메일을 발송하도록 내부 디폴트 로직이 되어있어 이 부분을 꺼줘야 한다. / settings.py # All auth 부분에 ACCOUNT_EMAIL_REQUIRED = False, ACCOUNT_EMAIL_VERIFICATION = 'none' 다음과 같은 변수를 설정해서 카카오 로그인 시 해당 유저의 이메일을 가져오지 않게 설정. 그리고 none 설정은 확인 이메일이 반복해서 가지 않게 설정     
  - **이러한 소셜 로그인 성공 시 --> django User 모델에 계정 데이터가 추가된다. 그리고 Social accounts 모델에도 계정 데이터가 추가된다.**

- **version 3.3 Navbar 장바구니 개수 모든 페이지에서 출력 가능하게 설정**   
  - base.html에 cartItem이라는 변수로 장바구니 개수를 Navbar에서 출력하고 있었으나, 메인페이지에서만 표시가 되고, 모든 앱 View에 cartItem 변수를 설정하기에는 코드가 너무 길어지게 됨
  - 그래서 products 앱 내부에 cartitems_tag.py라는 파일을 만들고 해당 파일에 공통적으로 들어가는 코드들을 cartitems_count 라는 이름의 함수로 설정   
    - 해당 함수는 if문으로 로그인이 되었다면 해당 유저로 customer모델에 접근하고 Order 모델의 인스턴스를 생성하거나 가져오게 된다. 그리고 Order모델에 정의한 get_cart_items 함수를 사용해서 장바구니에 추가한 개수를 cartItems라는 변수로 설정한다. 로그인을 하지 않았다면, cartItems를 0으로 설정해서 보내준다.
  - 해당 함수를 products / posts / accounts 앱 내부에 있는 views.py에서 모두 import를 진행하고, cartitems_count 함수를 cartItems_data라는 변수로 가져와서 모든 View에 cartItems 변수가 template으로 보내질 수 있도록 설정   
  - 그래서 어떤 페이지에서든 본인의 장바구니 상품 개수를 Navbar에서 확인할 수 있게 됨

- **version 3.31 Post 모델 및 admin.py 수정 / 메인페이지 검색창 수정**   
  - Post 모델에 추가로 Category 클래스를 정의하고 category 필드를 생성해서 공지사항 글의 종류를 선택할 수 있도록 설정
    - [해당 모델 필드 공식 문서에서](https://docs.djangoproject.com/en/4.0/ref/models/fields/) choices 속성 내용 참고 / 글의 카테고리는 일반/장애인/환경/고용/교육/노인 이렇게 설정
    - gettext_lazy 함수를 사용해서 다국어 처리가 가능하도록 코드 설정
    - author 필드에는 related_name을 author_post로 설정하고 / title 필드를 추가해서 게시판 글의 제목을 작성하게끔 설정 / body 필드는 CharField에서 TextField로 변경 (많은 양의 글자를 담을 수 있도록 하기 위함) / updated_at 필드를 추가해서 해당 글이 수정될 때마다 날짜와 시간이 기록될 수 있도록 설정
  - posts 앱 내부 admin.py 코드 수정   
    - admin.py에서 Brand 모델 관련, 다른 필드를 어드민 페이지에서 확인할 수 있게 추가
    - logo_tag라는 함수를 정의하고 mark_safe 함수를 사용해서 어드민 페이지에서 로고 이미지를 확인할 수 있도록 코드 추가
    - Post 모델 관련해서도 어드민 페이지에서 id와 작성자, 제목, 카테고리, 내용, 생성일자, 수정일자 필드가 보이도록 코드 설정
  - 메인페이지에서 검색창에 아무것도 검색하지 않은 상태일 경우, 메세지 보이게 설정   
    - 메인페이지에서 검색창에 아무것도 검색하지 않을 경우, “상품 이름이나 브랜드를 검색해 보세요!” 라는 메세지 출력하게끔 코드 추가
    - products 앱 내부 views.py - index 함수에서 → context 딕셔너리로 query 변수를 보낼 때, 'query': query if query else '상품 이름이나 브랜드를 검색해 보세요!' 이렇게 아무것도 검색하지 않을 경우, query 변수에 저장된 데이터가 없기 때문에 '상품 이름이나 브랜드를 검색해 보세요!' 라는 메세지를 띄울 수 있도록 if문 추가

- **version 3.4 공지사항 게시판 기본적인 CRUD 완료**   
  - posts 앱 내부에 board.html을 생성해서 공지사항 게시판 데이터 출력    
    - 카테고리 DB값이 아닌 display값을 출력하기 위해 {{ post.get_category_display }} 라는 django template language 작성
    - 카테고리 별로 게시판에서 다른 색깔로 표시되도록 if문 설정
    - 공지사항이기 때문에 어드민 계정이 아니면 글 생성 버튼 보이지 않게 설정
  - posts 앱 내부에 board_create.html을 생성해서 공지사항 게시판 글 작성페이지 추가   
    - POST방식일 때 글 생성될 수 있도록 views.py 코드 설정하고, Post 모델에 데이터 생성할 때는 create 함수로 진행 / author 필드는 request.user.customer로 설정
    - 카테고리 데이터를 드롭다운으로 받아서 Post 데이터 생성 시 들어갈 수 있도록 설정 완료
  - posts 앱 내부에 board_detail.html을 생성해서 공지사항 게시판 글 조회 페이지 추가   
    - 게시글 하나 조회 시, 카테고리가 상단에 표시되도록 설정
    - 상세 페이지에서 로그인된 계정과 게시글 작성자가 같은 경우에만 수정 및 삭제 버튼이 뜨도록 설정 완료
  - posts 앱 내부에 board_edit.html을 생성해서 공지사항 게시판 글 수정 페이지 추가
    - 로그인된 계정과 게시글 작성자가 같은 경우, 상세 페이지에서 수정 버튼을 누르면 수정할 수 있는 페이지를 띄우게 설정
    - 이미 선택 및 작성된 카테고리와 글 제목, 내용을 가져와서 수정할 수 있게 기능 구현 완료
  - 로그인된 계정과 게시글 작성자가 같은 경우, 상세 페이지에서 삭제 버튼을 누르면 해당 게시글을 삭제할 수 있도록 기능 구현 완료

- **version 3.41 공지사항 게시판 페이지네이션 적용**
  - posts 앱 내부 views.py - board 함수내에 페이지네이터 적용을 위한 코드 추가 
    - Paginator 클래스를 이용해서 Post 모델 데이터와 한 페이지 당 보여줄 데이터 개수를 설정
    - template에서 페이지 클릭 시, page라는 이름의 GET 데이터를 확인
    - paginator의 get_page 메소드로 해당 페이지 볼 수 있게 변수 설정
    - paginator의 page_range 메소드로 페이지 리스트를 template에서 볼 수 있게 변수 설정
  - board.html에서 페이지네이션을 위한 코드 작성
    - posts라는 변수에 has_previous / has_next로 이전 페이지 및 다음 페이지 버튼 생성
    - {% for i in page_range %} / {% if i == posts.number %} 해당 코드로 페이지 리스트에서 번호 1개씩 뽑고 그 번호가 현재 페이지와 일치할 경우, 다른 색깔의 버튼 보여주기

- **version 3.42 settings.py 데이터베이스 정보 환경변수로 관리**    
  - django-environ 라이브러리를 설치해서 settings.py에 있는 중요한 정보들을(SECRET_KEY, MySQL의 HOST, NAME, USER, PASSWORD 등) 환경변수로 관리할 수 있게 설정 완료
    - 루트 디렉터리 위치에 .env 파일을 만들어서 중요한 정보들을 변수로 지정
    - settings.py에서 environ를 import하고 환경변수를 불러올 수 있게 env를 정의하고 .env파일을 불러올 수 있게 설정 
    - 중요한 정보들을 env 변수로 불러오게끔 변경
    - [참고 블로그](https://velog.io/@kyleee/TIL56-django-environ%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98-%EA%B4%80%EB%A6%AC)
    - [참고 블로그2](https://ffoorreeuunn.tistory.com/358)
    - 그리고 .gitignore 파일에 .env를 포함시켜서 push 할 때 해당 파일을 포함시키지 않도록 하고 데이터가 github에 공개되지 않도록 설정 완료   
  - AWS 루트 계정에 MFA 설정 활성화 완료
    - AWS 루트 계정에 MFA 2단계 인증 과정을 설정 및 활성화 완료
    - 아이폰에 Google OTP 앱을 설치하여 QR코드 스캔 및 코드 입력으로 로그인 시 보안 강화

- **version 3.5 공지사항 게시판 게시글 전체 번호 내림차순으로 출력하기**
  - posts 앱 내부에 templatetags라는 패키지를 만들고 그 안에 post_filter.py라는 파일을 생성
  - 해당 파일에 sub라는 filter를 정의해서 template 값에서 수를 차감할 수 있게 설정
  - board.html에서 위의 필터를 사용해서 {{ posts.paginator.count|sub:posts.start_index|sub:forloop.counter0|add:1 }} 이렇게 게시글 전체 번호를 내림차순으로 출력
    - posts.paginator.count : paginator로 출력 할 총 객체 수
    - posts.start_index : 해당 paginator 페이지의 첫번째 데이터 index를 출력 / ex) 1페이지 당 10개로 설정했으니 1페이지는 1, 2페이지는 11
    - forloop.counter0 : for문을 순회하면서 0부터 출력 / 다른 paginator 페이지에서는 다시 0부터 출력

- **version 3.51 공지사항 게시판 상단에 고정 기능 추가**
  - [해당 블로그 참고](https://parkhyeonchae.github.io/2020/04/09/django-project-22/)
  - Post 모델에 top_fixed라는 필드를 BooleanField로 추가(default=False)
  - board_create.html에 “상단에 고정하기” 라는 체크박스를 추가하고 value를 True로 설정
  - board_create View에서는 상단 고정 체크 시, top_fixed 필드값을 True로 변경에서 글 생성하게 설정 / board View에서는 상단 고정 여부가 True인 게시글만 가져오도록 filter 사용
  - board.html에서 상단 고정 게시글을 보여주기 위해 top_fixed라는 값이 있으면 for문으로 상단 고정 여부가 True인 게시글을 상단에 출력하도록 설정

- **version 3.52 MySQL Strict 모드 default로 설정**
  - python manage.py migrate 실행 시, 관련 경고가 계속 발생
  - settings.py - DATABASES 변수에 MySQL Strict 모드를 기본으로 설정하는 코드 추가
  - Strict MODE란, 데이터의 무결성을 MySQL에서 체크해주는 기능
    - ex) NOT NULL로 설정하면 무조건 값을 넣어줘야 에러가 안나게끔 설정
  - [참고 블로그](https://zetawiki.com/wiki/Django_mysql-sql-mode_warning )

- **version 3.53 get_object_or_404로 상품 1개 조회 예외 처리 진행**
  - products 앱 내부 views.py의 상품 1개 조회 detail 함수에서 기존에는 try-except로 예외처리를 진행했으나, get_object_or_404를 사용해서 더 간결하게 예외 처리 설정 완료

- **version 3.54 requirements.txt 파일 생성**
  - 현재 프로젝트의 패키지들을 requirements.txt 파일에 기록 완료
  - pip freeze > requirements.txt 명령어로 기록

- **version 3.6 장바구니 기능 개선**
  - 상품 상세 페이지에서 "장바구니에 담기" 버튼 클릭 시, data-product와 data-action이라는 속성을 통해 자바스크립트로 장바구니 추가하는 기능인 updatedItem 함수 기반 View url로 request 진행
  - products 앱의 updatedItem View에서 cart.js에서 보내준 데이터를 JSON 형태로 가져오고 productID로 추가하려는 상품을 Product 모델에서 가져오기 / action으로는 add
와 remove에 따라 장바구니 개수 조절하게끔 설정
  - 상품 상세 페이지에서 "장바구니에 담기" 버튼 클릭 시, onClick 속성을 통해 popup() 함수로 해당 상품이 장바구니에 추가되었다는 확인창 생성
  - 장바구니 페이지에서 상품별 “삭제하기” 버튼 클릭 시, 수량과 상관없이 장바구니 목록에서 삭제하는 기능 생성
    - 새로운 url를 생성하고 cart_delete라는 함수 기반 View를 통해 장바구니 데이터 삭제
  
- **version 3.7 DRF(Django REST Framework)로 API 서버 구축**
  - pip install djangorestframework 이렇게 DRF 설치 완료
  - products와 posts 앱 내부에 있는 Product/Post 모델과 관련한 CRUD API 서버 설정
  - products와 posts 앱 내부에 serializers.py를 생성하고 ModelSerializer를 상속받아 각 모델에 해당하는 Serializer 클래스 정의 
  - products와 posts 앱 내부 views.py에서는 ModelViewSet를 상속받아 기본적인 CRUD가 가능하게끔 각 모델에 대한 ViewSet를 정의
  - products와 posts 앱 내부 urls.py에서 DefaultRouter를 설정하여 API ROOT 페이지를 응답하고 각 모델에 대한 ViewSet를 연결

- **version 3.73 lazy-loading 개선 사항 반영**
  - 먼저 페이지 로딩 시 날라가는 쿼리를 확인해보기 위해 django-debug-toolbar 설치 완료
  - products 앱 내부의 cartitems_tag.py에서 기존에는 **items = order.orderitem_set.all()** 라고 되어있는 코드를 -> **items = order.orderitem_set.select_related('product').all()** 이렇게 select_related 메소드를 사용해서 lazy-loading 문제를 해결
    - select_related('product') 라고 설정하면서 해당 ORM 코드에서 product와 관련된 데이터를 같이 가져와준다. (product와 orderitem이 1:N관계이기 때문)
    - 기존에는 장바구니 페이지로 넘어갈 때 관련된 쿼리의 개수가 9개 였는데 총 쿼리가 6개로 줄어든 것을 확인할 수 있었음
    - 줄어든 쿼리는 cart.html과 checkout.html에 있는 {{ item.product.imageURL }}, {{ item.product.product_name }} 다음 코드에서 개선된 것으로 확인 
    - select_related 메소드로 product 데이터를 ORM 코드에서 같이 가져와서 데이터베이스에 Hit할 필요가 없어지고, 쿼리가 적게 날라가서 페이지 속도가 개선됨

- **version 3.8 AWS EC2를 이용해서 Redis 인메모리 데이터베이스 서버 구축**
  - **로그인 시 서버에 저장되고 있는 세션을 redis 서버 메모리에 저장할 수 있도록 설정**
  - 서버가 여러 대 늘어나서 사용자가 다른 서버에 요청을 보내더라도 세션을 이렇게 Redis 서버로 공유하면 항상 로그인 유지가 가능해진다.
    - AWS EC2를 새롭게 생성하고 터미널로 해당 EC2에 접속한 다음, Redis server 5.0.7버전 설치
    - 메모리 사이즈를 제한하기 위해 redis.conf 파일에서 maxmemory 512mb로 설정 
    - 그리고 데이터가 쌓일 때 기존 데이터를 삭제해줘야 할 텐데, 사용하지 않는 데이터를 순차적으로 삭제하는 것으로 maxmemory-policy allkeys-lru로 설정
    - 추가로 외부에서도 이 redis 서버에 접속할 수 있게 redis.conf 파일에서 bind 0.0.0.0로 설정
    - 그 다음, 프로젝트에 pip install django-redis-sessions로 설치해주고 settings.py에 Redis 서버 연결 코드 추가
    - 여기까지 진행하고 서비스에서 로그인을 한 다음, Redis 서버에 접속해 redis-cli 입력 후, KEYS *를 입력해보면 세션 값이 저장된 것을 확인할 수 있다.
  - **기존에는 django_session 모델에 로그인이 될 때 session_key 값이 추가되었고 로그아웃을 하면 해당 row가 삭제되었는데, 지금은 로그인이 되어도 django_session 모델에 세션 값이 추가되지 않는다.**
    - 서비스에서 로그아웃 시 세션 값이 바로 삭제된다. 

  - **추가로 settings.py에 있는 Redis 관련 중요한 정보를 환경변수로 처리**
    - 민감한 정보를 github 레포지토리에 노출시키지 않도록 settings.py에 있는 redis와 관련된 중요한 정보들을 환경변수로 관리할 수 있게 .env 파일에 변수로 지정

- **version 3.82 serializers.py 코드 수정**
  - posts 앱의 serializers.py 코드 수정
  - PostModelSerializer 클래스 내부에 read_only_fields = ('id', 'top_fixed') 코드 추가
  - Post 모델의 데이터를 생성하기 위한 POST API를 가능하게끔 하기 위해 id와 top_fixed 필드에 따로 데이터를 넣지 않도록 설정
  - id는 자동으로 늘어나고 top_fixed는 False가 default로 되어있기 때문에 굳이 생성하지 않아도 된다고 판단

- **www.impactmuseum.com 이라는 도메인으로 배포 완료**
  - AWS EC2를 새롭게 생성하여 EC2 내부에서 impact museum github 소스코드를 git clone으로 가져오고 virtualenv 가상환경 설치 진행
  - requirements.txt로 필요한 라이브러리들을 반영하고 웹 서버와 django 앱 서버를 연결시켜주는 uWSGI 설치 진행
    - uwsgi.ini 파일 내부에 프로젝트 위치 설정 및 unix 소켓 파일 생성 / 또한 uWSGI를 백그라운드에서 실행시켜 runserver를 실행하지 않고도 uWSGI만 구동시키면, 터미널 종료와 상관없이 항상 웹 서비스가 도메인과 연결되도록 설정
  - 그리고 웹 서버인 nginx 설치 진행
    - nginx.conf 파일에 nginx가 uwsgi에 정보를 넘길 수 있도록 설정
    - sites-enabled 디렉터리에 있는 default 파일에는, 이미 기본적으로 IP주소:8000 일허게 우리가 입력해도 80포트로 포트포워딩 되도록 설정되어있음
    - 그래서 여기까지 IP주소만 브라우저에 입력해도 웹 서비스가 동작하는 것을 확인
  - 가비아에서 도메인 구입 후, AWS Route 53에서 호스팅 영역 생성 진행
    - 가비아 도메인을 AWS의 네임서버와 연동시켜서 이후에 도메인과 관련된 모든 작업을 AWS 내부에서만 수행할 수 있게끔 변경
    - 그래서 해당 도메인과 연동되어있는 네임서버를 AWS의 네임서버로 교체
  - 이제 브라우저에 http://www.impactmuseum.com/ 라는 주소로 입력 시, 웹 서비스가 작동된다.

<br>
 
## 8. 회고 / 느낀점
- 프로젝트를 진행하면서 가장 중요하다고 느꼈던 부분은 바로 '모델링'이었다. 프로젝트 시작 시 모델링이 자세하게 구축이 되어있었다면 조금 더 편리하게 개발을 진행할 수 있었지 않았을까 하는 아쉬움이 많다. 여전히 모델간의 관계, 모델의 필드를 계속해서 수정해나가고 있기 때문에 앞으로도 꾸준히 모델링을 진행해나가지 않을까 싶다.
- 에러가 기본적으로 항상 발생한다고 생각하는 마인드가 필요하다고 느꼈다. 강의에서 배운 내용을 그대로 해당 프로젝트에 적용을 시키는 과정에서도 강의 내용과 다른 오류가 발생할 수 있고, 그 과정에서 내가 몰랐던 내용들을 이해할 수 있는 좋은 단계가 된다. 따라서 항상 오류는 발생하고 그 오류를 해결하면 내가 발전할 수 있다고 생각하는 것이 좋은 마인드이다.
- 해당 프로젝트의 규모가 점점 커진다고 생각했을 때, 백엔드 개발자로서 고민해야 하는 부분이 무엇일지 생각해보자. 일단 지금까지는 사용자들의 로그인 세션 데이터를 AWS EC2를 생성하고 Redis 서버를 구축해서 메모리에 해당 데이터를 저장할 수 있도록 진행했다. 만약 추후에 사용자가 늘어나서 AWS RDS로 연결한 MySQL의 연결 상태가 좋지 못하다던지, 하나의 EC2로는 감당할 수 없을 만큼 사용자가 늘어난다면 어떤 방안들을 마련해야할지 고민해보자.

