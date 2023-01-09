from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Product, Category, Brand


class ProductSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = ('ProductID', 'Name', 'Description', 'Price', 'Category', 'Brand', 'Image', 'Tags')


class CategorySerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Brand
        fields = '__all__'
