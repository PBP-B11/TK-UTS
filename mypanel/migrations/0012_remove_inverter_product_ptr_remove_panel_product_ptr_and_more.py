# Generated by Django 4.1 on 2022-10-31 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0005_alter_orderitem_product'),
        ('mypanel', '0011_alter_address_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inverter',
            name='product_ptr',
        ),
        migrations.RemoveField(
            model_name='panel',
            name='product_ptr',
        ),
        migrations.DeleteModel(
            name='Battery',
        ),
        migrations.DeleteModel(
            name='Inverter',
        ),
        migrations.DeleteModel(
            name='Panel',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
