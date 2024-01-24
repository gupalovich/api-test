from uuid import uuid4

from django.db import models


class Domain(models.Model):
    class Meta:
        verbose_name = "Домен"
        verbose_name_plural = "Домены"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, verbose_name="Бренд", related_name="models", null=True
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, verbose_name="Домен", related_name="cars")
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name="Бренд", related_name="cars")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Модель", related_name="cars")

    vin = models.CharField(max_length=200, default=uuid4(), verbose_name="VIN")
    color = models.CharField(max_length=200, verbose_name="Цвет")
    transmission = models.CharField(max_length=200, verbose_name="Трансмиссия")

    def __str__(self):
        return f"{self.brand.name} - {self.model.name} - {self.color}"
