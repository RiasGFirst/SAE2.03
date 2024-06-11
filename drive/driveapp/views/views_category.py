from django.shortcuts import render, HttpResponseRedirect
from ..forms import CategoryForm
from .. import models

# Create your views here.


def home(request):
    category = models.Category.objects.all()
    return render(request, 'driveapp/category/home.html', {'categories': category})


def add(request):
    form = CategoryForm()
    return render(request, 'driveapp/category/add.html', {'form': form})


def processing(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'driveapp/category/success.html', {'category': form.cleaned_data})
    else:
        return render(request, 'driveapp/category/error.html')


def update(request, id):
    category = models.Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    return render(request, 'driveapp/category/update.html', {'form': form, 'category': category})


def processing_update(request, id):
    lform = CategoryForm(request.POST)
    if lform.is_valid():
        category = lform.save(commit=False)
        category.id = id
        category.save()
        return HttpResponseRedirect("/category/")
    else:
        return render(request, "driveapp/category/update.html", {"form": lform, "id": id})


def show(request, id):
    category = models.Category.objects.get(id=id)
    return render(request, 'driveapp/category/show.html', {'category': category})


def delete(request, id):
    category = models.Category.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect("/category/")