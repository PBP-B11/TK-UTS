# Generated by Django 4.1 on 2022-10-28 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mypanel', '0010_remove_customer_address_customer_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestiTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('reply', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypanel.customer')),
            ],
        ),
    ]
