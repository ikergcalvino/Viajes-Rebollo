from django.shortcuts import render, redirect, get_object_or_404
from ..models import Package
from ..forms import NewPackage, ModPackage


def manage_package(request, package_id=None):
    if package_id:
        package = get_object_or_404(Package, pk=package_id)
        form = ModPackage(request.POST or None, instance=package)
    else:
        form = NewPackage(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    template = 'packages/edit.html' if package_id else 'packages/create.html'
    return render(request, template, {'form': form, 'package_id': package_id})


def package_details(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    activities = package.activities.all()
    return render(request, 'packages/details.html', {'package': package, 'activities': activities})


def list_packages(request):
    packages = Package.objects.all()
    return render(request, 'packages/list.html', {'packages': packages})
