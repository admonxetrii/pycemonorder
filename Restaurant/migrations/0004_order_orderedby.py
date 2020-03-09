# Generated by Django 3.0.2 on 2020-03-06 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Restaurant', '0003_remove_order_orderedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
