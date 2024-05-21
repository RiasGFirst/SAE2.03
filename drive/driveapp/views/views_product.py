from django.shortcuts import render, HttpResponseRedirect
from PIL import Image
from ..forms import ProductForm
from .. import models

# Create your views here.


def home(request):
    product = models.Product.objects.all()
    return render(request, 'driveapp/product/home.html', {'products': product})


def add(request):
    form = ProductForm()
    return render(request, 'driveapp/product/add.html', {'form': form})


def processing(request):
    lform = ProductForm(request.POST, request.FILES)
    if lform.is_valid():
        product = lform.save()
        image = lform.cleaned_data.get('image')
        if image:
            img = Image.open(image)  # de la biblio de PIL
            img.thumbnail((300, 300))
            img.save(product.image.path)
        return render(request, 'driveapp/product/success.html', {'product': lform.cleaned_data})
    else:
        HttpResponseRedirect("/product/")


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