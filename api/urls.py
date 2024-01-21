from django.urls import path

from .devices.views import api as device_api

urlpatterns = [
    path("", device_api.urls),
]
