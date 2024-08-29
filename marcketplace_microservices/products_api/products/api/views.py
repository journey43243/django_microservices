from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products
import requests
import json


class ProductsViewSet(viewsets.ModelViewSet):

    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


    def get_to_redis(self):
        if self.request.method != 'GET':
            requests.post('http://192.168.0.106:5001',json.loads(self.queryset))