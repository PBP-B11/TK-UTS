# Generated by Django 4.1 on 2022-10-29 12:41

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
            name='Kalkulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity', models.IntegerField()),
                ('offset', models.IntegerField()),
                ('envfactor', models.IntegerField()),
                ('sizeestimate', models.IntegerField()),
                ('roofarea', models.IntegerField()),
                ('panel', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
