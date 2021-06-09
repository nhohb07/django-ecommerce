from django.http.response import JsonResponse
from .models import CategoryModel, ProductModel
from rest_framework import generics, permissions
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.

class ProductView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProductSerializer
class ListProductView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CategoryView(generics.CreateAPIView):
    queryset = CategoryModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer
    
class ListCategoryView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer