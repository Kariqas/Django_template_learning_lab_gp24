from django.shortcuts import render
from .models import Car
# Create your views here.

def test(request):
    cars = Car.objects.all().order_by("-price","-id")

    context = {
        "cars":cars,
        }

    return render(request, "tst/test.html", context)