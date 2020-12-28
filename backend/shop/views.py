from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def product_list(request, category_slug=None, format=None):
    if request.method == 'GET' or 'get':
        category = None
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        products = Product.objects.filter(available=True)
        product_serializer = ProductSerializer(products, many=True)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            #category_serializer = CategorySerializer(category, many=True)
            products = products.filter(category=category)
            product_serializer = ProductSerializer(products, many=True)
        return Response({'products': product_serializer.data,
                         'categories': category_serializer.data,
                         }, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def product_detail(request, pk):
    product = Category.objects.filter(pk=pk, available=True)
    product_serializer = ProductSerializer(product, many=True)
    return Response(product_serializer.data, status=status.HTTP_200_OK)