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
