import hashlib
import random
import time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodFypes, Goods, User, Cart


def home(request):

    wheels=Wheel.objects.all()

    navs=Nav.objects.all()

    mustbuys=Mustbuy.objects.all()

    shops=Shop.objects.all()
    shophead=shops[0]
    shoptab=shops[1:3]
    shopclass=shops[3:7]
    shopcommend=shops[7:11]

    mainshows=MainShow.objects.all()

    data={'wheels':wheels,
          'navs':navs,
          'mustbuys':mustbuys,
          'shophead':shophead,
          'shoptabs':shoptab,
          'shopclass':shopclass,
          'shopcommend':shopcommend,
          'mainshows':mainshows,
          }

    return render(request,'home/home.html',context=data)


def market(request,childid='0',sortid='0'):
    foodtypes=FoodFypes.objects.all()

    index = int(request.COOKIES.get('index','0'))
    categoryid=foodtypes[index].typeid

    if childid=='0':
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)


    if sortid=='1':
        goods_list=goods_list.order_by('-productnum')
    elif sortid=='2':
        goods_list=goods_list.order_by('price')
    else:
        goods_list=goods_list.order_by('-price')



    childtypenames = foodtypes[index].childtypenames
    childtype_list=[]
    for item in childtypenames.split('#'):
         item_arr=item.split(':')
         temp_dir={
             'name':item_arr[0],
             'id':item_arr[1],
         }
         childtype_list.append(temp_dir)




    return render(request,'market/market.html',context={
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'childtype_list':childtype_list,
        'childid':childid,
    })


def cart(request):
    return render(request,'cart/cart.html')

def mine(request):
    token=request.session.get('token')
    user=None
    if token:
        user=User.objects.get(token=token)

    return render(request,'mine/mine.html',context={'user':user})


def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()



def register(request):
    if request.method=='GET':
        return render(request,'mine/register.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        name=request.POST.get('name')
        tel=request.POST.get('tel')
        arr=request.POST.get('arr')
        token = generate_token()

        users=User()
        users.username=username
        users.password=password
        users.name=name
        users.tel=tel
        users.arr=arr
        users.token=token
        users.save()

        response=redirect('axf:mine')

        request.session['token']=users.token

        return response

def login(request):
    if request.method=='GET':
        return render(request,'mine/login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        users=User.objects.filter(username=username)
        if users.exists:
            user=users.first()
            if user.password==password:
                token=generate_token()
                user.token=token
                user.save()
                request.session['token']=user.token
                response=redirect('axf:mine')

                return response

            else:
                return render(request,'mine/login.html',context={'ps_err':'密码错误'})
        else:
            return render(request,'mine/login.html',context={'user_err':'用户不存在'})


def logout(request):
    request.session.flush()

    return redirect('axf:mine')


def checkusername(request):
    username=request.GET.get('username')
    users = User.objects.filter(username=username)
    if users.exists():
        response_data={
            'status':0,
            'msg':'账号已被注册',
        }
    else:
        response_data={
            'status':1,
            'msg':'账号可用'
        }


    return JsonResponse(response_data)


def addcart(request):
    token = request.session.get('token')
    response_data={}
    print(token)

    if token:
        userid =''
        print(userid,'1111')
        if userid:
            user = User.objects.get(pk=userid)
            print(user)


    return HttpResponse(123)