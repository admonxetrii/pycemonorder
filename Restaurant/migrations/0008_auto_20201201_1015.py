# Generated by Django 3.0.4 on 2020-12-01 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0007_auto_20201201_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbmsdata',
            name='fiscalyear',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='cbmsdata',
            name='sellerpan',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='cbmsdata',
            name='cbmspassword',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cbmsdata',
            name='cbmsusername',
            field=models.CharField(max_length=64),
        ),
    ]