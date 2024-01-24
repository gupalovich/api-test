from django.contrib import admin

from .models import Car, CarBrand, CarModel, Domain


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(CarModel)
class CarModel(admin.ModelAdmin):
    list_display = ["id", "name", "brand"]
    list_select_related = ["brand"]


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ["id", "brand", "model", "color", "domain"]
    list_select_related = ["domain", "brand", "model"]
