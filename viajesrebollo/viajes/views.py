from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Activity, Package, TripPlan  
from .forms import NewActivity, ModActivity, NewPackage, ModPackage, NewTripPlan, ModTripPlan
from django import forms

# Create your views here.

def index(request):
    return render(request, "viajes/index.html", context=None)



def create_package(request):
    if request.method == 'POST':
        form = NewPackage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
        else:
            
            return render(request, 'create-package.html', {'form': form})
    else:
        form = NewPackage()

    return render(request, 'create-package.html', {'form': form})




def create_activity(request):
    if request.method == 'POST':
        form = NewActivity(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = NewActivity()

    return render(request, 'create-activity.html', {'form': form})

def create_trip_plan(request):
    if request.method == 'POST':
        form = NewTripPlan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = NewTripPlan()

    return render(request, 'create-trip-plan.html', {'form': form})


def mod_trip_plan(request, trip_plan_id):
    trip_plan = get_object_or_404(TripPlan, pk=trip_plan_id)
    if request.method == 'POST':
        form = ModTripPlan(request.POST, instance=trip_plan)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ModTripPlan(instance=trip_plan)

    return render(request, 'mod-trip-plan.html', {'form': form})





def mod_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'POST':
        form = ModActivity(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('listactivities')
    else:
        form = ModActivity(instance=activity)

    return render(request, 'mod-activity.html', {'form': form})


def mod_package(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = ModPackage(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('index')  
        
    else:
        form = ModPackage(instance=package)

    return render(request, 'mod-package.html', {'form': form})




def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'detail-activity.html', {'activity': activity})

def package_detail(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    activities = package.activities.all()  
    return render(request, 'detail-package.html', {'package': package, 'activities': activities})

def trip_plan_detail(request, trip_plan_id):
    trip_plan = get_object_or_404(TripPlan, pk=trip_plan_id)
    activities = trip_plan.customized_activities.all()
    package = trip_plan.package
    return render(request, 'detail-trip-plan.html', {
        'trip_plan': trip_plan,
        'activities': activities,
        'package': package
    })


def list_trip_plans(request):
    trip_plans = TripPlan.objects.all()  
    return render(request, 'list-trip-plans.html', {'trip_plans': trip_plans})


