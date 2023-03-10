from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Category
        fields = ('CategoryID', 'Name', 'Description', 'Tags', 'product_count', 'average_rating', 'get_url')
        read_only_fields = ('product_count', 'average_rating', 'get_url')


class ProductSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()
    
    class Meta:
        model = Product
        fields = ('ProductID', 'Name', 'Description', 'Category', 'Price', 'Brand', 'Image', 'Tags', 'Prop_Rating', 'Highest_Rated', 'category_name')
        read_only_fields = ['Prop_Rating', 'Available', 'Highest_Rated']


class BrandSerializer(serializers.ModelSerializer, TaggitSerializer):

    Tags = TagListSerializerField()

    class Meta:
        model = Brand
        fields = '__all__'
