from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser

from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer


@permission_classes((permissions.IsAuthenticated,))
class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser,)

    category = openapi.Parameter('category', openapi.IN_QUERY, description="product of category", type=openapi.TYPE_INTEGER)
    name = openapi.Parameter('name', openapi.IN_QUERY, description="search by name", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="search by description", type=openapi.TYPE_STRING)
    min_price = openapi.Parameter('min_price', openapi.IN_QUERY, description="filter  by min_price", type=openapi.TYPE_NUMBER)
    max_price = openapi.Parameter('max_price', openapi.IN_QUERY, description="filter  by max_price", type=openapi.TYPE_NUMBER)
    order_by = openapi.Parameter('order_by', openapi.IN_QUERY, description="order_by field", type=openapi.TYPE_STRING)
    order = openapi.Parameter('order', openapi.IN_QUERY, description="order (desc or asc)", type=openapi.TYPE_STRING)
    parameters = [category,name,description, min_price, max_price, order_by, order]

    @swagger_auto_schema(operation_description="Get list Product",manual_parameters=parameters)    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):

        name, content, description, order_by, order, category,min_price, max_price = [self.request.GET.get(i, None) for i in ('name', 'content', 'description', 'order_by', 'order', 'category','min_price', 'max_price')]
        if order is None : order =  "desc"

        filter_kwargs = {}
        order_field = "-date_create_at"
        plus_order = "-" if order == "desc" else ""

        if name:
            filter_kwargs["name__contains"] = name

        if content:
            filter_kwargs["content__contains"] = content

        if description:
            filter_kwargs["description__contains"] = description

        if category:
            filter_kwargs["category__pk"] = category

        if min_price and max_price : 
            filter_kwargs["price__range"] = (min_price,max_price)
            
        if order_by : 
            order_field = plus_order + order_by
       
        return self.queryset.filter(**filter_kwargs).order_by(order_field)

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer
    parser_classes = (MultiPartParser,)

    name = openapi.Parameter('name', openapi.IN_QUERY, description="search by name", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="search by description", type=openapi.TYPE_STRING)
    order_by = openapi.Parameter('order_by', openapi.IN_QUERY, description="order_by field", type=openapi.TYPE_STRING)
    order = openapi.Parameter('order', openapi.IN_QUERY, description="order (desc or asc)", type=openapi.TYPE_STRING)
    parameters = [name,description,  order_by, order]

    @swagger_auto_schema(operation_description="Get list Catetory",manual_parameters=parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
    
        name, description, order_by, order, slug = [self.request.GET.get(i, None) for i in ('name', 'description', 'order_by', 'order', 'slug')]
        if order is None : order =  "desc"

        filter_kwargs = {}
        order_field = "-date_create_at"
        plus_order = "-" if order == "desc" else ""

        if name:
            filter_kwargs["name__contains"] = name

        if description:
            filter_kwargs["description__contains"] = description

        if slug:
            filter_kwargs["slug__pk"] = slug
            
        if order_by : 
            order_field = plus_order + order_by
       
        return self.queryset.filter(**filter_kwargs).order_by(order_field)
    

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
