from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_package", views.create_package, name="createpackage"),
    path("create_activity", views.create_activity, name="createactivity"),
    path("create_trip_plan", views.create_trip_plan, name="createtripplan"),
    path("mod_trip_plan", views.mod_trip_plan, name="modtripplan"),
    path("mod_activity", views.mod_activity, name="modactivity"),
    path("mod_package", views.mod_package, name="modpackage"),
]