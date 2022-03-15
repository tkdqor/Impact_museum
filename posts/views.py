from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import viewsets
import json
from django.db.models import Q     # 검색기능구현 시, filter 조건을 or로 설정하기 위해 Q 함수 import
from django.http import Http404    # 상품 1개 조회 시, 예외처리를 위한 Http404 import 

# Create your views here.








