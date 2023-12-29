from django.shortcuts import render, redirect, get_object_or_404
from ..models import TripPlan
from ..forms import NewTripPlan, ModTripPlan


def manage_trip_plan(request, trip_plan_id=None):
    if trip_plan_id:
        trip_plan = get_object_or_404(TripPlan, pk=trip_plan_id)
        form = ModTripPlan(request.POST or None, instance=trip_plan)
    else:
        form = NewTripPlan(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    template = 'trip_plans/edit.html' if trip_plan_id else 'trip_plans/create.html'
    return render(request, template, {'form': form, 'trip_plan_id': trip_plan_id})


def trip_plan_details(request, trip_plan_id):
    trip_plan = get_object_or_404(TripPlan, pk=trip_plan_id)
    activities = trip_plan.customized_activities.all()
    package = trip_plan.package
    return render(request, 'trip_plans/details.html', {'trip_plan': trip_plan, 'activities': activities, 'package': package})


def list_trip_plans(request):
    trip_plans = TripPlan.objects.all()
    return render(request, 'trip_plans/list.html', {'trip_plans': trip_plans})
