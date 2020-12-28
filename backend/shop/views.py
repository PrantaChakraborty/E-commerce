from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Product
# from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def product_list(request, category_slug=None, format=None):
    if request.method == 'GET' or 'get':
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return Response({
            'category': category,
            'categories': categories,
            'products': products,
            }, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
