# Generated by Django 4.2.5 on 2023-09-27 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_price_per_item_alter_product_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_per_item',
        ),
    ]
