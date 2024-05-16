from django.shortcuts import render, HttpResponseRedirect
from ..forms import ProductForm
from .. import models

# Create your views here.


def home(request):
    return render(request, 'driveapp/home.html')


def add(request):
    form = ProductForm()
    return render(request, 'driveapp/product/add.html', {'form': form})


def processing(request):
    lform = ProductForm(request.POST)
    if lform.is_valid():
        lform.save()
        return render(request, 'driveapp/product/success.html', {'product': lform.cleaned_data})
    else:
        return render(request, 'driveapp/product/error.html')


def update(request, id):
    product = models.Product.objects.get(id=id)
    form = ProductForm(instance=product)
    return render(request, 'driveapp/product/update.html', {'form': form, 'product': product})


def processing_update(request, id):
    lform = ProductForm(request.POST)
    if lform.is_valid():
        product = lform.save(commit=False)
        product.id = id
        product.save()
        return HttpResponseRedirect("/product/")
    else:
        return render(request, "driveapp/product/update.html", {"form": lform, "id": id})


def show(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, 'driveapp/product/show.html', {'product': product})


def delete(request, id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect("/product/")