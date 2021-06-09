from django.urls import path
from .views import CategoryView, DetailCategory, ListCategoryView


urlpatterns = [
    path("add", CategoryView.as_view(), name="add_category"),
    path("list", ListCategoryView.as_view(), name="list_category"),
    path('<int:pk>', DetailCategory.as_view(), name='single_category'),
]
