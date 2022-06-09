from pprint import pprint

from django.http import HttpResponse

from .tasks import test_func
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LocationForm, ShopForm, SalesForm, SalesInitialForm, CollectionForm
from .models import Location, ShopDetails, Sales, Rate, Collections
from django.contrib import messages
from django.core.paginator import Paginator


@login_required(login_url='login')
def Addlocation(request):
    form = LocationForm()
    location = Location.objects.all()

    p = Paginator(location, 5)
    page = request.GET.get('page')
    locations = p.get_page(page)

    if request.method == 'POST':
        form = LocationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-location')

        else:
            form = LocationForm()

    context = {'form': form, 'locations': locations}

    return render(request, template_name='addlocation.html', context=context)


@login_required(login_url='login')
def Editlocation(request, pk):

    location = Location.objects.get(id=pk)
    form = LocationForm(instance=location)

    if request.method == 'POST':
        form = LocationForm(data=request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('add-location')

        # else:
         # form = LocationForm(instance=id)

    context = {'form': form}

    return render(request, template_name='editlocation.html', context=context)


@login_required(login_url='login')
def Deletelocation(request, pk):
    location = Location.objects.get(id=pk)

    if request.method == 'GET':
        form = LocationForm(instance=location)

    if request.method == 'POST':
        location.delete()
        return redirect('add-location')

    context = {'item': location, 'form': form}
    return render(request, template_name='deletelocation.html', context=context)


@login_required(login_url='login')
def Addshop(request):
    form = ShopForm()
    shop = ShopDetails.objects.all()

    p = Paginator(shop, 5)
    page = request.GET.get('page')
    shops = p.get_page(page)

    if request.method == 'POST':
        form = ShopForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-shop')

        else:
            form = ShopForm()

    context = {'form': form, 'shops': shops}

    return render(request, template_name='addshop.html', context=context)


@login_required(login_url='login')
def Editshop(request, pk):

    shop = ShopDetails.objects.get(id=pk)
    form = ShopForm(instance=shop)

    if request.method == 'POST':
        form = ShopForm(data=request.POST, instance=shop)

        if form.is_valid():
            form.save()
            return redirect('add-shop')

    context = {'form': form}
    return render(request, template_name='editshop.html', context=context)


@login_required(login_url='login')
def Deleteshop(request, pk):
    shop = ShopDetails.objects.get(id=pk)

    if request.method == 'GET':
        form = ShopForm(instance=shop)

    if request.method == 'POST':
        shop.delete()
        return redirect('add-shop')

    context = {'item': shop, 'form': form}
    return render(request, template_name='deleteshop.html', context=context)


@login_required(login_url='login')
def Addsales(request):
    sale = Sales.objects.all()
    p = Paginator(sale, 5)
    page = request.GET.get('page')
    sales = p.get_page(page)

    if request.method == 'POST':
        form = SalesInitialForm(data=request.POST)

        if form.is_valid():
            form.save()
            half_form = Sales.objects.last().id

            filter_sales = Sales.objects.get(id=half_form)
            amount_check = Rate.objects.filter(shop=filter_sales.shop_name).exists()

            if amount_check == True:
                amount = Rate.objects.get(shop=filter_sales.shop_name)
                final_amount = filter_sales.no_of_cylinders * amount.rate
                filter_sales.amount = final_amount
                filter_sales.save()

                return redirect(reverse('finish-sales', kwargs={'pk': half_form}))
            else:
                filter_sales.delete()
                messages.error(request, "Ask the admin to provide the rate")
        else:
            messages.info(request, "Fill in proper details")

    else:
        form = SalesInitialForm()

    context = {'sales': sales, 'form': form}
    return render(request, template_name='addsales.html', context=context)


@login_required(login_url='login')
def Finishsales(request, pk):

    final_sales = Sales.objects.get(id=pk)

    if request.method == 'GET':

        form = SalesForm(instance=final_sales)

    if request.method == 'POST':
        final_form = SalesForm(data=request.POST, instance=final_sales)

        if final_form.is_valid():
            final_form.save()
            return redirect('add-sales')

    context = {'form': form}
    return render(request, template_name='finishaddsales.html', context=context)


@login_required(login_url='login')
def Editsales(request, pk):
    sale = Sales.objects.get(id=pk)

    if request.method == 'POST':
        form = SalesForm(data=request.POST, instance=sale)

        if form.is_valid():
            form.save()
            return redirect('add-sales')
    else:
        form = SalesForm(instance=sale)

    context = {'item': sale,'form': form}
    return render(request, template_name='editsales.html', context=context)


@login_required(login_url='login')
def Deletesales(request, pk):
    sale = Sales.objects.get(id=pk)
    form = SalesForm()

    if request.method == 'GET':
        form = SalesForm(instance=sale)

    if request.method == 'POST':
        sale.delete()
        return redirect('add-sales')

    context = {'form': form}
    return render(request, template_name='deletesales.html', context=context)


@login_required(login_url='login')
def Outstandingbalances(request):

    final_count = ShopDetails.objects.all()

    p = Paginator(final_count, 5)
    page = request.GET.get('page')
    balances = p.get_page(page)

    context = {'balances': balances}
    return render(request, template_name='outstandingbalances.html', context=context)


@login_required(login_url='login')
def Collection(request):
    collection = Collections.objects.all()
    form = CollectionForm()
    p = Paginator(collection, 5)
    page = request.GET.get('page')
    collections = p.get_page(page)

    if request.method == "POST":
        form = CollectionForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('collections')
        else:
            messages.info("Fill in proper details")
    else:
        form = CollectionForm()

    context = {'collections': collections, 'form': form}
    return render(request, template_name='collections.html', context=context)


@login_required(login_url='login')
def fun(request):
    # form = FunForm()
    #test_func.delay()
    # context = {'form': form}

    # return render(request, template_name='fun.html')
    return HttpResponse("Done")
