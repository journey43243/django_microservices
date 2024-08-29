import uuid
from django.db import models

class Products(models.Model):

    class Sale_Status(models.IntegerChoices):
        sale = 1, 'Sale'
        not_sale = 0, 'Not sale'

    class Stock_Status(models.IntegerChoices):
        in_stock = 1, 'In stock'
        out_stock = 0 , 'Out stock'
    
    class Sex_Choices(models.IntegerChoices):
        men = 3, 'Men'
        woman = 2 , 'Woman'
        boy = 1, 'Boy'
        girl = 0, 'Girl'

    class Seazon_Choices(models.IntegerChoices):
        multiseazon = 4, 'Multiseazon'
        winter = 3 , 'Winter'
        spring = 2, 'Spring'
        summer = 1 , 'Summer'
        autumn = 0, 'autumn'
    id = models.UUIDField(primary_key= True, default= uuid.uuid4)
    name = models.CharField(max_length= 255, null= False, blank= False)
    sale_status = models.IntegerField(choices= Sale_Status, default= Sale_Status.not_sale)
    price = models.FloatField(null= False, blank= False)
    stock_status = models.IntegerField(choices= Stock_Status, default= Stock_Status.out_stock)
    sex = models.IntegerField(choices= Sex_Choices, blank= False, null= False)
    seazon = models.IntegerField(choices= Seazon_Choices, blank= False, null= False)
    reviews = models.JSONField(null= True, blank= False)
    images_fk = models.ForeignKey('Images', on_delete= models.CASCADE, null= True, blank= False, related_name= 'images')

    def __str__(self) -> str:
        return self.name


class Categories(models.Model):

    class Relations_Choiches(models.IntegerChoices):
        outerwear = 0, 'outerwear'
        underwear = 1, 'underwear'
        accessories = 2, 'accessories'
        shoes = 3, 'shoes'


    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 25)
    relation_to = models.IntegerField(choices= Relations_Choiches, null= False, blank= False)
    products = models.ForeignKey('Products', on_delete= models.PROTECT ,null= True, blank= False, related_name= 'categories')

    def __str__(self) -> str:
        return self.name


class Images(models.Model):

    image = models.ImageField(upload_to='%Y%m%d')

class Sizes(models.Model):

    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=4)
    products_fk = models.ForeignKey('Products', on_delete= models.PROTECT,null= True, blank= False, related_name= 'sizes')


    def __str__(self) -> str:
        return self.name