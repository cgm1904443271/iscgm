from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)


class BaseModels(models.Model):
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True



class Wheel(BaseModels):
    class Meta:
        db_table='axf_wheel'



class Nav(BaseModels):
    class Meta:
        db_table='axf_nav'


class Mustbuy(BaseModels):
    class Meta:
        db_table='axf_mustbuy'

class Shop(BaseModels):
    class Meta:
        db_table='axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=200)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=200)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=200)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

    def __str__(self):
        return self.name

class FoodFypes(models.Model):
    typeid=models.CharField(max_length=20)
    typename=models.CharField(max_length=255)
    childtypenames=models.CharField(max_length=200)
    typesort=models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'

class Goods(models.Model):
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品长名字
    productlongname = models.CharField(max_length=256)
    # 是否精选
    isxf = models.IntegerField()
    # 是否买一送一
    pmdesc = models.IntegerField()
    # 商品规格
    specifics = models.CharField(max_length=100)
    # 商品价格
    price = models.DecimalField(max_digits=6,decimal_places=2)
    # 商品超市价格
    marketprice = models.DecimalField(max_digits=6, decimal_places=2)
    # 分类ID
    categoryid = models.IntegerField()
    # 子类ID
    childcid = models.IntegerField()
    # 子类名称
    childcidname = models.CharField(max_length=100)
    # 详情页ID
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销售
    productnum = models.IntegerField()

    class Meta:
        db_table='axf_goods'

class User(models.Model):
    username=models.CharField(max_length=100,default='0',unique=True)
    password=models.CharField(max_length=100,default='0')
    name=models.CharField(max_length=50,default='0')
    tel=models.CharField(max_length=50,default='0')
    arr=models.CharField(max_length=255,default='0')
    img=models.CharField(max_length=40,default='mine1.png')
    rank=models.IntegerField(default=1)
    token=models.CharField(max_length=255,default='0')

    class Meta:
        db_table='axf_user'


class Cart(models.Model):
    user = models.ForeignKey(User)

    goods = models.ForeignKey(Goods)

    number = models.IntegerField()

    isselect = models.BooleanField(default=True)

    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table='axf_cart'