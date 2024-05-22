# Generated by Django 5.0.6 on 2024-05-22 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveapp', '0004_remove_order_products_remove_list_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='product',
        ),
        migrations.RemoveField(
            model_name='list',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='list',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.order'),
        ),
        migrations.CreateModel(
            name='ListProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.list')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driveapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='products',
            field=models.ManyToManyField(through='driveapp.ListProduct', to='driveapp.product'),
        ),
    ]