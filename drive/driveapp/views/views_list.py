from django.shortcuts import render, HttpResponseRedirect
from ..forms import ListForm
from .. import models

# Create your views here.


def add(request):
    form = ListForm()
    return render(request, 'driveapp/list/add.html', {'form': form})


def processing(request):
    form = ListForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'driveapp/list/success.html', {'list': form.cleaned_data})
    else:
        return render(request, 'driveapp/list/error.html')


def update(request, id):
    list = models.List.objects.get(id=id)
    form = ListForm(instance=list)
    return render(request, 'driveapp/list/update.html', {'form': form, 'list': list})


def processing_update(request, id):
    lform = ListForm(request.POST)
    if lform.is_valid():
        list = lform.save(commit=False)
        list.id = id
        list.save()
        return HttpResponseRedirect("/list/")
    else:
        return render(request, "driveapp/list/update.html", {"form": lform, "id": id})


def show(request, id):
    list = models.List.objects.get(id=id)
    return render(request, 'driveapp/list/show.html', {'list': list})


def delete(request, id):
    list = models.List.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect("/list/")