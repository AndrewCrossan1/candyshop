from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer


# Shop Views
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
