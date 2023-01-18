from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product, Category, Brand
from .permissions import ProductPermission, CategoryPermission, BrandPermission
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer


# Shop Views
class ProductViewSet(ModelViewSet):
    permission_classes = [ProductPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def get_products_by_category(self, request):
        category_name = request.GET.get('category_name')
        if category_name is None or category_name == '' or category_name.isdigit():
            return Response({'error': 'category_name is required'}, status=400)
        category_name = category_name.replace('-and-', ' & ').replace('-', ' ')
        print(category_name)
        if not Category.objects.filter(Name__iexact=category_name).exists():
            return Response({'error': 'category not found'}, status=404)

        products = Product.objects.filter(Category__Name__iexact=category_name)
        serializer = ProductSerializer(products, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({'message': 'No products found'})

    @action(detail=False, methods=['get'])
    def get_products_by_brand(self, request):
        brand_name = request.GET.get('brand_name')
        if brand_name is None or brand_name == '' or brand_name.isdigit():
            return Response({'error': 'brand_name is required'}, status=400)
        brand_name = brand_name.replace('-and-', ' & ').replace('-', ' ')
        print(brand_name)
        if not Brand.objects.filter(Name__iexact=brand_name).exists():
            return Response({'error': 'category not found'}, status=404)
        products = Product.objects.filter(Brand__Name__iexact=brand_name)
        serializer = ProductSerializer(products, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({'message': 'No products found'})

    @action(detail=False, methods=['get'])
    def get_new_products(self, request):
        products = Product.objects.all()[3:]
        serializer = ProductSerializer(products, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({'message': 'No products found'})


class CategoryViewSet(ModelViewSet):
    permission_classes = [CategoryPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action (detail=False, methods=['get'])
    def by_name(self, request):
        name = request.GET.get('category_name')
        if name is None or name == '':
            return Response({'error': 'category_name is required'}, status=400)
        # Undo the get_url function
        name = name.replace('-and-', ' & ').replace('-', ' ')
        category = Category.objects.filter(Name__iexact=name)
        serializer = CategorySerializer(category, many=True)
        if serializer.data:
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'No categories found'}, status=404)


class BrandViewSet(ModelViewSet):
    permission_classes = [BrandPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @action(detail=False, methods=['get'])
    def by_name(self, request):
        name = request.GET.get('brand_name')
        if name is None or name == '':
            return Response({'error': 'brand_name is required'}, status=400)
        # Undo the get_url function
        name = name.replace('-and-', ' & ').replace('-', ' ')
        brand = Brand.objects.filter(Name__iexact=name)
        serializer = BrandSerializer(brand, many=True)
        if serializer.data:
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'No brands found'}, status=404)