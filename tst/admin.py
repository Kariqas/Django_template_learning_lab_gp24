from django.contrib import admin
from .models import Brand,Car
# Register your models here.

models_list = [
    Car,
    Brand,
]

def models_register(models):
    for i in models:
        admin.site.register(i)

models_register(models_list)    