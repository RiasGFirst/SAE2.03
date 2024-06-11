from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'category', 'date_peremption', 'image', 'brand', 'price']
        labels = {
            'name': _('Name'),
            'category': _('Category'),
            'date_peremption': _('Expiration date'),
            'image': _('Image'),
            'brand': _('Brand'),
            'price': _('Price'),
        }
        help_texts = {
            'name': _("Enter the product's name"),
            'category': _('Select an existing category for the product'),
            'date_peremption': _('Enter the expiration date of the product'),
            'image': _('Select an image of the product'),
            'brand': _("Enter the product's brand"),
            'price': _("Enter the product's price (in €/unit)"),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'description']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
        }
        help_texts = {
            'name': _("Enter the category's name"),
            'description': _('Enter a short description of the category'),
        }



class OrderForm(ModelForm):
    class Meta:
        model = models.Orders
        fields = ['customer', 'number', 'status']
        labels = {
            'customer': _('Customer'),
            'number': _('Number'),
            'status': _('Status'),
        }
        help_texts = {
            'customer': _('Select the customer who ordered'),
            'number': _("Enter the order's number"),
            'status': _("Select the order's status"),
        }


class ListForm(ModelForm):
    class Meta:
        model = models.List
        fields = ['product', 'quantity']
        labels = {
            'product': _('Product'),
            'quantity': _('Quantity'),
        }
        help_texts = {
            'order': _("Select the list's associated order"),
            'product': _("Select a product to add to the list"),
            'quantity': _("Select the product's quantity"),
        }


class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'forename', 'address']
        labels = {
            'name': _('Name'),
            'forename': _('forename'),
            'address': _('Address'),
        }
        help_texts = {
            'name': _("Enter the customer's name"),
            'forename': _("Enter the customer's forename"),
            'address': _("Enter the customer's address"),
        }



