# Generated by Django 4.1.3 on 2022-11-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_rename_proveedor_proveedore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]