from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as schema_view_api
from django.conf.urls.static import static


schema_view = schema_view_api(
    openapi.Info(
        title="Contact List API",
        default_version='v1',
        description="An api for contacts",
        terms_of_service="https://devblock.net/",
        contact=openapi.Contact(email="trieudc@devblock.net"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include("apps.product.urls")),
    path("category/", include("apps.product.urls_cat")),
    path("auth/", include("apps.authentication.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('rest_framework.urls')),
    
]

urlpatterns += [
    path(
        "openapi/",
        get_schema_view(
            title="School Service",
            description="API developers hpoing to use our service",
        ),
        name="openapi-schema",
    ),
    path('swagger-ui/', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)