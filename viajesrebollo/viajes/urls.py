from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_package", views.create_package, name="createpackage"),
    path("create_activity", views.create_activity, name="createactivity"),
    path("create_trip_plan", views.create_trip_plan, name="createtripplan"),
    path('mod_trip_plan/<int:trip_plan_id>/', views.mod_trip_plan, name='modtripplan'),
    path("mod_activity/<int:activity_id>", views.mod_activity, name="modactivity"),
    path('mod_package/<int:package_id>/', views.mod_package, name='mod_package'),

    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path("list_trip_plans", views.list_trip_plans, name="listtripplans"),
    path('trip_plan/<int:trip_plan_id>/', views.trip_plan_detail, name='tripplan_detail'),




]