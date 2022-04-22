from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'problem', 'logo_tag', 'homepage']

    def logo_tag(self, brand):     # logo_tag라는 함수를 정의해서 logo 필드에 경로가 있는 경우 admin에도 보여줄 수 있도록 설정
        if brand.logo:    
            return mark_safe(f'<img src="{brand.logo.url}" style="width: 150px; height: 150px;" />')  
            # mark_safe 함수로 안전함을 표시해야 admin 페이지에 사진 표시 가능


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'category', 'body', 'created_at', 'updated_at']



