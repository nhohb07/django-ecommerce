from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image= models.FileField(blank=False, null=False)
    description =  TextField(max_length=500)
    date_create_at = models.DateTimeField(auto_now_add=True)
    date_update_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image.name

class ProductModel(models.Model):
    date_create_at = models.DateTimeField(auto_now_add=True)
    date_update_at= models.DateTimeField(auto_now_add=True)
    image= models.FileField(blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    content = TextField(max_length=10000)
    description = TextField(max_length=5000)
    name = TextField(max_length=500)
    category = models.ForeignKey(CategoryModel, blank=True, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.image.name


