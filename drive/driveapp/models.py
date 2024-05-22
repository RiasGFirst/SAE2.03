from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    forname = models.CharField(max_length=100)
    inscription_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.forname}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.description}"
    






class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_peremption = models.DateField()
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.price}, {self.date_peremption}, {self.brand}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('preparation', 'Preparation'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    products = models.ManyToManyField(Product, through='List')

    def __str__(self):
        return f"{self.customer}, {self.number}, {self.date}, {self.status}"


class List(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order}, {self.product}, {self.quantity}"

