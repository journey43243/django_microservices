from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .serializers import DataMixins, ProductsSerializer,CategoriesSerializer
from .models import Products



class ProductsViewSet(viewsets.ModelViewSet,DataMixins):

    serializer_class = ProductsSerializer


    def get_queryset(request):

        return ProductsSerializer.get_queryset()


class CategoriesViewSet(viewsets.ModelViewSet):
    
    serializer_class = CategoriesSerializer

    def get_queryset(request):

        return CategoriesSerializer.get_queryset()