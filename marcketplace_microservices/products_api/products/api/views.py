from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductsSerializer
#from django.core.cache import cache
from .models import Products
#import requests
import json
from django.core.cache import cache
import ast


class ProductsViewSet(viewsets.ModelViewSet):

    serializer_class = ProductsSerializer
    #queryset = cache.get('*')

    def list(self,request):
        queryset = cache.get('products')
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Products.objects.all()
        #for key,value in  request.body.decode('utf-8').replace(' ', '').replace('\r\n', '')
        response = request.body.decode('utf')
        parse_response = ast.literal_eval(response)
        print(type(parse_response))
        return Response()



    # def get_to_redis(self):
    #     if self.request.method != 'GET':
    #         requests.post('http://192.168.0.106:5001',json.loads(self.queryset))