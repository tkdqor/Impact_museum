from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['name']

