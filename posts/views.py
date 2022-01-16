from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    product_name = request.POST.get('product_name')
    brand = request.POST.get('brand')
    post = Post(product_name=product_name, brand=brand, created_at=timezone.now())
    post.save()

    return redirect('posts:detail', post_id=post.id)


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }

    return render(request, 'posts/edit.html', context)


def update(request, post_id):
    post = Post.objects.get(id=post_id)
    post.product_name = request.POST.get('product_name')
    post.brand = request.POST.get('brand')
    post.save()

    return redirect('posts:detail', post_id=post.id)


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:index')




# RDF를 이용한 문자열 응답 API
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello World!")


# RDF를 이용한 상품 정보 1개에 대한 API
@api_view(['GET'])
def Postinfo(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)

    return Response(serializer.data)


# RDF를 이용한 CRUD API 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer