# Generated by Django 3.0.4 on 2020-05-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_tablediscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='disval',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='TableDiscount',
        ),
    ]