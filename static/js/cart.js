var updatedBtns = document.getElementsByClassName('cart-update')

for(var i = 0 ; i < updatedBtns.length; i++){
    updatedBtns[i].addEventListener('click', function(){
        var postID = this.dataset.post
        var action = this.dataset.action
        console.log('postID:',postID , 'action:',action)
        console.log('사용자:',user)
        if (user === 'AnonymousUser'){
            console.log('로그인이 되지 않았습니다.')
        }else{
            console.log('로그인 된 사용자 입니다.')
        }
    })
} 