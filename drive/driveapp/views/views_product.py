from django.shortcuts import render, HttpResponseRedirect
from PIL import Image
from ..forms import ProductForm
from .. import models
from datetime import datetime
from django.contrib import messages
import csv
from django.utils.datastructures import MultiValueDictKeyError

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
        return render(request,"driveapp/product/add.html",{"form" : lform})


def update(request, id):
    product = models.Product.objects.get(id=id)
    form = ProductForm(instance=product)
    return render(request, 'driveapp/product/update.html', {'form': form, 'product': product})


def processing_update(request, id):
    product = models.Product.objects.get(id=id)
    lform = ProductForm(request.POST, request.FILES, instance=product)
    if lform.is_valid():
        lform.save()
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


def import_product(request):
    if request.method == 'POST':
        try:
            myfile = request.FILES['myfile']
        except MultiValueDictKeyError:
            messages.error(request, "Submit a CSV File please")
            return HttpResponseRedirect("/product/")

        decoded_file = myfile.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        required_fields = ['name', 'date_peremption', 'brand', 'price', 'category_id']

        for row in reader:
            missing_fields = [field for field in required_fields if field not in row]
            if missing_fields:
                messages.error(request,
                               f"Le fichier CSV ne contient pas toutes les colonnes nécessaires. Manquantes: {', '.join(missing_fields)}")
                return HttpResponseRedirect("/product/")

            try:
                models.Product.objects.create(
                    name=row['name'],
                    category=models.Category.objects.get(id=row['category_id']),
                    date_peremption=datetime.strptime(row['date_peremption'], "%Y-%m-%d"),
                    brand=row['brand'],
                    price=row['price']
                )
            except (models.Product.DoesNotExist, models.Category.DoesNotExist) as e:
                messages.error(request, f"Erreur d'importation: {e}")
                return HttpResponseRedirect("/product/")
            except ValueError as e:
                messages.error(request, f"Erreur de format de date: {e}")
                return HttpResponseRedirect("/product/")

        messages.success(request, "Les vols ont été importés avec succès.")
        return HttpResponseRedirect("/product/")
    else:
        messages.error(request, "Erreur lors de l'importation. Veuillez réessayer.")
        return HttpResponseRedirect("/product/")