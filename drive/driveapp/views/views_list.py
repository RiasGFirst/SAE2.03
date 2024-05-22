from django.shortcuts import render, HttpResponseRedirect
from django.forms import inlineformset_factory
from ..forms import ListForm
from .. import models

def add(request, id):
    order = models.Order.objects.get(pk=id)
    ListFormSet = inlineformset_factory(models.Order, models.List, form=ListForm, extra=1)
    if request.method == 'POST':
        formset = ListFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/order/show/" + str(id))
    else:
        formset = ListFormSet(instance=order)
    return render(request, 'driveapp/list/list.html', {'formset': formset, 'order': order})

