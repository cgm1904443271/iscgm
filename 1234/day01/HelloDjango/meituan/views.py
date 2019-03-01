import random

from django.http import HttpResponse
from django.shortcuts import render


# 视图函数，第一个参数必须是 request
from meituan.models import Student


def index(request):
    return HttpResponse('首页')



def home(request):
    return HttpResponse('<h1>home页面</h1> <p>hello</>')


def cart(request):
    # 返回模板
    return render(request, 'cart.html')



# 添加学生数据
def addstu(request):
    # 实例化对象
    stu = Student()
    stu.name = str(random.randrange(1,1000000)) + '张三'
    stu.score = random.randrange(1,100)

    # 存入到数据库中
    stu.save()

    return HttpResponse('添加学生-' + stu.name)