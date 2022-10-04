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
    product_stocks = ProductsStocksSerializer(read_only=True)
    product_categories = CategoriesSerializer(many=True, read_only=True)
    # product_image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ("id", "product_categories", "product_stocks")
    
    # def get_product_image(self,product):
    #     request = self.context.get('request')
    #     product_image_url = product.product_image.url
    #     return request.build_absolute_uri(product_image_url)
    
    def create(self, validated_data):
        request = self.context.get('request')
        data_product_stocks = request.data.get('product_stocks')
        product_name = validated_data.get('product_name')
        data_product_categories = request.data.get('product_categories')
        product_categories = Categories.objects.filter(id__in=data_product_categories).values('id')
        product_stocks = ProductsStocks.objects.get_or_create(id=data_product_stocks, stock_name=product_name)
        product = Products.objects.create(**validated_data, product_stocks=product_stocks[0])
        for category in product_categories:
            product.product_categories.add(category['id'])
        product.save()
        return product
        
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