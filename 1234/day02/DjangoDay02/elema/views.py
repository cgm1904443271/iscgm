from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('首页 | 饿了吗')


def cart(request):
    return HttpResponse('购物车 | 饿了吗')