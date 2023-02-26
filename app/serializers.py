# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(max_length=None, allow_empty_file=True, required=False)

#     class Meta:
#         model = Product
#         fields = '__all__'

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'price', 'created_at', 'updated_at')
