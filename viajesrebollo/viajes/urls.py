from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views.views import index
from .views.activities import manage_activity, activity_details, list_activities, manage_activity2
from .views.packages import manage_package, package_details, list_packages
from .views.trip_plans import manage_trip_plan, trip_plan_details, list_trip_plans


urlpatterns = [
    path("", index, name="index"),

    path("activity/", manage_activity, name="create_activity"),
    path("activity2/", manage_activity2, name="create_activity2"),
    path("activity/<int:activity_id>/edit/",
         manage_activity, name="edit_activity"),
    path("activity/<int:activity_id>/",
         activity_details, name="activity_details"),
    path("activities/", list_activities, name="list_activities"),

    path("package/", manage_package, name="create_package"),
    path("package/<int:package_id>/edit/",
         manage_package, name="edit_package"),
    path("package/<int:package_id>/",
         package_details, name="package_details"),
    path("packages/", list_packages, name="list_packages"),


    path("trip-plan/", manage_trip_plan, name="create_trip_plan"),
    path("trip-plan/<int:trip_plan_id>/edit/",
         manage_trip_plan, name="edit_trip_plan"),
    path("trip-plan/<int:trip_plan_id>/",
         trip_plan_details, name="trip_plan_details"),
    path("trip-plans/", list_trip_plans, name="list_trip_plans"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
