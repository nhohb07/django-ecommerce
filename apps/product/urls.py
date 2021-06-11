from django.urls import path
from .views import CategoryView, DetailCategory, DetailProduct, ProductView


urlpatterns = [
    path("products", ProductView.as_view(), name="list_product"),
    path('products/<int:pk>', DetailProduct.as_view(), name='single_product'),

    path("categories", CategoryView.as_view(), name="add_category"),
    path('categories/<int:pk>', DetailCategory.as_view(), name='single_category'),

]
