# Generated by Django 4.1 on 2022-10-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypanel', '0010_remove_customer_address_customer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
