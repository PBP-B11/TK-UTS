# Generated by Django 4.1 on 2022-10-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypanel', '0004_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
