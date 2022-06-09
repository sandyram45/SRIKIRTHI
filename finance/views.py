from django.shortcuts import render
from .models import DailyExpenses, VehicleExpenses, SalaryExpenses
from .forms import OfficeForm, VehicleForm, SalaryForm
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def Addoffice(request):
    form = OfficeForm()
    office = DailyExpenses.objects.all()

    p = Paginator(office, 5)
    page = request.GET.get('page')
    offices = p.get_page(page)

    if request.method == 'POST':
        form = OfficeForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-office')

        else:
            form = OfficeForm()

    context = {'form': form, 'offices': offices}

    return render(request, template_name='addoffice.html', context=context)


@login_required(login_url='login')
def Addvehicle(request):
    form = VehicleForm()
    vehicle = VehicleExpenses.objects.all()

    p = Paginator(vehicle, 5)
    page = request.GET.get('page')
    vehicles = p.get_page(page)

    if request.method == 'POST':
        form = VehicleForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-vehicle')

        else:
            form = VehicleForm()

    context = {'form': form, 'vehicles': vehicles}

    return render(request, template_name='addvehicle.html', context=context)


@login_required(login_url='login')
def Addsalary(request):
    form = SalaryForm()
    salary = SalaryExpenses.objects.all()

    p = Paginator(salary, 9)
    page = request.GET.get('page')
    salaries = p.get_page(page)

    if request.method == 'POST':
        form = SalaryForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-salary')

        else:
            form = SalaryForm()

    context = {'form': form, 'salaries': salaries}

    return render(request, template_name='addsalary.html', context=context)







