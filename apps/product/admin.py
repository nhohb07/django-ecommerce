from apps.product.models import CategoryModel, ProductModel
from django.contrib import admin
# Register your models here.
admin.site.register(ProductModel)
admin.site.register(CategoryModel)