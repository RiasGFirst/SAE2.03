from django.shortcuts import render, HttpResponseRedirect
from django.forms import inlineformset_factory
from ..forms import ListForm
from .. import models

def add(request, id):
    form = ListForm()
    return render(request, 'driveapp/list/add.html', {'form': form, 'order_id': id})


def processing(request, id):
    order = models.Order.objects.get(pk=id)
    form = ListForm(request.POST)
    if form.is_valid():
        list = form.save(commit=False)
        list.order_id = id
        list.save()
        return HttpResponseRedirect("/order/show/" + str(id))
    else:
        return render(request, 'driveapp/list/error.html')


def update(request, id, order_id):
    list = models.List.objects.get(id=id)
    form = ListForm(instance=list)
    return render(request, 'driveapp/list/update.html', {'form': form, 'list': list, 'order_id': order_id})


def processing_update(request, id, order_id):
    lform = ListForm(request.POST)
    if lform.is_valid():
        order = models.Order.objects.get(pk=order_id)
        list = lform.save(commit=False)
        list.id = id
        list.order_id = order_id
        list.save()
        return HttpResponseRedirect("/order/show/" + str(order_id))
    else:
        return render(request, "driveapp/list/update.html", {"form": lform, "id": id})

def delete(request, id, order_id):
    list = models.List.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect("/order/show/" + str(order_id))

