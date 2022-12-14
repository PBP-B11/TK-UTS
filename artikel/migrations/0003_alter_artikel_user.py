from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypanel', '0009_customer_address'),
        ('artikel', '0002_remove_artikel_like_artikel_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='mypanel.customer'),
        ),
    ]
