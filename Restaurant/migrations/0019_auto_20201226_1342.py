# Generated by Django 3.1.4 on 2020-12-26 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0018_totalserveditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalserveditem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.menu'),
        ),
    ]