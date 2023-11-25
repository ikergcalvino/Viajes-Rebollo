from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_package", views.create_package, name="createpackage"),
    path("create_activity", views.create_activity, name="createactivity"),
    path("create_trip_plan", views.create_trip_plan, name="createtripplan"),
]