from .views import ProductsViewSet, CategoriesViewSet
from rest_framework import routers
from django.urls import path, include

products_router = routers.DefaultRouter()
categories_router = routers.DefaultRouter()


products_router.register(r'products', ProductsViewSet, basename = 'products')
categories_router.register(r'categories', CategoriesViewSet, basename = 'categories')


urlpatterns = [
    path('api/v1/', include(products_router.urls)),
    path('api/v1/', include(categories_router.urls))
]

