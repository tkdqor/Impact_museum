# :pushpin: Impact museum
- 사회적 가치를 추구하는 소셜벤처 이커머스 플랫폼
- url...

<br>

## 1. 제작 기간 & 참여 인원
- 2021년 1월 14일 ~
- 개인 프로젝트
<br>

## 2. 사용 기술
**Back-end**       => 해당 기술을 왜 사용했는지 이유 & 그리고 그 기술 버전을 왜 사용했는지 이유 필요!
- Python 3.9.1 
- Django 3.2.9
- DRF(Django Rest Framework) 3.13.1 (이 버전 맞는지 다시 확인 필요)
<br>

## 3. ERD 설계
<img src="https://user-images.githubusercontent.com/95380638/150262590-29403524-27cf-4329-8733-5a75ca70a8f8.png">

- Customer 모델은 User 모델과 1:1관계로 설정
- Order 모델은 Customer 모델과 1:N관계로 설정 - 1명의 사용자가 쇼핑몰에서 여러 번 주문할 수 있음
- Shipping Address 모델은 Customer 모델 & Order 모델과 1:N관계로 설정 - 1명의 사용자가 다양한 배송 주소지를 생성할 수 있고, 1개의 주문 건이 배송 취소 및 실패 등으로 다양한 배송 주소지를 가질 수 있음
- Order Item 모델(장바구니 기능을 생각하기)은 Product 모델 & Order 모델과 1:N관계로 설정 - 1개의 상품이 여러 번 장바구니에 포함될 수 있고, 1개의 주문 건에 많은 상품들이 장바구니에 추가될 수 있음
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
<br>

## 7. 회고 / 느낀점
- ㅇㅇㅇ

