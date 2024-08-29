from .models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'

    
    # def create(self, validated_data):
    #     product = Products.objects.create(**validated_data)
    #     product.save()
    #     return product
    
    # def update(self,instintance)
            
