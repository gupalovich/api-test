from api.schema import Error404
from src.ninja import api

from .schema import Device, DeviceSchema, Location, LocationSchema


@api.get("locations/", response=list[LocationSchema])
def location_list(request):
    return Location.objects.all()


@api.get("locations/{id}/", response={200: LocationSchema, 404: Error404})
def location_get(request, id):
    try:
        return Location.objects.get(id=id)
    except Location.DoesNotExist:
        return 404, 404


@api.get("devices/", response=list[DeviceSchema])
def device_list(request):
    return Device.objects.select_related("location")


@api.get("devices/{slug}/", response={200: DeviceSchema, 404: Error404})
def device_get(request, slug):
    try:
        return Device.objects.get(slug=slug)
    except Device.DoesNotExist:
        return 404, {"message": "Device not found"}
