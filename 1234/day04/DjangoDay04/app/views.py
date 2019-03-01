import os
import random

from django.http import HttpResponse
from django.shortcuts import render

from DjangoDay04.settings import BASE_DIR


def index(request):
    return render(request, 'index.html')


def basedemo(request):

    context = { # key:value
        'name': 'Hello World!',
        'age': 18,
        'score': [70,89,90],
        'username': 'root',   # root 超级管理员,
        'scoredir': [
            {'语文': 90},
            {'数学': 98},
            {'英语': 78}
        ],
        'names': ['张三', '李四', '王五', '赵柳']
    }

    return render(request, 'basedemo.html', context=context)


def includedemo(request):

    goods_list = ['ipad', 'iphone', 'mac', 'ipod']

    return render(request, 'includedemo.html', context={'goods_list':goods_list})


def home(request):
    temp = 'H<sub>2</sub>O'

    return render(request, 'home.html', context={'haha': temp})


def cart(request):
    return render(request, 'cart.html')


def mine(request):
    return render(request, 'mine.html')


def loginview(request):

    random_str = str(random.randrange(1000,10000))

    return render(request, 'login.html', context={'random_str':random_str})


def login(request):
    return HttpResponse('正在登录....')


from  PIL import Image,ImageDraw,ImageFont
import io
def verifycode(request):

    # 定义图片大小
    width = 120
    height = 40

    # 定义图片颜色
    bgcolor = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

    # 创建图片
    image = Image.new('RGB', (width,height), bgcolor)

    # 创建画笔
    draw = ImageDraw.Draw(image)


    # 添加噪点
    for i in range(0,500):
        xy = (random.randrange(0,width), random.randrange(0,height))
        fill = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
        draw.point(xy=xy, fill=fill)


    # 随机数生成(验证码)
    temp = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    random_str = ''
    for i in range(0,4):
        random_str += temp[random.randrange(0, len(temp))]

    # 字体类型
    # fontPath = os.path.join(BASE_DIR, 'app/fonts/Fangsong.ttf')
    fontPath = os.path.join(BASE_DIR, 'app/fonts/STXINGKA.ttf')
    font = ImageFont.truetype(fontPath, 30)

    # 字体颜色
    font_color_1 = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    font_color_2 = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    font_color_3 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    font_color_4 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

    # 绘制
    draw.text((10,5), random_str[0], fill=font_color_1, font=font)
    draw.text((40, 5), random_str[1], fill=font_color_1, font=font)
    draw.text((70, 5), random_str[2], fill=font_color_1, font=font)
    draw.text((100, 5), random_str[3], fill=font_color_1, font=font)


    # 线条颜色
    line_color_1 = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

    # draw.line((5,10), fill=line_color_1, width=10)
    # draw.line((100,10), fill=line_color_1, width=10)

    # 释放画笔
    del draw

    # 文件操作
    buff = io.BytesIO()
    image.save(buff, 'png')

    # 返回图片
    return HttpResponse(buff.getvalue(), 'image/png')