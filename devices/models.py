import uuid

from django.db import models
from django_extensions.db.fields import AutoSlugField


class Location(models.Model):
    class Meta:
        verbose_name_plural = "Locations"
        verbose_name = "Location"

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Device(models.Model):
    class Meta:
        verbose_name_plural = "Devices"
        verbose_name = "Device"

    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="devices"
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name")

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"
