# Generated by Django 5.0.6 on 2024-05-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveapp', '0009_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_peremption',
            field=models.DateField(blank=True, default=None),
        ),
    ]