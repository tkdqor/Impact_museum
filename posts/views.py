from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

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

