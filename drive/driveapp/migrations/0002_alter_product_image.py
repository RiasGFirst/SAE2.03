# Generated by Django 5.0.6 on 2024-05-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]