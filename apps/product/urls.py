from django.urls import path
from .views import CategoryView, DetailCategory, DetailProduct, ListCategoryView, ListProductView, ProductView


urlpatterns = [
    path("add", ProductView.as_view(), name="add_product"),
    path("list", ListProductView.as_view(), name="list_product"),
    path('<int:pk>', DetailProduct.as_view(), name='single_product'),

]
