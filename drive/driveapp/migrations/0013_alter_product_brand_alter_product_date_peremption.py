# Generated by Django 5.0.6 on 2024-05-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveapp', '0012_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_peremption',
            field=models.DateField(),
        ),
    ]