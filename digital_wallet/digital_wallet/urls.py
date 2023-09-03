from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title=" API",
        default_version='v1',
        description="apis",
        terms_of_service="",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('digital_wallet/', include('app_wallet.urls'))
    # re_path("", include('app_user.urls')),

    path('api/', include("app_user.urls")),

    path(
        'swagger<format>.json|.yaml',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
