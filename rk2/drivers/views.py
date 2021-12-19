from django.db.models.aggregates import Avg
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Autopark, Driver
from django.db import models


def index(request):
    return render(request, 'index.html')

# drivers

def read_driver(request):
    drivers = Driver.objects.all()
    return render(request, 'driver/driver_list.html', {'drivers': drivers})

def create_driver(request):
    if request.method == 'GET':
        autoparks = Autopark.objects.all()
        return render(request, 'driver/create_driver.html', {"autoparks": autoparks})
    else:
        dto = {}
        for key in request.POST:
            if key in Driver.__dict__:
                dto[key] = request.POST[key]
        dto['autopark'] = get_object_or_404(
            Autopark, pk=request.POST['autopark'])
        new_driver = Driver(**dto)
        new_driver.save()
        return redirect('read_driver')

def update_driver(request, driver_id):
    if request.method == 'GET':
        autoparks = Autopark.objects.all()
        driver = get_object_or_404(Driver, pk=driver_id)
        return render(request, 'driver/update_driver.html', {"driver": driver, "autoparks": autoparks})
    else:
        driver = get_object_or_404(Driver, pk=driver_id)
        for key in request.POST:
            if key in driver.__dict__ and key != 'autopark':
                setattr(driver, key, request.POST[key])
        if 'autopark' in request.POST:
            setattr(driver, 'autopark', get_object_or_404(
                Autopark, pk=request.POST['autopark']))
        driver.save()
        return redirect('read_driver')

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    driver.delete()
    return redirect(request.META.get('HTTP_REFERER'))

# autoparks

def read_autopark(request):
    autoparks = Autopark.objects.all()
    return render(request, 'autopark/autopark_list.html', {'autoparks': autoparks})

def create_autopark(request):
    if request.method == 'GET':
        return render(request, 'autopark/create_autopark.html')
    else:
        new_autopark = Autopark(name=request.POST['name'])
        new_autopark.save()
        return redirect('read_autopark')

def update_autopark(request, autopark_id):
    if request.method == 'GET':
        autopark = get_object_or_404(Autopark, pk=autopark_id)
        return render(request, 'autopark/update_autopark.html', {"autopark": autopark})
    else:
        autopark = get_object_or_404(Autopark, pk=autopark_id)
        for key in request.POST:
            if key in autopark.__dict__:
                setattr(autopark, key, request.POST[key])
        autopark.save()
        return redirect('read_autopark')

def delete_autopark(request, autopark_id):
    autopark = get_object_or_404(Autopark, pk=autopark_id)
    autopark.delete()
    return redirect(request.META.get('HTTP_REFERER'))

# REPORT

def report(request):
    # return HttpResponse('♥')
    found_drivers = Driver.objects.filter(name__endswith='ов')
    average_salaries = []
    for autopark in Autopark.objects.all():
        average_salaries.append({"autopark": autopark,  "salary": round(Driver.objects.filter(
            autopark=autopark.pk).aggregate(Avg('salary'))['salary__avg'] or 0)})
    return render(request, 'report.html', {"found_drivers": found_drivers, "average_salaries": sorted(average_salaries, key=lambda salary: salary['salary'])})
