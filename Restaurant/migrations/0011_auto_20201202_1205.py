# Generated by Django 3.0.4 on 2020-12-02 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0010_auto_20201202_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billsync',
            name='bill',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Bill'),
        ),
    ]
