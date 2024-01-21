from django.shortcuts import get_object_or_404

from api.schema import Error, Error404
from src.ninja import api

from .schema import (
    Device,
    DeviceCreateSchema,
    DeviceSchema,
    DeviceUpdateLocationSchema,
    Location,
    LocationSchema,
)


@api.get("locations/", response=list[LocationSchema])
def location_list(request):
    return Location.objects.all()


@api.get("locations/{id}/", response={200: LocationSchema, 409: Error404})
def location_get(request, id):
    try:
        return Location.objects.get(id=id)
    except Location.DoesNotExist:
        return 409, Error404


@api.get("devices/", response=list[DeviceSchema])
def device_list(request):
    return Device.objects.select_related("location")


@api.get("devices/{slug}/", response={200: LocationSchema, 409: Error404})
def device_get(request, slug):
    return get_object_or_404(Device, slug=slug)


@api.post("devices/", response={201: DeviceSchema, 404: Error})
def device_create(request, body: DeviceCreateSchema):
    location_exists = Location.objects.filter(id=body.location_id).exists()
    if not location_exists:
        return 404, {"message": "Location does not exist"}

    return Device.objects.create(**body.model_dump())


@api.patch("devices/{slug}/set-location/", response=DeviceSchema)
def device_location_update(request, slug, body: DeviceUpdateLocationSchema):
    device = get_object_or_404(Device, slug=slug)

    if body.location_id:
        location = get_object_or_404(Location, id=body.location_id)
        device.location = location
    else:
        device.location = None

    device.save()
    return device
