from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shopify API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hansu@myapi.com"),
        license=openapi.License(name=" @Hansu-all right reserved"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)