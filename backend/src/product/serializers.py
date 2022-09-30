from rest_framework import serializers
from django.contrib.auth.models import User

from. models import Categories, ProductsStocks, Products, OrderItem, Order

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"
        read_only_fields = ('id',)

class ProductsStocksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductsStocks
        fields = "__all__"
        read_only_fields = ('id',)

class ProductsSerializer(serializers.ModelSerializer):
    product_stocks = ProductsStocksSerializer()
    # product_image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ('id','product_stocks')
    
    # def get_product_image(self,product):
    #     request = self.context.get('request')
    #     product_image_url = product.product_image.url
    #     return request.build_absolute_uri(product_image_url)
    
        

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ('id',)

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ('id',)