from django.shortcuts import render

# Create your views here.

# 회원가입 기능
def sign_up(request):

    return render(request, 'accounts/sign_up.html')



# 로그인 기능
def login(request):
    
    return render(request, 'accounts/login.html')