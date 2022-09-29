from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_name = models.CharField(max_length=255, blank=False, null=False)
    category_description = models.TextField(max_length=255, blank=True, null=True)


class ProductsStocks(models.Model):
    stock_name = models.CharField(max_length=255, blank=True, null=True)
    stock_count = models.IntegerField(default=0)

class Products(models.Model):
    product_stocks = models.OneToOneField(ProductsStocks, related_name="products", on_delete=models.CASCADE)
    product_categories = models.ManyToManyField(Categories, related_name="categories")
    product_name = models.CharField(max_length=255, blank=False, null=True)
    product_price = models.SmallIntegerField(default=0)
    product_discount = models.FloatField(default=0.0)
    product_max_order_quantity = models.IntegerField(default=0)
    product_description = models.TextField(blank=True, max_length=500, null=True)

class OrderItem(models.Model):
    product_id = models.ForeignKey(Products, related_name="product_items", on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=1)
    user_id = models.ForeignKey(User, related_name="user_baskets", on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, null=False, blank=False)

class Order(models.Model):
    user_id = models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    items = models.ManyToManyField(OrderItem, related_name="items")
    quantity = models.IntegerField(default=1)


