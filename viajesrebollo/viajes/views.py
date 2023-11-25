from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Página de inicio")

def create_package(request):
    return HttpResponse("Crear paquete de viaje")

def create_activity(request):
    return HttpResponse("Crear nueva actividad")

def create_trip_plan(request):
    return HttpResponse("Crear plan de viaje")

def mod_trip_plan(request):
    return HttpResponse("Modificar plan de viaje")

def mod_activity(request):
    return HttpResponse("Modificar actividad")

def mod_package(request):
    return HttpResponse("Modificar paquete de viaje")