# Generated by Django 3.0.4 on 2020-09-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0005_restologs'),
    ]

    operations = [
        migrations.AddField(
            model_name='restologs',
            name='datentime',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
