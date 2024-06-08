from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from ..forms import OrderForm
from .. import models
import io

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


def export_orders(request, id):
    # Récupérer la liste des articles de la commande
    order_items = list(models.List.objects.filter(order_id=id))
    order = models.Orders.objects.get(id=id)

    # Création d'un buffer pour générer le PDF
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Titre du document
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, f"Purchase order #{order.number}")

    # Détails de la commande
    p.setFont("Helvetica", 12)
    p.drawString(100, 720, f"Customer: {order.customer}")
    p.drawString(100, 700, f"Order Date: {order.date.strftime('%Y-%m-%d')}")
    p.drawString(100, 680, f"Status Order: {order.status}")

    # Adresse du client
    p.drawString(100, 660, f"Shipping Address: {order.customer.address}")

    # Entête du tableau des articles
    p.drawString(100, 610, "Products:")
    p.drawString(100, 590, "Name")
    p.drawString(300, 590, "Quantity")
    p.drawString(400, 590, "Price/unit")

    # Lignes du tableau
    y = 570
    for item in order_items:
        p.drawString(100, y, item.product.name)
        p.drawString(300, y, str(item.quantity))
        p.drawString(400, y, f"{item.product.price:.2f} €")
        y -= 20

    # Total de la commande
    total_price = sum(item.product.price * item.quantity for item in order_items)
    p.drawString(100, y-30, f"Total: {total_price:.2f} €")

    # Finaliser le PDF
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"order_{id}.pdf")