from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, CategorySerializer


class LatestProductList(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, format=None):
        products = Product.objects.all()[0:5]
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
