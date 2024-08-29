from .views import ProductsViewSet
from rest_framework import routers
from django.urls import path, include

products_router = routers.DefaultRouter()
products_router.register(r'products', ProductsViewSet)
urlpatterns = [
    path('api/v1/', include(products_router.urls))
]


print(products_router.urls)