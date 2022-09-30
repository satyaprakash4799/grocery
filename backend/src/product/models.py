from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_name = models.CharField(max_length=255, blank=False, null=False)
    category_description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class ProductsStocks(models.Model):
    stock_name = models.CharField(max_length=255, blank=True, null=True)
    stock_count = models.IntegerField(default=0)

    def __str__(self):
        return self.stock_name
    class Meta:
        verbose_name = "Product Stock"
        verbose_name_plural = "Product Stocks"

class Products(models.Model):
    product_image = models.ImageField(upload_to="products", blank=True)
    product_stocks = models.OneToOneField(ProductsStocks, related_name="products", on_delete=models.CASCADE)
    product_categories = models.ManyToManyField(Categories, related_name="categories")
    product_name = models.CharField(max_length=255, blank=False, null=True)
    product_price = models.SmallIntegerField(default=0)
    product_discount = models.FloatField(default=0.0)
    product_max_order_quantity = models.IntegerField(default=0)
    product_description = models.TextField(blank=True, max_length=500, null=True)

    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class OrderItem(models.Model):
    product_id = models.ForeignKey(Products, related_name="product_items", on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=1)
    user_id = models.ForeignKey(User, related_name="user_baskets", on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

class Order(models.Model):
    user_id = models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    items = models.ManyToManyField(OrderItem, related_name="items")
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


