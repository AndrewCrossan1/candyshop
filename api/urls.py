from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CategoryViewSet, ProductViewSet

app_name = 'apiv1'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'brands', BrandViewSet, basename='brands')

urlpatterns = [
    path('', include(router.urls)),
]
