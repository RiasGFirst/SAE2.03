from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'category', 'date_peremption', 'image', 'brand', 'price']
        labels = {
            'name': _('Name of the product'),
            'category': _('Category of the product'),
            'date_peremption': _('Expiration date of the product'),
            'image': _('Image of the product'),
            'brand': _('Brand of the product'),
            'price': _('Price of the product'),
        }
        help_texts = {
            'name': _('Enter the name of the product'),
            'category': _('Select the category of the product'),
            'date_peremption': _('Enter the expiration date of the product'),
            'image': _('Select the image of the product'),
            'brand': _('Enter the brand of the product'),
            'price': _('Enter the price of the product'),
        }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'description']
        labels = {
            'name': _('Name of the category'),
            'description': _('Description of the category'),
        }
        help_texts = {
            'name': _('Enter the name of the category'),
            'description': _('Enter the description of the category'),
        }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = ['customer', 'number', 'status']
        labels = {
            'customer': _('Customer of the order'),
            'number': _('Number of the order'),
            'status': _('Status of the order'),
        }
        help_texts = {
            'customer': _('Select the customer of the order'),
            'number': _('Enter the number of the order'),
            'status': _('Enter the status of the order'),
        }
        error_messages = {
            'number': {
                'max_length': _("This number is too long."),
            },
        }


class ListForm(ModelForm):
    class Meta:
        model = models.List
        fields = ['product', 'quantity']
        labels = {
            'product': _('Product of the list'),
            'quantity': _('Quantity of the list'),
        }
        help_texts = {
            'order': _('Select the order of the list'),
            'product': _('Select the product of the list'),
            'quantity': _('Enter the quantity of the list'),
        }
        error_messages = {
            'quantity': {
                'max_length': _("This quantity is too long."),
            },
        }


class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'forname', 'address']
        labels = {
            'name': _('Name of the customer'),
            'forname': _('Forname of the customer'),
            'address': _('Address of the customer'),
        }
        help_texts = {
            'name': _('Enter the name of the customer'),
            'forname': _('Enter the forname of the customer'),
            'address': _('Enter the address of the customer'),
        }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }


