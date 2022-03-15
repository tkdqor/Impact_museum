var updatedBtns = document.getElementsByClassName('cart-update')  // detail.html의 button의 클래스와 연동

for(var i = 0 ; i < updatedBtns.length; i++){
    updatedBtns[i].addEventListener('click', function(){    // 클릭했을 때 -> 밑에 입력한 코드가 정의된 함수를 실행시키자!
        var productID = this.dataset.product                      // button의 data attribute를 가져와서 변수 정의
        var action = this.dataset.action
        console.log('productID:',productID , 'action:',action)    // 개발자도구 console에 해당 데이터를 출력
        console.log('사용자:',user)                           // 개발자도구 console에 로그인된 user 정보 출력(base.html에서 정의했기 때문에 가능)
        if (user === 'AnonymousUser'){                      // 만약, 로그인이 되지 않아 AnonymousUser라면
            console.log('로그인이 되지 않았습니다.')              // 개발자도구 console에 로그인 되지 않았다고 출력
        }else{
            updateUserOrder(productID,action)                  // 로그인이 된 사용자가 맞다면 -> updateUserOrder라는 함수 실행
        }
    })
} 



function updateUserOrder(productID,action){
    console.log('로그인 되었으니 정보를 보냅니다.')                 // 로그인이 된 사용자라면 일단 개발자도구 console에 출력

    var url ='/products/' + productID + '/update_item/'           
    // url를 새롭게 정의하는데 -> 우리가 앱 단위 urls.py에서 설정한 url를 입력 -> views에서 updatedItem라는 장바구니 추가 기능 함수가 실행되게끔 설정

    fetch(url,{                               // fetch()를 이용해서 정보를 views.py로 전달  
        method: 'POST',                       // 정보를 POST 방식으로 보내기 (장바구니를 생성하는 것이기 때문)
        headers:{
            'Content-Type':'application/json',  // json의 형태로 정보를 보내겠다는 것
            'X-CSRFToken': csrftoken            // POST방식으로 보내기 위해 csrf_token 설정 + base.html에서도 설정

        },
        body:JSON.stringify({'productID': productID, 'action': action})    // productID와 action를 JSON 형태의 정보로 보내주겠다는 의미                        
    })

    .then((response) =>{              // 데이터가 views.py로 잘 전달되었는지 확인하는 과정으로 views.py에서 return되는 response를 확인하는 것
        return response.json()
    })  
    .then((data) =>{              // 우리가 받은 response를 data라고 해주고, console에 출력 해주기   
        console.log('data:', data)
        // location.reload()         // 장바구니 화면 자동으로 새로고침 설정할 수 있음 -> 장바구니 화면에서 수량 +- 버튼 클릭 시 바로 화면에 보여줄 수 있다.  ==> 근데 잘 안되서 일단 주석처리 
                
    })                                             
}



