from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Plant


# Create your views here.


def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


def plant_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def about(request):
    return render(request, "about.html")


def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, "plants/details.html", {"plant": plant})


class PlantCreate(CreateView):
    model = Plant
    fields = "__all__"
    success_url = "/plants/"
