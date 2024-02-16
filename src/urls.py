from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("administrator/", admin.site.urls),
    path("api/v1/", include("api.urls")),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("api-auth/", include("rest_framework.urls")),
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
