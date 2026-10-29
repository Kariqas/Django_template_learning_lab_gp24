from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="cars",
    )
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    year = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.model