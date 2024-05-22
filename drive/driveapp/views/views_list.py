from django.shortcuts import render, HttpResponseRedirect
from ..forms import ListForm
from .. import models

# Create your views here.


def add(request, id):
    form = ListForm()
    return render(request, 'driveapp/list/add.html', {'form': form, 'id_order': id})


def processing(request, id):
    order = models.Order.objects.get(pk=id)
    lform = ListForm(request.POST)
    if lform.is_valid():
        liste = lform.save(commit=False)
        liste.order = order
        liste.order_id = id
        lform.save()
        return HttpResponseRedirect("/order/")
    else:
        return render(request,"driveapp/list/add.html",{"form": lform})


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
    return HttpResponseRedirect("/list/{{list.order.id}}")


