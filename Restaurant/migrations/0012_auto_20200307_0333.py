# Generated by Django 3.0.2 on 2020-03-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0011_order_orderedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='table',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
