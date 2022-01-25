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
</details>
<br>

## 5. 핵심 트러블 슈팅
### 5.1 ...

<br>

## 6. 그 외 트러블 슈팅    ==> 이러한 오류가 왜 발생했는지 & 그리고 어떤 문제를 해결해서 & 결국 내가 얻어낸 성과가 뭔지 
- models.py 설정 시 FloatField 및 IntegerField의 경우 default=0 처럼 default 값 설정 필요
- DB에서 ImageField 설정 시 이미지를 업로드 하지 않으면 html template에서 ValueError 발생 -> models.py에서 관련 모델에 @property를 설정해서 오류 방지
- Javascript 파일 - 새로 생성한 함수에서 url를 정의할 때, 상품 1개 조회 화면에서 장바구니 버튼을 클릭하기 때문에 url에 post_id(product_id) 값이 들어가야 했는데 그러지 않아 **uncaught (in promise) syntaxerror: unexpected token < in json at position 0** 와 같은 오류 발생 -> url 정의할 때 미리 정의한 post_id 변수를 +연산자로 url에 포함시키서 오류 해결   
<br>

## 7. 회고 / 느낀점
- ㅇㅇㅇ

