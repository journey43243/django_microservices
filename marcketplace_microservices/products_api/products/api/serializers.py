from .models import Products,Categories,Sizes, Images
from rest_framework import serializers
from django.core.cache import cache,caches
from rest_framework.response import Response


# def base_create_decorator(self,validate_data):
#     def wrapper(create):
#         .set_queryset(validate_data= validate_data)
#         object = self.Meta.model.objects.create(**validate_data)
#         object.save()
#         return create

#     return wrapper

class DataMixins:

    '''
    This class I use to abstarct and not repeat myself 
    '''


    '''
        get_queryset using in views, and so in many views using same algortims 
        I decided to abstract and extraction this method to DataMixins class
    '''
    @classmethod
    def get_queryset(cls):
        if cache.get(f'{cls.Meta.name}') is not None: 
            return cache.get(f'{cls.Meta.name}')
        else:
            serializer = cls(cls.Meta.model.objects.all(), many = True)
            cache.set(f'{cls.Meta.name}', serializer.data)
            return cache.get(f'{cls.Meta.name}')
        

    
    @classmethod
    def set_queryset(cls, validate_data):
        val_d_copy = validate_data.copy()
        if cls.Meta.name == 'categories':
            val_d_copy.update(relation_to = cls.Meta.model.Relations_Choiches(val_d_copy['relation_to']).name)
            return cache.set(f'{cls.Meta.name}', cls.get_queryset() + [val_d_copy])
        return cache.set(f'{cls.Meta.name}', cls.get_queryset() + [validate_data])
    

    @classmethod
    def base_create(cls, validate_data):
        cls.set_queryset(validate_data=validate_data)
        object = cls.Meta.model.objects.create(**validate_data)
        return object


class ProductsSerializer(serializers.ModelSerializer, DataMixins):

    class Meta:

        name = 'products'
        model = Products
        fields = '__all__'


    def create(self,validate_data):
        product = self.base_create(validate_data)
        return product



class CategoriesSerializer(serializers.ModelSerializer, DataMixins):

    class Meta:
        name = 'categories'
        model = Categories
        fields = '__all__'


    def create(self, validate_data):
        category = self.base_create(validate_data)
        return category