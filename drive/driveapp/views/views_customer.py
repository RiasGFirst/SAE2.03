from django.shortcuts import render, HttpResponseRedirect
from ..forms import CustomerForm
from .. import models

# Create your views here.


def home(request):
    customer = models.Customer.objects.all()
    return render(request, 'driveapp/customer/home.html', {'customers': customer})


def add(request):
    form = CustomerForm()
    return render(request, 'driveapp/customer/add.html', {'form': form})


def processing(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'driveapp/customer/success.html', {'customer': form.cleaned_data})
    else:
        return render(request, 'driveapp/customer/error.html')


def update(request, id):
    customer = models.Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)
    return render(request, 'driveapp/customer/update.html', {'form': form, 'customer': customer})


def processing_update(request, id):
    lform = CustomerForm(request.POST)
    if lform.is_valid():
        customer = lform.save(commit=False)
        customer.id = id
        customer.save()
        return HttpResponseRedirect("/customer/")
    else:
        return render(request, "driveapp/customer/update.html", {"form": lform, "id": id})


def show(request, id):
    customer = models.Customer.objects.get(id=id)
    return render(request, 'driveapp/customer/show.html', {'customer': customer})


def delete(request, id):
    customer = models.Customer.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect("/customer/")