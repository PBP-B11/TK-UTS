# Generated by Django 4.1 on 2022-10-25 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]