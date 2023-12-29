from django.shortcuts import render, redirect, get_object_or_404
from ..models import Activity
from ..forms import NewActivity, ModActivity


def manage_activity(request, activity_id=None):
    if activity_id:
        activity = get_object_or_404(Activity, pk=activity_id)
        form = ModActivity(request.POST or None, instance=activity)
    else:
        form = NewActivity(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    template = 'activities/edit.html' if activity_id else 'activities/create.html'
    return render(request, template, {'form': form, 'activity_id': activity_id})

def manage_activity2(request, activity_id=None):
    if activity_id:
        activity = get_object_or_404(Activity, pk=activity_id)
        form = ModActivity(request.POST or None, instance=activity)
    else:
        form = NewActivity(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create_package')

    template = 'activities/edit.html' if activity_id else 'activities/create.html'
    return render(request, template, {'form': form, 'activity_id': activity_id})


def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'activities/details.html', {'activity': activity})


def list_activities(request):
    activities = Activity.objects.all()
    return render(request, 'activities/list.html', {'activities': activities})
