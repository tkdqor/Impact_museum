from rest_framework.serializers import ModelSerializer
from .models import Post, Brand, Problem

class PostModelSerializer(ModelSerializer):  # ModelSerializer를 상속해서 모델만 설정하고 필드 쉽게 가져오기
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'category', 'body', 'created_at', 'updated_at', 'top_fixed')
        read_only_fields = ('id', 'top_fixed')


class BrandModelSerializer(ModelSerializer):  
    class Meta:
        model = Brand
        fields = '__all__'
        depth = 1   # depth = 1 코드를 추가해서 -> Brand 모델과 1:N관계로 설정되어있는 Problem 모델 데이터를 보여주기


class ProblemModelSerializer(ModelSerializer):  
    class Meta:
        model = Problem
        fields = '__all__'