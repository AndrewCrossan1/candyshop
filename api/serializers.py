from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()
    Category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ('ProductID', 'Name', 'Description', 'Category', 'Price', 'Brand', 'Image', 'Tags', 'Prop_Rating', 'Highest_Rated')
        read_only_fields = ['Prop_Rating', 'Available', 'Highest_Rated']


class BrandSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Brand
        fields = '__all__'
