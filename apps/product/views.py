from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer


@permission_classes((permissions.AllowAny,))
class ProductView(generics.CreateAPIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = ProductSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProductView(generics.ListAPIView):

    category = openapi.Parameter('category', openapi.IN_QUERY, description="product of category", type=openapi.TYPE_BOOLEAN)
    name = openapi.Parameter('name', openapi.IN_QUERY, description="search by name", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="search by description", type=openapi.TYPE_STRING)
    min_price = openapi.Parameter('min_price', openapi.IN_QUERY, description="filter  by min_price", type=openapi.TYPE_INTEGER)
    max_price = openapi.Parameter('max_price', openapi.IN_QUERY, description="filter  by max_price", type=openapi.TYPE_INTEGER)
    order_by = openapi.Parameter('order_by', openapi.IN_QUERY, description="order_by field", type=openapi.TYPE_STRING)
    order = openapi.Parameter('order', openapi.IN_QUERY, description="order (desc or asc)", type=openapi.TYPE_STRING)
    parameters = [category,name,description, min_price, max_price, order_by, order]

    queryset = ProductModel.objects.all()
    # filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProductSerializer
    # search_fields = ['name']
    
    @swagger_auto_schema(operation_description="Get list Product",manual_parameters=parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        request = self.request
        order = "date_create_at"
        kwargs = {
            'name': request.GET.get('name',None),
            'content': request.GET.get('content',None),
            'description': request.GET.get('description',None),
            'order_by': request.GET.get('order_by',None),
            'order': request.GET.get('order', 'desc'),
            'category': request.GET.get('category', None),
            'min_price': request.GET.get('min_price', None),
            'max_price': request.GET.get('max_price', None),
        }
        filter_kwargs = {}
        for key, value in kwargs.items():
            if value and key != "category" and key != "min_price" and key != "max_price" and key != "order_by" and key != "order":
                filter_kwargs[key+"__contains"] = value
            elif key == "category" and value:
                filter_kwargs[key+"__pk"] = value
        if kwargs["min_price"] and kwargs["max_price"]:
                filter_kwargs["price__range"] = (kwargs["min_price"], kwargs["max_price"])
        if kwargs["order_by"] and kwargs["order_by"]:
                order =  kwargs["order_by"]
                if kwargs["order"] == "desc":
                    order = "-"+ order
        query = self.queryset.filter(**filter_kwargs).order_by(order)
        return query

class DetailProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CategoryView(generics.CreateAPIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = CategorySerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListCategoryView(generics.ListAPIView):

    queryset = CategoryModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer

    name = openapi.Parameter('name', openapi.IN_QUERY, description="search by name", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="search by description", type=openapi.TYPE_STRING)
    order_by = openapi.Parameter('order_by', openapi.IN_QUERY, description="order_by field", type=openapi.TYPE_STRING)
    order = openapi.Parameter('order', openapi.IN_QUERY, description="order (desc or asc)", type=openapi.TYPE_STRING)
    parameters = [name,description,  order_by, order]
    @swagger_auto_schema(operation_description="Get list Catetory",manual_parameters=parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        request = self.request
        order = "date_create_at"
        kwargs = {
            'name': request.GET.get('name',None),
            'slug': request.GET.get('slug',None),
            'description': request.GET.get('description',None),
            'order_by': request.GET.get('order_by',None),
            'order': request.GET.get('order', 'desc'),
        }
        filter_kwargs = {}
        for key, value in kwargs.items():
            if value and  key != "order_by" and key != "order":
                filter_kwargs[key+"__contains"] = value

        if kwargs["order_by"] and kwargs["order_by"]:
                order =  kwargs["order_by"]
                if kwargs["order"] == "desc":
                    order = "-"+ order
        query = self.queryset.filter(**filter_kwargs).order_by(order)
        return query

class DetailCategory(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
