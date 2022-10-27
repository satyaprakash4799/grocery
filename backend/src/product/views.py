from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.pagination import PageNumberPagination


from product.models import Products
from product.serializers import ProductsSerializer
from user_profile.permissions import IsTokenValid

class ProductsView(APIView, PageNumberPagination):
    """
    List of products
    """
    permission_classes = [IsAuthenticated, IsTokenValid, IsAdminUser]
    allowed_methods = ['GET']

    def get_object(self):
        try:
            return Products.objects.all().order_by('-id')
        except Products.DoesNotExist:
            raise Http404

    def get(self, request):
        products = self.get_object()
        results = self.paginate_queryset(products, request, view=None)
        serializer = ProductsSerializer(results, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)