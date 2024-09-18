from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.core.cache import cache
from .serializers import DataMixins, ProductsSerializer,CategoriesSerializer
from .models import Products
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS,IsAuthenticatedOrReadOnly, IsAdminUser


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

@permission_classes([IsAuthenticated|ReadOnly])
class ProductsViewSet(viewsets.ModelViewSet,DataMixins):

    serializer_class = ProductsSerializer


    def get_queryset(request):

        return ProductsSerializer.get_queryset()

@permission_classes([IsAdminUser])
class CategoriesViewSet(viewsets.ModelViewSet, DataMixins):
    
    serializer_class = CategoriesSerializer

    def get_queryset(request):

        return CategoriesSerializer.get_queryset()
    

