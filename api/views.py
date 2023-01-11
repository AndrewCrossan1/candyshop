from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Product, Category, Brand
from .permissions import ProductPermission, CategoryPermission, BrandPermission
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer


# Shop Views
class ProductViewSet(ModelViewSet):
    permission_classes = [ProductPermission]
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [CategoryPermission]
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(ModelViewSet):
    permission_classes = [BrandPermission]
    authentication_classes = []
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
