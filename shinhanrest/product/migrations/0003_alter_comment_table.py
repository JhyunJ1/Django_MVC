# Generated by Django 4.1.5 on 2023-01-20 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='shinhan_product_comment',
        ),
    ]