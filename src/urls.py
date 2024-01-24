from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("administrator/", admin.site.urls),
    path("api/", include("api.urls")),
]
