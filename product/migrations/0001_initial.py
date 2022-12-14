# Generated by Django 4.1 on 2022-10-31 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('capacity', models.IntegerField()),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('output', models.IntegerField()),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('max_power', models.IntegerField()),
            ],
            bases=('product.product',),
        ),
    ]
