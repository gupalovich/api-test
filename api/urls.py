from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .filters.views import CarsFilterApiView

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


urlpatterns = router.urls
urlpatterns += [
    path("filter/", CarsFilterApiView.as_view(), name="filter"),
]
