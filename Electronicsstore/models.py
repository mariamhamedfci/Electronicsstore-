from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name  = models.CharField(max_length = 90, null =True)

    email = models.CharField(max_length = 90, null = True)

    phone = models.CharField(max_length = 90, null = True) 

    age   = models.CharField(max_length = 90, null = True)

    date_created =models.DateTimeField(auto_now_add = True , null=True)

    def __str__(self):
        return self.name
    

class Devices(models.Model):


    STATUSs = (
        ('Technology','Technology'),
        ('Household devices','Household devices'),
    )


    STATUS = (
        ('Iphone','Iphone'),
        ('Samsung','Samsung'),
        ('Huawei','Huawei'),
        ('LG','LG'),
        ('Sony','Sony'),
        ('TOSHIBA','TOSHIBA'),
    )

    #devices=  models.CharField(max_length = 60 ,null = True)
    type =  models.CharField(max_length = 60 ,null = True ,choices =STATUSs)
    name  = models.CharField(max_length = 60 ,null = True)

    price = models.FloatField(null = True)

    mark  = models.CharField(max_length = 60 ,null = True ,choices =STATUS)

    features = models.CharField(max_length = 60 ,null = True)

    date_created =models.DateTimeField(auto_now_add = True , null=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS= (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('In progress' , 'In progress'),
        ('Out of order', 'out of ordfer'),
    )

    customer = models.ForeignKey( Customer, null = True , on_delete=models.SET_NULL)
    devices = models.ForeignKey(Devices,null = True ,on_delete =models.SET_NULL )

    date_created =models.DateTimeField(auto_now_add = True , null=True)

    status = models.CharField(max_length =99 , null =True ,choices =STATUS)



class Category(models.TextChoices):
    WOMENCLOTHES = 'Women Clothes'
    BAGS = 'Bags'
    MENCLOTHES = 'Men Clothes'
    WATCHES = 'Watches'
    SHOES = ' Shoes'
    BEAUTYHEALTH = 'Beauty&Health'
    ELECTRONICDEVICES = 'ElectronicDevices'
    KIDS = 'Kid'
    HOME = 'Home'



    #pythom manage.py makemigrations
class Product(models.Model):
    name =models.CharField(max_length = 200 , default = "" , blank = False)
    description =models.TextField(max_length = 1000 , default = "" , blank = False)
    price =models.DecimalField(max_digits=7,decimal_places = 2 , default = 0)
    brand =models.CharField(max_length = 200 , default = "" , blank = False)
    category =models.CharField(max_length = 50 , choices= Category.choices , blank = False)
    ratings =models.DecimalField(max_digits= 3 ,decimal_places = 2 , default = 0)
    stock = models.IntegerField(default = 0)
    CreateAt = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User , null = True , on_delete = models.SET_NULL) 



    class ProductTwo(models.Model):
     name =models.CharField(max_length = 200 , default = "" , blank = False)
    description =models.TextField(max_length = 1000 , default = "" , blank = False)
    price =models.DecimalField(max_digits=7,decimal_places = 2 , default = 0)
    brand =models.CharField(max_length = 200 , default = "" , blank = False)
    category =models.CharField(max_length = 50 , choices= Category.choices , blank = False)
    ratings =models.DecimalField(max_digits= 3 ,decimal_places = 2 , default = 0)
    stock = models.IntegerField(default = 0)
    CreateAt = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User , null = True , on_delete = models.SET_NULL) 