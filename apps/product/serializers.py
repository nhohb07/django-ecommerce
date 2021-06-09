from rest_framework import serializers
from slugify import slugify
from .models import CategoryModel, ProductModel

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id', 'date_create_at', 'date_update_at', 'image', 'price', 'content', 'description', 'name', 'category'
        )
        extra_kwargs = {
            'image': {'required': True},
            'price': {'required': True},
            'content': {'required': True},
            'description': {'required': True},
            'name': {'required': True},
            'category': {'required': True},
        }
        model = ProductModel 

    def create(self, validated_data):
        product = ProductModel.objects.create(
            image=validated_data['image'],
            price=validated_data['price'],
            content=validated_data['content'],
            description=validated_data['description'],
            name=validated_data['name'],
        )

        product.save()

        return product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ( 'name', 'image', 'slug' , 'description')
        extra_kwargs = {
            'image': {'required': True},
            'slug': {'required': True},
            'description': {'required': True},
            'name': {'required': True},
        }
        model = CategoryModel 

    def create(self, validated_data):
        category = CategoryModel.objects.create(
            image=validated_data['image'],
            name=validated_data['name'],
            description=validated_data['description'],
            slug= slugify(validated_data['name'])
        )

        category.save()

        return category