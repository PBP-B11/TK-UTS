# Generated by Django 4.1 on 2022-11-02 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimoni', '0002_alter_testitemplate_customer_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]