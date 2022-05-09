from django import template

register = template.Library()

@register.filter
def sub(value, arg):     # sub라는 필터 정의하기
    return value - arg