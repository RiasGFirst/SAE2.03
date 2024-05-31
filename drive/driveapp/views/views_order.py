from django.shortcuts import render, HttpResponseRedirect
from ..forms import OrderForm
from .. import models

# Create your views here.


def home(request):
    order = models.Orders.objects.all()
    return render(request, 'driveapp/order/home.html', {'orders': order})


def add(request):
    form = OrderForm()
    return render(request, 'driveapp/order/add.html', {'form': form})


def processing(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'driveapp/order/success.html', {'order': form.cleaned_data})
    else:
        return render(request, 'driveapp/order/error.html')


def update(request, id):
    order = models.Orders.objects.get(id=id)
    form = OrderForm(instance=order)
    return render(request, 'driveapp/order/update.html', {'form': form, 'order': order})


def processing_update(request, id):
    order = models.Orders.objects.get(id=id)
    lform = OrderForm(request.POST, instance=order)
    if lform.is_valid():
        order = lform.save(commit=False)
        order.id = id
        order.save()
        return HttpResponseRedirect("/order/")
    else:
        return render(request, "driveapp/order/update.html", {"form": lform, "id": id})


def show(request, id):
    order = models.Orders.objects.get(id=id)
    l = list(models.List.objects.filter(order_id=id))
    return render(request, 'driveapp/order/show.html', {'order': order, "l": l})


def delete(request, id):
    order = models.Orders.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect("/order/")


def add_product(request, id):
    order = models.Orders.objects.get(id=id)

    pass

def product_process(request, id):
    order = models.Orders.objects.get(id=id)

    pass

