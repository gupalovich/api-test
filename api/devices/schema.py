from ninja import ModelSchema, Schema

from devices.models import Device, Location


class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ["id", "name"]


class DeviceSchema(ModelSchema):
    class Meta:
        model = Device
        fields = ["id", "name", "slug", "location"]

    location: LocationSchema | None = None


class DeviceCreateSchema(Schema):
    name: str
    location_id: int


class DeviceUpdateLocationSchema(Schema):
    location_id: int | None = None
