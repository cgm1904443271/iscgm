from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodFypes


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


def market(request):
    foodtypes=FoodFypes.objects.all()

    return render(request,'market/market.html',context={
        'foodtypes':foodtypes,
    })


def cart(request):
    return render(request,'cart/cart.html')

def mine(request):
    return render(request,'mine/mine.html')