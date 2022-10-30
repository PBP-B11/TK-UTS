# Generated by Django 4.1 on 2022-10-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200)),
                ('kota', models.CharField(default='', max_length=200)),
                ('kecamatan', models.CharField(default='', max_length=200)),
                ('kelurahan', models.CharField(default='', max_length=200)),
                ('postcode', models.CharField(default='', max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]